#one.py
#__name__ #built-in variable
def func():
	print("func() in one.py.")
print("top level in one.py.")
if __name__=="__main__ ":
	print("one.py is being run directly.")
else:
	print("one.py has been imported.")
