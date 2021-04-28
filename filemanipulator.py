class doOption:
	def binortext():
		bot_ = input("Binary or text ('bin' or 'txt'): ")
		return bot_

class fileAction:
	def readFile(f1):
		fil_bin_txt = doOption.binortext()

		if (fil_bin_txt == "bin"):
			file_x = open(f1, "rb")
			print("\n", file_x.read(), "\n")

		elif (fil_bin_txt == "txt"):
			file_x = open(f1, "rt")
			print("\n", file_x.read(), "\n")

		else:
			print("Invalid type.")

	def appendFile(f1):
		fil_bin_txt = doOption.binortext()

		file_x = open(f1)

		if (fil_bin_txt == "bin"):
			file_x = open(f1, "ab")
			written = input("Insert binary data to append: ")
			file_x.write(written)
		
		elif (fil_bin_txt == "txt"):
			file_x = open(f1, "at")
			written = input("Insert text data to append: ")
			file_x.write(written)
