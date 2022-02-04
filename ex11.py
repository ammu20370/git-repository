#check prime or not

num = int(input("enter a number: "))

if num<=1:
    print("it is not prime")
else:
    for i in range (2,num):
      if(num%i)==0:
        print("is not a prime number")
    else:
        print (num, "is a prime num")


















         
      
