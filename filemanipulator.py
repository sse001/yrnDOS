def readFile(f1):
	fil_bin_txt = input("Binary or text ('bin' or 'txt'): ")

	file_x = open(f1)

	if (fil_bin_txt == "bin"):
		file_x = open(f1, "rb")
	elif (fil_bin_txt == "txt"):
		file_x = open(f1, "rt")
	else:
		print("Invalid type.")

	print("\n", file_x.read(), "\n")