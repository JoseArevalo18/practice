#Escribir un programa qe me escriba una cadena de text0/caracteres y me devuelva un diccionario con cada palabra que contiene y cada cuanto se repite
#Programa con funciona que reciba el diccionario anterior y me regrese una tupla con la palabra mas repetida

#Cuenta el # que aparece en cada palabra

def count_word(text):
    text = text.split()
    word = {}
    for i in text:
        if i in word:
            word[i] += 1
        else:








# def max_repeated(words):
    max_word = ''
    max_repeated = 0
    



text = "Hola mundo mundo como estas tu y yo y tu"
print(count_word(text))