while True:
    num1=int(input("Enter first number :"))
    operator = input("Enter operator number (+,-,*,/,%) :")
    num2=int(input("Enter second  number :"))


    if operator=="+":
        result=num1+num2
        print("The value after addition is : ",result)

    elif operator=="-":
        result=num1-num2
        print("The value after subtraction is : ",result)

    elif operator=="*":
         result=num1*num2
         print("The value after multiplication is : ",result)

    elif operator=="/":
         result=num1/num2
         print("The value after division is : ",result)

    elif operator=="%":
         result=num1%num2
         print("The remainder is : ",result)

    else:
         print("INVALID OPERATOR ")

    option= input("Want to do it again (yes or no )?")

    if option == "yes" or option == "YES":
         continue

    else:
        break