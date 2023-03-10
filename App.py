from Home import home
from Clothes import clothes 
from Games import games 


class app:


    def checking_inventary(self):
        print("""Ingrese que desea ver:
        1.Hogar
        2.Ropa
        3.Juegos""")

        option_1=input("Ingrese el número que desea ver:")

        while not option_1.isnumeric():
            print("Error!")
            option_1=input("Ingrese el número que desea ver:")

        if option_1==1:
            print(new_products["Hogar"])
        elif option_1==2:
            print(new_products["Ropa"])
        elif option_1==3:
            print(new_products["Juegos"])



    def start():
        while True:
            print("Bienvenido a la Tienda Super Samancito")
            print("""Ingrese la acción que desea
        1.Ver productos
        2.Salir 
        """)
            option=input("Ingrese el número de la acción que desea: ")
            
            while not option.isnumeric():
                print("Error")
                option=input("Ingrese el número de la acción que desea:")
                option=int(option)
                
                if option==1:
                    checkin_inventary(self)
                else: 
                    break
