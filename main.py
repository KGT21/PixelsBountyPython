"""
Oil Painting Simulation Application

A realistic oil painting simulator that creates brush strokes with each keypress.
Features realistic blending, texture, and high-quality artistic effects.
"""

import pygame
import numpy as np
import random
import math
import sys
from typing import Tuple, List


class BrushStroke:
    """Represents a single brush stroke with realistic oil painting properties."""
    
    def __init__(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int], 
                 color: Tuple[int, int, int], brush_size: int = 20):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.brush_size = brush_size
        self.bristles = self._generate_bristles()
        
    def _generate_bristles(self) -> List[Tuple[Tuple[int, int], Tuple[int, int], int, int]]:
        """Generate individual bristles for realistic texture."""
        bristles = []
        num_bristles = max(8, self.brush_size // 2)  # More bristles for larger brushes
        
        for _ in range(num_bristles):
            # Add randomness to bristle positions
            start_offset_x = random.randint(-self.brush_size//2, self.brush_size//2)
            start_offset_y = random.randint(-self.brush_size//2, self.brush_size//2)
            end_offset_x = random.randint(-self.brush_size//2, self.brush_size//2)
            end_offset_y = random.randint(-self.brush_size//2, self.brush_size//2)
            
            bristle_start = (
                self.start_pos[0] + start_offset_x,
                self.start_pos[1] + start_offset_y
            )
            bristle_end = (
                self.end_pos[0] + end_offset_x,
                self.end_pos[1] + end_offset_y
            )
            
            # Varying bristle thickness and opacity
            thickness = random.randint(1, max(2, self.brush_size // 8))
            opacity = random.randint(100, 255)
            
            bristles.append((bristle_start, bristle_end, thickness, opacity))
            
        return bristles


class OilPaintingCanvas:
    """Main canvas for the oil painting simulation."""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surface.fill((255, 255, 255))  # White canvas background
        
        # Track paint layers for realistic blending
        self.paint_layers = np.zeros((height, width, 4), dtype=np.float32)
        self.paint_layers[:, :, 3] = 255.0  # Initial alpha
        self.paint_layers[:, :, 0] = 255.0  # White background
        self.paint_layers[:, :, 1] = 255.0
        self.paint_layers[:, :, 2] = 255.0
        
    def add_brush_stroke(self, stroke: BrushStroke):
        """Add a brush stroke to the canvas with realistic oil paint blending."""
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Draw each bristle of the brush stroke
        for bristle_start, bristle_end, thickness, opacity in stroke.bristles:
            # Create color variation within the stroke
            color_variation = [
                max(0, min(255, stroke.color[0] + random.randint(-20, 20))),
                max(0, min(255, stroke.color[1] + random.randint(-20, 20))),
                max(0, min(255, stroke.color[2] + random.randint(-20, 20))),
                opacity
            ]
            
            # Draw bristle path with varying pressure
            self._draw_bristle_path(temp_surface, bristle_start, bristle_end, 
                                  color_variation, thickness)
        
        # Apply oil paint blending to the main surface
        self._blend_oil_paint(temp_surface)
        
    def _draw_bristle_path(self, surface, start_pos, end_pos, color, thickness):
        """Draw a single bristle path with pressure variation."""
        distance = math.sqrt((end_pos[0] - start_pos[0])**2 + 
                           (end_pos[1] - start_pos[1])**2)
        
        if distance < 1:
            # Single point
            pygame.draw.circle(surface, color[:3], start_pos, thickness)
            return
            
        # Draw path with varying thickness (pressure simulation)
        num_points = max(5, int(distance / 2))
        
        for i in range(num_points):
            t = i / (num_points - 1) if num_points > 1 else 0
            
            # Interpolate position
            x = int(start_pos[0] + t * (end_pos[0] - start_pos[0]))
            y = int(start_pos[1] + t * (end_pos[1] - start_pos[1]))
            
            # Pressure variation - more paint at beginning, less at end
            pressure_factor = 1.2 - 0.4 * t  # Start thick, end thinner
            current_thickness = max(1, int(thickness * pressure_factor))
            
            # Opacity variation
            current_opacity = int(color[3] * (0.8 + 0.2 * (1 - t)))
            current_color = (color[0], color[1], color[2], current_opacity)
            
            if 0 <= x < self.width and 0 <= y < self.height:
                pygame.draw.circle(surface, current_color[:3], (x, y), current_thickness)
    
    def _blend_oil_paint(self, new_stroke_surface):
        """Blend new paint with existing paint using oil painting physics."""
        # Convert pygame surface to numpy array for blending calculations
        new_stroke_array = pygame.surfarray.array3d(new_stroke_surface)
        new_stroke_array = np.transpose(new_stroke_array, (1, 0, 2))
        
        # Get alpha channel from the new stroke
        alpha_array = pygame.surfarray.array_alpha(new_stroke_surface)
        alpha_array = np.transpose(alpha_array)
        
        # Oil paint blending: mix colors based on alpha and existing paint
        for y in range(self.height):
            for x in range(self.width):
                if alpha_array[y, x] > 0:  # There's new paint here
                    alpha_factor = alpha_array[y, x] / 255.0
                    
                    # Mix colors with wet oil paint behavior
                    existing_color = self.paint_layers[y, x, :3]
                    new_color = new_stroke_array[y, x]
                    
                    # Oil paint mixing simulation
                    mixed_color = self._mix_oil_colors(existing_color, new_color, alpha_factor)
                    self.paint_layers[y, x, :3] = mixed_color
        
        # Update the pygame surface
        self._update_surface_from_layers()
    
    def _mix_oil_colors(self, existing: np.ndarray, new: np.ndarray, alpha: float) -> np.ndarray:
        """Simulate realistic oil paint color mixing."""
        # Oil paints mix differently than digital colors
        # They blend more naturally, with some color bleeding
        
        # Convert to float for calculations
        existing = existing.astype(np.float32)
        new = new.astype(np.float32)
        
        # Subtractive color mixing (more realistic for paint)
        # This simulates how pigments interact
        mixed = existing * (1 - alpha * 0.7) + new * alpha * 0.7
        
        # Add slight color bleeding effect
        bleeding_factor = 0.1
        mixed = mixed * (1 - bleeding_factor) + (existing + new) * 0.5 * bleeding_factor
        
        return np.clip(mixed, 0, 255)
    
    def _update_surface_from_layers(self):
        """Update the pygame surface from the paint layers."""
        # Convert paint layers to surface
        surface_array = self.paint_layers[:, :, :3].astype(np.uint8)
        surface_array = np.transpose(surface_array, (1, 0, 2))
        pygame.surfarray.blit_array(self.surface, surface_array)


class OilPaintingApp:
    """Main application class for the oil painting simulator."""
    
    def __init__(self, width: int = 1024, height: int = 768):
        pygame.init()
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Oil Painting Simulator - Press any key to paint!")
        
        self.canvas = OilPaintingCanvas(width, height)
        self.clock = pygame.time.Clock()
        
        # Color palette for brush strokes
        self.color_palette = [
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
        ]
        
        self.stroke_count = 0
        
    def generate_random_stroke(self) -> BrushStroke:
        """Generate a random brush stroke."""
        # Random start position
        start_x = random.randint(50, self.width - 50)
        start_y = random.randint(50, self.height - 50)
        
        # Random stroke direction and length
        angle = random.uniform(0, 2 * math.pi)
        length = random.randint(30, 120)
        
        end_x = start_x + int(length * math.cos(angle))
        end_y = start_y + int(length * math.sin(angle))
        
        # Keep end position within bounds
        end_x = max(0, min(self.width - 1, end_x))
        end_y = max(0, min(self.height - 1, end_y))
        
        # Random color from palette
        color = random.choice(self.color_palette)
        
        # Random brush size
        brush_size = random.randint(15, 40)
        
        return BrushStroke((start_x, start_y), (end_x, end_y), color, brush_size)
    
    def run(self):
        """Main application loop."""
        running = True
        
        print("Oil Painting Simulator Started!")
        print("Press any key to create a brush stroke")
        print("Press ESC or close window to exit")
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    else:
                        # Any other key creates a new brush stroke
                        stroke = self.generate_random_stroke()
                        self.canvas.add_brush_stroke(stroke)
                        self.stroke_count += 1
                        print(f"Brush stroke #{self.stroke_count} added")
            
            # Clear screen and draw canvas
            self.screen.fill((240, 240, 240))  # Light gray background
            self.screen.blit(self.canvas.surface, (0, 0))
            
            # Add title text
            font = pygame.font.Font(None, 36)
            title_text = font.render("Oil Painting Simulator", True, (50, 50, 50))
            self.screen.blit(title_text, (10, 10))
            
            # Instructions
            font_small = pygame.font.Font(None, 24)
            instruction_text = font_small.render(f"Press any key to paint | Strokes: {self.stroke_count} | ESC to exit", True, (100, 100, 100))
            self.screen.blit(instruction_text, (10, 50))
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS for smooth performance
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    # Create and run the oil painting application
    app = OilPaintingApp(1024, 768)
    app.run()
