
number = 0.0
FEET_TO_METERS = .3048
METERS_TO_KILOMETERS = .001
METERS_TO_CENTIMETERS = 100.0
METERS_TO_MILIMETERS = 1000.0
FEET_TO_INCHES = 12.0
YARDS_TO_FEET = 3.0
answer = 0.0
converting_from = 'cm'
converting_to = 'ft'


converting_from = raw_input('Enter the unit abbreviation you wish to convert from: ')
converting_to = raw_input('Enter the unit abbreviation you wish to convert to: ')
number = float(raw_input('What is the value that needs converted? ')
while converting_from != converting_to:
	if(converting_from == 'ft'):    
		if(converting_to == 'in'):
			answer = number * FEET_TO_INCHES
			converting_from = 'in'
		elif(converting_to == 'yd'):
			answer = number / YARDS_TO_FEET
			converting_from = 'yd'
		elif(converting_to == 'mm' or 'cm' or 'm' or 'km'):
			number = number * FEET_TO_METERS
			converting_from = 'm'
	elif(converting_from == 'in'):
		if(converting_to == 'yd' or 'ft' or 'mm' or 'cm' or 'm' or 'km'):
			number = number / FEET_TO_INCHES
			converting_from = 'ft'
	elif(converting_from == 'yd'):
		if(converting_to == 'ft' or 'in' or 'mm' or 'cm' or 'm' or 'km'):
			number = number * YARDS_TO_FEET
			converting_from = 'ft'
	elif(converting_from == 'm'):
		if(converting_to == 'ft' or 'in' or 'yd'):
			number = number / FEET_TO_METERS
			converting_from = 'ft'
		elif(converting_to == 'mm'):
			answer = number * METERS_TO_MILIMETERS
			converting_from = 'mm'
		elif(converting_to == 'cm'):
			answer = number * METERS_TO_CENTIMETERS
			converting_from = 'cm'
		elif(converting_to == 'km'):
			answer = number * METERS_TO_KILOMETERS
			converting_from = 'km'
	elif(converting_from == 'mm'):
		if(coverting_to == 'in' or 'ft' or 'yd' or 'cm' or 'm' or 'km'):
			number = number / METERS_TO_MILIMETERS
			converting_from = 'm'
	elif(converting_from == 'cm'):
		if(converting_to == 'in' or 'ft' or 'yd' or 'cm' or 'm' or 'km'):
			number = number / METERS_TO_CENTIMETERS
			converting_from = 'm'
	elif(converting_from == 'km'):
		if(converting_to == 'in' or 'ft' or 'yd' or 'cm' or 'm' or 'km'):
			number = number / METERS_TO_KILOMETERS
			converting_from = 'm'
print(answer)
print(converting_to)
				