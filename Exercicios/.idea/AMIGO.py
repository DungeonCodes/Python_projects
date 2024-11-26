
alphabet_to_number = {chr(i + 64): i for i in range(1, 27)}


numbers = [16, 5, 20, 9, 13]

# Função para converter números em letras
def numbers_to_word(numbers):
    number_to_alphabet = {v: k for k, v in alphabet_to_number.items()}  # Inverte o dicionário
    return ''.join(number_to_alphabet[num] for num in numbers)

# Converter os números de volta para a palavra
word = numbers_to_word(numbers)

# Imprimir o resultado
print(word)
