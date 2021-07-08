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
            word[i] = 1
    return word



def max_repeated(words):
    max_word = ''
    max_repeated = 0
    for word, freq in words.items():
        #todos son mayores hasta que se encuentre lo contrario
        if freq > max_repeated:
            max_word = word
            max_repeated = freq
    return max_word, max_repeated

text = "Hola mundo mundo mundo como estas tu y yo y tu tu tu tu tu"
print(count_word(text))
print(max_repeated(count_word(text)))