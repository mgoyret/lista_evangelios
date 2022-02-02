# python 3.8.10
import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from time import sleep
from csv import writer
from itertools import zip_longest

anio = 2022


def load_mes(dias, mes):
    lista_mes = []
    for dia in range(1, dias+1):
        res = requests.get(
            f"https://www.aciprensa.com/calendario/calendario.php?dia={dia}&mes={mes}&ano={anio}#3")
        soup = BeautifulSoup(res.text, "html.parser")
        titulos = soup.find_all('i')
        if len(titulos):  # si la pagina no esta cargada, cargo error
            for titulo in titulos:
                lectura = str(titulo).replace('<i>', '').replace('</i>', '')
                if ('Mateo' in lectura) or ('Marcos' in lectura) or ('Lucas' in lectura) or (('Juan' in lectura) and ('I' not in lectura)):
                    lista_mes.append(lectura)
                    print(mes, dia, lectura)
                    break  # si ofrece dos evangelios, me quedo con el primero
        else:
            lista_mes.append('Error web')
            print(mes, dia, 'Error_web')
        # sleep(0.1)
    return lista_mes


dias = [''] + [num for num in range(1, 31+1)]
enero = ['ENERO'] + load_mes(31, 1)
febrero = ['FEBRERO'] + load_mes(28, 2)  # chequear dias segun el anio
marzo = ['MARZO'] + load_mes(31, 3)
abril = ['ABRIL'] + load_mes(30, 4)
mayo=['MAYO'] + load_mes(31, 5)
junio=['JUNIO'] + load_mes(30, 6)
julio=['JULIO'] + load_mes(31, 7)
agosto=['AGOSTO'] + load_mes(31, 8)
septiembre=['SEPTIEMBRE'] + load_mes(30, 9)
octubre=['OCTUBRE'] + load_mes(31, 10)
noviembre=['NOVIEMBRE'] + load_mes(30, 11)
diciembre=['DICIEMBRE'] + load_mes(31, 12)

ziped=zip_longest(dias, enero, febrero, marzo, abril, mayo, junio, julio,
                  agosto, septiembre, octubre, noviembre, diciembre, fillvalue='')
with open('./lecturas2022.csv', "w") as f:
    writer=writer(f)
    for row in ziped:
        writer.writerow(row)
