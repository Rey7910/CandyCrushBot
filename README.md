# CandyCrushBot

Equipo: Andromeda

- Carlos Andrés Rios Rojas
- Reinaldo Toledo Leguizamón

## Description
An on-screen automation bot that plays Candy Crush–style levels automatically. It captures the game board via screenshot, classifies each candy (including specials) using RGB thresholds, builds a 9×9 matrix, selects the best move with a solver, and performs the swap via mouse drag.

## Key modules
- `lastVersionStar.py`: Main sensor + executor loop (default runner) using `solver2` and `actuators`.
- `VersionSpecialStar.py`: Variant with explicit special-candy detection.
- `solver2.py`: Move selector prioritizing chocolate creation, special combos, bombs, 4-in-a-row, then normal matches.
- `boardSolver.py`: Earlier solver variant.
- `actuators.py`: Translates grid coordinates to pixel drags (Acer Nitro 5 full-screen calibration).
- `candyCrushAgent.py`: Simple agent loop that repeatedly senses and acts.

## Requirements
- Python 3.x
- Dependencies: `pyautogui`, `Pillow`

## Usage
- Open the game in full-screen. If needed, adjust the screenshot region in `lastVersionStar.py`/`VersionSpecialStar.py` and the pixel factors in `actuators.py` to match your screen.
- Install deps and run:
```bash
pip install pyautogui Pillow
python candyCrushAgent.py
```

## Strategy and heuristics
- **Priority order (`solver2.py`)**:
  - **Make a color bomb ("chocolate")**: Prefer 5-in-a-row/column setups (`checkChoco`).
  - **Combine specials**: If a candy is adjacent to any special (value ≥ 10), combine them (`checkSpecial`).
  - **Create wrapped/explosive (T/L shapes)**: Look for T or L formations to produce bombs (`checkT`, `checkL`).
  - **Create striped (4-in-a-row)**: Seek straight 4 matches to produce line candies (`check4`).
  - **Basic 3-match**: Fall back to standard matches (`checkBasic1..4`).
- **Special detection variant**: `VersionSpecialStar.py` pre-detects specials from pixels and passes their coordinates to the solver to bias moves around them.
- **Fallbacks**: If nothing better is available, the solver may trigger an existing color bomb as a last resort.

## General flow
1. **Capture**: Take a screenshot of the board region `(125, 60, 790, 690)`.
2. **Sampling**: For each grid cell (9×9), sample center and surrounding pixels to build a feature set.
3. **Classification**: Map RGB thresholds to candy IDs, including specials (striped, wrapped, color bomb).
4. **Solve**: Compute the best move as `((row, col), (dy, dx))` using the priority scheme.
5. **Actuate**: Convert grid coordinates to screen pixels and perform a drag in the chosen direction.
6. **Loop**: Sleep briefly (~0.13s) and repeat.

Note: The pixel region and actuator calibration are tuned for an Acer Nitro 5 fullscreen layout. Adjust constants in `lastVersionStar.py`/`VersionSpecialStar.py` and `actuators.py` for other screens.