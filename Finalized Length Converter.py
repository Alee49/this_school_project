FEET_TO_METERS = .3048
METERS_TO_KILOMETERS = .001
METERS_TO_CENTIMETERS = 100.0
METERS_TO_MILIMETERS = 1000.0
FEET_TO_INCHES = 12.0
YARDS_TO_FEET = 3.0

converting_from = input('Enter the unit abbreviation you wish to convert from: ')
converting_to = input('Enter the unit abbreviation you wish to convert to: ')
number = input('What is the value that needs converted? ')
number = float(number)
while (converting_from != converting_to):
	if(converting_from == 'ft'):    
		if(converting_to == 'in'):
			number = number * FEET_TO_INCHES
			converting_from = 'in'
		elif(converting_to == 'yd'):
			number = number / YARDS_TO_FEET
			converting_from = 'yd'
		elif(converting_to == 'mm' or 'cm' or 'km'):
			number = number * FEET_TO_METERS
			converting_from = 'm'
		elif(converting_to == 'm'):
		  number = number * FEET_TO_METERS
		  converting_from = 'm'
	elif(converting_from == 'in'):
		if(converting_to == 'mm' or 'cm' or 'm' or 'km'):
			number = number / FEET_TO_INCHES
			converting_from = 'ft'
		elif(converting_to == 'ft' or 'yd'):
		  number = number / FEET_TO_INCHES
		  converting_from = 'ft'
	elif(converting_from == 'yd'):
		if(converting_to ==  'mm' or 'cm' or 'm' or 'km'):
			number = number * YARDS_TO_FEET
			converting_from = 'ft'
		elif(converting_to == 'ft' or 'in'):
		  number = number * YARDS_TO_FEET
		  converting_from = 'ft'
	elif(converting_from == 'm'):
		if(converting_to == 'ft' or 'in' or 'yd'):
			number = number / FEET_TO_METERS
			converting_from = 'ft'
		elif(converting_to == 'mm'):
			number = number * METERS_TO_MILIMETERS
			converting_from = 'mm'
		elif(converting_to == 'cm'):
			number = number * METERS_TO_CENTIMETERS
			converting_from = 'cm'
		elif(converting_to == 'km'):
			number = number * METERS_TO_KILOMETERS
			converting_from = 'km'
	elif(converting_from == 'mm'):
		if(converting_to == 'cm' or 'm' or 'km'):
			number = number / METERS_TO_MILIMETERS
			converting_from = 'm'
		elif(converting_to == 'in' or 'ft' or 'yd'):
		  number = number / METERS_TO_MILIMETERS
		  converting_from = 'm'
	elif(converting_from == 'cm'):
		if(converting_to == 'cm' or 'm' or 'km'):
			number = number / METERS_TO_CENTIMETERS
			converting_from = 'm'
		elif(converting_to == 'in' or 'ft' or 'yd'):
		  number = number / METERS_TO_CENTIMETERS
		  converting_from = 'm'
	elif(converting_from == 'km'):
		if(converting_to == 'cm' or 'm' or 'km'):
			number = number / METERS_TO_KILOMETERS
			converting_from = 'm'
		elif(converting_to =='ft' or 'in' or 'yd'):
			number = number / METERS_TO_KILOMETERS
			converting_from = 'm'
print(number)
print(converting_to)
				