#Calculator using functions

#Creating functions for various operations

def add(a,b) :
	return a+b

def sub(a,b):
	return a-b

def div(a,b):
	return a/b

def mul(a,b):
	return a*b
	
#Operator options available

print(" Welcome to calculator")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Division")
print(" 4. Multiplication")

#Taking choice from input

choices= input(" Enter your choice 1/2/3/4 :- ")

#now assigning user input values

if choices in ('1','2','3','4'):
	
	num1= float(input(" Enter 1st number:- "))
	num2=float(input(" Enter 2nd number:- "))
	
	if choices=='1':
		print(num1, "+", num2, "=", add(num1, num2))
	
	elif choices=='2':
		print(num1, "-", num2, "=", sub(num1, num2))
	
	elif choices=='3':
		print(num1, "/", num2, "=", div(num1, num2))
	
	elif choices=='4':
		print(num1, "x", num2, "=", mul(num1, num2))
		
	else:
		print("Invalid operation...")
	
	
		
	
		