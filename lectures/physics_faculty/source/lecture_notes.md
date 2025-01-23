# Lessons on Data Analysis from CERN

## Lecture 1 - Motivation and intro to CERN 

## Lecture 2 - Introduction to Data Analysis (Python Basics installing, syntax, variables, data types)

- Interactive game with age - converting data to information. Clean and
  not-clean data. 

- The difference between applications and programming languages

  - Explain about scope, GUI, CLI, and learning curve
  
- Seminar - intro to python

https://docs.python.org/3/tutorial/introduction.html#id3

https://swcarpentry.github.io/shell-novice/instructor/02-filedir.html

https://www.simplilearn.com/tutorials/python-tutorial/python-variables

```python
import os
def clear():
    '''
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    '''
    os.system('cls||echo -e \\\\033c')
```
##  Lecture 3 - Computing Infrastructure (todo computing principles) (Python Basics IDEs / Scripting / container types functions )

- Start from Python Basics recap (for a student to do) (10 problems from L2)
- Show lists and dictionaries and functions 
- Explain where the problem with iPython is 
- Create a python file (wrong extension (show file extensions))
- Run in IDLE 
- Explain what VS Code is 
- Chosing Theme 
- Opening Files 
- IntelliSense
- Running code

- Go to Mac, show thesis and analysis 

- Set up GitHub Classroom 

## Lecture 4 - Computing Principles (matplotlib)

- history of computing at cern 
- Start with Unary, Binary, computing principles 

- 5 bananas exercise

- Recap on Python Basics
  - Running python on windows 
  - Python Interpreter CLI (show iPython)
  `%who`
  `%whos`
  input (default string)
  input cast to required 
- Comparisons 

  ==
  !=
  >
  <
  >= 
  <=

- Control Flow (if, elif, else, for, while)

- Recap on Lists / Tuples / List Comprehensions (mult. element vise .* is matlab)
  list slicing
  show `enumerate` and `zip` functions
  show list comprehension vs for loop 


- Lists (range with sum) (zip)

append()	Used for adding elements to the end of the List. 
2	copy()	It returns a shallow copy of a list
3	clear()	This method is used for removing all items from the list. 
4	count()	These methods count the elements.
5	extend()	Adds each element of an iterable to the end of the List
6	index()	Returns the lowest index where the element appears. 
7	insert()	Inserts a given element at a given index in a list. 
8	pop()	Removes and returns the last value from the List or the given index value.
9	remove()	Removes a given object from the List. 
10	reverse()	Reverses objects of the List in place.
11	sort()	Sort a List in ascending, descending, or user-defined order
12	min()	Calculates the minimum of all the elements of the List
13	max()	Calculates the maximum of all the elements of the List

- Dictionaries

- recap on functions
  - default arguments
  - keyword arguments
  - positional arguments
- Data structures FIFO LIFO 

- Packages / Modules / Libraries

# Lecture 5 Data Visualization and Matplotlib

- Matplotlib (plotting data)

# Lecture 6 - MarkDown, git, GitHub, 