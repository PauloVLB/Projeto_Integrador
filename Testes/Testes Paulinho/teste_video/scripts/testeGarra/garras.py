#!/usr/bin/env python
# -*- conding: utf-8 -*-

class Garras():
    def __init__(self):
        # braco

        self.ANG_INICIAL_BAIXAR_BRACO = 80
        self.ANG_FINAL_BAIXAR_BRACO = 10

        self.ANG_INICIAL_SUBIR_BRACO = 10
        self.ANG_FINAL_SUBIR_BRACO = 80

        # mao

        self.ANG_INICIAL_ABRIR_MAO = 90
        self.ANG_FINAL_ABRIR_MAO = 0

        self.ANG_INICIAL_FECHAR_MAO = 0
		self.ANG_FINAL_FECHAR_MAO = 90

    # braco
    def getAbaixarBraco():
        return self.ANG_INICIAL_BAIXAR_BRACO, self.ANG_FINAL_BAIXAR_BRACO
    def getSubirBraco():
        return self.ANG_INICIAL_SUBIR_BRACO, self.ANG_FINAL_SUBIR_BRACO

    # mao
    def getAbrirMao():
        return self.ANG_INICIAL_ABRIR_MAO, self.ANG_FINAL_ABRIR_MAO
    def getFecharMao():
        return self.ANG_INICIAL_FECHAR_MAO, self.ANG_FINAL_FECHAR_MAO
