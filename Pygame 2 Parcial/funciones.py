import pygame
import random
from constantes import *
import os
import json
pygame.init()

def crear_datos_juego() -> dict:
    datos_juego = {
        "nombre": "",
        "tiempo_restante": tiempo_total,
        "puntuacion": 0,
        "cantidad_vidas": CANTIDAD_VIDAS,
        "indice": 0,
        "volumen_musica": 50,
        "bandera_texto": False,
        "dificultad": dificultad,
        "racha_correcta": 0,

        "comodines": {
            "bomba": False,
            "x2": False,
            "doble": False,
            "pasar": False
        },
        "comodin_usado": {
            "bomba": False,
            "x2": False,
            "doble": False,
            "pasar": False
        },

        "doble_activo": False,
        "doble_primer_intento": True,


        "pregunta_actual": None,

        "botones_respuestas": None
    }

    return datos_juego


def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def crear_elemento_juego(textura_normal: str, textura_hover: str, ancho: int, alto: int, x: int, y: int, texto="") -> dict:
    boton = {}

    img_normal = pygame.image.load(textura_normal)
    img_hover  = pygame.image.load(textura_hover)

    img_normal = pygame.transform.scale(img_normal, (ancho, alto))
    img_hover  = pygame.transform.scale(img_hover, (ancho, alto))

    rect = img_normal.get_rect(topleft=(x, y))

    boton["normal"] = img_normal
    boton["hover"] = img_hover
    boton["superficie"] = img_normal
    boton["rectangulo"] = rect
    boton["texto"] = texto
    boton["oculto"] = False

    return boton

def crear_elemento_juego(textura_normal: str, textura_hover: str, ancho: int, alto: int, x: int, y: int, texto="") -> dict:
    boton = {}

    img_normal = pygame.image.load(textura_normal)
    img_hover  = pygame.image.load(textura_hover)

    img_normal = pygame.transform.scale(img_normal, (ancho, alto))
    img_hover  = pygame.transform.scale(img_hover, (ancho, alto))

    rect = img_normal.get_rect(topleft=(x, y))

    boton["normal"] = img_normal
    boton["hover"] = img_hover
    boton["superficie"] = img_normal
    boton["rectangulo"] = rect
    boton["texto"] = texto
    boton["oculto"] = False

    return boton

def crear_lista_botones(textura_1, textura_2, textura_hover,
                        x, y, cantidad, costado, separacion,
                        ancho, alto):
    lista = []

    for i in range(cantidad):

        if i == cantidad - 1:
            textura_normal = textura_2
        else:
            textura_normal = textura_1

        boton = crear_elemento_juego(
            textura_normal,
            textura_hover,
            ancho, alto, x, y
        )
        lista.append(boton)

        if costado:
            x += separacion
        else:
            y += separacion

    return lista


def dibujar_boton(pantalla, boton, texto, fuente, color):
    if boton["oculto"]:
        return
    pantalla.blit(boton["superficie"], boton["rectangulo"])

    txt_surface = fuente.render(texto, True, color)
    rect_txt = txt_surface.get_rect(center=boton["rectangulo"].center)
    pantalla.blit(txt_surface, rect_txt)


def actualizar_textura_botones(lista_botones, mouse_pos):
    for boton in lista_botones:
        if boton["oculto"]:
            continue
        if boton["rectangulo"].collidepoint(mouse_pos):
            boton["superficie"] = boton["hover"]
        else:
            boton["superficie"] = boton["normal"]



def manejar_sombreado_botones(lista_botones: list[dict],evento: pygame.event.Event) -> None:
    if evento.type == pygame.MOUSEMOTION:
        actualizar_textura_botones(lista_botones, evento.pos)


def cambiar_musica(diccionario_musica:dict, datos_juego:dict, ventana_actual:str) -> None:

    match ventana_actual:

        case "menu":
            lista_rutas = diccionario_musica.get("Musica Menu", [])
            ruta = random.choice(lista_rutas)
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(datos_juego.get("volumen_musica", 0))
            pygame.mixer.music.play(-3)

        case "jugar":
            lista_rutas = diccionario_musica.get("Musica Juego", [])
            ruta = random.choice(lista_rutas)
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(datos_juego.get("volumen_musica", 0))
            pygame.mixer.music.play(-3)

        case "rankings":
            ruta = random.choice(diccionario_musica.get("Musica Rankings", 0))
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(datos_juego.get("volumen_musica", 0))
            pygame.mixer.music.play(-3)

        case "juego terminado":
                pygame.mixer.music.load("sonido\Musica Game over.wav")
                pygame.mixer.music.set_volume(datos_juego.get("volumen_musica", 0))
                pygame.mixer.music.play(0)

        case "ajustes":

            pygame.mixer.music.load("sonido\Musica Ajustes.mp3")
            pygame.mixer.music.set_volume(datos_juego.get("volumen_musica", 0))
            pygame.mixer.music.play(-1)


