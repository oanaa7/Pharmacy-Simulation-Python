from copy import deepcopy
import datetime

import Repository
from Domain.add_operation import AddOperation
from Domain.card_client import CardClient
from Domain.card_client_validator import CardClientValidator
from Domain.delete_operation import DeleteOperation
from Domain.update_operation import UpdateOperation
from Repository.repository import FileRepository
from Service.undo_redo_service import UndoRedoService


class CardClientService:
    def __init__(self, card_client_validator: CardClientValidator, card_client_repository: FileRepository,
                 undo_redo_service: UndoRedoService):
        '''
        Initializeaza un obiect card client

        :param card_client_validator:
        :param card_client_repository:
        :param undo_redo_service:
        '''
        self.__card_client_repository = card_client_repository
        self.__card_client_validator = card_client_validator
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        '''
        Returneaza o lista cu cardurile client
        :return:
        '''
        return deepcopy(list(self.__card_client_repository.get_all()))

    def create(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        '''
        Adauga un card client

        :param id_card: id-ul cardului
        :param nume: numele clientului
        :param prenume: prenumele
        :param cnp: cnpu-ul
        :param data_nasterii: data nasterii in datetime
        :param data_inregistrarii: data inregistrarii in format datetime
        :return:
        '''
        if self.find_by_cnp(cnp) is not None:
            raise ValueError('Cnp-ul exista deja!')
        card_client = CardClient(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        self.__card_client_repository.create(card_client)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__card_client_repository, card_client))
        self.__undo_redo_service.clear_redo()

    def update(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        '''
        Modifica un card client

        :param id_card: id-ul cardului
        :param nume: numele clientului
        :param prenume: prenumele
        :param cnp: cnpu-ul
        :param data_nasterii: data nasterii in datetime
        :param data_inregistrarii: data inregistrarii in format datetime
        :return:
        '''
        card_client1 = self.__card_client_repository.find_by_id(id_card)
        card_client2 = self.__card_client_repository.find_by_id(id_card)
        if nume != '':
            card_client2.nume = nume
        if prenume != '':
            card_client2.prenume = prenume
        if cnp != '':
            card_client2.cnp = cnp
        card_client2.data_nasterii = data_nasterii
        card_client2.data_inregistrarii = data_inregistrarii
        if card_client2.cnp != cnp and self.find_by_cnp(cnp) is not None:
            raise ValueError('Cnp-ul exista deja!')
        self.__card_client_validator.validate(card_client2)
        self.__card_client_repository.update(card_client2)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__card_client_repository, card_client1, card_client2))
        self.__undo_redo_service.clear_redo()

    def delete(self, id_card_client):
        '''
        Sterge un card client dupa id

        :param id_card_client: id-ul cardului
        :return:
        '''
        card_client = self.__card_client_repository.find_by_id(id_card_client)
        self.__card_client_repository.delete(id_card_client)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__card_client_repository, card_client))
        self.__undo_redo_service.clear_redo()

    def find_by_cnp(self, cnp):
        '''
        Gaseste dupa cnp un card client

        :param cnp: cnp-ul
        :return: cardul client
        '''
        copie = self.get_all()
        for card_client in copie:
            if card_client.cnp == cnp:
                return card_client
        return None

    def find_by_id(self, id_entity):
        '''
        Gaseste dupa id un card client

        :param id_entity: id-ul cardului
        :return: cardul client
        '''
        return self.__card_client_repository.find_by_id(id_entity)

