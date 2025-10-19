#Here are some logical operator
x = int(input ('Enter x: '))
y = int(input ('Enter y: '))
print('x is:',x)
print('y is:',y)
print('both are same' if x==y else 'not same' )#to check equal to
print('x is greater or equal' if x>=y else 'x is not greater or equal')#to check greater than or equal to
print('y is greater or equal' if x<=y else 'y is not greater or equal')#to check less than or equal to
print('both are not same' if x!=y else 'both are not same')#to check not equal to
print('x is greater' if x>y else 'x is not greater')#to check greater than
print('y is greater' if x<y else ' is greater')#to check less than