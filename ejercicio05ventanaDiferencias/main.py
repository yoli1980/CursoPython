

from tkinter import *
import time
from tkinter import messagebox

tini = time.time()
tini_global = time.time()
adivinada_1 = False
adivinada_2 = False
adivinada_3 = False
adivinada_4 = False
adivinada_5 = False

def click_raton(evento): 
    global tini, tini_global, adivinada_1, adivinada_2, adivinada_3, adivinada_4, adivinada_5  
    x = evento.x
    y = evento.y
    print("x: " + str(x))
    print("y: " + str(y))
    
#ver si ha hecho click en la diferencia
    if x >= 352 and x <= 397 and y >= 304 and y <= 404:
        print("ENCONTRASTE UNA DIFERENCIA")
        tfin = time.time()   
        tardado = tfin - tini 
        print("Tiempo tardado para esta diferencia: " + str(tardado))
        tini = time.time()
        adivinada_1 = True        
        
    elif  x >= 494 and x <= 542 and y >= 143 and y <= 183:
        print("ENCONTRASTE UNA DIFERENCIA")
        tfin = time.time()   
        tardado = tfin - tini 
        print("Tiempo tardado para esta diferencia: " + str(tardado))
        tini = time.time()
        adivinada_2 = True
        
    elif  x >= 465 and x <= 499 and y >= 358 and y <= 390:
        print("ENCONTRASTE UNA DIFERENCIA")
        tfin = time.time()   
        tardado = tfin - tini 
        print("Tiempo tardado para esta diferencia: " + str(tardado))
        tini = time.time()
        adivinada_3 = True
        
    elif  x >= 564 and x <= 581 and y >= 334 and y <= 349:
        print("ENCONTRASTE UNA DIFERENCIA")
        tfin = time.time()   
        tardado = tfin - tini 
        print("Tiempo tardado para esta diferencia: " + str(tardado))
        tini = time.time()
        adivinada_4 = True
        
    elif  x >= 503 and x <= 526 and y >= 240 and y <= 267:
        print("ENCONTRASTE UNA DIFERENCIA")
        tfin = time.time()   
        tardado = tfin - tini 
        print("Tiempo tardado para esta diferencia: " + str(tardado))
        tini = time.time()
        adivinada_5 = True        
    else:
        print("FALLASTE") 
    
    if adivinada_1 == True and adivinada_2 == True and adivinada_3 == True and adivinada_4 == True and adivinada_5 == True:
        print("FELICIDADES ADIVINASTE TODAS LAS DIFERENCIAS")
        
    tfin = time.time()
    tardado = tfin - tini_global
    print("HAS TARDADO EN TOTAL: " + str(tardado))
    
#end click_raton
   
ventana = Tk() #asi creo un objeto de la clase Tk que representa 
#una ventana

canvas = Canvas(ventana, width = 800, height = 600) 
#esto es un componente que permite mostrar imagenes
canvas.pack(expand = YES, fill = BOTH)
imagen = PhotoImage(file = "imagen.png")
#para añadir la imagen
canvas.create_image(0,0, image = imagen, anchor = NW) 
#asi pintamos la imagen en el canvas

ventana.geometry("650x530") #asi creo la ventana
ventana.title("ADIVINA LAS 5 DIFERENCIAS PINCHANDO EN LA IMAGEN DE LA DERECHA")
#asi pongo titulo a la ventana
ventana.bind("<Button 1>", click_raton) #para asociar un evento a la ventana

# tiempo_inicial = time.time()  tambien podria ir aqui
messagebox.showinfo(message="Comienza a jugar", title="Encuentra las 5 diferencias")
ventana.mainloop() #asi muestro la ventana



