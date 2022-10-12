from Domain.undoredo_operation import UndoRedoOperation


class RandomOperation(UndoRedoOperation):
    '''
    Operatiunea pentru aduagarea random a medicamentelor, pt undo si redo
    '''
    def __init__(self, repository, lst_medicamente):
        super().__init__(repository)
        self.__lst_medicamente = lst_medicamente

    def undo(self):
        for elem in self.__lst_medicamente:
            self._repository.delete(elem.id_entity)

    def redo(self):
        for elem in self.__lst_medicamente:
            self._repository.create(elem)