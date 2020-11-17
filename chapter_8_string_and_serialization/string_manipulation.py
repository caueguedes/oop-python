a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More 
multiple"""
e = ("Three " "Strings " "Together")

a.isalpha()
a.isupper()  # /islower()
a.startswith('h')  # /endswith('')
' '.isspace()

"Is Title".istitle() # return true if each word is capitalized

'1'.isdigit()
'1'.isdecimal()
'1'.isnumeric()
'45.2'.isdecimal()  # False 45\u06602 or the number 45.2
'127.0.0.1'.isdigit()  # .isdecimal() .isnumeric evaluate to True on all three
float('45\u06602')  # 4502.0


s = "hello world"
s.count('l')  # 3
s.find('l')  # 2
# r from reverse, index raise Error while count evaluate to -1 if not found
s.rindex('m')  # Traceback ... ValueError: substring not found


# this methods create a new str
s.upper()
s.lower()
s.capitalize()
s.title()


s = "hello world, how are you"
s2 = s.split(' ')
s2  # ['hello', 'world,', 'how', 'are', 'you']

'#'.join(s2)  # 'hello#world,#how#are#you'
s.replace(' ', '**')  # 'hello**world,**how**are**you'
s.partition(' ')  # ('hello', ' ', 'world, how are you')
