from tkinter import *
import main
from main import Main, lectura, resultado
#COLORES
colorFondo1= '#EF9E4D'

#Configuración del root
anchoPantalla='800'
x='x'
altoPantalla='520'
root= Tk()
root.geometry(anchoPantalla+x+altoPantalla)
root.resizable(width=0,height=0)
root.config(bg=colorFondo1)

#Función btnStart

def empezar():
    Main()
    if btnStart.place_info()!={}:
        btnStart.place_forget()
        lblTitle.place_forget()
        lblPct.place_forget()
        lblTxt.place_forget()
        imgMulticapa.place_forget()
        lblOpcion.place(x=(int(anchoPantalla)/2)-111,y=50)
        entEntrada.place(x=(int(anchoPantalla)/2)-77,y=125)
        btnIniciar.place(x=(int(anchoPantalla)/2)-200,y=200)
        btnLimpiar.place(x=(int(anchoPantalla)/2)+50,y=200)

#Primera página
lblTitle= Label(root, text="Trabajo Final",bg=colorFondo1,font=("Impact",30))
lblTitle.place(x=(int(anchoPantalla)/2)-120,y=50)
btnStart=Button(root,text="Comenzar",font=("Verdana",18),command=empezar)
btnStart.place(x=(int(anchoPantalla)/2)-80,y=150)
lblPct= Label(root, text="Perceptrón Multicapa",bg=colorFondo1,font=("Arial",22))
lblPct.place(x=(int(anchoPantalla)/2)-150,y=230)
lblTxt= Label(root, text="Determinar esperanza de vida de personas con Covid-19",bg=colorFondo1,font=("Arial",15))
lblTxt.place(x=(int(anchoPantalla)/2)-260,y=290)
img=PhotoImage(file="imgMulticapa.png")
imgMulticapa=Label(root, image=img,bd=0)
imgMulticapa.place(x=(int(anchoPantalla)/2)-145,y=330)


#Entrada
entrada=IntVar()
entEntrada=Entry(root,justify=CENTER,textvariable=entrada,width=10,font=("Verdana",15))



def callR ():
    lista= lectura(entEntrada.get())
    p= int(lista[0])
  
    print ("p",p)
    X=100
    Y=300
    X1=475
    Y1=300
    if p==0:
        imgMuerte1.place(x=X,y=Y)
        print ("muer")
    else:
        print ("vive")
        imgVive1.place(x=X,y=Y)

    l=resultado(lista)[0]
    
    
    print("l",l)
    if l==0:
        print("muere")
        imgMuerte2.place(x=X1,y=Y1)
    else:
        print("vive")
        imgVive2.place(x=X1,y=Y1)


def limpiar():
    
    imgMuerte1.place_forget()
    imgVive1.place_forget()
    imgVive2.place_forget()
    imgMuerte2.place_forget()

#Segunda página
lblOpcion= Label (root, text="Elija una fila",bg=colorFondo1,font=("Verdana",24))
btnIniciar= Button(root,text="Iniciar", font=("Verdana",24),command=callR)
btnLimpiar= Button(root,text="Limpiar",font=("Verdana",24),command=limpiar)
imgM=PhotoImage(file="m.png")
imgMuerte1= Label(root, image=imgM,bd=0)
imgMuerte2= Label(root, image=imgM,bd=0)
imgV=PhotoImage(file="vive.png")
imgVive1= Label(root, image=imgV,bd=0)
imgVive2= Label(root, image=imgV,bd=0)

        #gif=PhotoImage(file="covid.gif")
        #gifCovid=Label(root, image=gif,bd=0)


root.mainloop()