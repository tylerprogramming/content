#!/usr/bin/env python3
"""Bouncing ball inside a spinning hexagon.

Gravity, air drag, restitution and Coulomb friction against walls that are
themselves moving (the contact impulse is solved against the wall's local
velocity, so the spinning hexagon actually drags and spins the ball).

    pip install pygame
    python hex_bounce.py

Controls
    SPACE        respawn the ball
    LEFT/RIGHT   hexagon spin speed
    UP/DOWN      gravity
    G            gravity on/off
    R            reset everything
    ESC / close  quit
"""

from __future__ import annotations

import math
import random
import sys
from collections import deque

import pygame
from pygame.math import Vector2

# ---------------------------------------------------------------- tunables
WIDTH, HEIGHT = 560, 560
FPS = 60
SUBSTEPS = 8                # physics iterations per rendered frame

HEX_RADIUS = 205.0          # circumradius in px
SPIN = 0.7                  # rad/s

GRAVITY = 1400.0            # px/s^2
AIR_DRAG = 0.12             # velocity lost per second in flight
SPIN_DRAG = 0.5             # ball's angular velocity lost per second

BALL_RADIUS = 13.0
BALL_MASS = 1.0
RESTITUTION = 0.68          # 0 = dead thud, 1 = perfectly elastic
FRICTION = 0.35             # Coulomb mu between ball and wall

BG = (14, 16, 22)
HEX_COLOR = (78, 92, 128)
HEX_HOT = (120, 200, 255)
BALL_COLOR = (255, 168, 76)
TEXT_COLOR = (150, 162, 186)


# ---------------------------------------------------------------- 2-D helpers
# Screen y points down, but every routine below uses the same handedness, so
# the signs stay consistent: perp() is the +90 deg rotation that matches cross().
def perp(v: Vector2) -> Vector2:
    return Vector2(-v.y, v.x)


def cross(a: Vector2, b: Vector2) -> float:
    return a.x * b.y - a.y * b.x


def hex_vertices(center: Vector2, radius: float, angle: float) -> list[Vector2]:
    return [center + Vector2(radius, 0).rotate_rad(angle + i * math.pi / 3)
            for i in range(6)]


class Ball:
    def __init__(self, pos, vel=(0.0, 0.0)):
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.radius = BALL_RADIUS
        self.mass = BALL_MASS
        self.inertia = 0.5 * self.mass * self.radius ** 2   # solid disc
        self.spin = 0.0        # rad/s
        self.angle = 0.0       # accumulated orientation, drawn as a spoke
        self.trail = deque(maxlen=110)
        self.touching: set[int] = set()


def spawn(center: Vector2) -> Ball:
    return Ball(center + Vector2(random.uniform(-60, 60), -HEX_RADIUS * 0.45),
                (random.uniform(-260, 260), random.uniform(-120, 60)))


# ---------------------------------------------------------------- physics
def resolve_contact(ball: Ball, n: Vector2, penetration: float,
                    center: Vector2, omega: float) -> None:
    """Impulse response for one wall. `n` is the unit inward normal."""
    ball.pos += n * penetration                 # positional correction

    rc = -n * ball.radius                       # ball centre -> contact point
    contact = ball.pos + rc

    # The wall is rotating about `center`, so the material point we hit is moving.
    wall_v = perp(contact - center) * omega
    # Velocity of the ball's own surface at the contact (translation + spin).
    u = ball.vel + perp(rc) * ball.spin - wall_v

    un = u.dot(n)
    if un >= 0.0:                               # already separating
        return

    t = perp(n)
    ut = u.dot(t)

    # Normal impulse. rc is parallel to n, so it contributes no torque here and
    # the effective mass along n is just the ball's mass.
    jn = -(1.0 + RESTITUTION) * un * ball.mass

    # Tangential impulse, clamped by the Coulomb cone. The effective mass along
    # t includes the rotational term, which is what makes the ball roll/spin up.
    inv_mass_t = 1.0 / ball.mass + cross(rc, t) ** 2 / ball.inertia
    jt = -ut / inv_mass_t
    limit = FRICTION * jn
    jt = max(-limit, min(limit, jt))

    ball.vel += (n * jn + t * jt) / ball.mass
    ball.spin += cross(rc, t * jt) / ball.inertia


