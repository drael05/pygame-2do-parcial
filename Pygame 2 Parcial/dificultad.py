import pygame
from funciones import *
from constantes import *

pygame.init()

lista_botones_dificultad = crear_lista_botones("imagenes\Boton menu Azul.jpg","imagenes\Boton menu Rojo.jpg","imagenes\Textura seleccion.jpg",150,150,4,False,90,ancho_boton,alto_boton)
lista_texto_botones_dificultad = ["FACIL","MEDIA","DIFICIL","PERSONALIZADA"]
fondo_dificultad = pygame.image.load("imagenes\Fondo Dificultad.jpg")

def administrar_botones_dificultad(lista_botones_dificultad:list, pos_mouse:tuple)->str:
    dificultad = ""
    for i in range(len(lista_botones_dificultad)):
        if lista_botones_dificultad[i]["rectangulo"].collidepoint(pos_mouse):
            SONIDO_CLICK.play()
            dificultad = lista_texto_botones_dificultad[i].lower()
    return dificultad


def seleccionar_dificultad(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], datos_juego:dict) -> str:
    dificultad = datos_juego.get("dificultad",0)
    pantalla.blit(fondo_dificultad, (0,0))
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            dificultad = administrar_botones_dificultad(lista_botones_dificultad,evento.pos)
        manejar_sombreado_botones(lista_botones_dificultad,evento)
    for i in range(len(lista_botones_dificultad)):
        dibujar_boton(pantalla,lista_botones_dificultad[i],lista_texto_botones_dificultad[i],fuente_jomantara_chica,blanco)

    return dificultad

