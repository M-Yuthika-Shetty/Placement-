#a=10
#b=3
#print((a-(-b))) #add
#print((a%b)) #mod

a = -4
b =2


def divide(a, b):
    quotient = 0
    abs_a, abs_b = abs(a), abs(b)
    while abs_a >= abs_b:
        abs_a -= abs_b
        quotient += 1
    if (a < 0) != (b < 0):
        quotient = -quotient
    return quotient
print(divide(a, b))