
class minhaClasse(object):
    """ Classe base """
    def __init__(self, dado) -> None:
        self.dadoPublico    = dado  # atributo publico do objeto (instancia)
        self._dadoProtegido = 0     # atributo protegido do objeto (instancia)
        self.__dadoPrivado  = 0     # atributo privado do objeto (instancia)

    def metodoPublico(self) -> int:
        """ Metodo publico do objeto (instancia) """
        return -1

    def _metodoProtegido(self) -> int:
        """ Metodo protegido do objeto (instancia) """
        return -1

    def __metodoPrivado(self) -> int:
        """ Metodo privado do objeto (instancia) """
        return -1


class minhaClasseExtendida(minhaClasse):
    def __init__(self, dado) -> None:
        super().__init__(dado)

    def meuMetodo(self) -> int:
        self.__dadoPrivado


# Instancias...
myObj1 = minhaClasse(1.1)
print(myObj1.dadoPublico)
