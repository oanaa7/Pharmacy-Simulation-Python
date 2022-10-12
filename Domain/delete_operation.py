from Domain.undoredo_operation import UndoRedoOperation


class DeleteOperation(UndoRedoOperation):
    '''
    Operatiunea de stergere pentru undo si redo


    '''
    def __init__(self, repository, deleted_object):
        super().__init__(repository)
        self.__deleted_object = deleted_object

    def undo(self):
        self._repository.create(self.__deleted_object)

    def redo(self):
        self._repository.delete(self.__deleted_object.id_entity)