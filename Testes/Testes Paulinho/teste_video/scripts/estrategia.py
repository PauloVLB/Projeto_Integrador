#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy
import message_filters
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray
from teste_video.msg import SensoresDistanciaMsg, RefletanciaMsg, Posicao
import time

# publishers
pubMotores = rospy.Publisher('motores', Int32MultiArray, queue_size=10)
pubGarras = rospy.Publisher('garra', Int32MultiArray, queue_size=10)


def callbackEstrategia(refle, dist, posicao):

    rate = rospy.Rate(20)

    # setando
    maisEsq = refle.refletancia[0]
    esq = refle.refletancia[1]
    dir = refle.refletancia[2]
    maisDir = refle.refletancia[3]

    # datas
    dataMotores = Int32MultiArray()
    dataGarras = Int32MultiArray()

    if posicao.sala == 1: ''' sala 1 e 2 '''
        # seguir linha
        if(esq > 4 and dir > 4 ): # branco, branco
            dataMotores.data = [25, 25]
        elif (esq > 4 and dir < 4  ): # branco, preto
            dataMotores.data = [25, -25]
        elif (esq < 4 and dir > 4 ): # preto, branco
            dataMotores.data = [-25,25]
        elif (esq < 4 and dir < 4 ): # preto, preto
            dataMotores.data = [25, 25]


    elif posicao.sala == 2: ''' rampa '''
        # subir rampa
        if(esq > 4 and dir > 4): # branco, branco
            dataMotores.data = [25, 25] # ?
        elif (esq > 4 and dir < 4  ): # branco, preto
            dataMotores.data = [25, -25] # ?
        elif (esq < 4 and dir > 4 ): # preto, branco
            dataMotores.data = [-25,25] # ?
        elif (esq < 4 and dir < 4 ): # preto, preto
            dataMotores.data = [25, 25] # ?


    elif posicao.sala == 3: ''' sala 3 '''

        # girar para alinhar
        dataMotores.data = [25, -25]
        pubMotoresDelay(100)
        # encostar na parede
        dataMotores.data = [-25, -25]
        pubMotoresDelay(200)
        # ir para frente
        dataMotores.data = [25, 25]
        pubMotoresDelay(200)
        # encostar na parede
        dataMotores.data = [-25, -25]
        pubMotoresDelay(200)

        ''' TESTE GARRA '''
        time = Time()
        time.sleep(300)

        # if robolog.achouVitima():

        dataAngInicial = garras.getAbaixarInicial()
        dataAngFinal = garras.getAbaixarFinal()

        # [90, 80] to [10, 10]?

        pubGarras.publish(dataGarras)

    #pubMotores.publish(dataMotores)
    #pubGarras.publish(dataGarras)

def pubMotoresDelay(delay):
    time = Time()
    i = 0
    while not i < 2:
        pubMotores.publish(dataMotores)
        time.sleep(delay)
        i = i + 1

def pubGarraDelay(delay):
    time = Time()
    i = 0
    while not i < 2:
        pubGarras.publish(dataGarras)
        time.sleep(delay)
        i = i + 1


def estrategia():
    rospy.init_node('estrategia', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', RefletanciaMsg)
    subDistancia = message_filters.Subscriber('distancia', SensoresDistanciaMsg)
    subPosicao = message_filters.Subscriber('posicao', Posicao)

    ts = message_filters.TimeSynchronizer([subRefle, subDistancia, subPosicao], 10)
    ts.registerCallback(callbackEstrategia)

    rospy.spin()

if __name__ == "__main__":
	try:
	      estrategia()
	except rospy.ROSInterruptException:
		pass
