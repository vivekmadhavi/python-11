#wapp to read radius from the user
#print area and circum using math module


from math import pi,pow
try:
	radius= float(input("enter the radius  "))
	if radius > 0.0:
		area = pi * pow(radius,2)
		circle = 2 * pi * radius
		print("area=", round(area,2))
		print("circle = ", round(circle,2))
	else:
		raise Exception("radius shud not be -ve")
except ValueError:
	print("u shud enter number only")
except Exception as e:
	print(e)
	

