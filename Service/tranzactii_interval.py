from copy import deepcopy

from Domain.delete_tranz_operation import DeleteTranzOperation
from Repository.repository import FileRepository
from Service.undo_redo_service import UndoRedoService
from Tests.utils import clear_file


class TranzactiiInterval:
    def __init__(self, tranzactii_repository: FileRepository, undo_redo_service: UndoRedoService):
        '''
        initializeaza un obiect de tip Tranzactiinterval

        :param tranzactii_repository:
        :param undo_redo_service:
        '''
        self.__tranzactii_repository = tranzactii_repository
        self.__undo_redo_service = undo_redo_service


    def tranzactii_interval(self, d1, d2):
        '''
        Determina toate tranzactiile dintr-un interval de zile

        :param d1: de tipul datetime
        :param d2: de tipul datetime
        :return: result, lista cu tranzactii
        '''
        if d2 < d1:
            aux = d1
            d1 = d2
            d2 = aux
        result = []
        for tranzactie in self.__tranzactii_repository.get_all():
            if tranzactie.data >= d1 and tranzactie.data <= d2:
                result.append(tranzactie)
        return result

    def stergere_tranzactii_din_interval(self, d1, d2):
        '''
        Sterge tranzactiile facute intr-un interval citit

        :param d1: data de la care se face stergerea
        :param d2: data pana la care se face stergerea
        :return:
        '''
        if d2 < d1:
            aux = d1
            d1 = d2
            d2 = aux


        result = self.__tranzactii_repository.get_all()
        lst_sterse = []
        i = 0
        while i < len(result):
            if result[i].data >= d1 and result[i].data <= d2:
                lst_sterse.append(result[i])
                self.__tranzactii_repository.delete(result[i].id_entity)
            i += 1

        self.__undo_redo_service.add_to_undo(DeleteTranzOperation(self.__tranzactii_repository, lst_sterse))
        self.__undo_redo_service.clear_redo()


    def stergere_tranzactii_din_interval_2(self, lst, d1, d2, lst_sterse):
        '''
        Sterge tranzactiile dintr-un interval citit

        :param lst: lista de tranzactii
        :param d1: data de inceput
        :param d2: data de final
        :return:
        '''
        if lst != []:
            if lst[0].data >= d1 and lst[0].data <= d2:
                lst_sterse.append(lst[0])
                self.__tranzactii_repository.delete(lst[0].id_entity)
            lst.pop(0)
            self.stergere_tranzactii_din_interval_2(lst, d1, d2, lst_sterse)
        else:
            self.__undo_redo_service.add_to_undo(DeleteTranzOperation(self.__tranzactii_repository, lst_sterse))
            self.__undo_redo_service.clear_redo()