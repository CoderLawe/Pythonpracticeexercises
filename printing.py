Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 25 *2
50
>>> 50+50
100
>>> 25(30*70)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    25(30*70)
TypeError: 'int' object is not callable
>>> 25(5+5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    25(5+5)
TypeError: 'int' object is not callable
>>> x=2
>>> y=3
>>> print(x+y)
5
>>> 
>>> import turtle
>>> my_turtle = turtle.Turtle()
>>> my_turtle.forward(100)
