from Repository.repository import FileRepository


class Cautare:
    def __init__(self, medicament_repository: FileRepository, card_client_repository: FileRepository):
        self.__medicament_repository = medicament_repository
        self.__card_client_repository = card_client_repository

    def cautare(self, string):
        '''
        Cauta medicamente, carduri, tranzactii, dupa un cuvant dat

        :param string:
        :return:
        '''
        #print(self.__medicament_repository.get_all())

        for medicament in self.__medicament_repository.get_all():
            if string in medicament.nume:
                print(medicament)
            elif string in medicament.producator:
                print(medicament)
            elif string in str(medicament.pret):
                print(medicament)
            elif string in medicament.necesita_reteta:
                print(medicament)

        for card_client in self.__card_client_repository.get_all():
            if string in card_client.nume:
                print(card_client)
            elif string in card_client.prenume:
                print(card_client)
            elif string in card_client.cnp:
                print(card_client)
            elif string.isdigit() == True:
                if int(string) == card_client.data_nasterii.year or int(string) == card_client.data_nasterii.day or int(string) == card_client.data_nasterii.month:
                    print(card_client)
                elif int(string) == card_client.data_inregistrarii.year or int(string) == card_client.data_inregistrarii.day or int(string) == card_client.data_inregistrarii.month:
                    print(card_client)


