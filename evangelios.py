# python 3.8.10
import requests
from time import sleep
from csv import writer
from itertools import zip_longest
import re


def accumulator(acc, item):
    return acc + item


def load_mes(dias, mes, anio):
    lista_mes = []
    for dia in range(1, dias+1):
        res = requests.get(
            f"https://www.aciprensa.com/calendario/calendario.php?dia={dia}&mes={mes}&ano={anio}#3")
        pattern = re.compile(
            "(?<!=(<i>))(Marcos|Mateo|Lucas|(?<!(I\s))Juan(?!(\sI))).+(?=(<\/i>))")
        lectura = re.search(pattern, res.text)
        try:
            lista_mes.append(lectura.group())
            print(mes, dia, lectura.group())
        except AttributeError as err:
            lista_mes.append('Error web')
            print(mes, dia, 'Error_web')
        sleep(0.4)  # tener compasion de aciprensa.com
    return lista_mes


dias = [''] + [num for num in range(1, 31+1)]
enero = ['ENERO'] + load_mes(31, 1, 2022)
febrero = ['FEBRERO'] + load_mes(28, 2, 2022)  # chequear dias segun el anio
marzo = ['MARZO'] + load_mes(31, 3, 2022)
abril = ['ABRIL'] + load_mes(30, 4, 2022)
mayo = ['MAYO'] + load_mes(31, 5, 2022)
junio = ['JUNIO'] + load_mes(30, 6, 2022)
julio = ['JULIO'] + load_mes(31, 7, 2022)
agosto = ['AGOSTO'] + load_mes(31, 8, 2022)
septiembre = ['SEPTIEMBRE'] + load_mes(30, 9, 2022)
octubre = ['OCTUBRE'] + load_mes(31, 10, 2022)
noviembre = ['NOVIEMBRE'] + load_mes(30, 11, 2022)
diciembre = ['DICIEMBRE'] + load_mes(31, 12, 2022)

ziped = zip_longest(dias, enero, febrero, marzo, abril, mayo, junio,
                    julio, agosto, septiembre, octubre, noviembre, diciembre, fillvalue='')
with open('./lecturas2022.csv', "w") as f:
    writer = writer(f)
    for row in ziped:
        writer.writerow(row)
