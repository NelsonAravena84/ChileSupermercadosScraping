import requests 
import json 

from bs4 import BeautifulSoup

def CategoriaDespensa(Mostrar):
    url = ('https://www.lider.cl/supermercado/category/Activaciones/Supermercado/Productos_Despensa?page=1&hitsPerPage=100')
    headers = {'user-agent' : 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
    peticion = requests.get(url, headers=headers)
    
    if peticion.status_code == 200:
        print("se hizo la conexiòn de manera correcta")
        cambiarDato = peticion.text
        soup = BeautifulSoup(cambiarDato, 'html.parser')
        encontrarEtiqueta = soup.find('script', {'type':'application/ld+json'})
        #print(encontrarEtiqueta)
        textosinetiqueta = encontrarEtiqueta.string
        print(textosinetiqueta)
        with open ('LiderDespensa.json', 'w') as f:
            json.dump(textosinetiqueta, f)
    else:
        print(f'erorr en la conexiòn {peticion.raise_for_status()}')

def CategoriaCarnesParte1(Mostrar):
    url = ('https://www.lider.cl/supermercado/category/Carnes_y_Pescados/Todas_las_Carnes?page=1&hitsPerPage=100')
    headers = {'user-agent' : 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
    peticion = requests.get(url, headers=headers)
    
    if peticion.status_code == 200:
        print("se hizo la conexiòn de manera correcta")
        cambiarDato = peticion.text
        soup = BeautifulSoup(cambiarDato, 'html.parser')
        encontrarEtiqueta = soup.find('script', {'type':'application/ld+json'})
        #print(encontrarEtiqueta)
        textosinetiqueta = encontrarEtiqueta.string
        print(textosinetiqueta)
        with open ('LiderCarnes1.json', 'w') as f:
            json.dump(textosinetiqueta, f)
    else:
        print(f'erorr en la conexiòn {peticion.raise_for_status()}')
