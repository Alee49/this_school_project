cont = 0;
while cont == 0:
  utype = input("Enter the type of conversion you want: (temperature, length, volume)");
  if utype == "temperature":
    F = 0
    C = 1
    K = 2
  
    print("Please enter your conversion in this format: lowercase_unit_from(value,uppercase_unit_to)")
    print("")
    print("Example:")
    print("To convert 45 degrees Fahrenheit to Celsius, type:")
    print("f(45,C)")
  
    def f(value, base):
      if base == F:
          return value
      elif base == C:
          return (value - 32)/1.8
      elif base == K:
          return (value - 32)/1.8 + 273.15
      else:
          print ("Error: incorrect format.")
  
    def c(value, base):
      if base == C:
          return value
      elif base == F:
          return (1.8 * value) + 32
      elif base == K:
          return value + 273.15
      else:
          print ("Error: incorrect format.")
  
    def k(value, base):
      if base == K:
          return value
      elif base == C:
          return (value - 273.15)
      elif base == F:
          return (value - 273.15) * 1.8 + 32
      else:
          print ("Error: incorrect format.")
  elif(utype == "length"):
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
  elif(utype == "volume"):
    uinput = input("Enter the type of volume you want to convert from (mL, L, floz, qt)");
    uinput = uinput.lower();
    ninput = float(input("How much?"));
    u2input=(input("Enter the type of volume you are converting to."));
    u2input = u2input.lower();
    if uinput == "ml":
      if u2input == "l":
        print(ninput*.001);
      elif u2input == "floz":
        print(ninput*0.0351950797)
      elif u2input == "qt":
        print(ninput*0.0010566887)
    elif uinput == "l":
      if u2input == "ml":
        print(ninput*1000)
      elif u2input == "qt":
        print(ninput*1.0566887074)
      elif u2input == "floz":
        print(ninput*33.814038638)
    elif uinput == "floz":
      if u2input == "ml":
        print(ninput*29.573515625)
      elif u2input == "l":
        print(ninput*0.0295735156)
      elif u2input == "qt":
        print(ninput*0.03125)
    elif uinput == "qt":
      if u2input == "ml":
        print(ninput*946.3525)
      elif u2input == "l":
        print(ninput*0.9463525)
      elif u2input == "floz":
        print(ninput*32)
  elif (utype == "weight"):
	print("Welcome please use the abriviated units for the following")
	print("We support Pounds(lb), Kilogram(kg), Gram(g), Milligram(mg), Ounce(oz)")
	unit1 = input ("Which unit would you like to convert from: ")
	unit2 = input("Which unit would you like to convert to: ")
	num1 = input("Enter value: ")

	Ref = {'lb':0.453592,'mg':0.001,'oz':16}

	if unit1 == "lb" and unit2 == "kg":
	    ans = float(num1)*Ref['lb']
	    ans = round(ans,3)
	    print(ans,'kg')
	elif unit1 == "kg" and unit2 == "lb":
		ans = float(num1)/Ref['lb']
		ans = round(ans,3)
		print(ans,'lb')
	elif unit1 == "lb" and unit2 == "g":
		ans = float(num1)*Ref['lb']/Ref['mg']
		ans = round(ans,3)
		print(ans,'g')
	elif unit1 == "g" and unit2 == "lb":
		ans = float(num1)/Ref['lb']*Ref['mg']
		ans = round(ans,3)
		print(ans,'lb')
	elif unit1 == "lb" and unit2 == "mg":
		ans = float(num1)*Ref['lb']/Ref['mg']/Ref['mg']
		ans = round(ans,3)
		print(ans,'mg')
	elif unit1 == "mg" and unit2 == "lb":
		ans = float(num1)/Ref['lb']*Ref['mg']*Ref['mg']
		ans = round(ans,4)
		print(ans,'lb')
	elif unit1 == "kg" and unit2 == "g":
		ans = float(num1)/Ref['mg']
		ans = round(ans,3)
		print(ans,'g')
	elif unit1 == "g" and unit2 == "kg":
		ans = float(num1)*Ref['mg']
		ans = round(ans,3)
		print(ans,'kg')
	elif unit1 == "g" and unit2 == "mg":
		ans = float(num1)/Ref['mg']
		ans = round(ans,3)
		print(ans,'mg')
	elif unit1 == "mg" and unit2 == "g":
		ans = float(num1)*Ref['mg']
		ans = round(ans,3)
		print(ans,'g')
	elif unit1 == "kg" and unit2 == "mg":
		ans = float(num1)/Ref['mg']/Ref['mg']
		ans = round(ans,3)
		print(ans,'mg')
	elif unit1 == "mg" and unit2 == "kg":
		ans = float(num1)*Ref['mg']*Ref['mg']
		ans = round(ans,4)
		print(ans,'kg')
	elif unit1 == "lb" and unit2 == "oz":
		ans = float(num1)*Ref['oz']
		ans = round(ans,3)
		print(ans,'oz')
	elif unit1 == "oz" and unit2 == "lb":
		ans = float(num1)/Ref['oz']
		ans = round(ans,3)
		print(ans,'lb')
	elif unit1 == "kg" and unit2 == "oz":
		ans = float(num1)/Ref['lb']*Ref['oz']
		ans = round(ans,3)
		print(ans,'oz')
	elif unit1 == "oz" and unit2 == "kg":
		ans = float(num1)*Ref['lb']/Ref['oz']
		ans = round(ans,3)
		print(ans,'kg')
	elif unit1 == "g" and unit2 == "oz":
		ans = float(num1)*Ref['mg']/Ref['lb']*Ref['oz']
		ans = round(ans,3)
		print(ans,'oz')
	elif unit1 == "oz" and unit2 == "g":
		ans = float(num1)/Ref['mg']*Ref['lb']/Ref['oz']
		ans = round(ans,3)
		print(ans,'g')
	elif unit1 == "mg" and unit2 == "oz":
		ans = float(num1)*Ref['mg']*Ref['mg']/Ref['lb']*Ref['oz']
		ans = round(ans,3)
		print(ans,'oz')
	elif unit1 == "oz" and unit2 == "mg":
		ans = float(num1)/Ref['mg']/Ref['mg']*Ref['lb']/Ref['oz']
		ans = round(ans,3)
		print(ans,'mg')
  cont = int(input("Would you like to do another conversion? 0 for yes, 1 for no"))

  
