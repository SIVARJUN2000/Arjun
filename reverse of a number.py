n=int(input("enter a number:"))
reverse=0
while(n>0):
    remainder=n%10
    reverse=(reverse*10)+remainder
    n=n//10
print("reverse of a number is:",reverse)
