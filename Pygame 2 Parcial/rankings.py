import pygame
from constantes import *
from funciones import *
pygame.init()

fondo_rankings= pygame.image.load("imagenes\Fondo Rankings.jpg")

def mostrar_rankings(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], datos_juego:dict) -> str:
    ventana = "rankings"
    pantalla.blit(fondo_rankings,(0,0))
    boton_volver = crear_elemento_juego("imagenes\Boton menu Rojo.jpg","imagenes\Textura seleccion.jpg",210,53,7,520)
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                ventana = "menu"
        manejar_sombreado_botones([boton_volver],evento)
    dibujar_boton(pantalla,boton_volver,"Volver",fuente_jomantara_chica,blanco)
    return ventana
