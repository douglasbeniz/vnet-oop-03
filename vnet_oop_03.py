#!/usr/bin/python3

import os
from time import sleep

class ReceitaDeBolo:
    """ Classe base para receitas de bolo """
    def __init__(self, qtdeFarinha:float, qtdeLeite:float, qtdeOvos:int, pesoUnidOvo:float=50, tBaterOvos:int=30, tBaterMassa:int=30, tAssarBolo:int=30) -> None:
        """ Construtor da classe base """
        self.__tipoBolo:str         = "Pao de lo"
        self.__qtdeFarinha:float    = qtdeFarinha   # atributo privado; quantidade de farinha; gramas
        self.__qtdeLeite:float      = qtdeLeite     # atributo privado; quantidade de leite; litros
        self.__qtdeOvos:int         = qtdeOvos      # atributo privado; quantidade de ovos; unidades
        self.__pesoUnidOvo:float    = pesoUnidOvo   # atributo privado; peso unitario dos ovos
        self.__tBaterOvos:int       = tBaterOvos    # atributo privado; tempo para bater os ovos; segundos
        self.__tBaterMassa:int      = tBaterMassa   # atributo privado; tempo para bater a massa; segundos
        self.__tAssarBolo:int       = tAssarBolo    # atributo privado; tempo para assar o bolo; segundos

    """ Metodos publicos Get/Set do atributo tipo de bolo """
    def getTipoBolo(self) -> str:
        return self.__tipoBolo

    def setTipoBolo(self, tipoBolo:str) -> None:
        self.__tipoBolo = tipoBolo

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

    """ Metodos publicos Get/Set do atributo tempo (s) para bater os ovos """
    def getTBaterOvos(self) -> int:
        return self.__tBaterOvos

    def setTBaterOvos(self, tBaterOvos:int) -> None:
        self.__tBaterOvos = tBaterOvos

    """ Metodos publicos Get/Set do atributo tempo (s) para bater a massa """
    def getTBaterMassa(self) -> int:
        return self.__tBaterMassa

    def setTBaterMassa(self, tBaterMassa:int) -> None:
        self.__tBaterMassa = tBaterMassa

    """ Metodos publicos Get/Set do atributo tempo (s) para assar o bolo """
    def getTAssarBolo(self) -> int:
        return self.__tAssarBolo

    def setTAssarBolo(self, tAssarBolo:int) -> None:
        self.__tAssarBolo = tAssarBolo

    """ Metodo privado que formata o objeto como string"""
    def __str__(self) -> str:
        objFormatado: str = ""
        objFormatado += "#" + "-" * 79
        objFormatado += f"\n# Bolo do tipo: {self.getTipoBolo()}"
        objFormatado += "\n#" + "-" * 79
        objFormatado += f"\nIngredientes ::"
        objFormatado += f"\n\tFarinha:   {self.getQtdeFarinha():.2f} g."
        objFormatado += f"\n\tLeite:     {self.getQtdeLeite():.2f} L."
        objFormatado += f"\n\tOvos:      {self.getQtdeOvos():d}"

        return objFormatado

    """ Metodo privado que processa os ovos """
    def __baterOvos(self) -> None:
        print("Iniciando o processo de bater os ovos...")
        tempo:int
        for tempo in range(self.getTBaterOvos(), 0, -1):
            print(f"Faltam {tempo} seg. para terminar de bater os ovos...", end="\r")
            sleep(1)    # considerando que o tempo informado esta em segundos
        print("\nOvos prontos para preparar o bolo!")

    """ Metodo privado que processa a mistura da massa """
    def __baterMassa(self) -> None:
        print("Iniciando o processo de misturar a massa do bolo...")
        tempo:int
        for tempo in range(self.getTBaterMassa(), 0, -1):
            print(f"Faltam {tempo} seg. para terminar de misturar a massa...", end="\r")
            sleep(1)    # considerando que o tempo informado esta em segundos
        print("\nA massa esta pronta!")

    """ Metodo privado que processa o cozimento do bolo """
    def __assarMassa(self) -> None:
        print("Iniciando o processo de cozimento do bolo...")
        tempo:int
        for tempo in range(self.getTAssarBolo(), 0, -1):
            print(f"Faltam {tempo} seg. para terminar de assar o bolo...", end="\r")
            sleep(1)    # considerando que o tempo informado esta em segundos
        print("\nO bolo esta pronto!")

    """ Metodo publico que prepara o bolo """
    def prepararBolo(self, etapa=1) -> None:
        _etapa: int = etapa
        # Etapa: bater os ovos
        print(f"# {_etapa}a etapa: os ovos!")
        print("#" + "-" * 79)
        self.__baterOvos()
        # Etapa: misturar a massa
        _etapa += 1
        print("#" + "-" * 79)
        print(f"# {_etapa}a etapa: a massa!")
        print("#" + "-" * 79)
        self.__baterMassa()
        # Etapa: assar o bolo
        _etapa += 1
        print("#" + "-" * 79)
        print(f"# {_etapa}a etapa: o bolo!")
        print("#" + "-" * 79)
        self.__assarMassa()
        print("\n")

