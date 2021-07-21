#!/usr/bin/python3

import os
from time import sleep

class ReceitaDeBolo(object):
    """ Classe base para receitas de bolo """
    def __init__(self, qtdeOvos:int, tBaterOvos:int=30) -> None:
        """ Construtor da classe base """
        self.__tipoBolo:str = "Pao de lo"
        self.qtdeOvos:int   = qtdeOvos      # atributo privado; quantidade de ovos; unidades
        self.tBaterOvos:int = tBaterOvos    # atributo privado; tempo para bater os ovos; segundos

    """ Metodos publicos Get/Set do atributo tipo de bolo """
    def getTipoBolo(self) -> str:
        return self.__tipoBolo

    def setTipoBolo(self, tipoBolo:str) -> None:
        self.__tipoBolo = tipoBolo

    """ Metodos publicos Get/Set do atributo quantidade de ovos da receita """
    def getQtdeOvos(self) -> int:
        return self.qtdeOvos

    def setQtdeOvos(self, qtdeOvos:int) -> None:
        self.qtdeOvos = qtdeOvos

    """ Metodos publicos Get/Set do atributo tempo (s) para bater os ovos """
    def getTBaterOvos(self) -> int:
        return self.tBaterOvos

    def setTBaterOvos(self, tBaterOvos:int) -> None:
        self.tBaterOvos = tBaterOvos

    """ Metodo privado que formata o objeto como string"""
    def __str__(self) -> str:
        objFormatado: str = ""
        objFormatado += "#" + "-" * 79
        objFormatado += f"\n# Bolo do tipo: {self.getTipoBolo()}"
        objFormatado += "\n#" + "-" * 79
        objFormatado += f"\n :: Ingredientes ::"
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

    """ Metodo publico que prepara o bolo """
    def prepararBolo(self, etapa=1) -> None:
        _etapa: int = etapa
        # Etapa: bater os ovos
        print(f"# {_etapa}a etapa: os ovos!")
        print("#" + "-" * 79)
        self.__baterOvos()


class ReceitaDeBoloDeChocolate(ReceitaDeBolo):
    """ Classe extendida para receitas de bolo de chocolate """
    def __init__(self, qtdeOvos:int, qtdeChocolate:float, tBaterOvos:int=30, tDerreteChocolate:int=30) -> None:
        """ Construtor da classe extendida """
        super().__init__(qtdeOvos, tBaterOvos)
        self.qtdeChocolate:float      = qtdeChocolate         # atributo privado
        self.tDerreteChocolate:float  = tDerreteChocolate     # atributo privado
        # Atualiza tipo de bolo
        self.setTipoBolo("Chocolate")

    """ Metodos publicos Get/Set do atributo qtdeChocolate """
    def getQtdeChocolate(self) -> float:
        return self.qtdeChocolate

    def setQtdeChocolate(self, qtdeChocolate:float) -> None:
        self.qtdeChocolate = qtdeChocolate

    """ Metodos publicos Get/Set do atributo tempo (s) para assar o bolo """
    def getTDerreteChocolate(self) -> int:
        return self.tDerreteChocolate

    def setTDerreteChocolate(self, tDerreteChocolate:int) -> None:
        self.tDerreteChocolate = tDerreteChocolate

    """ Metodo privado que processa chocolate """
    def __derreterChocolate(self) -> None:
        print("Iniciando o processo de derreter o chocolate...")
        tempo:int
        for tempo in range(self.getTDerreteChocolate(), 0, -1):
            print(f"Faltam {tempo} seg. para terminar de derreter o chocolate...", end="\r")
            sleep(1)    # considerando que o tempo informado esta em segundos
        print("\nChocolate pronto para preparar o bolo!")

    """ Metodo privado que formata o objeto como string """
    def __str__(self) -> str:
        objFormatado: str = ""
        objFormatado += f"\n\tChocolate: {self.getQtdeChocolate():.2f} g."

        return super().__str__() + objFormatado

    """ Metodo publico que prepara o bolo """
    def prepararBolo(self) -> None:
        # Etapa: bater os ovos
        _etapa: int = 1
        print(f"# {_etapa}a etapa: o chocolate!")
        print("#" + "-" * 79)
        self.__derreterChocolate()
        print("#" + "-" * 79)

        # Proximas etapas do preparo, herdadas da classe base
        _etapa += 1
        super().prepararBolo(_etapa)


