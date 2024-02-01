#wapp to create file


import os
fn = input("enter file name ")


if os.path.exists(fn):
	print(fn,"exist")
else:
	f = None
	try:
		f=open(fn,"w")
		print(fn, "create")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()