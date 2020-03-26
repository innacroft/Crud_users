
class Persona:
    def __init__(self, name,age):
        self.name=name
        self.age=age
        
    def say_hello(self):
        print('Hola , mi nombre es {} , y tengo {} años' .format(self.name,self.age))


if __name__ == "__main__":
    _nombre= input('porfavor digite su nombre')
    _edad= input('porfavor digite su edad')
    persona_= Persona(_nombre,_edad)
    persona_.say_hello()