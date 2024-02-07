again = 'y'
print("Hello Welcome to the Calculator Program")
while again.lower() == 'y':
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Write your choice 1/2/3/4/5:\n")
    
    if choice == "5":
        break
    elif choice not in ("1","2","3","4"):
        print ("idiot you didn't choose the calculation method")
        continue
    else:
        num1 = input("Enter a Number\n")
        num2 = input("Enter one more Number\n")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("You didn't enter valid numbers. Please enter numbers only.\n")
            continue

        if choice == '1':
            print (f"{num1} + {num2} = {num1+num2}") 
        elif choice == '2':
            print (f"{num1} - {num2} = {num1-num2}") 
        elif choice == '3':
            print (f"{num1} * {num2} = {num1*num2}") 
        elif choice == '4':
            if num2 == 0:
                print("You can't divide by zero.")
            else:
                print (f"{num1} / {num2} = {num1/num2}")
    again = '0'   
    while again not in ("y","Y","n","N"):
        again = input('Do you want to do new calculation? (y/n)\n')
    if again in("n","N"):
        break
