from copy import deepcopy

from Domain.scumpire_operatiune import ScumpireOperatiune
from Repository.repository import FileRepository
import operator

from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService


class OrdonareMedicamente:
    def __init__(self, medicament_repository: FileRepository, tranzactie_repository: FileRepository,
                 tranzactie_service: TranzactieService, card_client_repository: FileRepository, undo_redo_service: UndoRedoService):
        '''
        Initializeaza un obiect de tip ordonare medicamente

        :param medicament_repository: repository-ul medicamentelor
        :param tranzactie_repository: repository-ul tranzactiilor
        :param tranzactie_service: service-ul tranzactiilor
        :param card_client_repository: repository-ul cardurilor
        :param undo_redo_service: service-ul pentru undo si redo
        '''
        self.__medicament_repository = medicament_repository
        self.__tranzactie_repository = tranzactie_repository
        self.__tranzactie_service = tranzactie_service
        self.__card_client_repository = card_client_repository
        self.__undo_redo_service = undo_redo_service

    def ordonare_medicamente(self):
        '''
        Ordoneaza medicamentele descresctor in functie de numarul de vanzari

        :return: lista sortata
        '''
        dictionar = {}
        for tranzactie in self.__tranzactie_repository.get_all():
            if tranzactie.id_medicament in dictionar:
                dictionar[tranzactie.id_medicament] += int(tranzactie.nr_bucati)
            else:
                dictionar[tranzactie.id_medicament] = int(tranzactie.nr_bucati)

        lst_duble = sorted(dictionar.items(), key=operator.itemgetter(1), reverse=True)
        #print(lst_duble)
        result = {}
        for (key, item) in lst_duble:
            result[self.__medicament_repository.find_by_id(key)] = item
        return result

    def ordonare_card_client(self):
        '''
        Ordoneaza cardurile client in functie de valoarea reducerilor

        :return: lista sortata
        '''
        dict = {}
        for tranzactie in self.__tranzactie_repository.get_all():
            lst = self.__tranzactie_service.get_pret(tranzactie)
            card_client = self.__card_client_repository.find_by_id(tranzactie.id_card_client)
            if tranzactie.id_card_client != '':
                if lst[1] == True:
                    if card_client in dict:
                        dict[card_client] += 15
                    else:
                        dict[card_client] = 15
                elif lst[2] == True:
                    if card_client in dict:
                        dict[card_client] += 10
                    else:
                        dict[card_client] = 10
        #print([(a,dict[a]) for a in dict])
        dict = [(a,dict[a]) for a in dict]
        #lst_duble = sorted(dict, key = lambda x: x[1], reverse=True)
        #lst_duble = self.my_sort(dict, key = lambda x: x[1], reverse=True)
        lst_duble = self.mergeSort(dict, key=lambda x: x[1], reverse=True)

        #lst_duble = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
        '''
        for (key, item) in dict:
            result[self.__medicament_repository.find_by_id(key)] = item
            print(key,'----' , item)
        '''
        return lst_duble

    def scumpire_medicamente_2(self, value):
        '''
        Scumpeste cu un procent medicamentele cu prețul mai mic decât o valoare dată

        :param value:
        :return:
        '''
        lst_vechi = self.__medicament_repository.get_all()
        for medicament in self.__medicament_repository.get_all():
            if float(medicament.pret) < value:
                medicament.pret = float(medicament.pret) + float(medicament.pret) / 100
                self.__medicament_repository.update(medicament)
        lst_noi = self.__medicament_repository.get_all()
        self.__undo_redo_service.add_to_undo(ScumpireOperatiune(self.__medicament_repository, lst_vechi, lst_noi))
        self.__undo_redo_service.clear_redo()

    def scumpire_medicamente(self, value):
        '''
        Scumpeste cu un procent medicamentele cu prețul mai mic decât o valoare dată

        :param value: valoarea data
        :return:
        '''

        lst_vechi = self.__medicament_repository.get_all()
        vlst = [value for i in range(0, len(lst_vechi))]
        my_zip = zip(lst_vechi, vlst)
        lst_preturi = list(map(lambda p: float(p[0].pret) + float(p[0].pret) / 100 if float(p[0].pret) < p[1] else p[0].pret, my_zip))
        i = 0
        for medicament in self.__medicament_repository.get_all():
            medicament.pret = lst_preturi[i]
            i += 1
            self.__medicament_repository.update(medicament)

        lst_noi = self.__medicament_repository.get_all()

        self.__undo_redo_service.add_to_undo(ScumpireOperatiune(self.__medicament_repository, lst_vechi, lst_noi))
        self.__undo_redo_service.clear_redo()
        #print(lst_preturi)

    def my_sort(self, lst, key=lambda x: x, reverse=False):
        '''
        Sortare prin metoda selectiei directe

        :param lst: lista pe care se face sortarea
        :param key: in functie de ce se face sortarea
        :param reverse: False crescator, True descrescator
        :return: lista sortata
        '''
        for i in range(0, len(lst) - 1):
            for j in range(i + 1, len(lst)):
                if reverse == False:
                    if key(lst[i]) > key(lst[j]):
                        aux = lst[i]
                        lst[i] = lst[j]
                        lst[j] = aux
                elif reverse == True:
                    if key(lst[i]) < key(lst[j]):
                        aux = lst[i]
                        lst[i] = lst[j]
                        lst[j] = aux
        return lst

    def mergeSort(self, lst, key=lambda x: x, reverse=False):
        '''
        Sortare prin metoda mergesort

        :param lst: lista pentru sortare
        :param key: in functie de ce se face sortarea
        :param reverse: False pentru descrescator, True pentru crescator
        :return: lista sortata
        '''
        lst = list(lst)
        if len(lst) > 1:

            # Finding the mid of the array
            mid = len(lst) // 2

            # Dividing the array elements
            L = lst[:mid]

            # into 2 halves
            R = lst[mid:]

            # Sorting the first half
            L = self.mergeSort(L, key, reverse)

            # Sorting the second half
            R = self.mergeSort(R, key, reverse)

            i = j = k = 0
            result = deepcopy(lst)
            # Copy data to temp arrays L[] and R[]
            if L is not None and R is not None:
                while i < len(L) and j < len(R):
                    if reverse == False:
                        if key(L[i]) < key(R[j]):
                            result[k] = L[i]
                            i += 1
                        else:
                            result[k] = R[j]
                            j += 1
                    elif reverse == True:
                        if key(L[i]) > key(R[j]):
                            result[k] = L[i]
                            i += 1
                        else:
                            result[k] = R[j]
                            j += 1
                    k += 1

                # Checking if any element was left
                while i < len(L):
                    result[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    result[k] = R[j]
                    j += 1
                    k += 1
            return result
        return [lst[0]]


    #lst = [4, 2, 67, 34, 1, 23, -1, -299, 25]
    #lst2 = ['aaaaa', 'aaaaaaaaaaaaaaaaaa', 'b']
    #print(my_sort(lst))