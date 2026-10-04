Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#IF, IFELSE

=========== RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/Day 9.py ===========
Marksheet of the student
-------------
grade D

=========== RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/Day 9.py ===========
Marksheet of the student
-------------
grade D
Marksheet of the student
-------------
enter the correct mark
5
5

=========== RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/Day 9.py ===========
Marksheet of the student
-------------
grade D
Marksheet of the student
-------------
enter the correct mark
Marksheet of the student
-------------
enter the correct mark
5
5

=========== RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/Day 9.py ===========
Marksheet of the student
-------------
grade D
Marksheet of the student
-------------
enter the correct mark
Marksheet of the student
-------------
enter the correct mark
5
5

=========== RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/Day 9.py ===========
Marksheet of the student
-------------
grade D
Marksheet of the student
-------------
enter the correct mark
Marksheet of the student
-------------
enter your mark:5
enter the correct mark
100
100

#NESTED else
age=8
weight=4
if age>=10:
    print('eligible')
    else:
        
SyntaxError: invalid syntax
age=7
weight=8
if age>50:
    if weight>=50:
        print('eligible')
    else('weight is not eligible')
    
SyntaxError: expected ':'

if age>50:
    if weight>=50:
        print('eligible')
    else:
        print('weight is not eligible')
else:
    print('age is not eligible')

    
age is not eligible
age is not eligible
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    age is not eligible
NameError: name 'eligible' is not defined
45
45
45
45
age=7
weight=8
SyntaxError: multiple statements found while compiling a single statement
age=58
weight=87
if age>50:
    if weight>=50:
        print('eligible')
    else:
        print('weight is not eligible')
else:
    print('age is not eligible')

    
eligible
age=48
weight=87
if age>50:
    if weight>=50:
        print('eligible')
    else:
        print('weight is not eligible')
else:
    print('age is not eligible')
    
SyntaxError: multiple statements found while compiling a single statement
age=48
weight=87
if age>50:
    if weight>=50:
        print('eligible')
    else:
        print('weight is not eligible')
else:
    print('age is not eligible')

    
age is not eligible

 
#LOOPS
characters=["dora","bujji","jaggu","tuntun","kalia","bheem"]
characters
['dora', 'bujji', 'jaggu', 'tuntun', 'kalia', 'bheem']
for i in characters:
    print(i)

    
dora
bujji
jaggu
tuntun
kalia
bheem

characters.append('tango')
characters
['dora', 'bujji', 'jaggu', 'tuntun', 'kalia', 'bheem', 'tango']
for in characters:
    
SyntaxError: invalid syntax
for i in characters:
    print(i.startswith('t'))

    
False
False
False
True
False
False
True
for i in characters:
    print(i.startswith('a'))

    
False
False
False
False
False
False
False
for s in characters:
    print(i.find('d'))

    
-1
-1
-1
-1
-1
-1
-1
for s in characters:
    if i.startswith('t'))
    
SyntaxError: unmatched ')'
for s in characters:
    if i.startswith('t'):
        print(i)

        
tango
tango
tango
tango
tango
tango
tango
for s in characters:
    if s in startswith('t'):
        print(s)

        
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    if s in startswith('t'):
NameError: name 'startswith' is not defined
for s in characters:
for s in characters:
    
SyntaxError: expected an indented block after 'for' statement on line 1
for s in characters:
    if s.startswith('t'):
        print(s)

        
tuntun
tango

for s in characteres:
    if not s.startswith('t"):
                        
SyntaxError: incomplete input
for s in characters:
    if not s.startswith('t'):
        print(s)

                        
dora
bujji
jaggu
kalia
bheem

a=565
                        
b=56
if b>a
                        
SyntaxError: incomplete input
a=565
                        
b=56
...                         
if b
>>> >a
...                         
SyntaxError: invalid syntax
>>> if b>a:
... print("b is greater than a")
...                         
SyntaxError: expected an indented block after 'if' statement on line 1
>>> 
>>> a=66
...                         
>>> b=58
...                         
>>> if b<a:
...                         print("b is geeater than a")
... 
...                         
b is geeater than a
>>> age=20
...                         
>>> if age>=18:
...                         print('i am eigibe to vote')
...                         print('i am an adult')
...                         print('i can')
... 
...                         
i am eigibe to vote
i am an adult
i can
>>> 
>>> is_name_in=True
...                         
>>> if is_name_in:
...                         print("HII!")
... 
...                         
HII!
>>> 
