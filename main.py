import Multicapa as mc
#numero de entradas, ocultos y salidas de los nodos

def Main ():
    nodos_entrada = 7 #Columnas
    nodos_oculto = 100
    nodos_salida = 2 #Etiquetas

    #ratio de aprendizje
    ratio_aprendizaje = 0.0001

    r = mc.NN(nodos_entrada, nodos_oculto, nodos_salida, ratio_aprendizaje)

    #lectura de archivo de entrenamiento
    archivo_entreno = open("./enfermedades_covid19_train.csv",'r')
    lista_entreno = archivo_entreno.readlines()
    archivo_entreno.close()



    #Entrenamiento de la red
    for filas in lista_entreno:
        fila = filas.split(',')
        #entrada = (np.asfarray(fila[1:]) /255.0 * 0.99) +0.01
        entrada = mc.np.asfarray(fila[1:])
        objetivos = mc.np.zeros(nodos_salida) + 0.01
        objetivos[int(fila[0])] = 0.99
        r.train(entrada, objetivos)


def lectura(e):
    #Lectura del archivo de testeo
    archivo_prueba = open("./enfermedades_covid19_test.csv", 'r')
    lista_prueba = archivo_prueba.readlines()
    archivo_prueba.close()

    #Elegimos una fila del archivo de testo

    eleccion=e
    test = lista_prueba[int(eleccion)+1].split(',')
    print (test)
    return test




def resultado(test):
    #Consultamos a la red neuronal para que nos bote la respuesta
    #resultado = r.consulta((numpy.asfarray(fila[1:])/255.0 * 0.99)+0.01)
    resultado = mc.r.consulta(mc.np.asfarray(test[1:]))
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
    return i,resultado