####Tentando criar um restaurante  com dois atributos restuarant_name e cusine_type####
class Restuarant():
    "modelando um restaurante"
    def __init__(self,restaurant_name,cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    # Acima esta o metodo da classe ele indica que o metodo self esta disponivel a todos os metodos da classe
    # self.name usa o parametro armazenado no name / variaveis como essa acessiveis por meio de instancia -->
    # sao chamadas de atributo
    # self eh uma referencia a instancia Restaurant
    def describe_restaurante(self):
        restaurante = []
        for i in range(0,3):
            restaurant_name = input("O nome do restaurante:")
            cusine_type = input("o tipo de cozinha:")
            restaurante.append(restaurant_name)
            print('restaurantes:',restaurante)
            print('Seu nome eh'+ ' ' + restaurant_name + '  '  + 'sua cozinha' + '  ' + cusine_type)


    def open_restaurante(self):
        print('**restaurante aberto**')

#instancia restuarant

restaunt = Restuarant('','')
restaurante = restaunt.describe_restaurante()
print(restaurante)

