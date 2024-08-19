import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
numbers = ['0','1','2','3','4','5','6','7','8','9'] 
print('welcome to pass generator')
nletters=int(input("enter the letters you need:"))
nnumbers=int(input("enter the numbers you need:"))
password=""
for i in range(1,nletters+1):
    password += random.choice(letters)
for i in range(1,nnumbers+1):
    password += random.choice(numbers)
print(password)    
    