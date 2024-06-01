# Write a program to check whether a person is eligible to vote or not?

a = int(input("write your age\n"))
if a >= 18:
    print("Congratulations ur eligble to vote.\n")
else:
    print("your not eligible to vote")

# Write a program to check char is vowel or not.

bb = ('a')
ee = ('e')
ie = ('i')
oo = ('o')
uu = ('u')

c = input("Please enter One Letter to Check\n")
if (c == bb or c == ee) or (c == uu or c == oo) or (c ==uu):
    print("its vowel letter")
else:
    print("its a consonant letter")

# Write a program to check the number is positive or negative. User input.

num_1 = int(input("write any number to check it is postive or not \n"))
if num_1 % 2 == 0:
    print("its a postive number")
else:
    print("its a negative number")

# Write a program to check whether a number is odd or even?
num_2 = int(input("check number is even or odd \n"))
if num_2 % 2 == 0:
    print("its a even number")
else:
    print("its a odd number")

# Write a program to display the grade of the user in 
# subject A, ask user marks obtained out of 100

sub_1 = str(input("write sub name\n"))
num_3 = int(input("write your obtained marks\n"))

if num_3 >= 90:
    print("you got A Grade in" + str(sub_1))
elif num_3 >= 80:
    print("you got B Grade in" + str(sub_1))
elif num_3 >= 70:
    print("you got C Grade in" + str(sub_1))
elif num_3 >= 60:
    print("you got D Grade in" + str(sub_1))
elif num_3 >= 50:
    print("you got E Grade in" + str(sub_1))
elif num_3 < 50:
    print("Your fail in this Subject" + str(sub_1))

# Write a program to check whether a number is divisible by 7
num_4 = int(input("write to check if number is divisible by 7\n"))
if num_4 % 7 == 0:
    print("its divisible by 7")
else:
    print("its not divisible by 7")

# Write a program to check if year is leap year

year = int(input("write any year\n"))
if year % 4 == 0:
    print("its leap year")
elif year % 400 == 0:
    print("its a leap year")
else:
    print("its not a leap year")
# Write a program to ask user its name and
# check whether name consists of 5 or more letters
name_ur = str(input("Enter your name\n"))
print(len(name_ur))
if len(name_ur) >= 5:
    print("your name consist of " + str(len(name_ur)) + " letters")
else:
    print("your name consist of just " + str(len(name_ur)) + " letters")
# Write a program that accepts 3 inputs from user. input 1 
# input 2 should be numbers and the third input should be mathematical operator.
num_1 = int(input("write first num\n"))
num_2 = int(input("write second num\n"))
operator = input('Specify the math operation here (+, -, *, /, %): ')
if operator == '+':
    print(num_1 + num_2)
elif operator == '-':
    print(num_1 - num_2)
elif operator == '*':
    print(num_1 * num_2)
elif operator == '/':
    print(num_1 / num_2)
elif operator == '%':
    print(num_1 % num_2)
else:
    print('Invalid operator')

# Write a program that accepts 1 input from user
# and check if the number is divisible by 2 and 3 both.
num_11 = int(input("wirte the number to check didved by both 2 3\n"))
if num_11 % 2 == 0 and num_11 % 3 == 0:
    print(str(num_11) + ' was divisible by both 2 and 3\n')
elif num_11 % 2 == 0:
    print(str(num_11) + ' was only divisible by 2\n')
elif num_11 % 3 ==0:
    print(str(num_11) + ' was only divisible by 3\n')
else:
    print(str(num_11) + ' was not divisible by both 2 and 3\n')

# Write a program that accepts 2 inputs
# from user and check which number is largest
num_12 = int(input("wirte first for number checking\n"))
num_13 = int(input("wirte second for number checking\n"))
if num_12 > num_13:
    print(str(num_12) + " is larger than " + str(num_13))
elif num_13 > num_12:
    print(str(num_13) + " is Larger than " + str(num_12))
elif num_12 == num_13:
    print(str(num_12) + " and " + str(num_13) + " are equal")
else:
    print("invalid input")

# Write a program that accepts 3 input from user
# and check which number is largest.
num_14 = int(input("Enter a number to test for highest largest\n"))
num_15 = int(input("Enter a 2nd number to  test for highest largest\n"))
num_16 = int(input("Enter a 3rd number to test for highest largest\n"))

if (num_14 > num_15 and num_14 > num_16):
    print(str(num_14)+ " is larget number")

