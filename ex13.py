#13 fibonaci
#formed by adding preceding two numbers in series
#how many fibonaci series u want?
num = int(input("Enter any num: "))
n1= 0 #1st num
n2=1#2nd num
#to store sum value
sum = 0
if(num)<=0:
    print("please enter num greater than 0")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
        
#every iteration n2 value in n1 and sum value in n2 
