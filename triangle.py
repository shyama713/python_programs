a=float(input('Enter the First side of Triangle :'))
b=float(input('Enter the second side of Triangle :'))
c=float(input('Enter the Third side of Triangle :'))

s=(a + b + c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is : %0.2f' %area)