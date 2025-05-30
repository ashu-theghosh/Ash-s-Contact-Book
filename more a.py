i=1
while i<=10:
    print(i)
    i+=1
i=2
sum=0
while i<=50:
    sum+=i
    i+=2
print(sum)

fact=1
i=1
while True:
 num=int(input("Enter a number"))
 if num<=0:
    print("wrong entry")
    continue
 else:
     break
while i<=num:
    fact*=i
    i+=1
print("factorial of",num,"is",fact)

str=input("enter a word")
'''i=0
x=1
is_match=True
while i<len(str):
    if str[i]!=str[len(str)-x]:
        is_match=False
        break
    i+=1
    x+=1
if is_match:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")'''
x=1
is_match=True
for y in str:
    if y!= str[len(str) - x]:
        is_match = False
        break
    x+=1
if is_match:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")


