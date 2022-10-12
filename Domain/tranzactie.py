from Domain.entity import Entity


class Tranzactie(Entity):
    def __init__(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data):
        super().__init__(id_tranzactie)
        self.__id_medicament = id_medicament
        self.__id_card_client = id_card_client
        self.__nr_bucati = nr_bucati
        self.__data = data

    def __str__(self):
        return f'Tranzactia cu id = {self.id_entity}, id_medicament = {self.__id_medicament}, id_card_client = {self.__id_card_client}' \
               f', nr_bucati = {self.__nr_bucati}, data = {self.__data}'

    @property
    def id_medicament(self):
        return self.__id_medicament

    @id_medicament.setter
    def id_medicament(self, value):
        self.__id_medicament = value
    @property
    def id_card_client(self):
        return self.__id_card_client


    @id_card_client.setter
    def id_card_client(self, value):
        self.__id_card_client = value
    @property
    def nr_bucati(self):
        return self.__nr_bucati

    @nr_bucati.setter
    def nr_bucati(self, value):
        self.__nr_bucati = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __eq__(self, other):
        return type(self) == type(other) and self.id_entity == other.id_entity