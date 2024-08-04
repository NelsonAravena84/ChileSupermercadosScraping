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

categorias = {
    'Aseo': ListaNombresAseo,
    'Bebidas': ListaNombresBebidas,
    'Carnes': ListaNombresCarnes,
    'Despensa': ListaNombresDespensa,
    'Frescos': ListaNombresFrescos,
    'Frutas': ListaNombresFrutas,
    'Pescados': ListaNombresPescados
}


#nombre
fila = 1
for categoria, nombres in categorias.items():
    for nombre in nombres:
        worksheet.write(fila, 0, categoria)  # Categoría en la columna A
        worksheet.write(fila, 1, nombre)      # Nombre en la columna B
        fila += 1

workbook.close()
