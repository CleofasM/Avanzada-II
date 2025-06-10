#Programa que calcule la edad de una persona
print("PROGRAMA PARA CALCULAR LA EDAD DE UNA PERSONA")

nacimiento=int(input("Ingrese su anio de nacimiento: "))
anio=int(input("Ingrese el anio actual: "))

edad=anio-nacimiento

print(f"{edad} es su edad. ")

if edad>=21:
    print(f"ya tienes {edad} anios, por lo tanto eres mayor")
else:
    if edad>=18:
        print(f"Ya tienes {edad} anios, ya eres ciudadano")
    else:
        print(f"Ya tienes {edad} anios, ta bb")