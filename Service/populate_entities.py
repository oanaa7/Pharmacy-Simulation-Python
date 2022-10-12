import string
import random

from Domain.medicament import Medicament
from Domain.medicament_validator import MedicamentValidator
from Domain.random_operation import RandomOperation
from Repository.repository import FileRepository
from Service.undo_redo_service import UndoRedoService


class PopulateEntities:
    def __init__(self, medicament_repository: FileRepository, medicament_validator: MedicamentValidator, undo_redo_service: UndoRedoService):
        self.__medicament_repository = medicament_repository
        self.__medicament_validator = medicament_validator
        self.__undo_redo_service = undo_redo_service

    def get_random_number(self, length):
        '''
        Da un numar random
        :param length: lungimea numarului
        :return:
        '''
        letters_and_digits = string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    def get_random_string(self, length):
        '''
        Da un string random
        :param length: lungimea stringului
        :return:
        '''
        letters_and_digits = string.ascii_lowercase
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    def get_random_Up(self, length):
        '''
        Da un string random cu prima litera, litera mare
        :param length: lungimea stringului
        :return:
        '''
        letters_and_digits = string.ascii_uppercase
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    def populate_entities(self, n):
        '''
        Creaza n medicamente cu date random

        :param n: numarul de medicamente generat
        :return:
        '''
        lst_medicamente = []
        while n:
            try:
                n -= 1
                id_medicament = self.get_random_number(3)

                if self.__medicament_repository.find_by_id(id_medicament) is not None:
                    raise Exception

                nume = self.get_random_Up(1) + self.get_random_string(5)
                producator = self.get_random_Up(1) + self.get_random_string(5)
                pret = self.get_random_number(2)
                if int(self.get_random_number(1)) % 2 == 0:
                    necesita_reteta = 'da'
                else:
                    necesita_reteta = 'nu'

                medicament = Medicament(id_medicament, nume, producator, pret, necesita_reteta)
                self.__medicament_validator.validate(medicament)
                self.__medicament_repository.create(medicament)
                lst_medicamente.append(medicament)
                #print(medicament)
            except Exception:
                n += 1
        self.__undo_redo_service.add_to_undo(RandomOperation(self.__medicament_repository, lst_medicamente))
        self.__undo_redo_service.clear_redo()