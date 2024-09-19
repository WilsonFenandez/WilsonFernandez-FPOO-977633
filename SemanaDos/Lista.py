#  Product

#  id:int
#  name:str
#  price:int
#  section:int

# 1.tech
# 2.clothes
# 3.food
store{}

id = int(input('Por favor ingrese el id de su producto:/n'))
name = (input('Por favor ingrese el nombre de su producto:/n'))
price = float(input('Por favor ingrese el precio de su producto:/n'))
section = input ('Por favor ingrese la section para su producto:/n')

Product1 = {
    "id":id,
    "name":name,
    "price":price,
    "section":section
}

store.append{product1}