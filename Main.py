from App import app

def main():

    products = [
        { "id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800 },
        { "id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600  },
        { "id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25 },
        { "id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5 },
        { "id": 5, "name": "Laptop Gamer", "type": "Gaming", "stock": 11, "price": 2500 },
        { "id": 6, "name": "Nintendo Switch OLED", "type": "Gaming", "stock": 25, "price": 400 },]
    
    



    new_products={
        "Hogar":[], 
        "Ropa":[],
        "Juegos":[]}

    for key in products:
        if key["id"]== 1:
            new_products["Hogar"].append(key)
        if key["id"]==2:
            new_products["Hogar"].append(key)
        if key["id"]==3:
            new_products["Ropa"].append(key)
        if key["id"]==4:
            new_products["Ropa"].append(key)
        if key["id"]==5:
            new_products["Juegos"].append(key)
        if key["id"]==6:
            new_products["Juegos"].append(key)
 
    App=app 
    app.start()

main()
