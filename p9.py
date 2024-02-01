#wapp to make a copy of given file


import os
sfn = input("enter file name ")
if os.path.exists(sfn):
	dfn = input("enter destination file name ")
	if os.path.exists(dfn):
		print(dfn, "already exists")
	else:
		fsrc=None
		fdesh=None
	try:
		fsrc=open(sfn,"r")
		fdesh=open(dfn,"w")
		data = fsrc.read()
		fdesh.write(data)
		print("copy completed")
	except Exception as e:
		print("issue",e)
	finally:
		if fsrc is not None:
			fsrc.close()
		if fdesh is not None:
			fdesh.close()
else:
		print(sfn ,"does not exists")