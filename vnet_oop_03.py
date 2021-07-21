#!/usr/bin/python3

class ReceitaDeBolo:
    """ Classe base para receitas de bolo """
    def __init__(self, qtdeFarinha:float, qtdeLeite:float, qtdeOvos:int) -> None:
        """ Construtor da classe base """
        self.__qtdeFarinha:float    = qtdeFarinha   # atributo privado
        self.__qtdeLeite:float      = qtdeLeite     # atributo privado 
        self.__qtdeOvos:int         = qtdeOvos      # atributo privado

    """ Metodos publicos Get/Set do atributo qtdeFarinha """
    def getQtdeFarinha(self) -> float:
        return self.__qtdeFarinha

    def setQtdeFarinha(self, qtdeFarinha:float) -> None:
        self.__qtdeFarinha = qtdeFarinha

    """ Metodos publicos Get/Set do atributo qtdeLeite """
    def getQtdeFarinha(self) -> float:
        return self.__qtdeLeite

    def setQtdeFarinha(self, qtdeLeite:float) -> None:
        self.__qtdeLeite = qtdeLeite

    """ Metodos publicos Get/Set do atributo qtdeOvos """
    def getQtdeFarinha(self) -> int:
        return self.__qtdeOvos

    def setQtdeFarinha(self, qtdeOvos:int) -> None:
        self.__qtdeOvos = qtdeOvos