"""Ball bouncing inside a spinning hexagon.

Physics: gravity, air drag, and impulse-based collisions against moving
walls. Each bounce is computed in the wall's reference frame (the wall has
velocity omega x r at the contact point), with separate restitution
(normal) and friction (tangential) coefficients.

Requires: pygame  (pip install pygame)
"""

import math
import sys

import pygame

# ---------------------------------------------------------------- tunables
WIDTH, HEIGHT = 560, 440
CENTER = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

HEX_RADIUS = 175          # center-to-vertex distance, px
SPIN_SPEED = 0.9          # hexagon angular velocity, rad/s (+ = clockwise on screen)

GRAVITY = 1400.0          # px/s^2
AIR_DRAG = 0.25           # per-second velocity damping (0 = none)
BALL_RADIUS = 10
RESTITUTION = 0.90        # normal bounce energy retention (0..1)
WALL_FRICTION = 0.15      # fraction of tangential speed lost per bounce (0..1)

FPS = 120
BG = (16, 18, 26)
HEX_COLOR = (90, 200, 250)
BALL_COLOR = (255, 120, 90)
TRAIL_COLOR = (255, 120, 90)


def hexagon_vertices(angle):
    """The six vertices of the hexagon at the given rotation angle."""
    return [
        CENTER + pygame.Vector2(
            math.cos(angle + i * math.pi / 3),
            math.sin(angle + i * math.pi / 3),
        ) * HEX_RADIUS
        for i in range(6)
    ]


def closest_point_on_segment(p, a, b):
    ab = b - a
    t = (p - a).dot(ab) / ab.length_squared()
    return a + ab * max(0.0, min(1.0, t))


def wall_velocity_at(point, spin_speed):
    """Velocity of a point rigidly attached to the rotating hexagon."""
    r = point - CENTER
    # omega x r in 2D (screen coords, y down): (-w*ry, w*rx)
    return pygame.Vector2(-spin_speed * r.y, spin_speed * r.x)


def collide(pos, vel, vertices, spin_speed):
    """Resolve ball-vs-wall contacts; returns updated (pos, vel)."""
    for i in range(6):
        a, b = vertices[i], vertices[(i + 1) % 6]
        q = closest_point_on_segment(pos, a, b)
        offset = pos - q
        dist = offset.length()
        if dist >= BALL_RADIUS or dist == 0:
            continue

        n = offset / dist                      # wall -> ball (inward) normal
        pos = pos + n * (BALL_RADIUS - dist)   # push out of penetration

        v_wall = wall_velocity_at(q, spin_speed)
        v_rel = vel - v_wall
        vn = v_rel.dot(n)
        if vn < 0:                             # only if approaching the wall
            v_t = v_rel - n * vn
            v_rel = -RESTITUTION * vn * n + (1.0 - WALL_FRICTION) * v_t
            vel = v_rel + v_wall
    return pos, vel


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ball in a Spinning Hexagon")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,consolas,monospace", 16)

    spin_speed = SPIN_SPEED
    angle = 0.0
    pos = pygame.Vector2(CENTER.x, CENTER.y - HEX_RADIUS * 0.5)
    vel = pygame.Vector2(220.0, 0.0)
    trail = []

    while True:
        dt = min(clock.tick(FPS) / 1000.0, 1 / 30)  # clamp big frame hitches

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:  # reset ball
                    pos = pygame.Vector2(CENTER.x, CENTER.y - HEX_RADIUS * 0.5)
                    vel = pygame.Vector2(220.0, 0.0)
                    trail.clear()
                if event.key == pygame.K_UP:
                    spin_speed += 0.2
                if event.key == pygame.K_DOWN:
                    spin_speed -= 0.2

        # Substep so a fast ball can't tunnel through a wall in one frame.
        steps = max(1, int(vel.length() * dt / (BALL_RADIUS * 0.5)) + 1)
        h = dt / steps
        for _ in range(steps):
            angle += spin_speed * h
            vel.y += GRAVITY * h
            vel *= math.exp(-AIR_DRAG * h)      # frame-rate-independent drag
            pos += vel * h
            pos, vel = collide(pos, vel, hexagon_vertices(angle), spin_speed)

        trail.append(pos.copy())
        if len(trail) > 40:
            trail.pop(0)

        # ------------------------------------------------------------ draw
        screen.fill(BG)
        verts = hexagon_vertices(angle)
        pygame.draw.polygon(screen, HEX_COLOR, verts, width=3)

        for k, p in enumerate(trail):
            fade = (k + 1) / len(trail)
            radius = max(1, int(BALL_RADIUS * fade * 0.6))
            color = tuple(int(c * fade * 0.5) for c in TRAIL_COLOR)
            pygame.draw.circle(screen, color, p, radius)
        pygame.draw.circle(screen, BALL_COLOR, pos, BALL_RADIUS)

        hud = font.render(
            f"spin {spin_speed:+.1f} rad/s   [up/down] spin  [space] reset",
            True, (150, 155, 170),
        )
        screen.blit(hud, (16, 14))
        pygame.display.flip()


if __name__ == "__main__":
    main()