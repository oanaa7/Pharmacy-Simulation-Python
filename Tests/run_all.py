from Tests.teste_domain import test_medicament
from Tests.teste_operatiuni import teste_ordonare, teste_tranzactie_interval
from Tests.teste_repository import test_file_repository
from Tests.teste_service import test_service


def teste():
    test_medicament()
    test_file_repository()
    test_service()
    teste_ordonare()
    teste_tranzactie_interval()