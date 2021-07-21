#!/usr/bin/python3

class ReceitaDeBolo:
    """ Classe base para receitas de bolo """
    def __init__(self, qtdeFarinha:float, qtdeLeite:float, qtdeOvos:int, pesoUnidOvo:float=50, tBaterOvos:int=30, tBaterMassa:int=30) -> None:
        """ Construtor da classe base """
        self.__qtdeFarinha:float    = qtdeFarinha   # atributo privado; quantidade de farinha; gramas
        self.__qtdeLeite:float      = qtdeLeite     # atributo privado; quantidade de leite; litros
        self.__qtdeOvos:int         = qtdeOvos      # atributo privado; quantidade de ovos; unidades
        self.__pesoUnidOvo:float    = pesoUnidOvo   # atributo privado; peso unitario dos ovos
        self.__tBaterOvos:int       = tBaterOvos    # atributo privado; tempo para bater os ovos; segundos
        self.__tBaterMassa:int      = tBaterMassa   # atributo privado; tempo para bater a massa; segundos

    """ Metodos publicos Get/Set do atributo quantidade de farinha (g) da receita """
    def getQtdeFarinha(self) -> float:
        return self.__qtdeFarinha

    def setQtdeFarinha(self, qtdeFarinha:float) -> None:
        self.__qtdeFarinha = qtdeFarinha

    """ Metodos publicos Get/Set do atributo quantidade de leite (L) da receita """
    def getQtdeLeite(self) -> float:
        return self.__qtdeLeite

    def setQtdeLeite(self, qtdeLeite:float) -> None:
        self.__qtdeLeite = qtdeLeite

    """ Metodos publicos Get/Set do atributo quantidade de ovos da receita """
    def getQtdeOvos(self) -> int:
        return self.__qtdeOvos

    def setQtdeOvos(self, qtdeOvos:int) -> None:
        self.__qtdeOvos = qtdeOvos

    """ Metodos publicos Get/Set do atributo peso unitario de cada ovo """
    def getPesoUnidOvo(self) -> float:
        return self.__pesoUnidOvo

    def setPesoUnidOvo(self, pesoUnidOvo:float) -> None:
        self.__pesoUnidOvo = pesoUnidOvo

    """ Metodos publicos Get/Set do atributo tempo para bater os ovos """
    def getTBaterOvos(self) -> int:
        return self.__tBaterOvos

    def setTBaterOvos(self, tBaterOvos:int) -> None:
        self.__tBaterOvos = tBaterOvos

    """ Metodos publicos Get/Set do atributo tempo para bater a massa """
    def getTBaserMassa(self) -> int:
        return self.__tBaterMassa

    def setTBaterMassa(self, tBaterMassa:int) -> None:
        self.__tBaterMassa = tBaterMassa

    """ Metodo privado que processa os ovos no preparo da massa """
    def __baterOvos(self) -> None:
        print("Iniciando o processo de bater os ovos...")
        tempo:int
        for tempo in range(self.getTBaterOvos(), 0, -1):
            print(f"Faltam {tempo} seg. para bater os ovos...", end="\r")
        print("Ovos prontos para preparar o bolo!")


class ReceitaDeBoloDeChocolate(ReceitaDeBolo):
    """ Classe extendida para receitas de bolo de chocolate """
    def __init__(self, qtdeFarinha:float, qtdeLeite:float, qtdeOvos:int, qtdeChocolate:float) -> None:
        """ Construtor da classe extendida """
        super().__init__(qtdeFarinha, qtdeLeite, qtdeOvos)
        self.__qtdeChocolate:float = qtdeChocolate   # atributo privado

    """ Metodos publicos Get/Set do atributo qtdeChocolate """
    def getQtdeChocolate(self) -> float:
        return self.__qtdeChocolate

    def setQtdeChocolate(self, qtdeFarinha:float) -> None:
        self.__qtdeFarinha = qtdeFarinha
