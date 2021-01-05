a=int(input("Enter a number : "))
counter=0

for i in range(2,a+1):
    
    if a%i==0: #if the number is prime number, it can only divided itself and one.
        counter+=1 #since the number will only divided to itself, the programme will add plus 1 to the counter. 
        
if counter==1:
    print("This number is prime number.")
else:
    print("This number isn't prime number.")
    
    