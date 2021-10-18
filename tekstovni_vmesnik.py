from model import Model, Razdelek, Knjige

stanje = Model()

ZAMENJAJ_RAZDELEK = 1
DODAJ_KNJIGO = 2
POBRISI_KNJIGO = 3
PREBERI_STRANI = 4
PREBERI_KNJIGO = 5
IZHOD = 6

def ali_je_celo_stevilo():
    while True:
        vnos = input('-->')
        if int(vnos) == vnos:
            pass
        else:
            print('Prosim vnesite celo število.')

def tekstovni_vmesnik():
    #funkcija za prikaz osnvnega sporočila
    #naredim zanko while True
    #izberi ukaz
    #našteti if stavki, če ukaz == zgoraj določen ukaz, potem se izvvede funkcija

#tukaj moram definirati zgoraj zapisane ukaze npr.:

