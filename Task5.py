# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

x1 = float(input('Введите координату х для первой точки: '))
y1 = float(input('Введите координату y для первой точки: '))
x2 = float(input('Введите координату х для второй точки: '))
y2 = float(input('Введите координату y для второй точки: '))
from math import sqrt
print('Расстояние между этими точками: ', round(sqrt((x1 - x2)**2 + (y1 - y2)**2), 2))