from Domain.entity import Entity


class Medicament(Entity):
    def __init__(self, id_medicament, nume, producator, pret, necesita_reteta):
        super().__init__(id_medicament)
        self.__nume = nume
        self.__producator = producator
        self.__pret = pret
        self.__necesita_reteta = necesita_reteta

    def __str__(self):
        return f'Medicamentul cu id = {self.id_entity}, nume = {self.__nume}, producator = {self.__producator}, pret = {self.__pret},' \
               f' necesita_reteta = {self.__necesita_reteta}'
    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def producator(self):
        return self.__producator

    @producator.setter
    def producator(self, value):
        self.__producator = value

    @property
    def pret(self):
        return self.__pret

    @pret.setter
    def pret(self, value):
        self.__pret = value

    @property
    def necesita_reteta(self):
        return self.__necesita_reteta

    @necesita_reteta.setter
    def necesita_reteta(self, value):
        self.__necesita_reteta = value


    def __eq__(self, other):
        return type(self) == type(other) and self.id_entity == other.id_entity
    
    def __hash__(self):
        return hash(self.id_entity)
