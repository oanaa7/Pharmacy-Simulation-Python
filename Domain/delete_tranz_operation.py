from Domain.undoredo_operation import UndoRedoOperation


class DeleteTranzOperation(UndoRedoOperation):
    '''
    Operatiunea pentru stergerea mai multor tranzactii, pentru undo si redo
    '''
    def __init__(self, repository, lst_sterse):
        super().__init__(repository)
        self.__lst_sterse = lst_sterse

    def undo(self):
        for elem in self.__lst_sterse:
            self._repository.create(elem)

    def redo(self):
        for elem in self.__lst_sterse:
            self._repository.delete(elem.id_entity)