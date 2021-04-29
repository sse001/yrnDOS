import os

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

		if (fil_bin_txt == "bin"):
			file_x = open(f1, "ab")
			written = input("Insert binary data to append: ")
			file_x.write(written)
			file_x.close()
			print("File appended.")
		
		elif (fil_bin_txt == "txt"):
			file_x = open(f1, "at")
			written = input("Insert text data to append: ")
			file_x.write(written)
			file_x.close()
			print("File appended.")

		else:
			print("Invalid type.")

	def writeFile(f1):
		fil_bin_txt = doOption.binortext()

		if (fil_bin_txt == "bin"):
			file_x = open(f1, "wb")
			written = input("Insert binary data to overwrite: ")
			file_x.write(written)
			file_x.close()
			print("File overwritten.")
		
		elif (fil_bin_txt == "txt"):
			file_x = open(f1, "wt")
			written = input("Insert text data to overwrite: ")
			file_x.write(written)
			file_x.close()
			print("File overwritten.")
		
		else:
			print("Invalid type.")
	
	def createFile(cf1):
		fil_bin_txt = doOption.binortext()

		if (fil_bin_txt == "bin"):
			file_x = open(cf1, "xb")
			print("File created.")
		
		elif (fil_bin_txt == "txt"):
			file_x = open(cf1, "xt")
			print("File created.")
		
		else:
			print("Invalid type.")
	
	def deleteFile(f1):
		if os.path.exists(f1):
			os.remove(f1)
			print("File deleted.")
		else:
			print("File not found.")
	
	def deleteFolder(ff1):
		if os.path.exists(ff1):
			os.rmdir(ff1)
			print("Directory deleted.")
		
		else:
			print("Directory not found.")
