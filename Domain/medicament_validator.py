class MedicamentValidator:
    def validate(self, medicament):
        erori = []
        if medicament.necesita_reteta != 'da' and medicament.necesita_reteta != 'nu':
            erori.append('necesita_reteta introdusa gresit!')

        for i in medicament.pret:
            if i.isdigit() == False and i != '.':
                erori.append('pretul introdus gresit!')
                break
        if len(erori) > 0:
            raise ValueError(erori)