def step(ball: Ball, center: Vector2, hex_angle: float, omega: float,
         gravity: float, dt: float) -> None:
    ball.vel.y += gravity * dt
    ball.vel *= max(0.0, 1.0 - AIR_DRAG * dt)
    ball.spin *= max(0.0, 1.0 - SPIN_DRAG * dt)
    ball.pos += ball.vel * dt
    ball.angle += ball.spin * dt

    # A convex polygon is the intersection of half-planes, so each edge can be
    # treated as an infinite line -- corners fall out of the two adjacent pushes.
    verts = hex_vertices(center, HEX_RADIUS, hex_angle)
    ball.touching.clear()
    for i in range(6):
        a, b = verts[i], verts[(i + 1) % 6]
        n = perp(b - a)
        if n.length_squared() == 0.0:
            continue
        n.normalize_ip()
        penetration = ball.radius - (ball.pos - a).dot(n)
        if penetration > 0.0:
            resolve_contact(ball, n, penetration, center, omega)
            ball.touching.add(i)


# ---------------------------------------------------------------- rendering
def lerp_color(c0, c1, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c0, c1))


def draw(screen, font, ball, center, hex_angle, spin, gravity, gravity_on):
    screen.fill(BG)
    verts = hex_vertices(center, HEX_RADIUS, hex_angle)

    for i in range(6):
        a, b = verts[i], verts[(i + 1) % 6]
        hot = i in ball.touching
        pygame.draw.line(screen, HEX_HOT if hot else HEX_COLOR, a, b, 6 if hot else 3)
    for v in verts:
        pygame.draw.circle(screen, HEX_COLOR, v, 5)

    n = len(ball.trail)
    for i, p in enumerate(ball.trail):
        f = (i + 1) / max(n, 1)
        pygame.draw.circle(screen, lerp_color(BG, BALL_COLOR, f * 0.55),
                           p, max(1.0, ball.radius * 0.42 * f))

    pygame.draw.circle(screen, BALL_COLOR, ball.pos, ball.radius)
    spoke = Vector2(ball.radius * 0.82, 0).rotate_rad(ball.angle)
    pygame.draw.line(screen, BG, ball.pos, ball.pos + spoke, 3)

    lines = [
        f"spin      {spin:+6.2f} rad/s   [LEFT/RIGHT]",
        f"gravity   {gravity if gravity_on else 0.0:6.0f} px/s^2  [UP/DOWN, G]",
        f"speed     {ball.vel.length():6.0f} px/s",
        f"ball spin {ball.spin:+6.2f} rad/s",
        "SPACE respawn   R reset   ESC quit",
    ]
    for i, line in enumerate(lines):
        screen.blit(font.render(line, True, TEXT_COLOR), (18, 16 + i * 20))

    pygame.display.flip()


# ---------------------------------------------------------------- main loop
def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing ball in a spinning hexagon")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,consolas,dejavusansmono,monospace", 15)

    center = Vector2(WIDTH / 2, HEIGHT / 2)
    hex_angle, spin = 0.0, SPIN
    gravity, gravity_on = GRAVITY, True
    ball = spawn(center)

    while True:
        dt = min(clock.tick(FPS) / 1000.0, 1.0 / 30.0)   # clamp after a stall

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    ball = spawn(center)
                elif event.key == pygame.K_g:
                    gravity_on = not gravity_on
                elif event.key == pygame.K_r:
                    hex_angle, spin = 0.0, SPIN
                    gravity, gravity_on = GRAVITY, True
                    ball = spawn(center)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spin -= 1.6 * dt
        if keys[pygame.K_RIGHT]:
            spin += 1.6 * dt
        if keys[pygame.K_UP]:
            gravity = min(4000.0, gravity + 900.0 * dt)
        if keys[pygame.K_DOWN]:
            gravity = max(0.0, gravity - 900.0 * dt)

        g = gravity if gravity_on else 0.0
        h = dt / SUBSTEPS
        for _ in range(SUBSTEPS):
            hex_angle += spin * h          # advance the walls, then collide
            step(ball, center, hex_angle, spin, g, h)

        ball.trail.append(Vector2(ball.pos))
        draw(screen, font, ball, center, hex_angle, spin, g, gravity_on)


if __name__ == "__main__":
    main()