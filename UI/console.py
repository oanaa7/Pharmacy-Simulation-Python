import datetime

from Domain.card_client_validator import CardClientValidator
from Domain.exceptie import Exceptie
from Domain.medicament_validator import MedicamentValidator
from Domain.tranzactie_validator import TranzactieValidator
from Service.card_client_service import CardClientService
from Service.cautare import Cautare
from Service.medicament_service import MedicamentService
from Service.ordonare_medicamente import OrdonareMedicamente
from Service.populate_entities import PopulateEntities
from Service.tranzactie_service import TranzactieService
from Service.tranzactii_interval import TranzactiiInterval
from Service.undo_redo_service import UndoRedoService


class Console:
    def __init__(self, medicament_validator: MedicamentValidator, medicament_service: MedicamentService,
                card_client_validator: CardClientValidator, card_client_service: CardClientService,
                tranzactie_validator: TranzactieValidator,
                tranzactie_service: TranzactieService,
                ordonare_medicamente: OrdonareMedicamente, popoulate_entities: PopulateEntities,
                tranzactii_interval: TranzactiiInterval,
                cautare: Cautare, undo_redo_service: UndoRedoService):
        self.medicament_service = medicament_service
        self.card_client_service = card_client_service
        self.medicament_validator = medicament_validator
        self.card_client_validator = card_client_validator
        self.tranzactie_service = tranzactie_service
        self.tranzactie_validator = tranzactie_validator
        self.ordonare_medicamente = ordonare_medicamente
        self.popoulate_entities = popoulate_entities
        self.tranzactii_interval = tranzactii_interval
        self.cautare = cautare
        self.undo_redo_service = undo_redo_service

    def print_meniu(self):
        print('1. CRUD Medicamente')
        print('2. CRUD Carduri clienti')
        print('3. CRUD Tranzactii')
        print('4. Operatiuni')
        print('5. Undo')
        print('6. Redo')
        print('x. Iesire')

    def run_crud_tranzactie(self):
        while True:
            print('1. Adaugare tranzactie')
            print('2. Stergere tranzactie')
            print('3. Update tranzactie')
            print('a. Afisare tranzactii')
            print('b. Back')
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.handle_adaugare_tranzactie()
            elif op == '2':
                self.handle_delete_tranzactie()
            elif op == '3':
                self.handle_update_tranzactie()
            elif op == 'b':
                break
            elif op == 'a':
                self.handle_afisare_tranzactie()
            else:
                print('Comanda gresita!')

    def run_crud_medicament(self):
        while True:
            print('1. Adaugare medicament')
            print('2. Stergere medicament')
            print('3. Update medicament')
            print('a. Afisare medicamente')
            print('b. Back')
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.handle_adaugare_medicament()

            elif op == '2':
                self.handle_stergere_medicament()
            elif op == '3':
                self.handle_update_medicament()
            elif op == 'b':
                break
            elif op == 'a':
                self.handle_afisare_medicament()
            else:
                print('Comanda gresita!')

    def run_crud_card_client(self):
        while True:
            print('1. Adaugare card client')
            print('2. Stergere card client')
            print('3. Update card client')
            print('a. Afisare carduri client')
            print('b. Back')
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.handle_adaugare_card_client()
            elif op == '2':
                self.handle_delete_card_client()
            elif op == '3':
                self.handle_update_card_client()
            elif op == 'a':
                self.handle_afisare_card_client()
            elif op == 'b':
                break
            else:
                print('Comanda gresita!')



    def run_console(self):
        while True:
            self.print_meniu()
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.run_crud_medicament()
            elif op == '2':
                self.run_crud_card_client()
            elif op == '3':
                self.run_crud_tranzactie()
            elif op == '4':
                self.run_operatiuni()
            elif op == '5':
                self.undo_redo_service.do_undo()
                print('Undo-ul a fost realizat!')
            elif op == '6':
                self.undo_redo_service.do_redo()
                print('Redo-ul a fost realizat!')
            elif op == 'x':
                break
            else:
                print('Comanda gresita!')

    def handle_adaugare_medicament(self):
        try:
            id_medicament = input('Introdu id-ul: ')
            nume = input('Introdu numele: ')
            producator = input('Introdu producatorul: ')
            pret = input('Introdu pretul: ')
            necesita_reteta = input('Necesita reteta? da/nu: ')
            self.medicament_service.create(id_medicament, nume, producator, pret, necesita_reteta)
            print('Medicamentul a fost adaugat!')
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def handle_afisare_medicament(self):
        for medicament in self.medicament_service.get_all():
            print(medicament)

    def handle_stergere_medicament(self):
        try:
            id_medicament = input('Introdu id-ul pentru stergere: ')
            self.medicament_service.delete(id_medicament)
            print('Stergerea s-a efectuat!')
        except KeyError as e:
            print(e)

    def handle_update_medicament(self):
        try:
            id_medicament = input('Introdu id-ul pentru modificare: ')
            nume = input('Introdu numele sau gol pt. a nu se schimba: ')
            producator = input('Introdu producatorul sau gol pt. a nu se schimba: ')
            pret = input('Introdu pretul sau gol pt. a nu se schimba: ')
            necesita_reteta = input('Necesita reteta? da/nu sau gol pt. a nu se schimba: ')
            self.medicament_service.update(id_medicament, nume, producator, pret, necesita_reteta)
            print('Medicamentul a fost updatat!')
        except KeyError as e:
            print(e)

    def handle_adaugare_card_client(self):
        try:
            id_client = input('Introdu id-ul: ')
            nume = input('Introdu numele: ')
            prenume = input('Introdu prenumele: ')
            cnp = input('Introdu cnp-ul: ')
            dd = int(input('Introdu dd: '))
            mm = int(input('Introdu mm: '))
            yyyy = int(input('Introdu yyyy: '))
            data_nasterii = datetime.datetime(yyyy, mm, dd)
            dd = int(input('Introdu dd: '))
            mm = int(input('Introdu mm: '))
            yyyy = int(input('Introdu yyyy: '))
            data_inregistrarii = datetime.datetime(yyyy, mm, dd)
            self.card_client_service.create(id_client, nume, prenume, cnp, data_nasterii, data_inregistrarii)
            print('Cardul a fost adaugat!')
        except Exceptie as e:
            print(e)
        except Exception as e:
            print(e)

    def handle_delete_card_client(self):
        try:
            id_card_client = input('Introdu id-ul pentru stergere: ')
            self.card_client_service.delete(id_card_client)
            print('Cardul a fost sters!')
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)

    def handle_update_card_client(self):
        try:
            id_client = input('Introdu id-ul pentru modificare: ')
            nume = input('Introdu numele sau gol pt. a nu se schimba: ')
            prenume = input('Introdu prenumele sau gol pt. a nu se schimba: ')
            cnp = input('Introdu cnp-ul sau gol pt. a nu se schimba: ')
            #print('Pentru a nu se modifica data introdu ziua = 1, luna = 1 si anul = 1')

            dd = input('Introdu ziua: ')
            if dd == '':
                dd = self.card_client_service.find_by_id(id_client).data_nasterii.day
            mm = input('Introdu luna: ')
            if mm == '':
                mm = self.card_client_service.find_by_id(id_client).data_nasterii.month
            yyyy = input('Introdu anul: ')
            if yyyy == '':
                yyyy = self.card_client_service.find_by_id(id_client).data_nasterii.year
            data_nasterii = datetime.datetime(int(yyyy), int(mm), int(dd))

            dd = input('Introdu ziua: ')
            if dd == '':
                dd = self.card_client_service.find_by_id(id_client).data_nasterii.day
            mm = input('Introdu luna: ')
            if mm == '':
                mm = self.card_client_service.find_by_id(id_client).data_nasterii.month
            yyyy = input('Introdu anul: ')
            if yyyy == '':
                yyyy = self.card_client_service.find_by_id(id_client).data_nasterii.year

            data_inregistrarii = datetime.datetime(int(yyyy), int(mm), int(dd))
            self.card_client_service.update(id_client, nume, prenume, cnp, data_nasterii, data_inregistrarii)
            print('Cardul a fost updatat!')
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)

    def handle_afisare_card_client(self):
        for card_client in self.card_client_service.get_all():
            print(card_client)
    def handle_delete_tranzactie(self):
        try:
            id_tranzactie = input('Introdu id-ul pentru stergere: ')
            self.tranzactie_service.delete(id_tranzactie)
            print('Tranzactia a fost sters!')
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
    def handle_adaugare_tranzactie(self):
        try:
            id_tranzactie = input('Introdu id-ul: ')
            id_medicament = input('Introdu id medicament: ')
            id_card_client = input('Introdu id card client: ')
            nr_bucati = input('Introdu nr bucati: ')
            dd = int(input('Introdu ziua: '))
            mm = int(input('Introdu luna: '))
            yyyy = int(input('Introdu anul: '))
            ora = int(input('Introdu ora: '))

            data = datetime.datetime(yyyy, mm, dd, ora)
            self.tranzactie_service.create(id_tranzactie, id_medicament, id_card_client, nr_bucati, data)
            print('Tranzactia a fost adaugata!')
            lst = self.tranzactie_service.get_pret(self.tranzactie_service.find_by_id(id_tranzactie))
            print(f'Pretul e: {lst[0]}')
            if lst[1] == True:
                print('S-a aplicat o reducere de 15%!')
            elif lst[2] == True:
                print('S-a aplicat o reducere de 10%!')
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
    def handle_update_tranzactie(self):
        try:
            id_tranzactie = input('Introdu id-ul tranzactie: ')
            id_medicament = input('Introdu id medicament sau gol pt. a nu se schimba: ')
            id_card_client = input('Introdu id card client sau gol pt. a nu se schimba: ')
            nr_bucati = input('Introdu nr bucati sau gol pt. a nu se schimba: ')

            dd = input('Introdu ziua: ')
            if dd == '':
                dd = self.tranzactie_service.find_by_id(id_tranzactie).data.day
            mm = input('Introdu luna: ')
            if mm == '':
                mm = self.tranzactie_service.find_by_id(id_tranzactie).data.month
            yyyy = input('Introdu anul: ')
            if yyyy == '':
                yyyy = self.tranzactie_service.find_by_id(id_tranzactie).data.year
            ora = input('Introdu ora: ')
            if ora == '':
                ora = self.tranzactie_service.find_by_id(id_tranzactie).data.hour
            data = datetime.datetime(int(yyyy), int(mm), int(dd), int(ora))

            self.tranzactie_service.update(id_tranzactie, id_medicament, id_card_client, nr_bucati, data)
            print('Tranzactia a fost modificata!')
            lst = self.tranzactie_service.get_pret(self.tranzactie_service.find_by_id(id_tranzactie))
            print(f'Pretul e: {lst[0]}')
            if lst[1] == True:
                print('S-a aplicat o reducere de 15%!')
            elif lst[2] == True:
                print('S-a aplicat o reducere de 10%!')
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)
    def handle_afisare_tranzactie(self):
        for tranzactie in self.tranzactie_service.get_all():
            print(tranzactie)

    def run_operatiuni(self):
        while True:
            print('1. Ordonare- medicamente')
            print('2. Random')
            print('3. Afișarea tuturor tranzacțiilor dintr-un interval de zile dat')
            print('4. Ștergerea tuturor tranzacțiilor dintr-un anumit interval de zile')
            print('5. Ordonare carduri client')
            print('6. Scumpirea cu un procentaj dat a tuturor medicamentelor cu prețul mai mic decât o valoare data')
            print('7. Cautare')
            print('8. Export')
            print('b. Back')
            op = input('Introdu optiunea: ')
            if op == '1':
                dict = self.ordonare_medicamente.ordonare_medicamente()

                for a in dict:
                    print(f'{a}, nr_bucati = {dict[a]}')
                    #print(a)
            elif op == '2':
                try:
                    n = int(input('Citeste nr medicamentelor: '))
                    self.popoulate_entities.populate_entities(n)
                except ValueError as e:
                    print(e)
            elif op == '3':
                try:
                    dd = int(input('Introdu ziua 1: '))
                    mm = int(input('Introdu luna 1: '))
                    yyyy = int(input('Introdu anul 1: '))
                    d1 = datetime.datetime(yyyy, mm, dd)
                    dd = int(input('Introdu ziua 2: '))
                    mm = int(input('Introdu luna 2: '))
                    yyyy = int(input('Introdu anul 2: '))
                    d2 = datetime.datetime(yyyy, mm, dd)
                    result = self.tranzactii_interval.tranzactii_interval(d1, d2)
                    for tranzactie in result:
                        print(tranzactie)
                except ValueError as e:
                    print(e)
            elif op == '4':
                try:
                    dd = int(input('Introdu ziua 1: '))
                    mm = int(input('Introdu luna 1: '))
                    yyyy = int(input('Introdu anul 1: '))
                    d1 = datetime.datetime(yyyy, mm, dd)
                    dd = int(input('Introdu ziua 2: '))
                    mm = int(input('Introdu luna 2: '))
                    yyyy = int(input('Introdu anul 2: '))
                    d2 = datetime.datetime(yyyy, mm, dd)
                    self.tranzactii_interval.stergere_tranzactii_din_interval(d1, d2)
                    #self.tranzactii_interval.stergere_tranzactii_din_interval_2(self.tranzactie_service.get_all(), d1, d2, [])
                    print('Stergerea a fost efectuata')
                except ValueError as e:
                    print(e)
            elif op == '5':
                lst_duble = self.ordonare_medicamente.ordonare_card_client()
                for (key, item) in lst_duble:
                    print(key, ', valoarea reducerilor = ', item)
            elif op == '6':
                try:
                    value = float(input('Introdu valoarea: '))
                    self.ordonare_medicamente.scumpire_medicamente(value)
                    print('Scumpirea s-a efectuat!')
                except ValueError as e:
                    print(e)
            elif op == '7':
                string = input('Introdu string-ul: ')
                self.cautare.cautare(string)

            elif op == '8':
                self.medicament_service.export()
                print('Exportul s-a efectuat!')
            elif op == 'b':
                break