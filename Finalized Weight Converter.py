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
