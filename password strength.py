while True:
 print("Password should contains atleast 6 character/Any special character(!@#$%^&*)/Contains a upper case/Contains a digit")
 str1=input("Enter your new password")
 if (len(str1)<6 or (str1.find("!")==-1 and str1.find("@")==-1 and str1.find("#")==-1 and str1.find("$")==-1 and str1.find("%")==-1 and str1.find("^")==-1
     and str1.find("&")==-1 and str1.find("*")==-1) or not any(char.isupper() for char in str1) or not any(char.isdigit() for char in str1)):
     print("length is less tha 6 character weak password/special character(!@#$%^&*) missing/Does not contains a upper case/Does not contains a digit/Enter again")
     continue
 else:
     print("Password created")
     break