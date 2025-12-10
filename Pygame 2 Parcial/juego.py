import pygame
from funciones import *
from constantes import *

evento_1_segundo = pygame.USEREVENT
pygame.time.set_timer(evento_1_segundo, 1000)

fondo_juego = pygame.image.load("imagenes/Fondo juego.jpg")

lista_botones_datos = crear_lista_botones("imagenes/Boton datos.png", "imagenes/Boton datos.png", "imagenes/Boton datos.png", 5, 10, 3, True, 195, 200, 70)

botones_comodines = crear_lista_botones("imagenes/Boton comodin.png", "imagenes/Boton comodin.png", "imagenes/Boton comodin selccionado.png", 410, 200, 4, False, 80, 150, 70)

textos_comodines = ["Bomba", "X2", "Doble", "Pasar"]


def mostrar_juego(pantalla, cola_eventos, datos_juego, lista_preguntas):

    ventana = "jugar"
    preguntas_para_jugar = filtrar_preguntas_por_dificultad(datos_juego["dificultad"], lista_preguntas)
    pregunta_actual = obtener_pregunta_actual(datos_juego, preguntas_para_jugar)

    pantalla.blit(fondo_juego, (0, 0))

    if datos_juego.get("botones_respuestas") == None:

        datos_juego["botones_respuestas"] = crear_lista_botones(
            "imagenes/Boton menu Azul.jpg", "imagenes/Boton menu Azul.jpg", "imagenes/Textura seleccion.jpg",
            90, 210, 4, False, 85, ancho_boton, alto_boton
        )

        botones_respuestas = datos_juego["botones_respuestas"]

        for boton in botones_respuestas:
            boton["oculto"] = False

        opciones = [
            pregunta_actual["opcion1"],
            pregunta_actual["opcion2"],
            pregunta_actual["opcion3"],
            pregunta_actual["opcion4"]
        ]

        for i in range(4):
            botones_respuestas[i]["texto"] = opciones[i]

    else:
        botones_respuestas = datos_juego["botones_respuestas"]

    boton_pregunta = crear_elemento_juego(
        "imagenes/Boton pregunta.jpg", "imagenes/Boton pregunta.jpg",
        460, 100, 65, 85
    )

    for evento in cola_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            responder_pregunta_pygame(botones_respuestas, evento.pos, SONIDO_CLICK, datos_juego, preguntas_para_jugar, pregunta_actual)

        elif evento.type == evento_1_segundo:
            datos_juego["tiempo_restante"] -= 1

        if botones_respuestas is not None:
            manejar_sombreado_botones(botones_respuestas, evento)

        manejar_sombreado_botones(botones_comodines, evento)

        manejar_click_comodines(evento, datos_juego, botones_comodines, botones_respuestas, preguntas_para_jugar)

    textos_datos = [
        f"Tiempo: {datos_juego['tiempo_restante']}",
        f"Puntos: {datos_juego['puntuacion']}",
        f"Vidas: {datos_juego['cantidad_vidas']}"
    ]

    dibujar_botones(pantalla, fuente_jomantara_chica, blanco, lista_botones_datos, textos_datos)

    mostrar_pregunta_pygame(pregunta_actual, pantalla, boton_pregunta, botones_respuestas)

    dibujar_botones(pantalla, fuente_jomantara_chica, blanco, botones_comodines, textos_comodines)

    ventana = terminar_juego(datos_juego)
    return ventana
