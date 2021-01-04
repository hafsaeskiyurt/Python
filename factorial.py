a=int(input("Enter a number whose factorial you want to calculate : "))
counter=a
result=1
for i in range(a):
    result*=a-(a-counter) # in here, the programme will multiply each value by the previous variable value and assign it back to the variable.  
    counter-=1   
print(result)    





