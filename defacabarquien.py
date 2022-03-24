import copy
import random

lista_atributos = {'1':'sexo', '2':'gafas','3': 'barba','4': 'pendientes', '5':'color_pelo', '6':'gorra', '7':'sombrero', '8':'pelo_largo','9': 'pelo_corto', '10':'bigote','11':'tatuajes'}
lista_personajes=['Alejandro','Sara','Pedro','Laura','Lewis','Luis','Maricarmen','Joaquin','Alejandra','Joan']

# 'sexo', 'gafas', 'barba', 'pendientes', 'color_pelo', 'gorra', 'sombrero', 'pelo_largo', 'pelo_corto', 'bigote','calvo'
def random_ia(test):
    z = random.randint(1, 9)
    x=str(z)
    atr_ia = lista_atributos[x]
    return atr_ia


# DICCIONARIO DE PERSONAS



#hay que añadir los atributos que faltan.
dicci_pers_p1={
'Alejandro':{'sexo':'M','gafas':'yes','barba':'yes','pendientes':'no','color_pelo':'blanco','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'yes','tatuajes':'yes'},
'Sara':{'sexo':'F','gafas':'no','barba':'no','pendientes':'yes','color_pelo':'platino','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'no','tatuajes':'no'},
'Pedro':{'sexo':'M','gafas':'yes','barba':'yes','pendientes':'yes','color_pelo':'pelirrojo','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'yes','tatuajes':'yes'},
'Laura':{'sexo':'F','gafas':'no','barba':'no','pendientes':'no','color_pelo':'verde','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'no','tatuajes':'no'},
'Lewis':{'sexo':'M','gafas':'yes','barba':'yes','pendientes':'yes','color_pelo':'gris','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'no','tatuajes':'no'},
'Luis':{'sexo':'M','gafas':'no','barba':'yes','pendientes':'no','color_pelo':'rubio','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'yes','tatuajes':'yes'},
'Maricarmen':{'sexo':'F','gafas':'yes','barba':'no','pendientes':'yes','color_pelo':'azul','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'no','tatuajes':'no'},
'Joaquin':{'sexo':'M','gafas':'no','barba':'yes','pendientes':'yes','color_pelo':'marrón','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'yes','tatuajes':'yes'},
'Alejandra':{'sexo':'F','gafas':'yes','barba':'no','pendientes':'no','color_pelo':'negro','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'no','tatuajes':'no'},
'Joan':{'sexo':'M','gafas':'no','barba':'yes','pendientes':'yes','color_pelo':'lila','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'yes','tatuajes':'yes'}
}

dicci_pers_ia={
'Alejandro':{'sexo':'M','gafas':'yes','barba':'yes','pendientes':'no','color_pelo':'blanco','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'yes','tatuajes':'yes'},
'Sara':{'sexo':'F','gafas':'no','barba':'no','pendientes':'yes','color_pelo':'platino','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'no','tatuajes':'no'},
'Pedro':{'sexo':'M','gafas':'yes','barba':'yes','pendientes':'yes','color_pelo':'pelirrojo','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'yes','tatuajes':'yes'},
'Laura':{'sexo':'F','gafas':'no','barba':'no','pendientes':'no','color_pelo':'verde','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'no','tatuajes':'no'},
'Lewis':{'sexo':'M','gafas':'yes','barba':'yes','pendientes':'yes','color_pelo':'gris','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'no','tatuajes':'no'},
'Luis':{'sexo':'M','gafas':'no','barba':'yes','pendientes':'no','color_pelo':'rubio','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'yes','tatuajes':'yes'},
'Maricarmen':{'sexo':'F','gafas':'yes','barba':'no','pendientes':'yes','color_pelo':'azul','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'no','tatuajes':'no'},
'Joaquin':{'sexo':'M','gafas':'no','barba':'yes','pendientes':'yes','color_pelo':'marrón','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'yes','tatuajes':'yes'},
'Alejandra':{'sexo':'F','gafas':'yes','barba':'no','pendientes':'no','color_pelo':'negro','gorra':'yes','sombrero':'no','pelo_largo':'no','pelo_corto':'yes','bigote':'no','tatuajes':'no'},
'Joan':{'sexo':'M','gafas':'no','barba':'yes','pendientes':'yes','color_pelo':'lila','gorra':'no','sombrero':'yes','pelo_largo':'yes','pelo_corto':'no','bigote':'yes','tatuajes':'yes'}
}

def personaje_especial(test):  # seleccionamos el personaje especial de manera aleatoria.
    z = random.randint(0, 10)
    personaje_especial = lista_personajes[z]
    return (personaje_especial)


def opciones_pregunta(atributo, especial,who):  # Comprobamos si se cumple el atributo, y eliminamos los que cumplen con las caractaristicas.

    if who == 'P1':
        if dicci_pers_p1[especial][atributo] == "yes":
            print("Exacto, la persona cumple con esta caracteristica. ")
            for x in list(dicci_pers_p1.keys()):
                if dicci_pers_p1[x][atributo] == 'no' or dicci_pers_p1[x][atributo] == 'M' or dicci_pers_p1[x][atributo] == 'marrón':
                        print(dicci_pers_p1[x], "Ha sido eliminado ya que cumple con tu pregunta")
                        del dicci_pers_p1[x]
            print("El tablero actualizado es",dicci_pers_p1)
            return (dicci_pers_p1)
        elif dicci_pers_p1[especial][atributo] != "yes":
            print("La persona no cumple con esta caracteristica.")



    if who == 'IA':
        if dicci_pers_ia[especial][atributo] == "yes":
            print("Exacto, la persona cumple con esta caracteristica. ")
            for x in list(dicci_pers_ia.keys()):
                if dicci_pers_ia[x][atributo] == 'no' or dicci_pers_p1[x][atributo] == 'M' or dicci_pers_p1[x][atributo] == 'marrón':
                    print(dicci_pers_ia[x], "Ha sido eliminado ya que cumple con tu pregunta")
                    del dicci_pers_ia[x]
            print("El tablero actualizado es", dicci_pers_ia)
            return (dicci_pers_ia)
        elif dicci_pers_ia[especial][atributo] != "yes":
            print("La persona no cumple con esta caracteristica.")


acabar_juego()


