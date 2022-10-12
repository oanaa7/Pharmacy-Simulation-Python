from copy import deepcopy

from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.tranzactie import Tranzactie
from Domain.tranzactie_validator import TranzactieValidator
from Domain.update_operation import UpdateOperation

from Repository.repository import FileRepository
from Service.undo_redo_service import UndoRedoService


class TranzactieService:
    def __init__(self, tranzactie_validator: TranzactieValidator, tranzactie_repository: FileRepository,
                medicament_repository: FileRepository, card_client_repository: FileRepository, undo_redo_service: UndoRedoService):
        self.__tranzactie_validator = tranzactie_validator
        self.__tranzactie_repository = tranzactie_repository
        self.__medicament_repository = medicament_repository
        self.__card_client_repository = card_client_repository
        self.__undo_redo_service = undo_redo_service



    def get_all(self):
        '''
        Returneaza o lista cu toate tranzactiile

        :return:
        '''
        return deepcopy(self.__tranzactie_repository.get_all())

    def create(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data):
        '''
        Creaza o tranzactie

        :param id_tranzactie: id-ul tranzactiei
        :param id_medicament: id-ul medicamentului
        :param id_card_client: id-ul cardului
        :param nr_bucati: numarul de bucati, int
        :param data: data in format datetime
        :return:
        '''
        tranzactie = Tranzactie(id_tranzactie, id_medicament, id_card_client, nr_bucati, data)
        if tranzactie.id_card_client != '':
            if self.__card_client_repository.find_by_id(tranzactie.id_card_client) is None:
                raise ValueError('Id-ul cardului nu exista!')
        if self.__medicament_repository.find_by_id(tranzactie.id_medicament) is None:
            raise ValueError('Id-ul medicamentului nu exista!')
        self.__tranzactie_validator.validate(tranzactie)

        self.__tranzactie_repository.create(tranzactie)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__tranzactie_repository, tranzactie))
        self.__undo_redo_service.clear_redo()

    def update(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data):
        '''
        Modifica o tranzactie

        :param id_tranzactie: id-ul tranzactiei
        :param id_medicament: id-ul medicamentului
        :param id_card_client: id-ul cardului
        :param nr_bucati: numarul de bucati, int
        :param data: data in format datetime
        :return:
        '''
        tranzactie1 = self.__tranzactie_repository.find_by_id(id_tranzactie)
        tranzactie2 = self.__tranzactie_repository.find_by_id(id_tranzactie)
        if id_medicament != '':
            tranzactie2.id_medicament = id_medicament
        if id_card_client != '':
            tranzactie2.id_card_client = id_card_client
        if nr_bucati != '':
            tranzactie2.nr_bucati = nr_bucati

        tranzactie2.data = data
        self.__tranzactie_validator.validate(tranzactie2)
        self.__tranzactie_repository.update(tranzactie2)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__tranzactie_repository, tranzactie1, tranzactie2))
        self.__undo_redo_service.clear_redo()

    def delete(self, id_tranzactie):
        '''
        Sterge o tranzactie

        :param id_tranzactie: id-ul tranzactiei
        :return:
        '''
        tranzactie = self.__tranzactie_repository.find_by_id(id_tranzactie)
        self.__tranzactie_repository.delete(id_tranzactie)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__tranzactie_repository, tranzactie))
        self.__undo_redo_service.clear_redo()

    def find_by_id(self, id_tranzactie):
        '''
        Gaseste dupa un id o tranzactie
        :param id_tranzactie: id-ul tranzactiei
        :return: obiectul gasit sau None
        '''
        return self.__tranzactie_repository.find_by_id(id_tranzactie)

    def get_pret(self, tranzactie):
        '''
        Calculeaza pretul tranzactiei

        :param tranzactie: tranzactia
        :return: o lista care contine:
                primul element = pretul
                al 2 lea elemenet = True daca s-a acordat prima reducere
                al 3 lea element = True daca s-a acordat a 2 a reducere
        '''
        medicament = self.__medicament_repository.find_by_id(tranzactie.id_medicament)
        card_client = self.__card_client_repository.find_by_id(tranzactie.id_card_client)
        if medicament is not None:
            pret = float(tranzactie.nr_bucati) * float(medicament.pret)
            r1 = False
            r2 = False
            if card_client is not None:
                if medicament.necesita_reteta == 'da':
                    pret = pret - 15 * pret / 100
                    r1 = True
                elif medicament.necesita_reteta == 'nu':
                    pret = pret - 10 * pret / 100
                    r2 = True
            return [pret, r1, r2]
        return [None, None, None]