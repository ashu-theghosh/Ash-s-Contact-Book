'''my_list=[]

while True:
    num=int(input("Enter your number to add in the list"))
    my_list.append(num)
    again=input("Type yes to enter more numbers or any key to proceed").lower()
    if again=="yes":
        continue
    else:
        break
print("The created list of numbers is",my_list)'''


def check_max(my_list):
    max_val=my_list[0]
    min_val=my_list[0]
    for num in my_list:
        if num>max_val:
            max_val=num
        if num<min_val:
            min_val=num
    return max_val,min_val

def filter_even(my_list):
    new_list=[]
    for num in my_list:
        if num%2==0:
            new_list.append(num)
    return new_list


def check_u_no(my_list,x):
    max_val=my_list[0]
    fresh=[]
    for num in my_list:
        if num>x:
            fresh.append(num)
    while not fresh:
        return None
    return fresh

def check_prime(x):
    if x==1 or x==0:
        return False

    for i in range(2,x):
        if x%i==0:
            return False
    return True

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def add_tuple(tup1,tup2):
    return (tup1+tup2)

result=add_tuple((1,2,3,4,5),(6,7,8,9,10))

def add(r):
    sum=0
    for i in r:
        sum=sum+i
    return sum

def max_min_tup(r):
    maxi=result[0]
    mini=result[0]
    for num in r:
        if num>maxi:
            maxi=num
        if num<mini:
            mini=num
    return maxi,mini

def optup(tup):
    n,a,g,s=tup
    return n,a,g,s

"""original_tuple=(2,5,6,"ash","goku","tyson",55,22,8,"pika")


def operate(original_tuple):
    return original_tuple[2::2]

def op2(original_tuple):
    return original_tuple[0:2]

def op3(original_tuple):
    return original_tuple[3::2]

new_t=operate(original_tuple)

print(new_t)

remaining_tup=op2(original_tuple)+op3(original_tuple)

def rep(n,new,tup):
    temp=list(tup)
    temp[n]=new
    return temp

index=int(input("enter the index where you want to insert the new value"))
val=input("enter the new value")

brand_new=rep(index,val,new_t)
future_brand_new=tuple(brand_new)
print(future_brand_new)

modified_tuple=future_brand_new+remaining_tup
print(modified_tuple)

print(modified_tuple.count(22))

print(original_tuple)"""

set1={12,13,14,15,88,"ash","pika","tyson"}
set2={12,13,90,"tyson",777,222,555,444,234,567}

def un(set1,set2):
    return set1.union(set2)

def inter(set1,set2):
    return set1.intersection(set2)

def diff(set1,set2):
    return set1.difference(set2)

new_set=un(set1,set2)
print(new_set)

in_set=inter(set1,set2)
print(in_set)

diffren=diff(set1,set2)
print(diffren)

set3=(set1-set2)|(set2-set1)
print(set3)

def sub(set1,set2):
    return in_set.issubset(set1)

print(sub(set1,set2))

n=int(input("Enter a number"))
fact=1
for i in range(2,n+1):
    fact*=i

print(fact)



i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print(fact)


u=0
if type(u)==int:
    print("yes")

my_l=[1,2,3,3,4,5,"ab","cc","cl"]
sum=0
for ele in my_l:
    if type(ele)==int or type(ele)==float:
        sum=sum+ele
print(sum)


"""students_scores=dict()

students_scores["Alice"]=95
students_scores["Bob"]=88
students_scores["Charlie"]=92
students_scores["David"]=78

print(students_scores)

for key,values in students_scores.items():
    print(key,":",values)

sum=0
for keys in students_scores:
    sum+=students_scores[keys]
print("average of the students is",sum/len(students_scores))

students_scores["Eve"]=97

print(students_scores)"""


'''inventory={"apples": 50,
"bananas": 75,
"oranges": 100,
"grapes": 30}


def check_add_inventory(k,v):
    if k in inventory:
        inventory[k]+=v
    else:
        inventory[k]=v
    return inventory

def print_inventory():
    for key,value in inventory.items():
        print(key,":",value)

print(check_add_inventory("apples",50))
print(check_add_inventory("pineapple",50))

print(print_inventory())'''

students=["Alice","Bob","Charlie","David","Eve"]
scores=[97,88,75,66,99]
student_scores={students:scores for students,scores in zip(students,scores)}

def filter_scores(min_score):
    fresh={}
    for k in student_scores:
        if student_scores[k]>=min_score:
            fresh[k]=student_scores[k]
    return fresh

c=int(input("Enter mininmum score"))
x=filter_scores(c)
print(x)

def calculate_average_score():
    sum=0
    for k in student_scores:
        sum+=student_scores[k]
    average=sum/len(student_scores)
    return average

print("average score of all the students is",calculate_average_score() )


m=int(input("Hi student! Enter your marks"))

if m>= 90: print("Your Score is",m,"and your grade is A")
elif 80<=m<90: print("Your Score is",m,"and your grade is B")
elif 70<=m<80: print("Your Score is",m,"and your grade is C")
elif 60<=m<70: print("Your Score is",m,"and your grade is D")
else: print("Your Score is",m,"and your grade is F")
