x = 3
print(x, type(x))

print(x + 1)   
print(x - 1)   
print(x * 2)   
print(x ** 2)  

x += 1
print(x)
x *= 2
print(x)

y = 2.5
print(type(y))
print(y, y + 1, y * 2, y ** 2)

t, f = True, False
print(type(t))

print(t and f) 
print(t or f)  
print(not t)   
print(t != f)  

hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes; it does not matter
print(hello, len(hello))

hw = hello + ' ' + world  # String concatenation
print(hw)

def hello(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}!'.format(name))

hello('Bob')
hello('Fred', loud=True)

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
