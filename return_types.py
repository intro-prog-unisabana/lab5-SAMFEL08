def obtener_precio_usuario():
    precio_input=input("Enter the item's price:\n")
    return float(precio_input)
if __name__ == "__main__":
    precio = obtener_precio_usuario()
    print(precio)