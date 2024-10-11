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

- Recap on Python Basics
  - Running python on windows 
  - Python Interpreter CLI (show iPython)

  - Comparisons 
  - Control Flow (if, elif, else, for, while)

- Recap on Lists / Tuples / List Comprehensions (mult. element vise .* is
  matlab)

len(a) returns the length of a, i.e. the number of elements it contains,
max(a) returns the largest element of a,
min(a) returns the smallest element of a,
sum(a) returns the sum of the elements of a,
a.sort() sorts the elements of a,
a.append(x) adds a new element at the end of the listw, containing the contents of x,
a.insert(i, x) adds a new element containing x at location `a[i]``, shifting later elements ‘backwards’ by one,
a.remove(x) finds the first occurrence of x in the list and removes it,
a.count(x) counts the number of occurrences of x in the list,
a.index(x) returns the index of the first occurrence of x in the list,
a.reverse() flips the order of elements in a list, and
a.pop(i) removes and return the element at index i in the list (or if no
argument is provided, the last element in the list).

- Dictionaries (show how variables are referenced again, in dicts)

- Packages / Modules / Libraries

- Matplotlib (plotting data)