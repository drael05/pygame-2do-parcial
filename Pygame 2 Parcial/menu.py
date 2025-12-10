import pygame
from constantes import *
from funciones import *
pygame.init()
fondo_menu = pygame.image.load("imagenes\Fondo Menu.jpg")

lista_botones = crear_lista_botones("imagenes\Boton menu Azul.jpg","imagenes\Boton menu Rojo.jpg","imagenes\Textura seleccion.jpg",150,150,4,False,separacion_y,ancho_boton,alto_boton)
lista_texto_botones = ["JUGAR","AJUSTES","RANKINGS","SALIR"]

def mostrar_menu (pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    ventana = "menu"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    SONIDO_CLICK.play()
                    ventana = lista_texto_botones[i].lower()
        if evento.type == pygame.MOUSEMOTION:
            actualizar_textura_botones(lista_botones, evento.pos)
    pantalla.blit(fondo_menu,(0,0))
    dibujar_botones(pantalla,fuente_jomantara_mediana,blanco,lista_botones,lista_texto_botones)
    return ventana