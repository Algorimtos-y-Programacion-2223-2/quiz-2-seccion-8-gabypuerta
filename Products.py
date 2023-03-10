class products:
    
    def __init__(self, name, type,stock,price):
        self.name=name
        self.type=type
        self.stock=stock
        self.price=price

    def mostrar(self):
        print(f"""
        Nombre:{self.name},
        Tipo:{self.type},
        Cantidad disponible:{self.stock},
        Precio:{self.price}""")

    



