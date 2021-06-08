Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = [1,2,3,4,5,6,7]
>>> list(range(8,21))
[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> for number in range(8,21)
SyntaxError: invalid syntax
>>> for number in range(8,21):
	numbers.append(number)

	
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> details = [XBOX 360 | 150 | New ]
SyntaxError: invalid syntax
>>> details = ['XBOX 360 | 150 | New']
>>> details
['XBOX 360 | 150 | New']
>>> details.index(|)
SyntaxError: invalid syntax
>>> details.index('|')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    details.index('|')
ValueError: '|' is not in list
>>> details.index[|]
SyntaxError: invalid syntax
>>> details.index['|']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    details.index['|']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> Product = details[0]
>>> product
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    product
NameError: name 'product' is not defined
>>> Product
'XBOX 360 | 150 | New'
>>> details = data.split('|')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    details = data.split('|')
NameError: name 'data' is not defined
>>> details
['XBOX 360 | 150 | New']
>>> details = data.split('|')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    details = data.split('|')
NameError: name 'data' is not defined
>>> detailer = details.split('|')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    detailer = details.split('|')
AttributeError: 'list' object has no attribute 'split'
>>> details
['XBOX 360 | 150 | New']
>>> data
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> data = ['XBOX 360 | 150 | New']
>>> details = data.split('|')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    details = data.split('|')
AttributeError: 'list' object has no attribute 'split'
>>> product, price , condition = data.split('|')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    product, price , condition = data.split('|')
AttributeError: 'list' object has no attribute 'split'
>>> product, price , condition = details.split('|')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    product, price , condition = details.split('|')
AttributeError: 'list' object has no attribute 'split'
>>> data = 'Xbox 360 | 150 | New'
>>> details = data.index('|')
>>> data
'Xbox 360 | 150 | New'
>>> details
9
>>> product , price , condition = data.split('|')
>>> product
'Xbox 360 '
>>> price
' 150 '
>>> condition
' New'
>>> muscle_cars = ['Ford | Dodge | Chevrolet']
>>> blueoval , Ram , BowTie = data.index('|')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    blueoval , Ram , BowTie = data.index('|')
TypeError: cannot unpack non-iterable int object
>>> blueoval , Ram , BowTie = data.split('|')
>>> blueoval
'Xbox 360 '
>>> blueoval , Ram , BowTie = muscle_cars.split('|')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    blueoval , Ram , BowTie = muscle_cars.split('|')
AttributeError: 'list' object has no attribute 'split'
>>>  muscle_cars = 'Ford | Dodge | Chevrolet'
 
SyntaxError: unexpected indent
>>> muscle_cars = ['Ford | Dodge | Chevrolet']
>>> blueoval , Ram , Bowtie = data.split('|')
>>> blueoval
'Xbox 360 '
>>> blueoval , Ram , Bowtie = muscle_cars.split(|)
SyntaxError: invalid syntax
>>> blueoval , Ram , Bowtie = muscle_cars.split('|')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    blueoval , Ram , Bowtie = muscle_cars.split('|')
AttributeError: 'list' object has no attribute 'split'
>>> muscle_cars
['Ford | Dodge | Chevrolet']
>>>  muscle_cars = 'Ford | Dodge | Chevrolet'
 
SyntaxError: unexpected indent
>>> muscle_cars = 'Ford | Dodge | Chevrolet'
>>> Blueoval , Ram , Bowtie = data.split('|')
>>> BLueoval
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    BLueoval
NameError: name 'BLueoval' is not defined
>>> Blueoval
'Xbox 360 '
>>> Blueoval , Ram , Bowtie = muscle_cars.split('|')
>>> Blueoval
'Ford '
>>> RAm
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    RAm
NameError: name 'RAm' is not defined
>>> Ram
' Dodge '
>>> Bowtie
' Chevrolet'
>>> muscle_cars = 'Ford | Dodge | Chevy'
>>> Blue , Red , Gold = data.split('|')
>>> muscle_cars = 'Ford | Dodge | Chevy'
>>> Blue , Red , Gold = muscle_cars.split('|')
>>> Blue
'Ford '
>>> Red
' Dodge '
>>> Gold
' Chevy'
>>> SingleEngine = 'Cessna 172 , Cirrus SR22 , Piper Bonanza , Carbon Cub'
>>> SiingleEngine
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    SiingleEngine
NameError: name 'SiingleEngine' is not defined
>>> SingleEngine
'Cessna 172 , Cirrus SR22 , Piper Bonanza , Carbon Cub'
>>> 170 , 200 , 170 , 120 = SingleEngine.split(',')
SyntaxError: can't assign to literal
>>> SingleEngine = 'Cessna 172 | Cirrus SR22 | Piper Bonanza | Carbon Cub'
>>> 170 , 200 , 170 , 120 = SingleEngine.split('|')
SyntaxError: can't assign to literal
>>> '170' , '200' , '170' , '120' = SingleEngine.split('|')
SyntaxError: can't assign to literal
>>> Smallest, Small , Smaller = SingleEngine.split('|')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    Smallest, Small , Smaller = SingleEngine.split('|')
ValueError: too many values to unpack (expected 3)
>>> Smallest, Small , Smaller , Smallish = SingleEngine.split('|')
>>> Smallest
'Cessna 172 '
>>> Smallish
' Carbon Cub'
>>> Smaller
' Piper Bonanza '
>>> Small
' Cirrus SR22 '
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 16, in <module>
    Circle()
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 11, in Circle
    lawe_turtle.tight(90)
AttributeError: 'Turtle' object has no attribute 'tight'
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 16, in <module>
    Circle()
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 11, in Circle
    lawe_turtle.tight(90)
AttributeError: 'Turtle' object has no attribute 'tight'
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 4, in <module>
    lawe_turtle.pencolor(Red)
NameError: name 'Red' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 4, in <module>
    lawe_turtle.pencolor(Red)
NameError: name 'Red' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 4, in <module>
    lawe_turtle.pencolor(Red)
NameError: name 'Red' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 4, in <module>
    lawe_turtle.pencolor(Red)
NameError: name 'Red' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======

====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 5, in <module>
    lawe_turtle.right(90)
NameError: name 'lawe_turtle' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 9, in <module>
    lawe_turtle.forwad(100)
AttributeError: 'Turtle' object has no attribute 'forwad'
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 10, in <module>
    lawe_turle.left(90)
NameError: name 'lawe_turle' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 10, in <module>
    lawe_turle.left(90)
NameError: name 'lawe_turle' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 10, in <module>
    lawe_turle.left(90)
NameError: name 'lawe_turle' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
>>> phone_book = ['123-4567' '4564433']
>>> print(phone_book[1])
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(phone_book[1])
IndexError: list index out of range
>>> print phone_book
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(phone_book)?
>>> phone_book
['123-45674564433']
>>> print(phone_book[0])
123-45674564433
>>> print(phone_book[1])
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(phone_book[1])
IndexError: list index out of range
>>> #DICT[Key]--> value
>>> phonw_book = {'qazi': '123-456-7890' 'bob': '222-222-2222'}
SyntaxError: invalid syntax
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
['123-456-7890', 'sosah@sosah.com']
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
sosah@sosah.com
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
123-456-7890
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
333-333-3333
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
222-222-2222bob@bob.com
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 7, in <module>
    bob:['222-333-4444' 'bobpetersen@gmail.com'],
NameError: name 'bob' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 7, in <module>
    bob:['222-333-4444' 'bobpetersen@gmail.com'],
NameError: name 'bob' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 7, in <module>
    bob: ['222-333-4444' 'bobpetersen@gmail.com'],
NameError: name 'bob' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 8, in <module>
    mindy:['333-555-7979' 'mindyjackobson@mindy.com'],
NameError: name 'mindy' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 7, in <module>
    bob: ['222-333-4444', 'bobpetersen@gmail.com'],
NameError: name 'bob' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 12, in <module>
    print (phone_book[bob])
NameError: name 'bob' is not defined
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
['222-333-4444', 'bobpetersen@gmail.com']
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
['333-555-7979', 'mindyjackobson@mindy.com']
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
mindyjackobson@mindy.com
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/TurtleTest1.py", line 12, in <module>
    print (phone_book['mindy'][2])
IndexError: list index out of range
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
333-555-7979
>>> 
====== RESTART: C:/Users/User/Desktop/Practice exercises/TurtleTest1.py ======
mindyjackobson@mindy.com
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
sosahlawe@gmail.com
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
888-999-4649
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
888-999-4649
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 12, in <module>
    print (phone_book[::-1])
TypeError: unhashable type: 'slice'
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 12, in <module>
    print (phone_book[::-1])
TypeError: unhashable type: 'slice'
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 12, in <module>
    print (phone_book[-1])
KeyError: -1
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 12, in <module>
    print (phone_book[::])
TypeError: unhashable type: 'slice'
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 12, in <module>
    print (phone_book[1])
KeyError: 1
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
['sosahlawe@gmail.com', '888-999-4649']
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
moc.liamg@ewalhasos
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
moc.liamg@ewalhasos
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 14, in <module>
    email = phone_book[1]
KeyError: 1
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
moc.liamg@ewalhasos
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 14, in <module>
    email = phone_book['Lawe'][1]
KeyError: 'Lawe'
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
moc.liamg@ewalhasos
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
moc.liamg@ewalhasos
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
o
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
sosahlawe@gmail.com
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
sosahlawe@gmail.com
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 16, in <module>
    number , email = phone_book['lawe'].split[',']
AttributeError: 'list' object has no attribute 'split'
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 9, in <module>
    'lawe':['888-999-4649' | 'sosahlawe@gmail.com'],
TypeError: unsupported operand type(s) for |: 'str' and 'str'
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Practice exercises/CarteBlanche.py", line 9, in <module>
    'lawe':['888-999-4649' | 'sosahlawe@gmail.com'],
TypeError: unsupported operand type(s) for |: 'str' and 'str'
>>> False
False
>>> True
True
>>> if True:
	print("Hello")

	
Hello
>>> if false:
	print("hi")

	
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    if false:
NameError: name 'false' is not defined
>>> if False:
	print("hi")

	
>>> 5>5
False
>>> 5<5
False
>>> 5>3
True
>>> 5!=2
True
>>> 5>=5
True
>>> 
5=5
SyntaxError: can't assign to literal
>>> 5==5
True
>>> johnny_hours_worked = 40
>>> johnny_hours_worked > 40
False
>>> johnny_hours_worked >=40
True
>>> johnny_hours_worked ==40
True
>>> if johnny_hours_worked > 40:
	print("pay overtime")

	
>>> johnny_hours_worked > 40:
	
SyntaxError: invalid syntax
>>> johnny_hours_worked = 41
>>> if johnny_hours_worked > 40:
	print("Pay him overtime")

	
Pay him overtime
>>> if True:
	print("Pay him overtime")

	
Pay him overtime
>>> 
and
SyntaxError: invalid syntax
>>> 5 and 5
5
>>> True and True
True
>>> True and False
False
>>> math_homework = False
>>> long_essays+ False
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    long_essays+ False
NameError: name 'long_essays' is not defined
>>> long_essays =False
>>> pizza = True
>>> icecrean = True
>>> pizza and icecream
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    pizza and icecream
NameError: name 'icecream' is not defined
>>> pizza and icecrean
True
>>> False and True
False
>>> True and False
False
>>> True and True
True
>>> False or True
True
>>> poison = False
>>> pizza = true
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    pizza = true
NameError: name 'true' is not defined
>>> pizza = True
>>> pizza or poison
True
>>> 
True or False
True
>>> False or False
False
>>> not True
False
>>> not Fakse
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    not Fakse
NameError: name 'Fakse' is not defined
>>> not False
True
>>> not(True or False)
False
>>> 
True
True
>>> bob_hours_worked = 40
>>> if bob_hours_worked > 39:
	print('he worked overtime')

	
he worked overtime
>>> johnny_homework = True
>>> johnny_throw_out_garbage = True
>>> if johnny_homework and johnny_throw_out_garbage:
	print('johnny can play XBOX ONE')

	
johnny can play XBOX ONE
>>> not(johnny_homework or johnny_throw_out_garbage)
False
>>> human = 'rock'
>>> computer = 'scissors'
>>> if human == 'rock' and computer =='scissors:'
SyntaxError: invalid syntax
>>> human_score = 1
>>> 
>>> human_score
1
>>> computer ='bananas'
>>> if  human == 'rock ' and computer =='scissors':
	human_score=1

	
>>> if  human == 'rock ' and computer =='scissors':
	human_score=1
elseif human == 'rock' and computer =='bananas':
	
SyntaxError: invalid syntax
>>> elif human == 'rock' and computer =='bananas':
	
SyntaxError: invalid syntax
>>>  if  human == 'rock ' and computer =='scissors':
	human_score=1
elsif human == 'rock' and computer =='bananas':
	
SyntaxError: unexpected indent
>>> if  human == 'rock ' and computer =='scissors':
	human_score=1
elsif human == 'rock' and computer =='bananas':
	
SyntaxError: invalid syntax
>>> if  human == 'rock ' and computer =='scissors':
	human_score=1
elif human == 'rock' and computer =='bananas':
	computer_score = 0
	human_score= 0
	print('You cant pick anything other than rock paper or scissors ')

	
You cant pick anything other than rock paper or scissors 
>>>  if  human == 'rock ' and computer =='scissors':
	human_score=1
elif human == 'rock' and computer =='bananas':
	computer_score = 0
	human_score= 0
	print('You cant pick anything other than rock paper or scissors ')
	
SyntaxError: unexpected indent
>>> if computer != 'rock' or computer !='scissors' or computer != 'paper':
	print('Wrong Pick Again')

	
Wrong Pick Again
>>> computer = rock
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    computer = rock
NameError: name 'rock' is not defined
>>> if computer != 'rock' or computer !='scissors' or computer != 'paper':
	print('Wrong Pick Again')

	
Wrong Pick Again
>>> if computer != 'rock' and computer != 'scissors' and computer !='paper':
	print('Wrong Chice pick again')

	
Wrong Chice pick again
>>> computer = 'banana'
>>> if computer != 'rock' and computer != 'scissors' and computer !='paper':
	print('Wrong Chice pick again')

	
Wrong Chice pick again
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Hello
Hello
Hello
Hello
Hello
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
Hello
Hello
Hello
Hello
Hello
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
[0, 1, 2, 3, 4]
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
range(0, 5)
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
[0, 1, 2, 3, 4]
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
0
1
2
3
4
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
0
1
2
3
4
>>> 
===== RESTART: C:/Users/User/Desktop/Practice exercises/CarteBlanche.py =====
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
>>> 