def dibujar_botones(pantalla, fuente, color, lista_botones, lista_textos):
    for i, boton in enumerate(lista_botones):
        dibujar_boton(pantalla, boton, lista_textos[i], fuente, color)

def obtener_pregunta_actual(datos_juego, lista_preguntas):
    idx = datos_juego["indice"]
    pregunta = lista_preguntas[idx]
    datos_juego["pregunta_actual"] = pregunta
    return pregunta

def modificar_vida(datos_juego:dict,incremento:int) -> bool:
    if type(datos_juego) == dict and datos_juego.get("cantidad_vidas") != None:
        retorno = True
        datos_juego["cantidad_vidas"] += incremento
    else:
        retorno = False
        
    return retorno

def modificar_puntuacion(datos_juego:dict,incremento:int) -> bool:
    if type(datos_juego) == dict and datos_juego.get("puntuacion") != None:
        retorno = True
        datos_juego["puntuacion"] += incremento
    else:
        retorno = False
        
    return retorno



def reemplazar_caracteres(cadena:str, caracter_viejo:str, caracter_nuevo:str) -> str:
    cadena_nueva = ""
    
    for i in range(len(cadena)):
        if cadena[i] == caracter_viejo:
            cadena_nueva += caracter_nuevo
        else:
            cadena_nueva += cadena[i]
    return cadena_nueva

def separar_cadena(cadena:str, separador:str) -> list:
    lista_separada = []
    cadena_nueva = ""
    
    if type(cadena) == str and (type(separador) == str and len(separador) == 1):

        for i in range(len(cadena)):
            if cadena[i] == separador:
                lista_separada.append(cadena_nueva)
                cadena_nueva = ""
            else:
                cadena_nueva += cadena[i]

        lista_separada.append(cadena_nueva)

    return lista_separada

def crear_diccionario_preguntas(lista_valores:list) -> dict :

    diccionario_pregunta = {}
    diccionario_pregunta["pregunta"] = lista_valores[0]
    diccionario_pregunta["dificultad"] = lista_valores[1]
    diccionario_pregunta["opcion1"] = lista_valores[2]
    diccionario_pregunta["opcion2"] = lista_valores[3]
    diccionario_pregunta["opcion3"] = lista_valores[4]
    diccionario_pregunta["opcion4"] = lista_valores[5]
    diccionario_pregunta["respuesta_correcta"] = lista_valores[6]

    return diccionario_pregunta

def leer_csv_preguntas(nombre_archivo:str, lista_preguntas:list) -> bool:

    if os.path.exists(nombre_archivo) and type(lista_preguntas) == list:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            archivo.readline() 

            for linea in archivo:
                linea = reemplazar_caracteres(linea, "\n", "")
                lista_valores = separar_cadena(linea, ",")

                diccionario_pregunta = crear_diccionario_preguntas(lista_valores)

                lista_preguntas.append(diccionario_pregunta)

        retorno = True
    retorno= False
    return retorno



def filtrar_preguntas_por_dificultad(dificultad_elegida: str, lista_preguntas: list) -> list:

    if dificultad_elegida == "personalizada":
        return lista_preguntas.copy()

    preguntas_filtradas = []

    for pregunta in lista_preguntas:
        if pregunta["dificultad"] == dificultad_elegida:
            preguntas_filtradas.append(pregunta)

    return preguntas_filtradas



def terminar_juego(datos_juego:dict)-> str:
    if datos_juego.get("cantidad_vidas") == 0 or datos_juego.get("tiempo_restante") == 0:
        ventana = "juego terminado"
    else:
        ventana = "jugar"
    return ventana

