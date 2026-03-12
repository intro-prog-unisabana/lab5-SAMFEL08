def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0 
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = suma / cantidad
    return float(promedio)

promedio = promedio_estudiante([85, 92, 78])
print(promedio)