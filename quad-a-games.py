class var:
	name = str()

class games:
	def ABox_ornot():
		var.name = input("Welcome to ABox! What is your name? ")
		print("\nHello, ", var.name, "! This will be a questionnaire. Choose wrong and things will get a bit, let's just say, \"wonky.\"\n")

		while answer == 'A' or 'B':
			answer = input("So let's start. First question: Where would you be more likely to go and live?\n\tA. A peaceful island\n\tB. ")

games.ABox_ornot()
