#1. Creamos los productos disponibles. 
productos = [
  {"id": 1, "nombre": "Camiseta Ronsoco", "precio": 35.90, "stock": 50},
  {"id": 2, "nombre": "Llavero Ronsoco", "precio": 12.50, "stock": 100},
  {"id": 3, "nombre": "Peluche Ronsoco", "precio": 45.00, "stock": 30}
]

# 2 Función mostrar.

def mostrar_catalogo():
  print("\nProductos Disponibles:")
  for p in productos:
    print(f"{p['id']}. {p['nombre']} - S/{p['precio']} (Stock: {p['stock']})")



# 3. Función principal
def main():
  print("""
  *****************************
  *  TIENDA DE RONSOCO   *
  *****************************
  """)
  carrito = []
  total = 0

  while True:
    mostrar_catalogo()
    opcion = input("\nElige un producto (número) o 'p' para pagar: ")
     
    if opcion.lower() == 'p':
      break
    try:
      id_producto = int(opcion)
      producto = next((p for p in productos if p["id"] == id_producto), None)
      if producto:
        if producto["stock"] > 0:
          carrito.append(producto)
          producto["stock"] -= 1
          total += producto["precio"]
          print(f"✅ Añadido: {producto['nombre']}")
        else:
          print("❌ ¡Producto agotado!")
      else:
        print("❌ Producto no válido")
    except ValueError:
      print("❌ Ingresa un número o 'p' para pagar")
   
  # Resumen de la compra
  print("\n----- TU COMPRA -----")
  for p in carrito:
    print(f"- {p['nombre']}: S/{p['precio']}")
    print(f"TOTAL: S/{total:.2f}")
    print("\n¡Gracias por comprar!")
    if __name__ == "__main__":
        main()
