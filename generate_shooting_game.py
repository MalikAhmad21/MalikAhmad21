#!/usr/bin/env python3
"""
Working SVG Shooting Animation (No JS, No Errors)
Gun moves randomly.
Boxes fade out and regenerate.
"""

import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 420

BOX_SIZE = 12
COLS = 40
ROWS = 6

GUN_WIDTH = 40
GUN_HEIGHT = 50

BULLET_RADIUS = 4

BG_COLOR = "#0d1117"
BOX_COLOR = "#26a641"
GUN_COLOR = "#58a6ff"
BULLET_COLOR = "#f85149"

ANIMATION_DURATION = 12


def generate_svg():

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
    viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">

    <rect width="100%" height="100%" fill="{BG_COLOR}" />

    <!-- GUN -->
    <g id="gun">
        <rect x="{CANVAS_WIDTH//2 - GUN_WIDTH//2}"
              y="{CANVAS_HEIGHT - GUN_HEIGHT - 10}"
              width="{GUN_WIDTH}"
              height="{GUN_HEIGHT}"
              rx="6"
              fill="{GUN_COLOR}">
              
            <!-- Gun left-right animation -->
            <animate attributeName="x"
                     values="50;750;100;700;200;600;400"
                     dur="6s"
                     repeatCount="indefinite"/>
        </rect>
    </g>

    <!-- BULLETS -->
'''

    # Bullets
    for i in range(10):
        start_time = i * 0.6
        svg += f'''
    <circle cx="{CANVAS_WIDTH//2}" 
            cy="{CANVAS_HEIGHT - GUN_HEIGHT - 10}"
            r="{BULLET_RADIUS}"
            fill="{BULLET_COLOR}">
        <animate attributeName="cy"
                 from="{CANVAS_HEIGHT - GUN_HEIGHT - 10}"
                 to="0"
                 begin="{start_time}s"
                 dur="2s"
                 repeatCount="indefinite"/>
    </circle>
'''

    svg += "\n<!-- BOXES -->\n"

    # Boxes
    for _ in range(120):
        x = random.randint(40, CANVAS_WIDTH - 40)
        y = random.randint(40, 250)
        delay = random.uniform(1, ANIMATION_DURATION)

        svg += f'''
    <rect x="{x}" y="{y}"
          width="{BOX_SIZE}" height="{BOX_SIZE}"
          fill="{BOX_COLOR}" rx="3">

        <!-- fade out when hit -->
        <animate attributeName="opacity"
                 values="1;1;0;1"
                 keyTimes="0;0.6;0.7;1"
                 dur="4s"
                 begin="{delay}s"
                 repeatCount="indefinite"/>
    </rect>
'''

    svg += "\n</svg>"

    return svg


def main():
    svg_content = generate_svg()

    with open("shooting-game-fixed.svg", "w") as f:
        f.write(svg_content)

    print("✅ shooting-game-fixed.svg generated successfully!")


if __name__ == "__main__":
    main()
