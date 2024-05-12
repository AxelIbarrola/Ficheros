PATH_ENTRADA = "./temperaturas.txt"
PATH_SALIDA = "./media_temperaturas.txt"

with open(PATH_ENTRADA) as archivo_temperaturas:
    promedios = []
    
    for linea in archivo_temperaturas:
        valores_temperaturas = linea.strip().split()
        largo_valores = len(valores_temperaturas)

        suma_temperaturas = 0
        for temperatura in valores_temperaturas:
            suma_temperaturas += int(temperatura)/largo_valores

        promedios.append(f"\n{suma_temperaturas:.2f}")
    
    promedios[0] = promedios[0].strip()

    with open(PATH_SALIDA, "w") as archivo_promedios:
        archivo_promedios.writelines(promedios)