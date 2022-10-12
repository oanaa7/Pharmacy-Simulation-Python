class TranzactieValidator:
    def validate(self, tranzactie):
        erori = []
        if tranzactie.nr_bucati.isdigit() == False:
            erori.append('Numarul bucatilor este introdus gresit!')
        if len(erori) > 0:
            raise ValueError(erori)