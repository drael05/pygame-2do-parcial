import pygame
from constantes import *
from funciones import *
pygame.init()

fondo_ajustes = pygame.image.load("imagenes\Fondo Ajustes.jpg")
img_mute = pygame.image.load("imagenes/Mute .png")
img_mute = pygame.transform.scale(img_mute, (150, 150))

boton_suma = crear_elemento_juego("imagenes\Boton mas.png","imagenes\Boton mas seleccionado.png",100,100,475,200)
boton_resta = crear_elemento_juego("imagenes\Boton menos.png","imagenes\Boton menos seleccionado.png",100,100,25,200)
boton_volver = crear_elemento_juego("imagenes\Boton menu Rojo.jpg","imagenes\Textura seleccion.jpg",210,53,7,520)
lista_botones_sonido = crear_lista_botones("imagenes\Boton menu Azul.jpg","imagenes\Boton menu Rojo.jpg","imagenes\Textura seleccion.jpg",0,380,2,True,310,ancho_boton,alto_boton)
lista_texto_botones_sonido = ["Desmutear","Mutear"]

def administrar_botones(lista_botones:list,boton_suma:dict, boton_resta:dict, boton_volver:dict, datos_juego:dict, pos_mouse:tuple) -> str:
    ventana = "ajustes"
    vol_musica = datos_juego.get("volumen_musica", 0)
    
    if boton_suma["rectangulo"].collidepoint(pos_mouse):
        if vol_musica <= 95:
            datos_juego["volumen_musica"] += 5
            SONIDO_CLICK.play()

    elif boton_resta["rectangulo"].collidepoint(pos_mouse):
        if vol_musica > 0:
            datos_juego["volumen_musica"] -= 5
            SONIDO_CLICK.play()

    elif boton_volver["rectangulo"].collidepoint(pos_mouse):
        SONIDO_CLICK.play()
        ventana = "menu"


    
    for i in range(len(lista_botones)):
        if lista_botones[i]["rectangulo"].collidepoint(pos_mouse):
            SONIDO_CLICK.play()
            if lista_texto_botones_sonido[i]== "Mutear":
                datos_juego["volumen_musica"]= 0
            elif lista_texto_botones_sonido[i]== "Desmutear":
                if datos_juego["volumen_musica"]== 0:
                    datos_juego["volumen_musica"] += 50

    pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)
    return ventana


def dibujar_elementos_ajustes(pantalla:pygame.Surface, boton_suma:dict, boton_resta:dict, boton_volver:dict, datos_juego:dict) -> None:
    volumen = datos_juego["volumen_musica"]
    pantalla.blit(fondo_ajustes, (0,0))
    pantalla.blit(boton_suma["superficie"], boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"], boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])
    for i in range(len(lista_botones_sonido)):
        dibujar_boton(pantalla,lista_botones_sonido[i],lista_texto_botones_sonido[i],fuente_jomantara_mediana,blanco)
    if volumen == 0:
        pantalla.blit(img_mute,(220,190))
    else:
        mostrar_texto(pantalla, f"{volumen}%", (220,200), fuente_jomantara_grande, blanco)
    dibujar_boton(pantalla,boton_volver,"Volver",fuente_jomantara_mediana,blanco)


def mostrar_ajustes(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], datos_juego:dict) -> str:
    ventana = "ajustes"

    for evento in cola_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            ventana = administrar_botones(lista_botones_sonido,boton_suma, boton_resta, boton_volver, datos_juego, evento.pos)

        manejar_sombreado_botones([boton_resta, boton_suma, boton_volver], evento)
        for i in range(len(lista_botones_sonido)):
            dibujar_boton(pantalla,lista_botones_sonido[i],lista_texto_botones_sonido[i],fuente_jomantara_mediana,blanco)
            manejar_sombreado_botones(lista_botones_sonido,evento)

    dibujar_elementos_ajustes(pantalla, boton_suma, boton_resta, boton_volver, datos_juego)

    return ventana



































# import pygame
# from constantes import *
# from funciones import *
# pygame.init()

# fondo_ajustes = pygame.image.load("imagenes\Fondo Ajustes.jpg")

# boton_suma = crear_elemento_juego("imagenes\Boton mas.png","imagenes\Boton mas seleccionado.png",95,95,500,250)
# boton_resta = crear_elemento_juego("imagenes\Boton menos.png","imagenes\Boton menos seleccionado.png",95,95,100,250)
# boton_volver =crear_elemento_juego("imagenes\Boton menu Rojo.jpg","imagenes\Textura seleccion.jpg",180,45,0,555)

# def administrar_botones(boton_suma:dict,boton_resta:dict,boton_volver:dict,datos_juego:dict,pos_mouse:tuple) -> str:
#     ventana = "ajustes"
#     vol_musica = datos_juego.get("volumen_musica",0)
    
#     if boton_suma["rectangulo"].collidepoint(pos_mouse):
#         if vol_musica <= 95:
#             datos_juego["volumen_musica"] += 5
#             SONIDO_CLICK.play()
#     elif boton_resta["rectangulo"].collidepoint(pos_mouse):
#         if vol_musica > 0:
#             datos_juego["volumen_musica"] -= 5
#             SONIDO_CLICK.play()
#     elif boton_volver["rectangulo"].collidepoint(pos_mouse):
#         SONIDO_CLICK.play()
#         ventana = "menu"
        
#     return ventana

# def dibujar_elementos(pantalla:pygame.Surface,boton_suma:dict,boton_resta:dict,boton_volver:dict,datos_juego:dict) -> None:
#     pantalla.blitill(fondo_ajustes)
#     pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
#     pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
#     pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    
#     mostrar_texto(pantalla,f"{datos_juego.get("volumen_musica",0)} %",(200,200),fuente_jomantara_50,blanco)
#     mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),fuente_jomantara_50,blanco)


# def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
#     ventana = "ajustes"
    
#     for evento in cola_eventos:
#         if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
#             ventana = administrar_botones(boton_suma,boton_resta,boton_volver,datos_juego,evento.pos)
#         manejar_sombreado_botones([boton_resta,boton_suma,boton_volver],evento)


#     return ventana
    