from Domain.medicament_validator import MedicamentValidator
from Repository.repository import FileRepository
from Service.medicament_service import MedicamentService
from Service.undo_redo_service import UndoRedoService
from Tests.utils import clear_file


def test_service():
    undoredo_service = UndoRedoService()
    filename = 'test_medicament.txt'
    clear_file(filename)

    repository = FileRepository(filename)
    validator = MedicamentValidator()
    service = MedicamentService(validator, repository, undoredo_service)
    service.create('1', 'aaa', 'prod', '123', 'da')
    assert len(service.get_all()) == 1

    added = repository.find_by_id('1')
    assert added.necesita_reteta == 'da'
    assert added.nume == 'aaa'
    assert added.producator == 'prod'


    service.delete('1')
    assert len(service.get_all()) == 0


