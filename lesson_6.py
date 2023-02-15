'''
try:
    name = "Serhii"
    print("start code")
    print(name)
    print(2/0)
    print('No errors')
except:
    print("We have a problems (error).")

print('This code after capsule.')
'''
'''
try:
    print('start code.')
    print(name)
    print(2/0)
    print("No errors")
except (NameError, ZeroDivisionError):
    print("We have an Error.")

except (NameError, ZeroDivisionError) as error:
    print(error)

print("code afrer capsule.")
'''
''''
try:
    try:
        print('start code')
        print(error)
        print('no error.')
    except SyntaxError:
        print('Wrong Syntax')
except NameError as error:
    print(error)
'''
try:
    error = 'q'
    print('start code')
    print(error)
    print('no error.')
except SyntaxError as error:
    print(error)
else:
    print("I am ELSE.")
finally:
    print("Finally code")