class ReceitaDeBoloDeCenoura(ReceitaDeBolo):
    """ Classe extendida para receitas de bolo de cenoura """
    def __init__(self, qtdeOvos:int, qtdeCenoura:float, tBaterOvos:int=30, tRalaCenoura:int=30) -> None:
        """ Construtor da classe extendida """
        super().__init__(qtdeOvos, tBaterOvos)
        self.qtdeCenoura:float    = qtdeCenoura       # atributo privado
        self.tRalaCenoura:float   = tRalaCenoura      # atributo privado
        # Atualiza tipo de bolo
        self.setTipoBolo("Cenoura")

    """ Metodos publicos Get/Set do atributo qtdeCenoura """
    def getQtdeCenoura(self) -> float:
        return self.qtdeCenoura

    def setQtdeCenoura(self, qtdeCenoura:float) -> None:
        self.qtdeCenoura = qtdeCenoura

    """ Metodos publicos Get/Set do atributo tempo (s) para assar o bolo """
    def getTRalaCenoura(self) -> int:
        return self.tRalaCenoura

    def setTRalaCenoura(self, tRalaCenoura:int) -> None:
        self.tRalaCenoura = tRalaCenoura

    """ Metodo privado que processa cenoura """
    def __ralarCenoura(self) -> None:
        print("Iniciando o processo de ralar a cenoura...")
        tempo:int
        for tempo in range(self.getTRalaCenoura(), 0, -1):
            print(f"Faltam {tempo} seg. para terminar de ralar a cenoura...", end="\r")
            sleep(1)    # considerando que o tempo informado esta em segundos
        print("\nCenoura pronta para preparar o bolo!")

    """ Metodo privado que formata o objeto como string """
    def __str__(self) -> str:
        objFormatado: str = ""
        objFormatado += f"\n\tCenoura:   {self.getQtdeCenoura():.2f} g."

        return super().__str__() + objFormatado

    """ Metodo publico que prepara o bolo """
    def prepararBolo(self) -> None:
        # Etapa: bater os ovos
        _etapa: int = 1
        print(f"# {_etapa}a etapa: a cenoura!")
        print("#" + "-" * 79)
        self.__ralarCenoura()
        print("#" + "-" * 79)

        # Proximas etapas do preparo, herdadas da classe base
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

        tipoBolo:int = 0

        try:
            tipoBolo = int(input("Escolha: ") or "-1")
        except ValueError:
            tipoBolo = -1

        # Caso o usuario não entre com um numero
        if tipoBolo in [1,2,3]:
            # Recebe os ingredientes
            print("Excelente escolha! Agora, os ingredientes...")
            qtdeOvos:int    = int(input("Ovos (unidades): ") or "0")
            print("Tudo bem. E o tempo de preparo?")
            tBaterOvos:int  = int(input("Para bater os ovos (segundos); padrao 30s: ") or "30")

        # Declara o objeto para receber a instancia
        objBolo = None
        # Instanciando o objeto de acordo com o bolo
        if (int(tipoBolo) == 1):
            # Pao de lo
            objBolo = ReceitaDeBolo(qtdeOvos, tBaterOvos)
        elif (int(tipoBolo) == 2):
            # Chocolate
            print("Esse bolo tem algo especial...")
            qtdeChocolate = float(input("Chocolate (gramas): ") or "0.0")
            tDerreteChoc  = int(input("Tempo para derreter o chocolate (segundos); padrao 30s: ") or "30")
            objBolo = ReceitaDeBoloDeChocolate(qtdeOvos, qtdeChocolate, tBaterOvos,tDerreteChoc)
        elif (int(tipoBolo) == 3):
            # Cenoura
            print("Esse bolo tem algo a mais...")
            qtdeCenoura     = float(input("Cenoura (gramas): ") or "0.0")
            tRalaCenoura    = int(input("Tempo para ralar a cenoura (segundos); padrao 30s: ") or "30")
            objBolo = ReceitaDeBoloDeCenoura(qtdeOvos, qtdeCenoura, tBaterOvos, tRalaCenoura)
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

        # Espera o usuario pressionar qualquer tecla antes de limpar a tela
        #   e esperar pelo proximo bolo
        input("Pressione <ENTER> para prosseguir...")
    #except:
    #    print("Ocorreu uma excecao!!!")

if __name__ == "__main__":
    main()
