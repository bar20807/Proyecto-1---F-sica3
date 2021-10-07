"""
    Proyecto #1 - Física 3
    Integrantes:
    Roberto Vallecillos
    Rodrigo Barrera
    Simulación de un tubo de rayos catódicos
    30/09/2021

"""

from tkinter import *
import tkinter
import math as mt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Función que se encarga de realizar cada uno de los cálculos, recibiendo como parametro dos cantidades de voltaje para las placas verticales.
def Calc_of_Variables(Vx,Vy,Va,I):
    #Valores estáticos que no serán tocados por el usuario
    h = 0.20
    l = 0.02
    C = -1.60e-19
    me = 9.11e-31
    Dx = 0.02
    D = 0.05    
    #Velocidad de la particula
    vx = mt.sqrt(abs((2*Va*C)/(me))) #Velocidad en x

    distancia = []
    # Calculos para la primera placa
    t=(Dx)/vx #Tiempo
    a_y=((C*Vy)/(me*D))#Aceleración en Y
    D_y = (a_y/2)*(t)**2 #Delta Y
    ang_max1=mt.degrees(mt.atan(D_y/(h*2)))#Ángulo
    arriba = []
    for i in range(21):
        j = i/1000
        distancia.append(i/1000)
        t1 = j/vx
        arriba.append((a_y/2)*(t1)**2)

    # Calculos para la primera placa
    t=(Dx)/vx #Tiempo
    a_y=((C*Vx)/(me*D))#Aceleración en Y
    ang_max2=mt.degrees(mt.atan(D_y/(h*2)))#Ángulo

    lado = []
    for i in range(21):
        j = i/1000
        t1 = j/vx
        lado.append((a_y/2)*(t1)**2)
        
    #Lados de nuestra placa
    L1=0.02 * (mt.degrees(mt.atan(ang_max1)))
    L2=0.02 * (mt.degrees(mt.atan(ang_max2)))
        
        

    fig, ax = plt.subplots()
    if(I == 1):
        x = L1
        y = L2
        plt.subplot(2,2,1)
        plt.plot(distancia, arriba, "r")
        plt.xlim([-0.0,0.02])
        plt.subplot(2,2,2)
        plt.plot(L1,L2,"ro")
        plt.xlim([-0.1,0.1])
        plt.ylim([-0.1,0.1])
        plt.subplot(2,2,3)
        plt.plot(distancia, lado, "r")
        plt.xlim([-0.0,0.02])
    else:
        data_skip = 1
        T = np.linspace(-10, 10, 900, endpoint = False)
        x = []
        y = []
        for i in T:
            x_i = np.sin(i)*.10
            y_i = np.sin(2*i+mt.pi/4)*.10
            x.append(x_i)
            y.append(y_i)

        def init():
            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)


        def update(i):
            if(i < len(x)+1):
                ax.plot(x[i:i+data_skip],y[i:i+data_skip],color = 'k')
                ax.scatter(x[i],y[i],color='r')
                plt.xlim(x[0],x[-1])
                if(y[-1] > 0):
                    plt.ylim(y[0],y[-1])
                else:
                    plt.ylim(y[-1],y[0])
                ax.set_xlim(-.11, .11)
                ax.set_ylim(-.11, .11)
        ani = FuncAnimation(fig, update, frames=10000, init_func=init)
    plt.show()


Ventana= Tk()
Ventana.geometry("700x300")
Ventana.title("Proyecto #1 - Física 3")

#Creando las etiquetas
etiqueta=Label(Ventana,text=("Tubo de rayos catódicos"),background="Yellow")
etiqueta.pack(fill=tkinter.X)
etiqueta=Label(Ventana,text=("ESTÁTICO"),background="Red",foreground="White")
etiqueta.pack(side=LEFT,fill=tkinter.Y)
etiqueta_1=Label(Ventana,text=("DINÁMICO"),background="Red",foreground="White")
etiqueta_1.pack(side=RIGHT,fill=tkinter.Y)

#Creando titulos de A,B y Delta
A_Titulo=Label(Ventana,text=("A"))
A_Titulo.place(x=500,y=50)
B_Titulo=Label(Ventana,text=("B"))
B_Titulo.place(x=500,y=100)
Delta_Titulo=Label(Ventana,text=("Delta"))
Delta_Titulo.place(x=490,y=150)

#Creando los Scale
sclBarra=Scale(Ventana, label="Voltaje horizontal",orient=HORIZONTAL,length=140,from_=-5,to=5)
sclBarra.place(x=80,y=100)
sclBarra_1=Scale(Ventana,label="Voltaje vertical",orient=HORIZONTAL,length=140,from_=-5,to=5)
sclBarra_1.place(x=80,y=30)
sclBarra_2=Scale(Ventana, label="Voltaje de aceleración",orient=HORIZONTAL,length=140,from_=5,to=100)
sclBarra_2.place(x=80,y=170)


#Funciones de acción al momento de dar click
def static_click():
    a = sclBarra.get()
    b = sclBarra_1.get()
    c = sclBarra_2.get()
    d=1
#Parámetro global
    global param
    param = [int(a),int(b),int(c),d]
    Calc_of_Variables(param[0],param[1],param[2],param[3])
    Ventana.destroy()
def dinamic_click():
    a = int(A_entrada.get())
    b = int(B_entrada.get())
    d=2
    if (Delta_entrada.get() == 0):
        c = int(Delta_entrada.get())
    else:
        c = mt.pi/int(Delta_entrada.get())
        global params
        params = [a,b,c,d]
    Calc_of_Variables(params[0],params[1],params[2],params[3])
    Ventana.destroy()

#Creando los txt_box para dinámicas
A_entrada=Entry(Ventana)
A_entrada.place(x=450,y=70)
B_entrada=Entry(Ventana)
B_entrada.place(x=450,y=120)
Delta_entrada=Entry(Ventana)
Delta_entrada.place(x=450,y=170)

#Creando los botones
btn_Estatico=Button(Ventana,text=("Generar gráfica estática"),command=static_click) #Aún falta agregarle acciones
btn_Estatico.place(x=90,y=250)
btn_Dinámico=Button(Ventana,text=("Genera gráfica dinámica"),command=dinamic_click) #Aún falta agregarle acciones
btn_Dinámico.place(x=440,y=200)


Ventana.resizable()
Ventana.mainloop()
