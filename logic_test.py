def somar(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += numero
        else:
            impares += numero
    return pares, impares

if __name__ == "__main__":
    entrada = input("Digite uma lista de números separados por espaços: ")
    list_num = [int(num) for num in entrada.split()]
    pares, impares = somar(list_num)
    print(f"Soma dos pares: {pares}")
    print(f"Soma dos ímpares: {impares}")