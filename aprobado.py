

def determinarAprobado(promedio):
    
    if 0<=promedio<=10:
        print("El alumno está desaprobado.")
        
    elif 20>=promedio>10:
        print("El alumno está aprobado.")
    
    else:
        print("La entrada es incorrecta.")
        
        
promedio = int(input("Ingrese el promedio: "))

determinarAprobado(promedio)