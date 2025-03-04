import numpy as np

codigos = np.arange(1, 6501)  
nombres = np.array(["Estudiante" + str(i) for i in codigos])
codigos_carrera = np.random.randint(1, 11, size=6500) 
años_ingreso = np.random.randint(1980, 2025, size=6500)  
promedios = np.round(np.random.uniform(2.0, 5.0, size=6500), 2)  


estudiantes = np.column_stack((codigos, nombres, codigos_carrera, años_ingreso, promedios))


codigo_carrera_x = int(input("Ingrese código de la carrera(Del 1 al 10): "))


filtro1 = (estudiantes[:, 2].astype(int) == codigo_carrera_x) & (estudiantes[:, 4].astype(float) >= 4)
estudiantes_carrera = estudiantes[filtro1]

print("\nEstudiantes con promedio >= 4 en la carrera", codigo_carrera_x)
for est in estudiantes_carrera:
    print(f"Código: {est[0]}, Nombre: {est[1]}")
print(f"Total: {len(estudiantes_carrera)} estudiantes.")


filtro2 = (estudiantes[:, 3].astype(int) < 1990) & (estudiantes[:, 4].astype(float) < 3)
estudiantes_condicionales = estudiantes[filtro2]

print("\nEstudiantes que ingresaron antes de 1990 y están condicionales:")
for est in estudiantes_condicionales:
    print(f"Código: {est[0]}, Nombre: {est[1]}")
print(f"Total: {len(estudiantes_condicionales)} estudiantes.")

