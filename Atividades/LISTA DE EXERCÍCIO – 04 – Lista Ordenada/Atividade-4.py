def ordenar_vetor_selecao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_min]:
                indice_min = j
        vetor[i], vetor[indice_min] = vetor[indice_min], vetor[i]

def ordenar_vetor(vetor, crescente=True):
    vetor.sort(reverse=not crescente)

def encontrar_maximo(vetor):
    maximo = vetor[0]
    for numero in vetor:
        if numero > maximo:
            maximo = numero
    return maximo

def encontrar_minimo(vetor):
    minimo = vetor[0]
    for numero in vetor:
        if numero < minimo:
            minimo = numero
    return minimo

def encontrar_segundo_menor(vetor):
    vetor_unico = list(set(vetor))
    vetor_unico.sort()
    if len(vetor_unico) >= 2:
        return vetor_unico[1]
    else:
        return None

def remover_duplicatas(vetor):
    vetor_sem_duplicatas = list(set(vetor))
    return vetor_sem_duplicatas

def contar_pares_impares(vetor):
    pares = 0
    impares = 0
    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def encontrar_terceiro_maior(vetor):
    vetor_unico = list(set(vetor))
    vetor_unico.sort(reverse=True)
    if len(vetor_unico) >= 3:
        return vetor_unico[2]
    else:
        return None

def calcular_mediana(vetor):
    vetor.sort()
    n = len(vetor)
    if n % 2 == 1:
        return vetor[n // 2]
    else:
        medio1 = vetor[(n // 2) - 1]
        medio2 = vetor[n // 2]
        return (medio1 + medio2) / 2

if __name__ == "__main__":
    vetor = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    ordenar_vetor_selecao(vetor)
    print("Vetor ordenado em ordem crescente:", vetor)
    
    ordenar_vetor(vetor, crescente=False)
    print("Vetor ordenado em ordem decrescente:", vetor)
    
    maximo = encontrar_maximo(vetor)
    minimo = encontrar_minimo(vetor)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    
    segundo_menor = encontrar_segundo_menor(vetor)
    print("Segundo menor número:", segundo_menor)
    
    vetor_sem_duplicatas = remover_duplicatas(vetor)
    print("Vetor sem duplicatas:", vetor_sem_duplicatas)
    
    pares, impares = contar_pares_impares(vetor)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

    terceiro_maior = encontrar_terceiro_maior(vetor)
    print("Terceiro maior número:", terceiro_maior)
    
    mediana = calcular_mediana(vetor)
    print("Mediana:", mediana)
