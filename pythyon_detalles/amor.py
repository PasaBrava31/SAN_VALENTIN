import turtle
import time
import pygame
import random

from PIL import Image

# ---------------- MUSICA ----------------
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

# ---------------- PANTALLA ----------------
pantalla = turtle.Screen()
pantalla.setup(900, 700)
pantalla.bgcolor("#0b0c10")
pantalla.title("Para Ti Mi Amor ❤️")

# ---------------- CORAZON ----------------
corazon = turtle.Turtle()
corazon.hideturtle()
corazon.speed(0)
corazon.color("#ff4d6d")

def dibujar_corazon(tamano):
    corazon.penup()
    corazon.goto(0, -50)
    corazon.pendown()
    corazon.begin_fill()
    corazon.left(140)
    corazon.forward(tamano)
    corazon.circle(-tamano/2, 200)
    corazon.left(120)
    corazon.circle(-tamano/2, 200)
    corazon.forward(tamano)
    corazon.end_fill()
    corazon.setheading(0)

# animacion latido
for i in range(3):
    dibujar_corazon(160)
    time.sleep(0.3)
    corazon.clear()
    dibujar_corazon(180)
    time.sleep(0.3)
    corazon.clear()

dibujar_corazon(180)

# ---------------- FOTO ----------------
pantalla.addshape("vane.gif")

foto = turtle.Turtle()
foto.penup()
foto.goto(0, 100)
foto.shape("vane.gif")

# ---------------- TEXTO ANIMADO ----------------
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.color("white")

def escribir(texto_mensaje, y, size):
    texto.goto(0, y)
    mensaje = ""
    for letra in texto_mensaje:
        mensaje += letra
        texto.clear()
        texto.write(mensaje, align="center",
                   font=("Segoe UI", size, "bold"))
        time.sleep(0.06)

time.sleep(1)

escribir("Para la mujer más hermosa del mundo", -120, 22)
time.sleep(1)

escribir("Feliz San Valentín ❤️", -160, 28)
time.sleep(1)

escribir("Te amo con todo mi corazón", -200, 20)
time.sleep(1)

escribir("Con amor, Manuel", -240, 16)

# ---------------- EFECTOS ----------------
efecto = turtle.Turtle()
efecto.hideturtle()
efecto.color("#ffccd5")

for i in range(25):
    efecto.penup()
    efecto.goto(
random.randint(-400, 400),
random.randint(-300, 300)

    )
    efecto.write("✨", align="center", font=("Arial", 14, "normal"))
    time.sleep(0.05)

pantalla.mainloop()
