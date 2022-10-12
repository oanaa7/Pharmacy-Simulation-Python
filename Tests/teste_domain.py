from Domain.medicament import Medicament


def test_medicament():

    m = Medicament('1', 'aaa', 'bbb', '1111', 'da')
    assert m.id_entity == '1'
    assert m.nume == 'aaa'
    assert m.producator == 'bbb'
    assert m.pret == '1111'
    assert m.necesita_reteta == 'da'
