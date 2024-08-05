import xlsxwriter


from Acuenta import ListaNombresAseo, ListaPrecioAseo
from Acuenta import ListaNombresBebidas, ListaPrecioBebidas
from Acuenta import ListaNombresCarnes, ListaPrecioCarnes
from Acuenta import ListaNombresDespensa, ListaPrecioDespensa
from Acuenta import ListaNombresFrescos, ListaPrecioFrescos
from Acuenta import ListaNombresFrutas, ListaPrecioFrutas
from Acuenta import ListaNombresPescados, ListaPrecioPescados

workbook = xlsxwriter.Workbook('DatosAcuenta.xlsx')

worksheet = workbook.add_worksheet()

# Escribir los encabezados
worksheet.write('A1', 'Categoria')
worksheet.write('B1', 'Nombre')
worksheet.write('C1', 'Precio')

categorias = {
    'Aseo': ListaNombresAseo,
    'Bebidas': ListaNombresBebidas,
    'Carnes': ListaNombresCarnes,
    'Despensa': ListaNombresDespensa,
    'Frescos': ListaNombresFrescos,
    'Frutas': ListaNombresFrutas,
    'Pescados': ListaNombresPescados
}

# Lista de precios correspondientes para cada categoría
precios = {
    'Aseo': ListaPrecioAseo,
    'Bebidas': ListaPrecioBebidas,
    'Carnes': ListaPrecioCarnes,
    'Despensa': ListaPrecioDespensa,
    'Frescos': ListaPrecioFrescos,
    'Frutas': ListaPrecioFrutas,
    'Pescados': ListaPrecioPescados
}

#nombre
fila = 1
for categoria, nombres in categorias.items():
    lista_precios = precios[categoria]
    for nombre, precio in zip(nombres, lista_precios):
        worksheet.write(fila, 0, categoria)  # Categoría en la columna A
        worksheet.write(fila, 1, nombre)      # Nombre en la columna B
        worksheet.write(fila, 2, precio)      # Precio en la columna C
        fila += 1

workbook.close()
