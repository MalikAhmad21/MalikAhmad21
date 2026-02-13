#!/usr/bin/env python3
"""
Advanced Animated SVG Shooting Game
- Gun moves randomly left/right
- Bullets shoot from moving gun
- Boxes disappear on hit
- New boxes keep spawning
"""

import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450

BOX_SIZE = 14
COLS = 40
ROWS = 6

GUN_WIDTH = 40
GUN_HEIGHT = 50

BULLET_RADIUS = 4

BG_COLOR = "#0d1117"
BOX_COLOR = "#26a641"
GUN_COLOR = "#58a6ff"
BULLET_COLOR = "#f85149"


def generate_svg():

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
    viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">

    <rect width="100%" height="100%" fill="{BG_COLOR}" />

    <g id="boxes"></g>
    <g id="bullets"></g>

    <!-- Gun -->
    <g id="gun">
        <rect id="gunBase" x="{CANVAS_WIDTH//2 - GUN_WIDTH//2}" 
              y="{CANVAS_HEIGHT - GUN_HEIGHT - 10}"
              width="{GUN_WIDTH}" height="{GUN_HEIGHT}"
              rx="6" fill="{GUN_COLOR}"/>
    </g>

<script><![CDATA[

const svg = document.documentElement;
const boxesGroup = document.getElementById("boxes");
const bulletsGroup = document.getElementById("bullets");
const gun = document.getElementById("gunBase");

let gunX = {CANVAS_WIDTH//2 - GUN_WIDTH//2};
let direction = 1;

// =======================
// RANDOM GUN MOVEMENT
// =======================
setInterval(() => {{
    direction = Math.random() > 0.5 ? 1 : -1;
}}, 1000);

function moveGun() {{
    gunX += direction * 3;

    if (gunX < 0) gunX = 0;
    if (gunX > {CANVAS_WIDTH - GUN_WIDTH})
        gunX = {CANVAS_WIDTH - GUN_WIDTH};

    gun.setAttribute("x", gunX);
    requestAnimationFrame(moveGun);
}}

moveGun();

// =======================
// BOX GENERATION
// =======================
function createBox() {{
    const box = document.createElementNS("http://www.w3.org/2000/svg", "rect");

    let x = Math.random() * ({CANVAS_WIDTH} - {BOX_SIZE});
    let y = Math.random() * 200 + 40;

    box.setAttribute("x", x);
    box.setAttribute("y", y);
    box.setAttribute("width", {BOX_SIZE});
    box.setAttribute("height", {BOX_SIZE});
    box.setAttribute("fill", "{BOX_COLOR}");
    box.setAttribute("rx", 3);

    boxesGroup.appendChild(box);
}}

setInterval(createBox, 600);

// =======================
// SHOOTING SYSTEM
// =======================
function shoot() {{

    const bullet = document.createElementNS("http://www.w3.org/2000/svg", "circle");

    bullet.setAttribute("cx", gunX + {GUN_WIDTH/2});
    bullet.setAttribute("cy", {CANVAS_HEIGHT - GUN_HEIGHT - 10});
    bullet.setAttribute("r", {BULLET_RADIUS});
    bullet.setAttribute("fill", "{BULLET_COLOR}");

    bulletsGroup.appendChild(bullet);

    let interval = setInterval(() => {{
        let cy = parseFloat(bullet.getAttribute("cy"));
        bullet.setAttribute("cy", cy - 6);

        // collision detection
        let boxes = boxesGroup.querySelectorAll("rect");
        boxes.forEach(box => {{
            let bx = parseFloat(box.getAttribute("x"));
            let by = parseFloat(box.getAttribute("y"));

            if (
                gunX + {GUN_WIDTH/2} > bx &&
                gunX + {GUN_WIDTH/2} < bx + {BOX_SIZE} &&
                cy < by + {BOX_SIZE} &&
                cy > by
            ) {{
                box.remove();
                bullet.remove();
                clearInterval(interval);
            }}
        }});

        if (cy < 0) {{
            bullet.remove();
            clearInterval(interval);
        }}

    }}, 20);
}}

setInterval(shoot, 500);

]]></script>

</svg>'''

    return svg


def main():
    svg_content = generate_svg()

    with open("shooting-game-advanced.svg", "w") as f:
        f.write(svg_content)

    print("✅ shooting-game-advanced.svg generated successfully!")


if __name__ == "__main__":
    main()
