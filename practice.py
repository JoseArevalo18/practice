print("hola mundo")
#escribir una funcion que convierta # decimal en binaario y otra que convierta # binario en decimal, ingresado por el usuario

#binario en decimal
def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0

    #num+=1 es equivalente a decir num=(num+1)
    #num=+1 es equivalente a decir num=(+1)

    for num in range(len(n)):
        decimal += int(n[num]) * 2 ** num
    return decimal

#decimal a binario
def to_binary(n):
    binary =[]
    while n > 0:
        binary.append(str(n % 2))
        n //=2
    binary.reverse()
    #12 % 2 = 0
    #6  % 2 = 0 
    #3  % 2 = 1
    #1  % 2 = 1
    #[0011]->[1100]
    return ''.join(binary)

print(to_decimal('0110110'))
print(to_binary(12))

