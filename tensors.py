import tensorflow as tf #linea para importar lib de tensorflow
#creando u tensor de unos
t1 = tf.ones([5,5,5,5]) #para saber cuantos elementos hay en el tensor se multiplican los elementos
#para visualizarlo mejor el número más de la izquierda es la cantidad de datos agrupados en el subset menor
t2 = tf.reshape(t,[125,-1]) 
# con el reshape se crean 125 grupos de los mismos elementos solos y todos los demás se anulan con el -1

#imprimir dos tensores
print(t1)
print(t2)
