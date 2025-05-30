
def calcu():
 print("Welcome To Ash's Calculator")


 x=float(input("Enter a number"))
 y=float(input("Enter a second number"))

 print("The Number you entered are",x,y)
 print("What operation do you want to perform enter the number from the list")
 print("1 For Addition")
 print("2 For Subtraction")
 print("3 For Multiplication")
 print("4 For Division")

 n=int(input())

 if n==1:
        add=x+y
        print(f"Addition of {x} and {y} is",add)
 elif n==2:
        sub=x-y
        print(f"Subtraction of {x} and {y} is",sub)
 elif n==3:
        mult=x*y
        print(f"Multiplication of {x} and {y} is",mult)
 elif n==4:
        div=x/y
        print(f"Division of {x} and {y} is",div)
 else:
        print("You have entered a wrong choice")

while True:
  calcu()
  again=input("Do you want to use calculator again? yes/no").lower()
  if again!="yes":
      break

