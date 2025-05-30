'''s=input("Enter any word").lower()

def check_v_c(s):
    c=0
    v=0
    for i in s:
     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        v=v+1
     else:
        c=c+1
    print("The number of vovels in the word is",v)
    print("The number of consonent in the word is", c)

check_v_c(s)'''

'''n=int(input("enter a number"))

def rev_num(n):

    rev=0

    while n!=0:

        a=n%10
        n=n//10
        rev=rev*10+a

    return rev

ans=rev_num(n)

print(ans)'''

'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter any number"))

print("Factorial of the given number is",fact(n))'''

'''def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("Enter a number"))

if is_prime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")'''

'''l=[]

def enter_val():
 n = int(input("enter a number"))
 return n

while True:
    x=enter_val()
    l.append(x)
    print(l)
    again=input("Do you want to enter more elements to the list yes/no").lower()
    if again!="yes":
        break
'''

"""def rev_num(num):

    rev = 0

    while num!=0:
      digit=num%10
      num=num//10
      rev=rev*10+digit

    return rev

x=int(input("Enter a number"))
print("The reverse of the number is",rev_num(x))



def check_prime(n):

    if n==0 or n==1:
        return False

    for i in range(2,n):
        if n%i==0:
         return False

    return True

n=int(input("Enter a number"))

ans=check_prime(n)

if ans==True:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
"""


def check_palindrom(num2):

 is_negative=num2<0
 num3=abs(num2)
 new=int(str(num3)[::-1])
 return -new if is_negative else new

num2=int(input("enter a number"))

result=check_palindrom(num2)

if result==num2:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")

