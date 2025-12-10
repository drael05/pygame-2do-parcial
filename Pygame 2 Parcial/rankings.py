import pygame
from constantes import *
from funciones import *
pygame.init()

fondo_rankings = pygame.image.load("imagenes/Fondo Rankings.jpg")

def mostrar_rankings(pantalla: pygame.Surface, cola_eventos: list, datos_juego: dict) -> str:
    ventana = "rankings"
    pantalla.blit(fondo_rankings, (0, 0))

    boton_volver = crear_elemento_juego(
        "imagenes/Boton menu Rojo.jpg",
        "imagenes/Textura seleccion.jpg",
        210, 53, 7, 520
    )


    lista_rankings = leer_json("rankings.json")
    if lista_rankings is False:
        lista_rankings = []

    for entrada in lista_rankings:
        if "puntaje" not in entrada and "puntuacion" in entrada:
            entrada["puntaje"] = entrada["puntuacion"]

    bubble_sort(lista_rankings)

    textos_rankings = generar_textos_rankings (lista_rankings)

    mostrar_lista_textos(
        pantalla,
        textos_rankings,
        x=80,
        y_inicial=130,
        salto=35,
        fuente=fuente_jomantara_chica,
        color=blanco
    )

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                ventana = "menu"

        manejar_sombreado_botones([boton_volver], evento)

    dibujar_boton(pantalla, boton_volver, "Volver", fuente_jomantara_chica, blanco)
    reiniciar_estadisticas(datos_juego)
    return ventana