elif (num_15 > num_14 and num_15 > num_16):
    print(str(num_15)+ " is larget number")
elif (num_16 > num_14 and num_16 > num_15):
    print(str(num_16)+ " is larget number")
else:
    print("invalid input")

# Write a program that accepts 
# 3 input from user and check the second largest.
num_17 = int(input("write number to check 2nd largest\n"))
num_18 = int(input("write number to check 2nd largest\n"))
num_19 = int(input("write number to check 2nd largest\n"))
if (num_17 < num_18 and num_17 > num_19):
    print(str(num_17)+ " is 2nd larget number")
elif (num_17 < num_19 and num_17 > num_18):
    print(str(num_17)+ " is 2nd larget number")
elif (num_18 < num_19 and num_18 > num_17):
    print(str(num_18)+ " is 2nd larget")
elif (num_18 > num_19 and num_18 < num_17):
    print(str(num_18)+ " is 2nd larget")
elif (num_19 > num_18 and num_19 < num_17):
    print(str(num_19)+ " is 2nd larget")
elif (num_19 < num_18 and num_19 > num_17):
    print(str(num_19)+ " is 2nd larget")
else:
    print("Invalid")

# Write a python program that accept user an input.
# The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yEL
light = str(input("write Singnal color to show Cars\n"))
if light == "green" or light == "GREEN" or light == "gREEN":
    print("Car is allowed to go\n")
elif light == "RED" or light == "red" or light == "rED\n":
    print("Car has to wait")
elif light == "YELLOW" or light == "yellow" or light == "yELLOW":
    print("Car has to Stop\n")
else:
    print("invalid light")

#Write a program that takes two numbers as input and prints:
num_20 = float(input("write a first number\n"))
num_21 = float(input("write a second number\n"))
if num_20 > num_21:
    print("First number is greater than second number")
elif num_21 > num_20:
    print("Second number is greater than first number")
elif num_21 == num_20:
    print("both numbers are equal")
else:
    print("invalid input")

#Write a program that takes a
#password as input and checks its strength:
code = str(input("Write a password\n"))
if len(code) < 6:
        print("weak Password\n")
        print("try again\n")
elif len(code) >= 6 and len(code) <= 12:
        print("Moderate password")
elif len(code) > 12:
        print("strong Password")
else:
        print("invalid input")
#Write a program that takes an employee's
#salary and years of service as input. Calculate the bonus as follows:
salary = float(input("write your current salary\n"))
service = int(input("write your Total service years in number of years\n"))
if service > 5:
    print("Sorry your not enough services for bouns")
if service >= 5 and service <= 10:
    bouns = (10/100)*salary
    print("Congratulations u got 10% bonus ur new salary is "+str(bouns))
elif service > 10:
    bouns = (20/100)*salary
    print("Congratulations u got 20% bonus ur new salary is "+str(bouns))
else:
    print("Sorry U service is too low")

#Write a program that takes the total 
#amount of a purchase as input and applies a discount:
amount = int(input("input amount\n"))
if amount < 100:
    print("No discount\n")
    print("$" +str(amount))
elif amount > 100 and amount >= 500:
    discount = (10/100)*amount
    new_amount = amount - discount
    print("after discount the amount is $" + str(new_amount))
elif amount > 500:
    discount = (20/100)*amount
    new_amount = amount - discount
    print("after discount the amount is $" + str(new_amount))
else:
    print("invalid input")

#Write a program that takes a person's 
#age as input and prints the age group they belong to:
age = int(input("Enter your age"))
if age < 13 :
    print("you are child now")
elif age >= 13 and age <= 19:
    print("Inculsive")
elif age == 20:
    print("Teenager")
elif age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")

#Write a program that checks if a customer
#is eligible for a discount based on their membership status and purchase amount:
yes = True
no = False
member = bool(input("Are you member "))
purchase_amount = int(input("write Purchase amount $"))
if member == yes and purchase_amount >= 50:
    print("Congratulations u got 5% discount\n")
    new_amount = (10/100)*purchase_amount
    purchase_amount = purchase_amount-new_amount
    print("$" + str(purchase_amount))
elif member == no and purchase_amount >=100:
    print("Congratulations u got 5% discount\n")
    new_amount = (10/100)*purchase_amount
    purchase_amount = purchase_amount-new_amount
    print("$"+ str(purchase_amount))
else:
    print("your not eligible for the discount")
    