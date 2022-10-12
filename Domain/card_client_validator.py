from Domain.card_client import CardClient


class CardClientValidator:
    def validate(self, card_client: CardClient):
        erori = []
        '''
        data_nasterii = card_client.data_nasterii
        if len(data_nasterii) != 10:
            erori.append('Data nasterii introdusa gresit!')
        elif data_nasterii[2] != '.' or data_nasterii[5] != '.' or data_nasterii[0:2].isdigit() == False or data_nasterii[3:5].isdigit() == False or data_nasterii[6:10].isdigit() == False:
            erori.append('Data nasterii introdusa gresit!')

        data_inregistrarii = card_client.data_inregistrarii
        if len(data_inregistrarii) != 10:
            erori.append('Data inregistrarii introdusa gresit!')
        elif data_inregistrarii[2] != '.' or data_inregistrarii[5] != '.' or data_inregistrarii[0:2].isdigit() == False or data_inregistrarii[3:5].isdigit() == False or data_inregistrarii[6:10].isdigit() == False:
            erori.append('Data inregistrarii introdusa gresit!')
        '''
        if len(erori) > 0:
            raise ValueError(erori)


