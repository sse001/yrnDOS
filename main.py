import calculator
import filemanipulator

inputn = str()
number1 = int()
number2 = int()
answer = float()
selectForm = str()

def Variables_0():
	print("Current Variable Configurations in 'main.py' (GLOBAL):")
	print("(string) inputn = ", inputn)
	print("(integer) number1 = ", number1)
	print("(integer) number2 = ", number2)
	print("(floating point) answer = ", answer)
	print("(string) selectForm = ", selectForm)

print("Welcome to yrnDOS!\n")

while (inputn != "shut"):
	inputn = input("input> ")

	if (inputn == "shut"):
		print("Shutting off...")
	
	elif (inputn == "V_0"):
		Variables_0()
	
	elif (inputn == "help"):
		print("Commands: shut, help, basic-add, basic-subtract, basic-multiply, basic-divide, file-read, file-append, file-write, file-create, file-delete, dir-delete")

	elif (inputn == "basic-add"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicAddition(number1, number2)
		print("Answer:", answer)
	
	elif (inputn == "basic-subtract"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicSubtraction(number1, number2)
		print("Answer:", answer)

	elif (inputn == "basic-multiply"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicMultiplication(number1, number2)
		print("Answer:", answer)

	elif (inputn == "basic-divide"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicDivision(number1, number2)
		print("Answer:", answer)
	
	elif (inputn == "file-read"):
		selectForm = input("Insert file directory: ")
		filemanipulator.fileAction.readFile(selectForm)

	elif (inputn == "file-append"):
		selectForm = input("Insert file directory: ")
		filemanipulator.fileAction.appendFile(selectForm)
	
	elif (inputn == "file-write"):
		selectForm = input("Insert file directory: ")
		filemanipulator.fileAction.writeFile(selectForm)
	
	elif (inputn == "file-create"):
		selectForm = input("Name of file: ")
		filemanipulator.fileAction.createFile(selectForm)
	
	elif (inputn == "file-delete"):
		selectForm = input("Insert file directory: ")
		filemanipulator.fileAction.deleteFile(selectForm)
	
	elif (inputn == "dir-delete"):
		selectForm = input("Insert directory: ")
		filemanipulator.fileAction.deleteFolder(selectForm)

	elif (inputn == "cookie"):
		print("You found the secret! :O")
		print("Here's a cookie: \U0001F36A")

	else:
		print("Not a valid command.")
