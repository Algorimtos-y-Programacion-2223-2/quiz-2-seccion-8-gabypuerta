from Products import products

class games:
    def __init__(self, name,type,stock, price):
        super().__init__(name,type,stock, price )

    def mostrar(self):
        print(f"""Nombre:{self.name},
              Tipo:{self.type},
              Cantidad disponible:{self.stock},
              Precio:{self.price}""")