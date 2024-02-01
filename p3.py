#wapp to create file


import os
fn = input("enter file name ")


if os.path.exists(fn):
	print(fn,"exist")
else:
	f =open(fn,"w")
	print(fn, "create")
	f.close()