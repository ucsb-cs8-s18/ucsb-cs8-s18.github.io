---
num: "Lecture 1"
desc: "Orientation to the course"
ready: false
date: 2017-04-03 15:30:00.00-7:00
---

The syllabus is here:  <https://ucsb-cs8-s18.github.io/info/syllabus/>

# Some of the code from lecture

```python
import math

def factorialTable(limit):
    for i in range(limit):
        print(i,math.factorial(i))

```


```python
import turtle

fred = turtle.Turtle("turtle")
fred.color("green")

fred.forward(200)


def drawSquare(side):
  for i in range(4): 
    fred.forward(side)
    fred.right(90)
```

```python
for i in range(5):
	drawSquare(i * 20)

```


# Abstractions and Algorithms


(a review of part of the syllabus)

Abstractions and notation: three, index.

An index takes in as input a topic, and gives us back a page number.

A Point-of-Sale bar code scanner at a store checkout maps a barcode, to info about the item (description and price).

A FUNCTION in general, takes in an input (or a set of inputs) and gives us back a value.

In math, for example, 

f(x) = x<sup>2</sup>



# Learning Something New

* Basketball: drills vs. playing the game

* Swimming, Painting, Guitar

* Fixed vs. Growth Mindset

# Python REPL (Read Eval Print Loop)

Also called the Python Shell Prompt

```
login as: pconrad
pconrad@csil-01.cs.ucsb.edu's password:
Last login: Mon Aug  7 15:29:19 2017 from 98.188.150.204
-bash-4.3$
-bash-4.3$ python3
Python 3.4.3 (default, Aug  9 2016, 15:36:17)
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 2 + 7 *4
30
>>> 2 ** 3
8
>>> 2 ** 3 ** 2
512
>>> 2 * 3 * 4
24
>>> (2 * 3) * 4
24
>>> 2 * (3 * 4)
24
>>> (2 ** 3) ** 2
64
>>> 2 ** (3 ** 2)
512
>>>
```

Note that `**` is right associative, not left associative.

# The textbook and the homework

* Look over H00, H01, H02, and show the calendar.

# IDLE and Python




# For loops


This:

```
>>> for x in schools:
	print(x)

	
A
B
C
D
>>>
```

Is a short hand for this:


```
>>> x = schools[0]
>>> print(x)
A
>>> x = schools[1]
>>> print(x)
B
>>> x = schools[2]
>>> print(x)
C
>>> x = schools[3]
>>> print(x)
D
>>> 
```
