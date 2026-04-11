#                  create a calculator
ch="Yes"
print("+:Addition\n-:Subtraction\n*:Multiplication\n/:Division")
print("//:Quotient of Division\n%:Remainder of Division\n**:Exponential\n")
while ch:
    a=int(input("Enter Number 1: "))
    b=int(input("Enter Number 2: "))  
    op=input("Operation: ")
    match op:
        case "+":
            print("Addition: ",a, op, b, "=", a+b)
        case "-":
            print("Subtraction: ",a, op, b, "=", a-b)
        case "*":
            print("Multiplication: ",a, op, b, "=", a*b)
        case "/":
            print("Division: ",a, op, b, "=", a/b)
        case "//":
            print("Quotient: ",a, op, b, "=", a//b)
        case "%":
            print("Remainder: ",a, op, b, "=", a%b)
        case "**":
            
            print("Exponential of a raise to b: ",a, op, b, "=", a**b)
            
    print("Do you Want to Continue?")
    ch=input("Enter Yes to Continue: ")
    if ch=="YEs" or ch=="YES" or ch=="Yes" or ch=="yes":
        continue
    else:
        break
print("Hope you enjoyed our calculator!!")
    
    
        
      
    