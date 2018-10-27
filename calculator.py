e = input('Do you want to: add, subtract, times or divide? ')

if e == 'times':
    a = input('choose a number ')
    b = input('choose a number ')
    c = float(a) * float(b)
    print('answer: ' + str(c))
    input()
    
elif e == 'subtract':
    a = input('choose a number ')
    b = input('choose a number ')
    c = float(a) - float(b)
    print('answer: ' + str(c))
    input()

elif e == 'add':
    a = input('choose a number ')
    b = input('choose a number ')
    c = float(a) + float(b)
    print('answer: ' + str(c))
    input()

elif e == 'divide':
    a = input('choose a number ')
    b = input('choose a number ')
    c = float(a) / float(b)
    print('answer: ' + str(c))
    input()
