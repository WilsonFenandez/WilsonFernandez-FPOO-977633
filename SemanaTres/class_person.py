#-------------------------
#person

#dni: int
#name: str
#lastname: int
#role:int
#-----------------------

class Person:
 def __init__(self,dni:int,name:str,lastname:str,role:int):
    self.dni = dni
    self.name = name
    self.lastname = lastname
    self.role = role
 ## con esta funcion puedo traer solo un campo de la lista no toda la informacion
 ##def __repr__(self):
   ## return f"name={self.name,self.lastname}"
   
 ## otra manera de traer campos de una lista
 def __repr__(self):
    return "dni={}".format(self.dni)     

person1= Person(dni=123, role=1, name = "luisito", lastname="velez")

print(person1)
