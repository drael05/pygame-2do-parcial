import pygame
from funciones import *
from constantes import *
pygame.init()

fondo_game_over = pygame.image.load("imagenes/Fondo Juego terminado.jpg")

EVENTO_CURSOR = pygame.USEREVENT + 5
pygame.time.set_timer(EVENTO_CURSOR, 500)




def mostrar_juego_terminado(pantalla: pygame.Surface, cola_eventos: list, datos_juego: dict) -> str:
    ventana = "juego terminado"

    boton_puntaje = crear_elemento_juego("imagenes/Boton menu Rojo.jpg","imagenes/Boton menu Rojo.jpg",300,80,150,375)
    boton_texto = crear_elemento_juego("imagenes/Boton menu Azul.jpg","imagenes/Boton menu Azul.jpg",ancho_boton,alto_boton,150,250)

    for evento in cola_eventos:

        if evento.type == pygame.TEXTINPUT:
            datos_juego["nombre"] += evento.text

        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_BACKSPACE:
                datos_juego["nombre"] = datos_juego["nombre"][:-1]

            elif evento.key == pygame.K_RETURN:
                if len(datos_juego["nombre"]) > 0:
                    guardar_puntaje_json(datos_juego["nombre"], datos_juego["puntuacion"])
                    return "rankings"  

        elif evento.type == EVENTO_CURSOR:
            datos_juego["bandera_texto"] = not datos_juego["bandera_texto"]

    pantalla.blit(fondo_game_over, (0,0))

    texto = datos_juego["nombre"]
    if texto == "":
        mostrar_texto(boton_texto["superficie"],"Ingrese su nombre",(10,10),fuente_jomantara_mediana,"#656565")
    else:
        if datos_juego["bandera_texto"]:
            texto += "|"
        mostrar_texto(boton_texto["superficie"],texto,(10,10),fuente_jomantara_mediana,blanco)

    pantalla.blit(boton_texto["superficie"], boton_texto["rectangulo"])

    dibujar_boton(pantalla,boton_puntaje,f"Puntaje: {datos_juego['puntuacion']}",fuente_jomantara_chica,blanco)
    return ventana


