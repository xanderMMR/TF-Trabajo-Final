#import libraries
import numpy as np
import scipy.special
import matplotlib.pyplot
import random

#definición de la red neuronal
class NN:
  def __init__(self, nodos_entrada, nodos_escondidos, nodos_salida, ratio_aprendizaje):
    self.entranode = nodos_entrada
    self.escondinode = nodos_escondidos
    self.salinode = nodos_salida

    self.wih = np.random.normal(0.0, pow(self.escondinode, -0.5), (self.escondinode, self.entranode))
    self.who = np.random.normal(0.0, pow(self.salinode, -0.5), (self.salinode, self.escondinode))

    self.ra = ratio_aprendizaje

    self.funcion_activacion = lambda x:scipy.special.expit(x)

  def train(self, lista_entrada, lista_objetivo):
    entradas = np.array(lista_entrada, ndmin=2).T
    objetivos = np.array(lista_objetivo, ndmin=2).T

    entrada_escondida = np.dot(self.wih, entradas)
    salida_escondida = self.funcion_activacion(entrada_escondida)

    entrada_final = np.dot(self.who, salida_escondida)
    salida_final = self.funcion_activacion(entrada_final)

    error_salida = objetivos - salida_final
    error_escondido = np.dot(self.who.T, error_salida)
    self.who += self.ra*np.dot((error_salida * salida_final * (1.0 - salida_final)), np.transpose(salida_escondida))

    self.wih += self.ra*np.dot((error_escondido * salida_escondida * (1.0 - salida_escondida)), np.transpose(entradas))
  
  def consulta(self, lista_entradas):
    entradas = np.array(lista_entradas, ndmin=2).T
    entradas_ocultas = np.dot(self.wih, entradas)
    salidas_ocultas = self.funcion_activacion(entradas_ocultas)

    entradas_final = np.dot(self.who, salidas_ocultas)
    salidas_final = self.funcion_activacion(entradas_final)

    return salidas_final

#numero de entradas, ocultos y salidas de los nodos
nodos_entrada = 7 #Columnas
nodos_oculto = 100
nodos_salida = 2 #Etiquetas

#ratio de aprendizje
ratio_aprendizaje = 0.1

r = NN(nodos_entrada, nodos_oculto, nodos_salida, ratio_aprendizaje)

#lectura de archivo de entrenamiento
archivo_entreno = open("./enfermedades_covid19_train.csv",'r')
lista_entreno = archivo_entreno.readlines()
archivo_entreno.close()



#Entrenamiento de la red
for filas in lista_entreno:
  fila = filas.split(',')
  #entrada = (np.asfarray(fila[1:]) /255.0 * 0.99) +0.01
  entrada = np.asfarray(fila[1:])
  objetivos = np.zeros(nodos_salida) + 0.01
  objetivos[int(fila[0])] = 0.99
  r.train(entrada, objetivos)

  #Lectura del archivo de testeo
archivo_prueba = open("./enfermedades_covid19_test.csv", 'r')
lista_prueba = archivo_prueba.readlines()
archivo_prueba.close()

#Elegimos una fila del archivo de testo
test = lista_prueba[random.randint(0,40000)].split(',')
print(test[0])

#Consultamos a la red neuronal para que nos bote la respuesta
#resultado = r.consulta((numpy.asfarray(fila[1:])/255.0 * 0.99)+0.01)
resultado = r.consulta(np.asfarray(test[1:]))
print(resultado)

#Obtenemos la etiqueta
cont = 0
i = 0
mayor = 0
for j in resultado:
  if j > mayor:
    mayor = j
    i = cont
  cont += 1
print(i)