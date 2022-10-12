from Domain.undoredo_operation import UndoRedoOperation


class ScumpireOperatiune(UndoRedoOperation):
    '''
    Operatiunea de scumpire a medicamentelor pentru undo si redo

    '''
    def __init__(self, repository, lst_vechi, lst_noua):
        super().__init__(repository)
        self.__lst_vechi = lst_vechi
        self.__lst_noua = lst_noua

    def undo(self):
        for medicament in self.__lst_vechi:
            self._repository.update(medicament)

    def redo(self):
        for medicament in self.__lst_noua:
            self._repository.update(medicament)