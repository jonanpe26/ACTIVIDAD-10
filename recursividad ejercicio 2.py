def invertir(c, i=0):
    if i == len(c):
        return ""
    return invertir(c, i + 1) + c[i]}

def suma(n):
    if n == 0:
        return 0
    return n + suma(n-1)

def cuenta(n):
    if n == 0:
        return
    print(n)
    cuenta(n-1)

def sumd(n):
    if n == 0:
        return 0
    div = n // 10
    dig = n - div*10
    return dig + sumd(div)

def contd(n):
    if n < 0:
        n = -n
    if n < 10:
        return 1
    return 1 + contd(n // 10)

    while True:
        print("1. Invertir cadena")
        print("2. Suma primeros N")
        print("3. Cuenta regresiva")
        print("4. Suma digitos")
        print("5. Contar digitos")
        print("6. Salir")
        op = input("Opcion: ")

        if op == "1":
            t = input("Texto: ")
            print("Invertido:", inv(t))
        elif op == "2":
            n = int(input("Numero positivo: "))
            if n < 0:
                print("Error, debe ser positivo")
            else:
                print("Suma:", suma(n))
        elif op == "3":
            n = int(input("Numero positivo: "))
            if n < 0:
                print("Error, debe ser positivo")
            else:
                cuenta(n)
        elif op == "4":
            n = int(input("Numero positivo: "))
            if n < 0:
                print("Error, debe ser positivo")
            else:
                print("Suma digitos:", sumd(n))
        elif op == "5":
            n = int(input("Numero: "))
            print("Digitos:", contd(n))
        elif op == "6":
            print("Adios")
            break
        else:
            print("Opcion no valida")
