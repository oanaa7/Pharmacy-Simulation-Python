from Domain.undoredo_operation import UndoRedoOperation


class UpdateOperation(UndoRedoOperation):
    '''
    Operatiunea de update pentru undo si redo
    '''
    def __init__(self, repository, object1, object2):
        super().__init__(repository)
        self.__object1 = object1
        self.__object2 = object2

    def undo(self):
        self._repository.update(self.__object1)

    def redo(self):
        self._repository.update(self.__object2)