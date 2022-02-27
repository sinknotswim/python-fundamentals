
def name():
	"""personal message"""
	person="Eric"
	print("Hello " + person + " how are you doing today?")

name()

def cases():
	"""print upper, lower, titlecase"""
	c_name="Mara Sov"
	print(c_name.upper(), c_name.lower(), c_name.title())

cases()

def famous_quote():
	"""famous quote"""
	quote='Bill Nighty once said, "Do you feel it? The Light is back. We are back. Eyes up, Guardian."'
	print(quote)

famous_quote()

def famous_quote2():
	"""above + famous"""
	quote='"Do you feel it? The Light is back. We are back. Eyes up, Guardian."'
	famous_person="Bill Nighty"
	print(famous_person + " once said, " + quote)

famous_quote2()

whitespace_name="\nada one	"
print(whitespace_name)

whitespace_name.rstrip()
print(whitespace_name)

whitespace_name.lstrip()
print(whitespace_name)

whitespace_name.strip()
print(whitespace_name)