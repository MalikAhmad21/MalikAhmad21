#!/usr/bin/env python3
"""
GitHub Contribution Style Shooting Animation
Gun moves horizontally over the contribution grid
Bullets fire from gun's current position and move independently
"""

import random

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 330

# Contribution grid
COLS = 52
ROWS = 7
BOX_SIZE = 12
BOX_GAP = 4

# Gun
GUN_WIDTH = 50
GUN_HEIGHT = 50
BARREL_WIDTH = 8
BARREL_HEIGHT = 30

BULLET_RADIUS = 4

# Colors (GitHub dark theme style)
BG_COLOR = "#0d1117"
TEXT_COLOR = "#c9d1d9"
GREENS = ["#0e4429", "#006d32", "#26a641", "#39d353"]
GUN_COLOR = "#58a6ff"
BULLET_COLOR = "#f85149"

def generate_svg():

    grid_width = COLS * (BOX_SIZE + BOX_GAP)
    grid_x = (CANVAS_WIDTH - grid_width) // 2
    grid_y = 60

    gun_y = CANVAS_HEIGHT - GUN_HEIGHT - 20
    gun_start_x = grid_x
    gun_end_x = grid_x + grid_width - GUN_WIDTH

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
    viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">

    <rect width="100%" height="100%" fill="{BG_COLOR}" />

    <!-- Contribution Grid -->
    <g id="grid">
'''

    # Contribution boxes
    for col in range(COLS):
        for row in range(ROWS):
            x = grid_x + col * (BOX_SIZE + BOX_GAP)
            y = grid_y + row * (BOX_SIZE + BOX_GAP)
            color = random.choice(GREENS)
            fade_delay = random.uniform(2, 10)

            svg += f'''
        <rect x="{x}" y="{y}"
              width="{BOX_SIZE}" height="{BOX_SIZE}"
              fill="{color}" rx="2">
            <animate attributeName="opacity"
                     values="1;1;0.2;1"
                     dur="6s"
                     begin="{fade_delay}s"
                     repeatCount="indefinite"/>
        </rect>
'''

    svg += "\n    </g>\n"

    # Gun group (barrel + base)
    svg += f'''
    <!-- Gun -->
    <g id="gun">
        <animateTransform attributeName="transform"
            type="translate"
            values="{gun_start_x} 0; {gun_end_x} 0; {gun_start_x} 0"
            dur="12s"
            repeatCount="indefinite"/>

        <!-- Barrel -->
        <rect x="0"  # relative to group
              y="{gun_y}"
              width="{BARREL_WIDTH}"
              height="{BARREL_HEIGHT}"
              fill="{GUN_COLOR}" rx="3"/>

        <!-- Base -->
        <rect x="-{GUN_WIDTH//2}"  # relative to group
              y="{gun_y + BARREL_HEIGHT}"
              width="{GUN_WIDTH}"
              height="{GUN_HEIGHT - BARREL_HEIGHT}"
              fill="{GUN_COLOR}" rx="6"/>
    </g>
'''

    # Bullets (spawn from gun barrel position at time of firing)
    num_bullets = 12
    fire_interval = 1.0  # seconds between bullets
    for i in range(num_bullets):
        delay = i * fire_interval
        # Calculate bullet X relative to gun movement (using same values as gun animation)
        # We approximate: bullet X = start + ((end - start) * progress) at fire time
        # SVG animate cannot calculate dynamically, so we precompute start X
        gun_progress = (delay % 12) / 12  # normalize to gun animation duration
        bullet_x = gun_start_x + (gun_end_x - gun_start_x) * gun_progress + GUN_WIDTH // 2

        svg += f'''
    <circle cx="{bullet_x}"
            cy="{gun_y}"
            r="{BULLET_RADIUS}"
            fill="{BULLET_COLOR}">
        <animate attributeName="cy"
                 from="{gun_y}"
                 to="40"
                 dur="2s"
                 begin="{delay}s"
                 repeatCount="indefinite"/>
        <animate attributeName="opacity"
                 values="0;1;1;0"
                 dur="2s"
                 begin="{delay}s"
                 repeatCount="indefinite"/>
    </circle>
'''

    svg += "\n</svg>"

    return svg


def main():
    svg_content = generate_svg()

    with open("shooting-game.svg", "w") as f:
        f.write(svg_content)

    print("✅ shooting-game.svg generated successfully!")


if __name__ == "__main__":
    main()
