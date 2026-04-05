# Python Part
print("Welcome To The Calculator")
number1=int(input("Put the first value"))
number2=int(input("Put the second value"))
operation=input("What Operation you're going to select? 1: +  2: - 3: *  4: / Write Only The Number  ")
if operation == "1": 
  add=number1 + number2
  print(f"The result is {add}")
elif operation =="2": 
   minus=number1 - number2
   print(f"The result is {minus}")
elif operation == "3":
  multiply=number1 * number2
  print(f"The result is{multiply}")
elif operation == "4":
  divide=number1 / number2
  print(f"The result is {divide}")
