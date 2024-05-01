promedios = []

with open("./temperaturas.txt") as archivo_temperaturas:
    
    for linea in archivo_temperaturas:
        
        linea.strip()
        
        temperaturas_formato_cadena = linea.split()
        temperaturas_formato_enteros = []
        suma_temperaturas = 0
        
        for cadena in temperaturas_formato_cadena:
            temperaturas_formato_enteros.append(int(cadena))
        
        for temperatura in temperaturas_formato_enteros:
            suma_temperaturas += temperatura
        
        promedios.append(f"{suma_temperaturas/31:.2f}")
        

with open("./media_temperaturas.txt", "w") as archivo_promedios:
        
    for promedio in promedios:
        archivo_promedios.write(str(promedio) + "\n")
        
