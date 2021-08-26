def readint(prompt, min, max):
    try:
        number = int(input(prompt))
        assert(number>=min and number<=max)
        return number
    except AssertionError:
        print("Error: el valor no está en el rango permitido (-10..10)")
        return False
    except:
        print("Error:Error en el ingreso")
        return False

while True:
    v = readint("Enter a number from -10 to 10: ", -10, 10)
    if v:
        print("The number is:", v)
        break

