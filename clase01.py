#crearemos la clase animal

class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def correr(self):
        print(f"{self.nombre} esta corriendo")

class Perro(Animal):
    def ladrar(self):
        print("Grrrr grrrrrrr guauuuuuuuu guau grrr")
    
class Gato(Animal):
    def maullar(self):
        print("miau miau miau miau")

#Definir objeto para usar la clase 

miPerro=Perro("Canducho")

miPerro.ladrar()
miPerro.comer()
miPerro.correr()

miGato=Gato("Kirito")
miGato.maullar
miGato.comer
miGato.correr
#perro= Animal("Cristian")

#perro.correr()
#perro.ladrar()
#perro.comer()

