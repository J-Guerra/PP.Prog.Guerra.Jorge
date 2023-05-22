def ordenarCaracteres(cadena: str) -> str:
    tam = len(cadena)
    caracteres = list(cadena)
    
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if caracteres[i] > caracteres[j]:
                caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
    
    cadena_ordenada = ''.join(caracteres)
    return cadena_ordenada


print(ordenarCaracteres("algoritmo"))