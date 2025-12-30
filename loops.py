#for loop
for i in range(1,5):
 print(i)
#while loop 
i=1
while i<5:
    print(i)
    
    #break condition
    i+=1
for i in range(1, 5):
    if i == 3:
        break
    print(i)
    
    #continue condition 
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
    
    #if and else condition

a=50
b=100
if a<b:
    print("yes a is less then b")
elif a>b:
        print("no  a is not greater then b")
        
#boolean value
logged_in= False
if  logged_in:
     print("log in successful")
else:
    print("log in successful")