def modificar_tiempo(datos_juego:dict,incremento:int):
    if type(datos_juego) == dict and datos_juego.get("tiempo_restante") != None:
        retorno = True
        datos_juego["tiempo_restante"] += incremento
    else:
        retorno = False
        
    return retorno

def bonificar_racha(datos_juego:dict)-> None :
    if datos_juego["racha_correcta"] == 5:
        modificar_vida(datos_juego,1)
        modificar_tiempo(datos_juego,10)
def verificar_respuesta(pregunta_actual: dict, datos_juego: dict, respuesta) -> int:

    if type(pregunta_actual) != dict or pregunta_actual.get("respuesta_correcta") is None:
        return False

    correcta = pregunta_actual["respuesta_correcta"]

    if respuesta == correcta:

        datos_juego["racha_correcta"] += 1

        puntaje = 100

        if datos_juego["comodines"]["x2"] == True:
            puntaje *= 2
            datos_juego["comodines"]["x2"] = False

        modificar_puntuacion(datos_juego, puntaje)

        datos_juego["doble_activo"] = False
        datos_juego["doble_primer_intento"] = True

        bonificar_racha(datos_juego)
        return True

    if datos_juego["doble_activo"] == True:

        if datos_juego["doble_primer_intento"]== True:
            datos_juego["doble_primer_intento"] = False
            return True    
        else:
            datos_juego["doble_activo"] = False
            datos_juego["doble_primer_intento"] = True
            datos_juego["comodines"]["doble"] = False

    datos_juego["racha_correcta"] = 0
    modificar_puntuacion(datos_juego, -25)
    modificar_vida(datos_juego, -1)

    return True

def pasar_pregunta(datos_juego, lista):
    datos_juego["indice"] += 1
    if datos_juego["indice"] >= len(lista):
        datos_juego["indice"] = 0
        mezclar_lista(lista)



def verificar_indice(datos_juego:dict,lista_preguntas:list) -> None:
    if datos_juego["indice"] == len(lista_preguntas):
        datos_juego["indice"] = 0
        mezclar_lista(lista_preguntas)


def mezclar_lista(lista_preguntas: list) -> bool:
    if type(lista_preguntas) == list and len(lista_preguntas) > 0:
        random.shuffle(lista_preguntas)
        return True
    return False

def reiniciar_estadisticas(datos_juego: dict) -> bool:
    if type(datos_juego) != dict:
        return False

    datos_juego["tiempo_restante"] = tiempo_total
    datos_juego["puntuacion"] = 0
    datos_juego["cantidad_vidas"] = CANTIDAD_VIDAS
    datos_juego["indice"] = 0
    datos_juego["racha_correcta"] = 0


    datos_juego["botones_respuestas"] = None

    datos_juego["pregunta_actual"] = None


    datos_juego["comodin_usado"] = {
        "bomba": False,
        "x2": False,
        "doble": False,
        "pasar": False
    }


    datos_juego["comodines"] = {
        "bomba": False,
        "x2": False,
        "doble": False,
        "pasar": False
    }

    datos_juego["doble_activo"] = False
    datos_juego["doble_primer_intento"] = True

    return True

def responder_pregunta_pygame(lista_respuestas, pos_click, sonido, datos_juego, lista_preguntas, pregunta_actual):

    if lista_respuestas is None:
        return False

    for i in range(len(lista_respuestas)):

        boton = lista_respuestas[i]

        if boton.get("oculto", False) == False:

            if boton["rectangulo"].collidepoint(pos_click):

                sonido.play()
                respuesta_texto = boton.get("texto", None)

                doble_antes = datos_juego["doble_activo"]
                primer_intento = datos_juego["doble_primer_intento"]

                verificar_respuesta(pregunta_actual, datos_juego, respuesta_texto)

                pasar = True
                if doble_antes and primer_intento:
                    pasar = False

                if pasar == True:
                    pasar_pregunta(datos_juego, lista_preguntas)
                    datos_juego["botones_respuestas"] = None

                return True

    return False


