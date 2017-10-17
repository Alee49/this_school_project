F = 0
C = 1
K = 2

print("Please enter your conversion in this format: lowercase_unit_from(value,uppercase_unit_to)")
print("")
print("Example:")
print("To convert 45 degrees Fahrenheit to Celsius, type:")
print("f(45,C)")

def f(value, new):
    if new == F:
        return value
    elif new == C:
        return (value - 32)/1.8
    elif new == K:
        return (value - 32)/1.8 + 273.15
    else:
        print ("Error: incorrect format.")

def c(value, new):
    if new == C:
        return value
    elif new == F:
        return (1.8 * value) + 32
    elif new == K:
        return value + 273.15
    else:
        print ("Error: incorrect format.")

def k(value, new):
    if new == K:
        return value
    elif new == C:
        return (value - 273.15)
    elif new == F:
        return (value - 273.15) * 1.8 + 32
    else:
        print ("Error: incorrect format.")
