#wapp to write into an existing file


import os
fn = input("enter file name ")
if os.path.exists(fn):
	f=None
	try:
		f=open(fn,"w")
		data = input("enter data")
		f.write(data +"\n")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
		print(fn ,"does not exists")