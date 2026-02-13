def generate_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" 
     width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
     viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">

<style>
    .box {{
        rx: 2;
    }}
</style>

<rect width="100%" height="100%" fill="{BG_COLOR}" />

<g id="boxes"></g>
<g id="bullets"></g>

<!-- Gun -->
<rect id="gun" x="{CANVAS_WIDTH//2}" 
      y="{CANVAS_HEIGHT-60}" 
      width="40" height="40" 
      fill="{GUN_COLOR}" rx="4"/>

<script><![CDATA[

const canvasWidth = {CANVAS_WIDTH};
const canvasHeight = {CANVAS_HEIGHT};
const boxSize = 12;
const gap = 4;
const cols = 52;
const rows = 7;

const colors = ["#0e4429","#006d32","#26a641","#39d353"];
const boxesGroup = document.getElementById("boxes");
const bulletsGroup = document.getElementById("bullets");
const gun = document.getElementById("gun");

let gunX = canvasWidth/2;
let bullets = [];
let boxes = [];

function createGrid() {{
    boxesGroup.innerHTML = "";
    boxes = [];
    let startX = (canvasWidth - (cols*(boxSize+gap))) / 2;
    let startY = 40;

    for(let r=0;r<rows;r++){{
        for(let c=0;c<cols;c++){{
            let x = startX + c*(boxSize+gap);
            let y = startY + r*(boxSize+gap);

            let rect = document.createElementNS("http://www.w3.org/2000/svg","rect");
            rect.setAttribute("x",x);
            rect.setAttribute("y",y);
            rect.setAttribute("width",boxSize);
            rect.setAttribute("height",boxSize);
            rect.setAttribute("fill",colors[Math.floor(Math.random()*4)]);
            rect.setAttribute("class","box");

            boxesGroup.appendChild(rect);
            boxes.push(rect);
        }}
    }}
}}

function shoot() {{
    let bullet = document.createElementNS("http://www.w3.org/2000/svg","circle");
    bullet.setAttribute("cx",gunX+20);
    bullet.setAttribute("cy",canvasHeight-60);
    bullet.setAttribute("r",4);
    bullet.setAttribute("fill","#f85149");
    bulletsGroup.appendChild(bullet);

    bullets.push(bullet);
}}

function update() {{

    // Random gun movement
    gunX += (Math.random()-0.5)*10;
    if(gunX < 0) gunX = 0;
    if(gunX > canvasWidth-40) gunX = canvasWidth-40;
    gun.setAttribute("x",gunX);

    bullets.forEach((bullet,i)=>{{
        let cy = parseFloat(bullet.getAttribute("cy"));
        cy -= 8;
        bullet.setAttribute("cy",cy);

        // Collision detection
        boxes.forEach((box,j)=>{{
            if(!box) return;

            let bx = parseFloat(box.getAttribute("x"));
            let by = parseFloat(box.getAttribute("y"));

            if(cy < by+boxSize && 
               cy > by &&
               parseFloat(bullet.getAttribute("cx")) > bx &&
               parseFloat(bullet.getAttribute("cx")) < bx+boxSize) {{

                boxesGroup.removeChild(box);
                boxes[j] = null;

                bulletsGroup.removeChild(bullet);
                bullets[i] = null;
            }}
        }});

        if(cy < 0 && bullet.parentNode) {{
            bulletsGroup.removeChild(bullet);
            bullets[i] = null;
        }}
    }});

    // Regenerate grid if all destroyed
    if(boxes.every(b=>b===null)) {{
        createGrid();
    }}

    requestAnimationFrame(update);
}}

createGrid();
setInterval(shoot,500);
update();

]]></script>
</svg>'''
