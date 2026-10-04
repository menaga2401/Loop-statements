Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=58
b=87
if b>a:
    print("b is greater than a")

    
b is greater than a
else
SyntaxError: incomplete input
if b>a:
    print("b is greater than a")
else a<=b:
    
SyntaxError: expected ':'
else a<b:
    
SyntaxError: invalid syntax
if b<a:
    print("b is greater than a")
else:
    print("a is greater than b")

    
a is greater than b
if b<a:
    print("b is greater than a")
else a>b:
    
SyntaxError: expected ':'
else a>=b:
    
SyntaxError: invalid syntax
elif a>=b:
    
SyntaxError: invalid syntax

a=58
b=87
if b>a:
    print('b is greater than a")
          
SyntaxError: incomplete input
if b>a:
          print('b is gereater than a')
elif a==b:
    print('a and b are equal')

    
b is gereater than a
if b>a:
    print('b is gereater than a')
elif a>=b:
    print('a is lesser than b')

    
b is gereater than a

#NESTED IF
username=="menaga"
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    username=="menaga"
NameError: name 'username' is not defined

============ RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/9.3.py ============
Traceback (most recent call last):
  File "C:/Users/hp/OneDrive/Desktop/techpanda/9.3.py", line 2, in <module>
    username=="Menaga"
NameError: name 'username' is not defined

============ RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/9.3.py ============
login successful

============ RESTART: C:/Users/hp/OneDrive/Desktop/techpanda/9.3.py ============
login successful
Invalid username

#For Loop
games=['cricket','tennis','football','basketball']
for x in games:
    print(x)

    
cricket
tennis
football
basketball
for x in "tennis":
    print(x)

    
t
e
n
n
i
s
#BREAK
for x in games:
    print(x)
    if x=="tennis":
        break

    
cricket
tennis
for x in games:
    print(x)
    if x=="football":
        break
    print(x)

    
cricket
cricket
tennis
tennis
football
 for x in games:
     
SyntaxError: unexpected indent
for x in games:
    if x=="tennis":
        break
    print(x)

    
cricket
for x in range(4):
    print(x)

    
0
1
2
3
for x in range(0,3):
    print(x)

    
0
1
2
for x in range(0,1,-1)
SyntaxError: incomplete input
for x in range(3):
    print(x)
else:
    print("finally done")

    
0
1
2
finally done
for x in range(3):
    print(x)

    
0
1
2
else:
    
SyntaxError: invalid syntax
for x in range(3):
    if x==3: break
    print(x)
else:
    print("finally done")

    
0
1
2
finally done
>>> for x in range(3):
...     if x==3:break
...     print(x)
... else:
...     print("Finally done")
... 
...     
0
1
2
Finally done
>>> for x in range(3):
...     if x==3: break
...     print(x)
... else:
...     print("Finally done")
... 
...     
0
1
2
Finally done
>>> app=["insta","watsapp","utube"]
>>> fruits=["banana","apple","plum"]
>>> for x in app:
...     for y in fruits:
...         print(x,y)
... 
...         
insta banana
insta apple
insta plum
watsapp banana
watsapp apple
watsapp plum
utube banana
utube apple
utube plum
