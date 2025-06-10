#Condicionales en python
a=int(input("a: "))


if a%2==0:
    if a==0:
        print("Es cero.")
    else:
        print(f"{a} es par.")
else:
    print(f"{a} es impar.")