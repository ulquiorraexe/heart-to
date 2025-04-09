# Heart Shape with Turtle

This project demonstrates how to create a heart shape using Python's `turtle` graphics library. The heart shape is created by plotting points based on mathematical equations for the x and y coordinates. You can run the script in either of two versions: with or without the commented-out code. Below is an explanation of how both versions work.

## Requirements

- Python 3.x
- `turtle` library (usually comes with Python)
- `math` library (also comes with Python)

## How It Works

### Version 1: With Commented-Out Code
In this version, the code is commented out, and when you run the script, it draws the heart shape with a pink background (`bgcolor("black")`) and the heart itself drawn in black. Here's how it works:

1. **Math Functions for Heart Shape**:
   - `hearta(k)`: This function calculates the x-coordinate of the heart shape based on the sine function.
   - `heartb(k)`: This function calculates the y-coordinate of the heart shape based on a combination of cosine functions.

2. **Turtle Movement**:
   - The turtle moves based on the calculated x and y values (`hearta(i)*20` and `heartb(i)*20`), where `i` ranges from `0` to `10000`, covering the entire curve of the heart shape.
   - A loop draws the shape by calculating the next point and moving the turtle there.

3. **Final Appearance**:
   - The code uses a `for` loop to create 10000 points for the heart.
   - The heart is drawn in magenta and then filled with black.

```python
# import math
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)
# speed(10000)
# bgcolor("black")
# for i in range(10000):
#     goto(hearta(i)*20, heartb(i)*20)
#     for j in range(5):
#         color("magenta3")
#     goto(0,0)
# done()
```

### Version 2: Without Commented-Out Code
In this version, the heart shape is drawn similarly, but with slight differences in the loop range and turtle settings:

1. **Math Functions for Heart Shape**:
   - `hearta(k)` and `heartb(k)` functions remain the same, but now the loop runs from `0` to `628` (which corresponds to `0` to `2π` when using radians).

2. **Turtle Movement**:
   - The code moves the turtle based on the calculated x and y values (`hearta(i / 100) * 20` and `heartb(i / 100) * 20`), where `i` now increments from `0` to `628`, dividing the range by 100. This gives a smoother curve.

3. **Final Appearance**:
   - This version uses `speed(10000)` to make the turtle draw faster.
   - The heart shape is drawn with a background color of `magenta3` and the heart itself drawn in black.

```python
import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

speed(10000)
bgcolor("magenta3")
color("black")

for i in range(0, 628):  # 0'dan 2*pi'ye kadar bir döngü.
    x = hearta(i / 100) * 20
    y = heartb(i / 100) * 20
    goto(x, y)

done()
```

## Installation

To install and run the Heart Shape Drawing project, follow the steps below:

  1. Clone the repository to your local machine:
     ```bash
     git clone https://github.com/ulquiorraexe/heart-to.git

  2. Navigate into the project directory:
     ```bash
     cd heart-to

  3. Install the required dependencies:
     - You will need Python 3.x and the turtle module (which comes pre-installed with Python).

  4. Run the script:
     ```bash
     python main.py

## License

This project does not have a license.
