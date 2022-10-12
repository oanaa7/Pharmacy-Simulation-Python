class UndoRedoService:
    '''
    Service-ul pentru undo si redo
    '''
    def __init__(self):
        self.__undo_stack = []
        self.__redo_stack = []

    def add_to_undo(self, operation):
        '''
        Adauga in lista de undo o operatiune

        :param operation: operatiunea
        :return:
        '''
        self.__undo_stack.append(operation)

    def add_to_redo(self, operation):
        '''
        Adauga in lista de redo o operatiune

        :param operation: operatiunea
        :return:
        '''
        self.__redo_stack.append(operation)

    def clear_redo(self):
        '''
        Goleste redo-ul

        :return:
        '''
        self.__redo_stack = []

    def do_undo(self):
        '''
        Efectueaza undo-ul

        :return:
        '''
        if len(self.__undo_stack) > 0:
            operation = self.__undo_stack.pop()
            self.add_to_redo(operation)
            operation.undo()


    def do_redo(self):
        '''
        Efectueaza redo-ul

        :return:
        '''
        if len(self.__redo_stack) > 0:
            operation = self.__redo_stack.pop()
            self.add_to_undo(operation)
            operation.redo()

