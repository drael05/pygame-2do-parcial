import pygame
from funciones import *
from constantes import *
pygame.init()


fondo_game_over = pygame.image.load("imagenes\Fondo Juego terminado.jpg")





def mostrar_juego_terminado(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    datos_juego["bandera_texto"] = not datos_juego["bandera_texto"]
    ventana = "terminado"
    
    boton_puntaje = crear_elemento_juego("imagenes/Boton menu Rojo.jpg","imagenes/Boton menu Rojo.jpg",300,80,150,370)
    boton_texto = crear_elemento_juego ("imagenes\Boton menu Azul.jpg","imagenes\Boton menu Azul.jpg",ancho_boton,alto_boton,150,250)
    for evento in cola_eventos:
            if evento.type == pygame.TEXTINPUT:
                datos_juego["nombre"] += evento.text
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    datos_juego["nombre"] = datos_juego["nombre"][0:-1]

    


    pantalla.blit(fondo_game_over,(0,0))

    if len(datos_juego.get("nombre","")) > 0:
        if datos_juego["bandera_texto"]:
            mostrar_texto(boton_texto["superficie"],f"{datos_juego.get("nombre","")}|",(10,10),fuente_jomantara_mediana,blanco)
        else:
            mostrar_texto(boton_texto["superficie"],f"{datos_juego.get("nombre","")}",(10,10),fuente_jomantara_mediana,blanco)
    else:
        mostrar_texto(boton_texto["superficie"],f"Ingrese su nombre",(10,10),fuente_jomantara_mediana,"#656565")
    
    pantalla.blit(boton_texto["superficie"],boton_texto["rectangulo"])
    dibujar_boton(pantalla,boton_puntaje,f"Puntaje: {datos_juego.get("puntuacion")}",fuente_jomantara_mediana,blanco)
    return ventana