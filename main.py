#r=float(input("enter the radius"))
#area=3.14*r*r
#print("the area of circle is",area) #assignment 1

#f=float(input("Enter temperature in fahrenheit"))
#c=(f-32)*5/9
#print(c) #assignment 2

#P=float(input("Enter principle amount in Rs"))
#R=float(input("Enter rate of intrest in %"))
#T=float(input("Enter time in years"))
#SI=(P*R*T)/100
#print("Simple intrest is",SI) assignment 4

#name=input("Enter your name")
#age=int(input("Enter your age"))
#colour=input("Enter your favourite colour name")
#print("Hello",name,"your age is",age,"and your favourite colour is",colour) assignment 6

name=input("Hi customer what is your name")
print("Hi!",name,"hope you are doing well. Please enter the price of items listed below which you want to buy")
print("Chocolate Rs 20, Chips Rs 20, Coke Rs 30, Lassi Rs 20")
item1=int(input())
if item1<=30:
    print("do you want to add more item price")
item2=int(input())
if item2<=30:
    print("do you want to add more item price")
item3=int(input())
if item3<=30:
    print("do you want to add more item price")
item4=int(input())
if item4<=30:
     sum=item1+item2+item3+item4
     print("Total cost is",sum)




