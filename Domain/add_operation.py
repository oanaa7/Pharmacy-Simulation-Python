from Domain.undoredo_operation import UndoRedoOperation


class AddOperation(UndoRedoOperation):
    '''
    Operatiunea de adaugare pentru undo si redo

    '''
    def __init__(self, repository, added_object):
        super().__init__(repository)
        self.__added_object = added_object

    def undo(self):
        '''

        :return:
        '''
        self._repository.delete(self.__added_object.id_entity)

    def redo(self):
        '''

        :return:
        '''
        self._repository.create(self.__added_object)