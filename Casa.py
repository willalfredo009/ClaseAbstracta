from abc import ABC, abstractmethod


class Casa():
    def _init_(self, Nombre, Edad, Genero):
        self.Nombre= Nombre
        self.Edad= Edad
        self.Genero= Genero
        
    @abstractmethod
    def Informacion(self):
        pass
    
        
class Persona(Casa):
    def _init_(self, Nombre, Edad, Genero):
        self.Nombre= Nombre
        self.Edad= Edad
        self.Genero= Genero

    def Informacion(self):
        return 'El nombre de esa persona es {} y su edad es {} años, género {}'.format(self.nombre, self.edad, self.genero)
    
class Animal(Casa):
    def _init_(self, Nombre, Edad):
        self.Nombre= Nombre
        self.Edad= Edad

    def Informacion(self):
        return 'El perrito se llama {}, tiene {} meses'.format(self.Nombre, self.Edad)

class Super(Casa):
    def _init_(self, Precio):
        self.Precio= Precio

    def Infromacion(self):
        return 'El precio del jabon es ${} en el super que esta emfrente de mi casa'.format(self.Precio)
    
Nombre = Persona('Wil', 27, 'Masculino')
Perro = Animal('Canelo', 7)
Mini = Super(5)
print(Nombre.Informacion())
print(Perro.Informacion())
print(Mini.Informacion())