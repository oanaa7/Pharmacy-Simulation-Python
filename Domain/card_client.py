from Domain.entity import Entity


class CardClient(Entity):
    def __init__(self, id_card, nume, prenume, cnp, data_nasterii, data_inregisistrarii):

        super().__init__(id_card)
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__data_nasterii = data_nasterii
        self.__data_inregisistrarii = data_inregisistrarii

    def __str__(self):
        return f'Clientul cu id = {self.id_entity}, nume = {self.__nume}, prenume = {self.__prenume}, cnp = {self.__cnp}, ' \
               f'data_nasterii = {self.__data_nasterii}, data_inregistrarii = {self.__data_inregisistrarii}'

    def __hash__(self):
        return hash(self.id_entity)
    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, value):
        self.__cnp = value

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value
    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, value):
        self.__prenume = value
    @property
    def data_nasterii(self):
        return self.__data_nasterii


    @data_nasterii.setter
    def data_nasterii(self, value):
        self.__data_nasterii = value
    @property
    def data_inregistrarii(self):
        return self.__data_inregisistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, value):
        self.__data_inregisistrarii = value




