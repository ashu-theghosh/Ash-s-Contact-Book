id_password=["ash@gmail.com","mypass123","pika@gmail.com","ppp123"]

def manager(off):
    return lambda MRP:MRP*(100-off)/100

print("Welcome to manager panel")

while True:
 m_user_id=input("Please enter your email id").lower()
 m_pass=input("Please enter your password").lower()
 if m_user_id==id_password[0] and m_pass==id_password[1]:
    off=float(input("please enter the offer value"))
    cashier=manager(off)
    break
 else:
    print("you entered a wrong id/password/please enter again")
    continue

print("Welcome to cashier panel")

my_list=[]
while True:
 c_user_id=input("Please enter your email id").lower()
 c_pass=input("Please enter your password").lower()
 if c_user_id==id_password[2] and c_pass==id_password[3]:
     while True:
      q1=int(input("Please enter the quantity of product"))
      price=float(input("Please enter the price of the product"))
      my_list.append(q1)
      my_list.append(price)
      again=input("enter yes to enter more products or any key to proceed").lower()
      if again=="yes":
       continue
      else:
          break
     i=0
     sum=0
     while i<len(my_list):
         cross=my_list[i]*my_list[i+1]
         sum=sum+cross
         i=i+2
     TPB=cashier(sum)
     break
 else:
    print("you entered a wrong id/password/please enter again")
    continue
print("total payable bill is",TPB)