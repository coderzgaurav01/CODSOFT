# We will call random module to choose random characters
import random
#we will define here what characters we are going to use in password
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=:/?><.,"
#length of password
length_password = int(input("Enter the length of password"))

a= "".join(random.sample(password,length_password))
print(f"suggested password is : {a}")