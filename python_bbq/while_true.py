while True:
    try:
        zahl = input('Geben Sie eine Zahl ein: ')
        float(zahl)
        break
    except:
        print('Dies ist keine Zahl!')
print('Danke')


while True:
    zahl = input('Geben Sie eine Zahl ein: ')
    if zahl.isdigit():
        break
    else:
        print('Dies ist keine Zahl!')
print('Danke')