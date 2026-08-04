"""
Ball bouncing inside a spinning hexagon.
Gravity + friction, with realistic bounces off the rotating walls
(the moving wall imparts velocity to the ball on impact).

Run:  pip install pygame  &&  python bouncing_hexagon.py
"""

import math
import pygame

# ---- Config ---------------------------------------------------------------
WIDTH, HEIGHT = 560, 560
FPS           = 120           # high FPS => stable collision handling

HEX_RADIUS    = 200           # distance from center to each vertex
HEX_SPIN      = 0.6           # hexagon angular velocity (radians / second)

BALL_RADIUS   = 11
GRAVITY       = 900.0         # pixels / second^2, pulling down (+y)
RESTITUTION   = 0.9           # bounciness: fraction of normal speed kept (0..1)
WALL_FRICTION = 0.15          # tangential friction on impact (0 = slippery, 1 = grippy)
AIR_DRAG      = 0.999         # per-frame velocity damping (subtle)

BG      = (14, 16, 22)
HEX_CLR = (90, 200, 255)
BALL_CLR = (255, 120, 90)


def hexagon_vertices(cx, cy, radius, angle):
    """Six vertices of a regular hexagon centered at (cx, cy), rotated by `angle`."""
    return [
        (cx + radius * math.cos(angle + i * math.pi / 3),
         cy + radius * math.sin(angle + i * math.pi / 3))
        for i in range(6)
    ]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ball in a Spinning Hexagon")
    clock = pygame.time.Clock()

    cx, cy = WIDTH / 2, HEIGHT / 2

    # Ball state
    px, py = cx, cy - 120     # start a bit above center
    vx, vy = 220.0, 0.0
    angle  = 0.0              # current hexagon rotation

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        dt = min(dt, 1 / 60)  # clamp so a lag spike can't tunnel the ball

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # --- Physics: integrate the ball ---
        vy += GRAVITY * dt
        vx *= AIR_DRAG
        vy *= AIR_DRAG
        px += vx * dt
        py += vy * dt

        # Advance the hexagon
        angle += HEX_SPIN * dt
        verts = hexagon_vertices(cx, cy, HEX_RADIUS, angle)

        # --- Collision against each of the 6 edges ---
        for i in range(6):
            ax, ay = verts[i]
            bx, by = verts[(i + 1) % 6]

            ex, ey = bx - ax, by - ay              # edge vector
            elen2  = ex * ex + ey * ey
            # Project ball center onto the edge segment, clamped to [0,1]
            t = ((px - ax) * ex + (py - ay) * ey) / elen2
            t = max(0.0, min(1.0, t))
            clx, cly = ax + t * ex, ay + t * ey     # closest point on edge

            dx, dy = px - clx, py - cly             # from wall -> ball
            dist   = math.hypot(dx, dy)
            if dist >= BALL_RADIUS or dist == 0:
                continue

            # Inward normal (points from wall toward ball center)
            nx, ny = dx / dist, dy / dist

            # Velocity of the wall at the contact point (rigid rotation about center):
            #   v = omega x r,  with r = contact - center
            rx, ry = clx - cx, cly - cy
            wall_vx = -HEX_SPIN * ry
            wall_vy =  HEX_SPIN * rx

            # Ball velocity relative to the moving wall
            rel_vx = vx - wall_vx
            rel_vy = vy - wall_vy
            vn = rel_vx * nx + rel_vy * ny          # normal component (relative)

            # Push the ball out of the wall (positional correction)
            overlap = BALL_RADIUS - dist
            px += nx * overlap
            py += ny * overlap

            if vn < 0:  # only respond if moving into the wall
                # Split relative velocity into normal + tangential parts
                vn_vec_x, vn_vec_y = vn * nx, vn * ny
                vt_x = rel_vx - vn_vec_x
                vt_y = rel_vy - vn_vec_y

                # Reflect normal (restitution), damp tangential (friction)
                new_rel_vx = (vt_x * (1 - WALL_FRICTION)) - vn_vec_x * RESTITUTION
                new_rel_vy = (vt_y * (1 - WALL_FRICTION)) - vn_vec_y * RESTITUTION

                # Back to world frame: add the wall's velocity
                vx = new_rel_vx + wall_vx
                vy = new_rel_vy + wall_vy

        # --- Render ---
        screen.fill(BG)
        pygame.draw.polygon(screen, HEX_CLR, verts, width=4)
        pygame.draw.circle(screen, BALL_CLR, (int(px), int(py)), BALL_RADIUS)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()