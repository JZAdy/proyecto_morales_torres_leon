"""Ejemplo de inventario de memorias usando variables, listas, diccionarios y for."""

nombre_tienda = "Tienda de Memorias"
inventario_memoria = [
    {"producto": "Memoria RAM DDR4", "capacidad": "8 GB", "cantidad": 10, "precio": 25.50},
    {"producto": "Memoria RAM DDR5", "capacidad": "16 GB", "cantidad": 6, "precio": 48.00},
    {"producto": "Memoria USB", "capacidad": "64 GB", "cantidad": 15, "precio": 12.75},
]

total_unidades = 0
valor_inventario = 0

print(f"Inventario de {nombre_tienda}")
print("-" * 50)

for memoria in inventario_memoria:
    print(
        f"Producto: {memoria['producto']} | "
        f"Capacidad: {memoria['capacidad']} | "
        f"Cantidad: {memoria['cantidad']} | "
        f"Precio: ${memoria['precio']:.2f}"
    )
    total_unidades += memoria["cantidad"]
    valor_inventario += memoria["cantidad"] * memoria["precio"]

print("-" * 50)
print(f"Total de unidades: {total_unidades}")
print(f"Valor total del inventario: ${valor_inventario:.2f}")
