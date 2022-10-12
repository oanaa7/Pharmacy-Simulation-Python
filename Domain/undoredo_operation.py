from Repository.repository import FileRepository


class UndoRedoOperation:
    '''
    Clasa pentru undo si redo
    '''
    def __init__(self, repository: FileRepository):
        self._repository = repository

    def undo(self):
        raise NotImplemented('Should use a derived class!')

    def redo(self):
        raise NotImplemented('Should use a derived class!')