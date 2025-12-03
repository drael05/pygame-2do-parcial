import pygame
from funciones import *
from constantes import *

fondo_juego = pygame.image.load("imagenes\Fondo juego.jpg")
lista_botones_datos = crear_lista_botones("imagenes\Boton datos.png","imagenes\Boton datos.png","imagenes\Boton datos.png",5,10,3,True,195,200,70) 

evento_1_segundo = pygame.USEREVENT
pygame.time.set_timer(evento_1_segundo, 1000)




def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_preguntas) -> str:
    ventana = "jugar"
    
    

    preguntas_para_jugar = filtrar_preguntas_por_dificultad(datos_juego["dificultad"],lista_preguntas)
    pregunta_actual = obtener_pregunta_actual(datos_juego, preguntas_para_jugar)
    
    pantalla.blit(fondo_juego, (0,0))
    boton_pregunta = crear_elemento_juego("imagenes\Boton pregunta.jpg","imagenes\Boton pregunta.jpg",460,100,65,85)
    botones_respuestas = crear_lista_botones("imagenes\Boton menu Azul.jpg","imagenes\Boton menu Azul.jpg","imagenes\Textura seleccion.jpg",90,210,4,False,85,ancho_boton,alto_boton)
    
    evento_tiempo = pygame.USEREVENT + 1
    pygame.time.set_timer(evento_tiempo, 1000)


    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

            
            responder_pregunta_pygame(botones_respuestas,evento.pos,SONIDO_CLICK,datos_juego,botones_respuestas,pregunta_actual)
            pregunta_actual = obtener_pregunta_actual(datos_juego,preguntas_para_jugar)
            boton_pregunta = crear_elemento_juego("imagenes\Boton pregunta.jpg","imagenes\Boton pregunta.jpg",460,100,65,85)
            botones_respuestas = crear_lista_botones("imagenes\Boton menu Azul.jpg","imagenes\Boton menu Azul.jpg","imagenes\Textura seleccion.jpg",90,210,4,False,85,ancho_boton,alto_boton)
        elif evento.type == evento_1_segundo:
            datos_juego["tiempo_restante"] -= 1



        manejar_sombreado_botones(botones_respuestas,evento)

    textos_datos = [f"Tiempo: {datos_juego.get("tiempo_restante")} ",f"Puntos: {datos_juego.get("puntuacion")}",f"Vidas: {datos_juego.get("cantidad_vidas")}"]
    dibujar_botones(pantalla,fuente_jomantara_chica,blanco,lista_botones_datos,textos_datos)
    mostrar_pregunta_pygame(pregunta_actual,pantalla,boton_pregunta,botones_respuestas)
    ventana=terminar_juego(datos_juego)
    return ventana
