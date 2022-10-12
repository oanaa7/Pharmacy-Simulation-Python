
from Domain.card_client_validator import CardClientValidator
from Domain.medicament import Medicament
from Domain.medicament_validator import MedicamentValidator
from Domain.tranzactie import Tranzactie
from Domain.tranzactie_validator import TranzactieValidator
from Repository.repository import FileRepository
from Service.card_client_service import CardClientService
from Service.cautare import Cautare
from Service.medicament_service import MedicamentService
from Service.ordonare_medicamente import OrdonareMedicamente
from Service.populate_entities import PopulateEntities
from Service.tranzactie_service import TranzactieService
from Service.tranzactii_interval import TranzactiiInterval
from Service.undo_redo_service import UndoRedoService
from Tests.run_all import teste
from UI.console import Console
import datetime

def main():
    medicament_repository = FileRepository('medicament.txt')
    card_client_repository = FileRepository('card_client.txt')
    tranzactie_repository = FileRepository('tranzactie.txt')
    undo_redo_service = UndoRedoService()

    medicament_validator = MedicamentValidator()
    card_client_validator = CardClientValidator()
    tranzactie_validator = TranzactieValidator()

    medicament_service = MedicamentService(medicament_validator, medicament_repository, undo_redo_service)
    card_client_service = CardClientService(card_client_validator, card_client_repository, undo_redo_service)
    tranzactie_service = TranzactieService(tranzactie_validator, tranzactie_repository, medicament_repository,
                                           card_client_repository, undo_redo_service)
    x = datetime.datetime(1111, 11, 11)
    y = datetime.datetime(1111, 11, 11, 12)


    ordonare_medicamente = OrdonareMedicamente(medicament_repository, tranzactie_repository,
                                               tranzactie_service, card_client_repository, undo_redo_service)
    tranzactie_interval = TranzactiiInterval(tranzactie_repository, undo_redo_service)
    populate_entities = PopulateEntities(medicament_repository, medicament_validator, undo_redo_service)
    cautare = Cautare(medicament_repository, card_client_repository)



    console = Console(medicament_validator, medicament_service, card_client_validator, card_client_service,
                      tranzactie_validator, tranzactie_service, ordonare_medicamente, populate_entities,
                      tranzactie_interval, cautare, undo_redo_service)


    x = datetime.datetime(1111, 11, 11)
    #card_client_service.create('1', 'nume1', 'pren1', '5011', x , x)

    y = datetime.datetime(1111, 11, 11, 12)
    #tranzactie_service.create('1', '1', '', '5', y)
    console.run_console()
#teste()
main()