def mostrar_pregunta_pygame(pregunta_actual, pantalla, cuadro_pregunta, botones_respuestas):

    if type(pregunta_actual) != dict:
        return False

    if botones_respuestas is None:
        return True


    cuadro_pregunta["superficie"] = cuadro_pregunta["normal"].copy()

    mostrar_texto(
        cuadro_pregunta["superficie"],
        pregunta_actual.get("pregunta"),
        (15, 15),
        fuente_jomantara_chica,
        blanco
    )

    pantalla.blit(cuadro_pregunta["superficie"], cuadro_pregunta["rectangulo"])

    opciones = [
        pregunta_actual.get("opcion1"),
        pregunta_actual.get("opcion2"),
        pregunta_actual.get("opcion3"),
        pregunta_actual.get("opcion4")
    ]

    for i in range(len(botones_respuestas)):

        boton = botones_respuestas[i]

        if boton.get("oculto", False) == False:

            boton["superficie"] = boton["normal"].copy()

            mostrar_texto(
                boton["superficie"],
                opciones[i],
                (15, 15),
                fuente_jomantara_mediana,
                blanco
            )

            pantalla.blit(boton["superficie"], boton["rectangulo"])

    return True



def comodin_bomba(datos_juego, botones_respuestas, pregunta):

    if datos_juego["comodin_usado"]["bomba"]:
        return

    datos_juego["comodin_usado"]["bomba"] = True
    datos_juego["comodines"]["bomba"] = True

    correcta = pregunta["respuesta_correcta"]
    eliminadas = 0

    for boton in botones_respuestas:
        if boton["texto"] != correcta and eliminadas < 2 and not boton["oculto"]:
            boton["oculto"] = True
            eliminadas += 1



def comodin_x2(datos_juego):
    if datos_juego["comodin_usado"]["x2"]:
        return

    datos_juego["comodin_usado"]["x2"] = True
    datos_juego["comodines"]["x2"] = True

def comodin_doble(datos_juego):
    if datos_juego["comodin_usado"]["doble"]:
        return

    datos_juego["comodin_usado"]["doble"] = True
    datos_juego["comodines"]["doble"] = True

    datos_juego["doble_activo"] = True
    datos_juego["doble_primer_intento"] = True


def comodin_pasar(datos_juego, preguntas):
    if datos_juego["comodin_usado"]["pasar"]:
        return False

    datos_juego["comodin_usado"]["pasar"] = True
    pasar_pregunta(datos_juego, preguntas)
    return True



def manejar_click_comodines(evento, datos_juego, botones_comodines, botones_respuestas, preguntas):
    if evento.type != pygame.MOUSEBUTTONDOWN or evento.button != 1:
        return

    for i, boton in enumerate(botones_comodines):
        if boton["rectangulo"].collidepoint(evento.pos):

            if i == 0:
                comodin_bomba(datos_juego, botones_respuestas, datos_juego["pregunta_actual"])


            elif i == 1:
                comodin_x2(datos_juego)

            elif i == 2:
                comodin_doble(datos_juego)


            elif i == 3:
                comodin_pasar(datos_juego, preguntas)

            return


def leer_json(nombre_archivo: str) -> any:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            retorno = json.load(archivo)
        del archivo
    else:
        retorno = False
    return retorno




def guardar_puntaje_json(nombre, puntaje):
    archivo = "rankings.json"

    lista = leer_json(archivo)
    if lista == False:
        lista = []

    lista.append({"nombre": nombre, "puntuacion": puntaje})

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def resetear_rankings():
    nombre_archivo = "rankings.json"

    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump([], archivo, ensure_ascii=False, indent=4)


def mostrar_lista_textos(pantalla, lista_textos, x, y_inicial, salto, fuente, color):
    y = y_inicial

    for texto in lista_textos:
        mostrar_texto(pantalla, texto, (x, y), fuente, color)
        y += salto


def bubble_sort(arreglo: list) -> list:

    for i in range( len(arreglo) - 1):               
        for j in range( len(arreglo) - 1 - i):
            puntaje_actual = arreglo[j]["puntaje"]
            puntaje_siguiente = arreglo[j + 1]["puntaje"]
            if puntaje_actual < puntaje_siguiente:
                temp = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = temp

    return arreglo

def generar_textos_rankings(lista_rankings:list):


    textos = []                        
    len_lista_rankings = len(lista_rankings)
    if len_lista_rankings > 10:
        len_lista_rankings = 10


    for i in range(len_lista_rankings):

        entrada = lista_rankings[i]        
        nombre = entrada["nombre"]         
        puntaje = entrada["puntaje"]       

        texto_linea = f"{i + 1}. {nombre} - {puntaje} pts"

        textos.append(texto_linea)        

    return textos
