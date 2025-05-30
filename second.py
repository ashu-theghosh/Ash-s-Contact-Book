"""name=input("Enter your name")
char=input("Hello "+name+" please enter a character from your name which you want to count")
count=name.count(char)
print(count)"""
from operator import truediv

"""name=input("Enter your name")
name2=name.upper()
f=name2[0]
space=name2.find(" ")
m=name2[space+1]
s2=name2.find(" ",space+1)
l=name2[s2+1]
print(f+m+l)"""

'''name=input("Enter your name")
name1=name.title()
space=name1.find(" ")
last=name1[space+1::]
first=name1[0:space]
print(last,first)
c=0
for n in name1:
    c=c+1
print(c)
f=name1[0]
space=name1.find(" ")
l=name1[space+1]
print(f+l)'''

'''paragraph="Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances"
c=paragraph.count('python')
c2=paragraph.count("Python")
print(c+c2)
p2=paragraph.replace("Python","PYTHON")
p3=p2.replace("python","PYTHON")
print(p3)'''

'''w=input("please enter your word")
p=w[::-1]
print(w==p)'''


x=10
y=2.0
r=x+y
print(r)

a=True
b=1
print(a==b)

l=[1,2,3]
print(l[::-1])





