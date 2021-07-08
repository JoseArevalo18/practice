print("hola mundo")
#escribir una funcion que convierta # decimal en binaario y otra que convierta # binario en decimal, ingresado por el usuario

#binario en decimal
def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0

    for num in range(len(n)):
        decimal += int(n[num]) * 2 ** num
    return decimal

print(to_decimal('0110110'))

