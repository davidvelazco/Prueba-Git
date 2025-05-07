numeros = list(range(1, 1001))

def Es_un_numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros_primos = [num for num in numeros if Es_un_numero_primo(num)]
print("Los números primos entre 1 y 1000 son:", numeros_primos)