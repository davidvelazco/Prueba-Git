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

# INICIO
#     Definir lista NUMEROS con valores de 1 a 1000
    
#     FUNCION Es_un_numero_primo(numero)
#         SI numero < 2 ENTONCES
#             RETORNAR FALSO
#         FIN SI
#         PARA i DESDE 2 HASTA raíz cuadrada de numero
#             SI numero MOD i = 0 ENTONCES
#                 RETORNAR FALSO
#             FIN SI
#         FIN PARA
#         RETORNAR VERDADERO
    
#     FIN FUNCION

#     Definir lista NUMEROS_PRIMOS = []
    
#     PARA cada numero EN NUMEROS HACER
#         SI Es_un_numero_primo(numero) ENTONCES
#             Agregar numero a NUMEROS_PRIMOS
#         FIN SI
#     FIN PARA
    
#     Imprimir "Los números primos entre 1 y 1000 son:", NUMEROS_PRIMOS
# FIN