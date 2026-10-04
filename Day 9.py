print("Marksheet of the student")
print("-------------")
mark=50
if mark>=90 and mark<=100:
    print("grade O")
elif mark>=80 and mark<=89:
    print("grade A")
elif mark>=70 and mark<=79:
    print("grade B")
elif mark>=60 and mark<=69:
    print("grade C")
elif mark>=50 and mark<=59:
    print("grade D")
else:
    print("FAIL")

print("Marksheet of the student")
print("-------------")
mark=105
if mark>=90 and mark<=100:
    print("grade O")
elif mark>=80 and mark<=89:
    print("grade A")
elif mark>=70 and mark<=79:
    print("grade B")
elif mark>=60 and mark<=69:
    print("grade C")
elif mark>=50 and mark<=59:
    print("grade D")
elif mark<=1 and mark>=49:
    print("fail")
else:
    print("enter the correct mark")

#nested if
print("Marksheet of the student")
print("-------------")
mark=int(input('enter your mark:'))
if mark>=90 and mark<=100:
    print(mark, "grade O")
elif mark>=80 and mark<=89:
    print(mark,"grade A")
elif mark>=70 and mark<=79:
    print(mark,"grade B")
elif mark>=60 and mark<=69:
    print(mark,"grade C")
elif mark>=50 and mark<=59:
    print(mark,"grade D")
elif mark<=1 and mark>=49:
    print("fail")
else:
    print("enter the correct mark")