class ReceitaDeBoloDeChocolate(ReceitaDeBolo):
    """ Classe extendida para receitas de bolo de chocolate """
    def __init__(self, qtdeFarinha:float, qtdeLeite:float, qtdeOvos:int, qtdeChocolate:float, pesoUnidOvo:float=50, tBaterOvos:int=30, tBaterMassa:int=30, tAssarBolo:int=30, tDerreteChocolate:int=30) -> None:
        """ Construtor da classe extendida """
        super().__init__(qtdeFarinha, qtdeLeite, qtdeOvos, pesoUnidOvo, tBaterOvos, tBaterMassa, tAssarBolo)
        self.__qtdeChocolate:float      = qtdeChocolate         # atributo privado
        self.__tDerreteChocolate:float  = tDerreteChocolate     # atributo privado
        # Atualiza tipo de bolo
        self.setTipoBolo("Chocolate")

    """ Metodos publicos Get/Set do atributo qtdeChocolate """
    def getQtdeChocolate(self) -> float:
        return self.__qtdeChocolate

    def setQtdeChocolate(self, qtdeChocolate:float) -> None:
        self.__qtdeChocolate = qtdeChocolate

    """ Metodos publicos Get/Set do atributo tempo (s) para assar o bolo """
    def getTDerreteChocolate(self) -> int:
        return self.__tDerreteChocolate

    def setTDerreteChocolate(self, tDerreteChocolate:int) -> None:
        self.__tDerreteChocolate = tDerreteChocolate

    """ Metodo privado que processa chocolate """
    def __derreterChocolate(self) -> None:
        print("Iniciando o processo de derreter o chocolate...")
        tempo:int
        for tempo in range(self.getTDerreteChocolate(), 0, -1):
            print(f"Faltam {tempo} seg. para terminar de derreter o chocolate...", end="\r")
            sleep(1)    # considerando que o tempo informado esta em segundos
        print("Chocolate pronto para preparar o bolo!")

    """ Metodo privado que formata o objeto como string """
    def __str__(self) -> str:
        objFormatado: str = ""
        objFormatado += f"\n\tChocolate: {self.getQtdeChocolate():.2f} g."

        return super().__str__() + objFormatado

    """ Metodo publico que prepara o bolo """
    def prepararBolo(self) -> None:
        _etapa: int = 1
        # Etapa: bater os ovos
        print(f"# {_etapa}a etapa: o chocolate!")
        print("#" + "-" * 79)
        self.__derreterChocolate()
        _etapa += 1
        super().prepararBolo(_etapa)

# -----------------------------------------------------------------------------
# Script de tests....
# -----------------------------------------------------------------------------
def main():
    """ Funcao principal do script """

    #try:
    while(True):
        # Limpando a tela
        os.system('cls' if os.name == 'nt' else 'clear')

        # Iniciando...
        print("#" + "-" * 79)
        print("# RECEITA DE BOLOS ")
        print("#" + "-" * 79)

        # Questiona o tipo de bolo
        print("Qual bolo voce vai querer?")
        print("\tPao de lo: 1")
        print("\tChocolate: 2")
        print("\tCenoura:   3")
        print("Qualquer outra entrada encerra o programa.")
        tipoBolo = int(input("Escolha: ") or "-1")

        # Caso o usuario não entre com um numero
        #if type(tipoBolo != int):
        #    tipoBolo = -1
        if tipoBolo in [1,2,3]:
            # Recebe os ingredientes
            print("Excelente escolha! Agora, os ingredientes...")
            qtdeFarinha = float(input("Farinha (gramas): ") or "0.0")
            qtdeLeite   = float(input("Leite (litros): ") or "0.0")
            qtdeOvos    = int(input("Ovos (unidades): ") or "0")
            pesoOvos    = float(input("Peso por ovo (gramas); padrao 50g: ") or "50.0")
            print("Tudo bem. E o tempo de preparo?")
            tBaterOvos      = int(input("Para bater os ovos (segundos); padrao 30s: ") or "30")
            tBaterMassa     = int(input("Para misturar a massa (segundos); padrao 30s: ") or "30")
            tAssarBolo      = int(input("Para assar o bolo (segundos); padrao 30s: ") or "30")

        # Declara o objeto para receber a instancia
        objBolo = None
        # Instanciando o objeto de acordo com o bolo
        if (int(tipoBolo) == 1):
            # Pao de lo
            objBolo = ReceitaDeBolo(qtdeFarinha, qtdeLeite, qtdeOvos, pesoOvos, tBaterOvos, tBaterMassa, tAssarBolo)
        elif (int(tipoBolo) == 2):
            # Chocolate
            print("Esse bolo tem algo especial...")
            qtdeChocolate = float(input("Chocolate (gramas): ") or "0.0")
            tDerreteChoc  = int(input("Tempo para derreter o chocolate (segundos); padrao 30s: ") or "30")
            objBolo = ReceitaDeBoloDeChocolate(qtdeFarinha, qtdeLeite, qtdeOvos, pesoOvos, qtdeChocolate, tBaterOvos, tBaterMassa, tAssarBolo, tDerreteChoc)
        elif (int(tipoBolo) == 3):
            # Cenoura
            pass
        else:
            # Interrompe o looping
            print("\nAte logo!\n")
            break

        if (objBolo != None):
            # Exibe os ingredientes
            print(objBolo)

            # Preparando o bolo...
            print("#" + "-" * 79)
            print("# Preparando o bolo... ")
            print("#" + "-" * 79)
            objBolo.prepararBolo()
    #except:
    #    print("Ocorreu uma excecao!!!")

if __name__ == "__main__":
    main()
