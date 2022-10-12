import datetime

from Domain import tranzactie_validator
from Domain.card_client import CardClient
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie
from Domain.tranzactie_validator import TranzactieValidator
from Repository.repository import FileRepository
from Service.ordonare_medicamente import OrdonareMedicamente
from Service.tranzactie_service import TranzactieService
from Service.tranzactii_interval import TranzactiiInterval
from Service.undo_redo_service import UndoRedoService
from Tests.utils import clear_file


def teste_ordonare():

    undoredo_service = UndoRedoService()
    medicament_repository = FileRepository('test_ordonare_medicament.txt')
    clear_file('test_ordonare_medicament.txt')
    card_client_repository = FileRepository('test_ordonare_card_client.txt')

    clear_file('test_ordonare_card_client.txt')
    tranzactie_repository = FileRepository('test_ordonare_tranzactie.txt')
    tranzactie_validator = TranzactieValidator()
    clear_file('test_ordonare_tranzactie.txt')
    tranzactie_service = TranzactieService(tranzactie_validator, tranzactie_repository, medicament_repository, card_client_repository, undoredo_service)
    ord = OrdonareMedicamente(medicament_repository, tranzactie_repository, tranzactie_service, card_client_repository, undoredo_service)

    m1 = Medicament('1', 'meda', 'proda', '100', 'da')
    medicament_repository.create(m1)
    m2 = Medicament('2', 'medb', 'prodb', '200', 'da')
    medicament_repository.create(m2)
    m3 = Medicament('3', 'medc', 'prodc', '140', 'da')
    medicament_repository.create(m3)
    m4 = Medicament('4', 'medd', 'prodd', '500', 'nu')
    medicament_repository.create(m4)
    m5 = Medicament('5', 'mede', 'prode', '340', 'da')
    medicament_repository.create(m5)

    y = datetime.datetime(2020, 11, 11, 12)
    t1 = Tranzactie('1', '1', '', '5', y)
    tranzactie_repository.create(t1)
    y = datetime.datetime(2019, 2, 3, 12)
    t2 = Tranzactie('2', '2', '2', '3', y)
    tranzactie_repository.create(t2)
    y = datetime.datetime(2022, 4, 3, 12)
    t3 = Tranzactie('3', '4', '3', '5', y)
    tranzactie_repository.create(t3)
    y = datetime.datetime(2021, 7, 6, 12)
    t = Tranzactie('4', '1', '4', '2', y)
    tranzactie_repository.create(t)

    x = datetime.datetime(2020, 11, 11)
    c = CardClient('1', 'nume1', 'pren1', '5011', x, x)
    card_client_repository.create(c)
    c2 = CardClient('2', 'nume2', 'pren2', '5012', x, x)
    card_client_repository.create(c2)
    c3 = CardClient('3', 'nume3', 'pren3', '5013', x, x)
    card_client_repository.create(c3)
    c = CardClient('4', 'nume4', 'pren4', '5014', x, x)
    card_client_repository.create(c)
    c = CardClient('5', 'nume5', 'pren5', '11', x, x)
    card_client_repository.create(c)
    c = CardClient('6', 'nume6', 'pren6', '14', x, x)
    card_client_repository.create(c)
    c = CardClient('7', 'nume7', 'pren7', '5017', x, x)
    dict = ord.ordonare_medicamente()
    #print(dict)

    assert dict[m1] == 7
    assert dict[m4] == 5
    assert dict[m2] == 3

    lst_duble = ord.ordonare_card_client()
    assert lst_duble[0][0] == c2
    assert lst_duble[2][0] == c3





def teste_tranzactie_interval():
    undoredo_service = UndoRedoService()
    tranzactie_repository = FileRepository('test_ordonare_tranzactie.txt')
    tranzactie_interval = TranzactiiInterval(tranzactie_repository, undoredo_service)
    clear_file('test_ordonare_tranzactie.txt')

    y = datetime.datetime(2020, 11, 11, 12)
    t1 = Tranzactie('1', '1', '', '5', y)
    tranzactie_repository.create(t1)
    y = datetime.datetime(2019, 2, 3, 12)
    t2 = Tranzactie('2', '2', '2', '3', y)
    tranzactie_repository.create(t2)
    y = datetime.datetime(2022, 4, 3, 12)
    t3 = Tranzactie('3', '4', '3', '5', y)
    tranzactie_repository.create(t3)
    y = datetime.datetime(2021, 7, 6, 12)
    t = Tranzactie('4', '1', '4', '2', y)
    tranzactie_repository.create(t)
    d1 = datetime.datetime(2020, 1, 1, 12)
    d2 = datetime.datetime(2021, 12, 30, 12)
    result = tranzactie_interval.tranzactii_interval(d1, d2)

    assert result[0] == t1
    assert result[1] == t


    tranzactie_interval.stergere_tranzactii_din_interval(d1, d2)
    assert tranzactie_repository.get_all()[0] == t2
    assert tranzactie_repository.get_all()[1] == t3

def teste_scumpire_medicamente():
    undoredo_service = UndoRedoService()
    medicament_repository = FileRepository('test_ordonare_medicament.txt')
    clear_file('test_ordonare_medicament.txt')
    card_client_repository = FileRepository('test_ordonare_card_client.txt')

    clear_file('test_ordonare_card_client.txt')
    tranzactie_repository = FileRepository('test_ordonare_tranzactie.txt')
    tranzactie_validator = TranzactieValidator()
    clear_file('test_ordonare_tranzactie.txt')
    tranzactie_service = TranzactieService(tranzactie_validator, tranzactie_repository, medicament_repository,
                                           card_client_repository, undoredo_service)
    ord = OrdonareMedicamente(medicament_repository, tranzactie_repository, tranzactie_service, card_client_repository, undoredo_service)
    ord.scumpire_medicamente(10)
    for medicament in medicament_repository.get_all():
        print(medicament)


