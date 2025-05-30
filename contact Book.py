'''with open("myfile.txt","w") as file:
    file.write("hey my first line\n")
    file.write("hey my second line\n")

with open("myfile.txt","r") as file:
    content=file.read()
    print(content)

with open("myfile.txt","r") as file:
    for line in file:
        print("line:",line.strip())'''

'''lst=["ash","pika","misty"]

with open("myfile.txt","a") as file:
    for word in lst:
        file.write(word+"\n")'''

'''with open("myfile.txt","r") as file:
    content=[line.strip() for line in file]
    print(content)'''

test={}

name=input("Enter the Contact name")
num=input("Enter the Contact number")

test[name]=num

with open("Contacts.txt","a") as file:
    for k,v in test.items():
        file.write(k+":"+v+"\n")

with open("Contacts.txt","r") as file:
    for line in file:
        content=line.strip()
        print(content)
        if ":" in content:
            key,value=content.split(":",1)
            test[key]=value
print(test)

