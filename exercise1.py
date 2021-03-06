
print("Hello World")

#I took out the quotation marks and it gave me SyntaxError: invalid syntax, so it was pretty easy to make sense of.
#However, putting a typo in the message to print gives no error message. This is because it
#isn't technically an error.

import this

#It outputs the full Zen of Python, starting with Beautiful is better than ugly
#and ending with Namespaces are one honking great idea.

message = "Hello Python!"
print(message)
message = "Hello V2!"
print(message)

#This one was pretty straightforward. I stored a message in a variable,
#printed, changed the message, printed again.

def display_message():
	"""Display a simple message."""
	print("A Simple Message!")

display_message()

def favorite_book(bookname):
	"""Prints a message and something accepted."""
	print("This is my favorite book: " + bookname.title() + "!")

favorite_book('Alice in Wonderland')

#This one was also straightforward. We take a function, make it accept something
#inside of it, and print them both.