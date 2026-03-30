# short hand if-else statement
a=300
b=3002
print("A") if a>b else print("=") if (a==b) else print("B")
c=9 if (a<b) else 0



num=int(input("Enter the number: "))
q1="Positive" if num>0 else "Negative"
q2="Even" if num%2==0 else "Odd"
q3="Yes" if num%5==0 else "No"
a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
q4="A" if a>b else "B" if b>a else "="

print(q1)
print(q2)
print(q3)
print(q4)

temp=int(input("Enter the temperature: "))
weather="Hot" if temp>35 else "Warm" if temp>=20 and temp<=35 else "Cold" 
print("Given {} degree celcius the weather is {}".format(temp, weather))