# Python program for simple calculator

def add(number1,number2):
    return number1+number2
def sub(number1,number2):
    return number1-number2
def mul(number1,number2):
    return number1*number2
def div(number1,number2):
    return number1/number2

print("Please select the below operators\n"
      "1.Add\n"
      "2.Sub\n"
      "3.Mul\n"
      "4.Div\n")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))


select = int(input("Select operations form 1, 2, 3, 4 :"))

if select==1:
    print("Addition of",number_1,"+",number_2,"=",add(number_1,number_2))
elif select==2:
    print("Subtraction",number_1,"-",number_2,"=",sub(number_1,number_2))
elif select==3:
    print("Multiplication",number_1,"x",number_2,"=",mul(number_1,number_2))
elif select==4:
    print("Divsion",number_1,"/",number_2,"=",div(number_1,number_2))
else:
    print("Sorry invalid Input")


