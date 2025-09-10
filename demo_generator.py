"""
Demo generator for the Oil Painting Simulation
Creates sample images to demonstrate the oil painting effects.
"""

import pygame
import numpy as np
import random
import math
from main import OilPaintingCanvas, BrushStroke


def create_demo_painting(width=800, height=600, num_strokes=50):
    """Create a demo painting with multiple brush strokes."""
    pygame.init()
    
    canvas = OilPaintingCanvas(width, height)
    
    # Color palette for the demo
    color_palette = [
        (120, 80, 40),    # Brown
        (180, 140, 100),  # Light brown
        (60, 120, 60),    # Green
        (100, 150, 200),  # Blue
        (200, 100, 100),  # Red
        (150, 100, 200),  # Purple
        (200, 200, 100),  # Yellow
        (100, 100, 100),  # Gray
        (50, 30, 20),     # Dark brown
        (220, 180, 140),  # Beige
        (80, 50, 30),     # Darker brown
        (200, 150, 100),  # Orange
    ]
    
    print(f"Creating demo painting with {num_strokes} brush strokes...")
    
    for i in range(num_strokes):
        # Generate random stroke
        start_x = random.randint(50, width - 50)
        start_y = random.randint(50, height - 50)
        
        angle = random.uniform(0, 2 * math.pi)
        length = random.randint(40, 150)
        
        end_x = start_x + int(length * math.cos(angle))
        end_y = start_y + int(length * math.sin(angle))
        
        # Keep within bounds
        end_x = max(0, min(width - 1, end_x))
        end_y = max(0, min(height - 1, end_y))
        
        color = random.choice(color_palette)
        brush_size = random.randint(20, 50)
        
        stroke = BrushStroke((start_x, start_y), (end_x, end_y), color, brush_size)
        canvas.add_brush_stroke(stroke)
        
        if (i + 1) % 10 == 0:
            print(f"Added {i + 1}/{num_strokes} strokes")
    
    return canvas


def save_demo_images():
    """Generate and save demo images."""
    print("Generating oil painting demonstrations...")
    
    # Create different demo paintings
    demos = [
        ("demo_light.png", 25, "Light painting with 25 strokes"),
        ("demo_medium.png", 50, "Medium painting with 50 strokes"), 
        ("demo_heavy.png", 100, "Heavy painting with 100 strokes")
    ]
    
    for filename, stroke_count, description in demos:
        print(f"\nCreating {description}...")
        canvas = create_demo_painting(800, 600, stroke_count)
        
        # Save the canvas surface as an image
        pygame.image.save(canvas.surface, filename)
        print(f"Saved: {filename}")
    
    print("\nDemo images generated successfully!")
    print("The application creates realistic oil painting effects with:")
    print("- Realistic brush stroke textures with multiple bristles")
    print("- Natural color blending that mimics wet oil paint behavior")
    print("- Pressure variation effects (thick to thin strokes)")
    print("- High-quality artistic appearance with detailed shadows and highlights")


if __name__ == "__main__":
    save_demo_images()