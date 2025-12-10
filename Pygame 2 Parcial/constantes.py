import pygame

pygame.init()

separacion_y = 105

alto_boton =  75
ancho_boton = 300
blanco = (255,255,255)

fuente_jomantara_chica =pygame.font.Font("fuentes\Jomantara.ttf",42)
fuente_jomantara_mediana=pygame.font.Font("fuentes\Jomantara.ttf",52)
fuente_jomantara_grande=pygame.font.Font("fuentes\Jomantara.ttf",100)

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
ANCHO = 600
ALTO = 600
PANTALLA = (ANCHO,ALTO)
FPS = 30
tiempo_total =30

SONIDO_CLICK = pygame.mixer.Sound("sonido\sonido click.mp3")

dificultad = ""





diccionario_musica = {
    "Musica Menu": [
        "sonido\Musica menu 1.mp3",
        "sonido\Musica menu 2.mp3",
        "sonido\Musica menu 3.mp3"
    ],
    "Musica Juego": [
        "sonido\Musica Juego 1.mp3",
        "sonido\Musica Juego 2.mp3",
        "sonido\Musica Juego 3.mp3"
    ],
    "Musica Rankings": [
        "sonido\Musica Rankings.mp3"
    ],
    "Musica juego terminado": [
        "sonido\Musica Game over.wav"
    ],
    "Musica Ajustes": [
        "sonido\Musica Ajustes.mp3"
    ]
}



