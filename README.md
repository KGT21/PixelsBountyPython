# Oil Painting Simulation Application

A realistic oil painting simulator that creates beautiful brush strokes with each keypress, featuring authentic oil paint blending and high-quality artistic effects.

## Features

### 🎨 Realistic Oil Painting Effects
- **Multi-bristle brush strokes**: Each stroke consists of multiple individual bristles for authentic texture
- **Realistic color blending**: New paint mixes with existing colors using subtractive color mixing (like real pigments)
- **Pressure variation**: Strokes vary from thick (high pressure) at the beginning to thin at the end
- **Natural paint flow**: Colors blend, blur, and flow together mimicking wet oil paint behavior
- **High-quality rendering**: Detailed brush strokes with shadows and artistic appearance

### 🖥️ User Interface
- **Windows compatibility**: Optimized for smooth performance on Windows systems
- **Simple interaction**: Press any key to create a new brush stroke
- **Real-time painting**: Watch your oil painting build up stroke by stroke
- **60 FPS rendering**: Smooth, fluid performance

### 🛠️ Technical Implementation
- **Advanced graphics**: Built using pygame and numpy for high-performance rendering
- **Realistic physics**: Oil paint mixing simulation with proper color theory
- **Optimized performance**: Efficient algorithms for smooth real-time painting
- **Cross-platform**: Works on Windows, Linux, and macOS

## Installation

1. Ensure you have Python 3.7+ installed
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application
```bash
python main.py
```

### Controls
- **Any key**: Create a new brush stroke at a random location
- **ESC**: Exit the application
- **Close window**: Exit the application

### Testing the Application
Run the comprehensive test suite:
```bash
python test_oil_painting.py
```

Generate demo images:
```bash
python demo_generator.py
```

## File Structure

```
├── main.py              # Main oil painting application
├── requirements.txt     # Dependencies (pygame, numpy)
├── test_oil_painting.py # Comprehensive test suite
├── demo_generator.py    # Creates demo images showcasing effects
└── README.md           # This file
```

## Technical Details

### Brush Stroke Realism
The application implements several techniques to achieve realistic oil painting effects:

1. **Multi-bristle simulation**: Each brush stroke consists of 8-20 individual bristles with varying positions, thickness, and opacity
2. **Pressure modeling**: Stroke thickness and opacity vary along the stroke path to simulate brush pressure
3. **Color variation**: Each bristle can have slight color variations within the same stroke
4. **Texture generation**: Random offsets and variations create natural, organic brush textures

### Oil Paint Blending Physics
The color blending system mimics real oil paint behavior:

1. **Subtractive color mixing**: Colors mix like real pigments, not like digital light
2. **Wet-on-wet effects**: New paint blends naturally with existing wet paint
3. **Color bleeding**: Slight color bleeding effects for more natural appearance
4. **Non-destructive blending**: New strokes enhance rather than overwrite existing colors

### Performance Optimization
- **Efficient rendering**: Uses pygame's optimized surface operations
- **Smart blending**: Only processes areas with new paint
- **60 FPS target**: Maintains smooth performance even with complex brush strokes
- **Memory efficient**: Uses numpy arrays for fast color calculations

## Requirements Analysis

The application addresses all specified requirements:

✅ **Core Functionality**
- Runs on Windows with optimized performance
- Opens drawing window with pygame
- Creates new brush stroke with each keypress
- Realistic oil painting brush stroke style

✅ **Visual Quality**
- High-quality, detailed brush strokes
- Realistic shadows and artistic appearance
- Multi-pixel brush textures with bristle details

✅ **Paint Behavior**
- Paint builds up over time with each keypress
- Colors blend, blur, and flow naturally
- No simple overwriting - authentic wet paint mixing

✅ **Performance**
- Optimized for smooth Windows operation
- 60 FPS rendering with fluid interactions
- Efficient graphics processing

✅ **Realism Features**
- Bristle shape and texture variation
- Color and opacity variation within strokes
- Realistic paint deposition (thick to thin)
- Pressure effects on stroke appearance

## Demo Images

The application generates beautiful oil paintings. Run `python demo_generator.py` to create sample images showing:
- Light paintings (25 strokes)
- Medium complexity (50 strokes)
- Heavy, rich paintings (100+ strokes)

## Customization

You can modify various aspects of the painting:

### Colors
Edit the `color_palette` in `OilPaintingApp` to change available colors.

### Brush Properties
Modify brush size range, bristle count, or stroke length in the `generate_random_stroke()` method.

### Canvas Size
Change the default window size by modifying the parameters in the `OilPaintingApp()` initialization.

### Blending Behavior
Adjust the oil paint mixing algorithm in the `_mix_oil_colors()` method for different paint behaviors.

## License

This project is open source and available under the MIT License.