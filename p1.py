#check if file exist 


import os
fn=input("enter the file name")

if os.path.exists(fn):
	print(fn,"exist")
else:
	print(fn,"does not exists")
