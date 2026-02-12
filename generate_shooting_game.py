#!/usr/bin/env python3
"""
Generate an animated SVG shooting game with a gun at the bottom shooting at green boxes.
The boxes are arranged like a GitHub contribution graph.
"""

import random
import math

# Configuration
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400
BOX_SIZE = 12
BOX_GAP = 4
COLS = 52  # Like GitHub contribution graph (52 weeks)
ROWS = 7   # 7 days of the week
GUN_WIDTH = 30
GUN_HEIGHT = 40
BULLET_RADIUS = 4
ANIMATION_DURATION = 20  # Total animation duration in seconds

# GitHub contribution colors (darker to lighter green)
COLORS = ["#0e4429", "#006d32", "#26a641", "#39d353"]
BG_COLOR = "#0d1117"  # GitHub dark background
GUN_COLOR = "#58a6ff"
BULLET_COLOR = "#f85149"

def generate_svg():
    """Generate the animated shooting game SVG."""
    
    # Calculate grid dimensions
    grid_width = COLS * (BOX_SIZE + BOX_GAP) - BOX_GAP
    grid_height = ROWS * (BOX_SIZE + BOX_GAP) - BOX_GAP
    
    # Center the grid
    grid_x = (CANVAS_WIDTH - grid_width) // 2
    grid_y = 40  # Top margin
    
    # Gun position (centered at bottom)
    gun_x = CANVAS_WIDTH // 2 - GUN_WIDTH // 2
    gun_y = CANVAS_HEIGHT - GUN_HEIGHT - 10
    
    # Generate random box colors
    boxes = []
    for row in range(ROWS):
        for col in range(COLS):
            x = grid_x + col * (BOX_SIZE + BOX_GAP)
            y = grid_y + row * (BOX_SIZE + BOX_GAP)
            color = random.choice(COLORS)
            boxes.append({
                'x': x,
                'y': y,
                'color': color,
                'id': f'box_{row}_{col}'
            })
    
    # Generate bullet paths (multiple bullets shooting up)
    num_bullets = 15
    bullets = []
    for i in range(num_bullets):
        start_time = i * (ANIMATION_DURATION / num_bullets)
        # Vary x position slightly around center
        bullet_x = CANVAS_WIDTH // 2 + random.randint(-100, 100)
        
        bullets.append({
            'id': f'bullet_{i}',
            'x': bullet_x,
            'start_y': gun_y,
            'end_y': 0,
            'start_time': start_time,
            'duration': 2.5
        })
    
    # Start building SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}" viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">
  <defs>
    <style>
      @keyframes fadeOut {{
        0%   {{ opacity: 1; }}
        100% {{ opacity: 0; }}
      }}
      
      @keyframes shoot {{
        0%   {{ cy: {gun_y}; opacity: 1; }}
        95%  {{ cy: 0; opacity: 1; }}
        100% {{ cy: 0; opacity: 0; }}
      }}
      
      @keyframes flash {{
        0%, 100% {{ opacity: 0.3; }}
        50% {{ opacity: 1; }}
      }}
    </style>
  </defs>
  
  <!-- Background -->
  <rect width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}" fill="{BG_COLOR}"/>
  
  <!-- Title -->
  <text x="{CANVAS_WIDTH // 2}" y="25" text-anchor="middle" fill="#c9d1d9" font-family="monospace" font-size="18" font-weight="bold">
    🎯 Shooting Game
  </text>
  
  <!-- Boxes (contribution graph style) -->
  <g id="boxes">
'''
    
    # Add boxes with hit animations
    for i, box in enumerate(boxes):
        # Random hit time
        hit_time = random.uniform(0.5, ANIMATION_DURATION - 2)
        hit_duration = 0.5
        
        svg += f'''    <rect id="{box['id']}" x="{box['x']}" y="{box['y']}" width="{BOX_SIZE}" height="{BOX_SIZE}" 
          fill="{box['color']}" rx="2">
      <animate attributeName="opacity" values="1;0" begin="{hit_time}s" dur="{hit_duration}s" fill="freeze"/>
    </rect>
'''
    
    svg += '''  </g>
  
  <!-- Bullets -->
  <g id="bullets">
'''
    
    # Add bullets
    for bullet in bullets:
        svg += f'''    <circle id="{bullet['id']}" cx="{bullet['x']}" cy="{bullet['start_y']}" r="{BULLET_RADIUS}" fill="{BULLET_COLOR}">
      <animate attributeName="cy" from="{bullet['start_y']}" to="{bullet['end_y']}" 
        begin="{bullet['start_time']}s" dur="{bullet['duration']}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;1;1;0" 
        begin="{bullet['start_time']}s" dur="{bullet['duration']}s" repeatCount="indefinite"/>
    </circle>
'''
    
    svg += '''  </g>
  
  <!-- Gun/Shooter -->
  <g id="gun">
'''
    
    # Draw simple gun shape
    barrel_x = CANVAS_WIDTH // 2 - 3
    barrel_y = gun_y
    barrel_width = 6
    barrel_height = 25
    
    base_x = gun_x
    base_y = gun_y + barrel_height
    base_width = GUN_WIDTH
    base_height = GUN_HEIGHT - barrel_height
    
    svg += f'''    <!-- Barrel -->
    <rect x="{barrel_x}" y="{barrel_y}" width="{barrel_width}" height="{barrel_height}" 
      fill="{GUN_COLOR}" rx="2">
      <animate attributeName="opacity" values="1;0.7;1" dur="0.3s" repeatCount="indefinite"/>
    </rect>
    
    <!-- Base -->
    <rect x="{base_x}" y="{base_y}" width="{base_width}" height="{base_height}" 
      fill="{GUN_COLOR}" rx="3"/>
    
    <!-- Muzzle flash effect -->
    <circle cx="{CANVAS_WIDTH // 2}" cy="{barrel_y}" r="8" fill="{BULLET_COLOR}" opacity="0">
      <animate attributeName="opacity" values="0;0.8;0" dur="0.15s" repeatCount="indefinite"/>
    </circle>
  </g>
  
  <!-- Score/Info text -->
  <text x="{CANVAS_WIDTH // 2}" y="{CANVAS_HEIGHT - 10}" text-anchor="middle" 
    fill="#8b949e" font-family="monospace" font-size="14">
    🎮 Auto-shooting at GitHub contribution boxes!
  </text>
  
  <!-- Loop animation -->
  <animate attributeName="opacity" values="1" dur="{ANIMATION_DURATION}s" repeatCount="indefinite"/>
  
</svg>'''
    
    return svg

def main():
    """Main function to generate and save the SVG."""
    svg_content = generate_svg()
    
    # Save to file
    output_file = "shooting-game.svg"
    with open(output_file, "w") as f:
        f.write(svg_content)
    
    print(f"✅ Generated {output_file}")
    print(f"   Size: {CANVAS_WIDTH}x{CANVAS_HEIGHT}")
    print(f"   Boxes: {COLS}x{ROWS}")
    print(f"   Animation duration: {ANIMATION_DURATION}s")

if __name__ == "__main__":
    main()
