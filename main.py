# import math
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*\
#             math.cos(2*k)-2*\
#             math.cos(3*k)-\
#             math .cos(4*k)
# speed(10000)
# bgcolor("black")
# for i in range(10000):
#     goto(hearta(i)*20, heartb(i)*20)
#     for j in range(5):
#         color("magenta3")
#     goto(0,0)
# done()
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