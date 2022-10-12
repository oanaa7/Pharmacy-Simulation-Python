from Domain.medicament import Medicament
from Repository.repository import FileRepository
from Tests.utils import clear_file


def test_file_repository():

    filename = 'test_medicament.txt'
    clear_file(filename)

    repository = FileRepository(filename)
    m1 = Medicament('1', 'algo', 'aaa', '123', 'da')
    repository.create(m1)

    all = repository.get_all()
    assert all[-1] == m1