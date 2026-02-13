#!/usr/bin/env python3
"""
Advanced SVG Shooting Game
- Bullet fires from moving gun nozzle
- Collision detection
- Explosion effect
- Shooting sound
"""

import random

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 300

COLS = 52
ROWS = 7
BOX_SIZE = 12
BOX_GAP = 4

GUN_WIDTH = 50
GUN_HEIGHT = 60
BARREL_HEIGHT = 30

BG_COLOR = "#0d1117"
GREENS = ["#0e4429", "#006d32", "#26a641", "#39d353"]
GUN_COLOR = "#58a6ff"
BULLET_COLOR = "#f85149"

def generate_svg():

    grid_width = COLS * (BOX_SIZE + BOX_GAP)
    grid_x = (CANVAS_WIDTH - grid_width) // 2
    grid_y = 40

    gun_y = CANVAS_HEIGHT - GUN_HEIGHT - 10

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
    viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">

    <rect width="100%" height="100%" fill="{BG_COLOR}" />

    <g id="boxes">
'''

    # Contribution Grid
    for col in range(COLS):
        for row in range(ROWS):
            x = grid_x + col * (BOX_SIZE + BOX_GAP)
            y = grid_y + row * (BOX_SIZE + BOX_GAP)
            color = random.choice(GREENS)

            svg += f'''
        <rect x="{x}" y="{y}"
              width="{BOX_SIZE}" height="{BOX_SIZE}"
              fill="{color}" rx="2"/>
'''

    svg += '''
    </g>

    <g id="bullets"></g>
    <g id="effects"></g>

    <!-- Gun -->
    <g id="gun">
        <rect id="barrel"
              x="425"
              y="''' + str(gun_y) + '''"
              width="6"
              height="''' + str(BARREL_HEIGHT) + '''"
              fill="''' + GUN_COLOR + '''"/>
        <rect id="base"
              x="400"
              y="''' + str(gun_y + BARREL_HEIGHT) + '''"
              width="50"
              height="30"
              fill="''' + GUN_COLOR + '''" rx="6"/>
    </g>

<script><![CDATA[

const gun = document.getElementById("gun");
const bulletsGroup = document.getElementById("bullets");
const boxesGroup = document.getElementById("boxes");
const effectsGroup = document.getElementById("effects");

let gunX = 400;
let direction = 1;

function moveGun() {{
    gunX += direction * 1.5;

    if (gunX < 200 || gunX > 650)
        direction *= -1;

    gun.setAttribute("transform", `translate(${gunX-400},0)`);
    requestAnimationFrame(moveGun);
}}

moveGun();

// Shooting sound
function playSound() {{
    const audio = new Audio("https://actions.google.com/sounds/v1/alarms/beep_short.ogg");
    audio.volume = 0.2;
    audio.play();
}}

function shoot() {{

    playSound();

    const bullet = document.createElementNS("http://www.w3.org/2000/svg","circle");
    bullet.setAttribute("cx", gunX + 25);
    bullet.setAttribute("cy", ''' + str(gun_y) + ''');
    bullet.setAttribute("r", 4);
    bullet.setAttribute("fill", "''' + BULLET_COLOR + '''");

    bulletsGroup.appendChild(bullet);

    let interval = setInterval(() => {{

        let cy = parseFloat(bullet.getAttribute("cy"));
        bullet.setAttribute("cy", cy - 4);

        const boxes = boxesGroup.querySelectorAll("rect");

        boxes.forEach(box => {{
            let bx = parseFloat(box.getAttribute("x"));
            let by = parseFloat(box.getAttribute("y"));

            if (gunX + 25 > bx &&
                gunX + 25 < bx + {BOX_SIZE} &&
                cy < by + {BOX_SIZE} &&
                cy > by) {{

                // Explosion effect
                const explosion = document.createElementNS("http://www.w3.org/2000/svg","circle");
                explosion.setAttribute("cx", bx + {BOX_SIZE}/2);
                explosion.setAttribute("cy", by + {BOX_SIZE}/2);
                explosion.setAttribute("r", 2);
                explosion.setAttribute("fill", "orange");
                effectsGroup.appendChild(explosion);

                explosion.animate([
                    {{r:2, opacity:1}},
                    {{r:15, opacity:0}}
                ], {{
                    duration:300
                }});

                box.remove();
                bullet.remove();
                clearInterval(interval);
            }}
        }});

        if (cy < 0) {{
            bullet.remove();
            clearInterval(interval);
        }}

    }}, 16);
}}

setInterval(shoot, 900);

]]></script>

</svg>
'''

    return svg


def main():
    with open("shooting-game.svg", "w") as f:
        f.write(generate_svg())

    print("🔥 Advanced shooting-game.svg generated!")


if __name__ == "__main__":
    main()
