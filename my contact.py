def write():
    with open("new_contacts.txt","a") as file:
        name=input("Enter contact name")
        num=input("Enter number")
        file.write(name+":"+num+"\n")
        print("contact added")

def read():
    con={}
    with open("new_contacts.txt","r") as file:
        for line in file:
            content=line.strip()
            if ":" in content:
                key,value=content.split(":",1)
                con[key]=value
    print(con)
    return con

def delete():
    con=read()
    naam=input("Enter a contact name to delete")
    if naam in con:
        con.pop(naam)
        print("contact deleted")
        with open("new_contacts.txt","w") as file:
         for k in con:
            file.write(k+":"+con[k]+"\n")
    else:
      print("Contact not found")

def update():
    con=read()
    nam=input("Enter contact name to update")
    if nam in con:
        num=input("Enter the number")
        con[nam]=num
        with open("new_contacts.txt","w") as file:
            for k in con:
                file.write(k+":"+con[k]+"\n")
            print("Contact updated")
    else:
        print("Contact not found")


def main():
    while True:
      print("Welcome To Ash's Contact Book")
      print("Enter 1 to add contact")
      print("Enter 2 to view contact")
      print("Enter 3 to delete contact")
      print("Enter 4 to update contact")
      print("Enter 5 to exit the Contact Book")

      n=input("Enter your choice")

      if n=="1":
          write()
      elif n=="2":
          read()
      elif n=="3":
          delete()
      elif n=="4":
          update()
      elif n=="5":
          print("Exited")
          break
      else:
          print("Wrong choice/enter again")
main()