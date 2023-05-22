def ordenarCaracteres(cadena: str) -> str:
    tam = len(cadena)
    caracteres = list(cadena)
    
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if caracteres[i] > caracteres[j]:
                aux = caracteres[i]
                caracteres[i] = caracteres[j]
                caracteres[j] = aux
    
    cadena_ordenada = ''.join(caracteres)
    return cadena_ordenada


print(ordenarCaracteres("algoritmo"))