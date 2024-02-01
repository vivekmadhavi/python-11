#wapp to delete an existing file


import os
fn = input("enter file name ")


if os.path.exists(fn):
	try:
		os.remove(fn)
		print(fn, "remove")
	except Exception as e:
		print("issue",e)
else:
		print(fn ,"does not exists")