
def simple():
	"""5 vari, print each"""
	vari_1="One!"
	vari_2="Two!"
	vari_3="Three!"
	vari_4="Four!"
	vari_5="Five!"
	print(vari_1, vari_2, vari_3, vari_4, vari_5)

simple()

def simple2():
	"""1 vari, print, change message, print. 4x"""
	message="First!"
	print(message)
	message="Second!"
	print(message)
	message="Third!"
	print(message)
	message="Fourth!"
	print(message)

simple2()

def message(letter):
	"""function takes argument, print"""
	print("You've got " + letter + " letters!")

message("two")