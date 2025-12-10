import pygame
from constantes import *
from funciones import *
from menu import *
from ajustes import *
from juego import *
from dificultad import *
from terminado import *
from rankings import *
ventana_actual ="menu"

lista_preguntas = []
leer_csv_preguntas("archivos/preguntas.csv", lista_preguntas)

datos_juego = crear_datos_juego()

ventana_anterior = None
pygame.init()

pygame.display.set_caption("¿Preguntados?")
pantalla = pygame.display.set_mode(PANTALLA)

pygame.display.set_icon(pygame.image.load("imagenes/icono.png"))
reloj = pygame.time.Clock()


while True:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()


    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual = "salir"

    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla, cola_eventos)
    elif ventana_actual == "jugar":
        if datos_juego.get("dificultad", "") == "":
            nueva_dificultad = seleccionar_dificultad(pantalla, cola_eventos, datos_juego)
            if nueva_dificultad != "":
                datos_juego["dificultad"] = nueva_dificultad  
        else:
            ventana_actual = mostrar_juego(pantalla, cola_eventos, datos_juego, lista_preguntas)
    elif ventana_actual == "juego terminado":
        ventana_actual = mostrar_juego_terminado(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "salir":
        break
    if ventana_actual != ventana_anterior:
        cambiar_musica(diccionario_musica, datos_juego, ventana_actual)
        ventana_anterior = ventana_actual
    pygame.display.flip()

resetear_rankings()
pygame.quit()
