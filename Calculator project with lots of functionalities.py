


def operations_1(): # declaring the function will be key in the program 
    try: # the try block looking for errors
        print("***This is a calculator application***")
        print("Please enter the operands availabe (+,-,*,/,**)")
        print("+ = Addition")
        print("- = Subtraction")
        print("* = Multiplication")
        print("/ = Division")
     
        print("** = Power number")
        num = int(input("Enter first number: ")) # asking user for first number also it will convert to an integer if it is not it will occur and exception due to this
        num2 = int(input("Enter second number: ")) # asking user for secondQ number the int() is fundamental if it is not an int() then it will occur an exception
        operations = input("Enter the operations you want(+,-,*,/): ") # asking the user for an operation on what they want to do with the numbers
        
        if operations == "+": # if the user clicks + it will add the numbers the user has entered
                   print(num + num2) # outputting the numbers to the compiler if user chooses "+"

        elif operations == "-":
            print(num - num2) #outputs it to the user 
            


        elif operations == "*": 
            print(num * num2) # outputs it to the user
            

            
        elif operations == "/":
            print(num / num2) # outputs it to the user


        elif operations == "**": # the power number
            print(num ** num2) #outputting the power number


        elif operations != "+"  or "-" or "*" or "/" or "**": # if the user does not give one of the 4 operands then the program will not progress 
            print("Please enter one of the 4 operators: (+,-,*,/,**)") # asking them to enter of the operands
            operations_1() # if they do not they the whole program will restart a while loop could be more sufficent in this case but trying new things by calling the function the program restarts
          


    except ValueError: # if any errors in the porgram occur it will not crash it 
        print("Invalid input try again") # the message when this happens  # telling the user to try again if an exception occurs
        operations_1()# so if an error occurres exception then user will be given another chance
        

    except ZeroDivisionError: # because it is a calculator program so if it divides anything by zero then it will give it an error and stop it this exception is key in this kind of program
        print("You can' divide by zero")
        print("Try again")
        operations_1() # if an exception occurs like dividing by zero user will be given another chance



operations_1()# calling the function so it works if you do not use this then the program wont work you have to call upon the function






                   
        

