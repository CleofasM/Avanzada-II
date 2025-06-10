#ciclo for para mostrar las tablas de multiplicacion

print("PROGRAMA DE TABLAS DE MULTIPLICAR")

x=int(input("Ingrese la tabla que quiere que se realice: "))

for i in range(1,11):
    print(f"{x}x{i} = {i*x} ")