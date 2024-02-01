#check if file exists


import os
fn = input("enter file name")


if os.path.isfile(fn):
	print(fn,"exist")
else:
	print(fn, "does not exist")