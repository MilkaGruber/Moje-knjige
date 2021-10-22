from model import Model, Razdelek, Knjige

model = Model()

ZAMENJAJ_RAZDELEK = 1
DODAJ_KNJIGO = 2
POBRISI_KNJIGO = 3
ZACNI_BRATI_KNJIGO = 4
PREBERI_KNJIGO = 5
PREBERI_STRANI = 6


ZELIM_PREBRATI = Razdelek('ZELIM PREBRATI')
V_BRANJU = Razdelek('V BRANJU')
PREBRANE = Razdelek('PREBRANA')
IZHOD = Razdelek('IZHOD')

moznosti_prvic = [(DODAJ_KNJIGO, 'dodaj knjigo v razdelek'), 
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(ZACNI_BRATI_KNJIGO, 'začni brati knjigo'),
(ZAMENJAJ_RAZDELEK, 'Pojdi na drug razdelek'),
(PREBERI_KNJIGO, 'preberi celo knjigo')]

moznosti_drugic = [(PREBERI_STRANI, 'zabeleži koliko strani si prebral'),
(PREBERI_KNJIGO, 'preberi celo knjigo'),
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(ZAMENJAJ_RAZDELEK, 'Pojdi na drug razdelek')]

moznosti_tretjic = [(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(ZAMENJAJ_RAZDELEK, 'Pojdi na drug razdelek')]

razdelki = [(ZELIM_PREBRATI , 'seznam knjig, ki jih želim prebrati'), 
(V_BRANJU, 'knjige, ki jih trenutno berem'), 
(PREBRANE, 'seznam že prebranih knjig'),
(IZHOD, 'izhod iz programa')]


def prazen_razdelek(razdelek):
    return razdelek.stevilo_knjig_v_razdelku() == 0

def izberi_moznost(moznosti):
    for i in range(len(moznosti)):
        print(f"{i + 1} {moznosti[i][1]}")
    while True:
        vnos_stevila = input('> ')
        try:
            int(vnos_stevila)
            if 1 <= int(vnos_stevila) <= len(moznosti):
                return moznosti[int(vnos_stevila) - 1][0]
        except ValueError:
            print(f'Vnesti morate celo število med 1 in {len(moznosti)}')

def izberi_knjigo(sez_knjig):
    for i in range(len(sez_knjig)):
        print(f"{i + 1} {sez_knjig[i]}")
    while True:
        vnos_stevila = input('> ')
        try:
            int(vnos_stevila)
            if 1 <= int(vnos_stevila) <= len(sez_knjig):
                return sez_knjig[int(vnos_stevila) - 1]
        except ValueError:
            print(f'Vnesti morate celo število med 1 in {len(sez_knjig)}')

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    zamenjaj_razdelek()
    while True:
        if model.aktualni_razdelek == ZELIM_PREBRATI:
            predstavitev_aktualnega_razdelka()
            drugi_ukaz = izberi_moznost(moznosti_prvic)
            if drugi_ukaz == DODAJ_KNJIGO:
                dodaj_knjigo()
            elif drugi_ukaz == POBRISI_KNJIGO:
                pobrisi_knjigo_z_razdelka()
            elif drugi_ukaz == ZACNI_BRATI_KNJIGO:
                zacni_brati_knjigo()
            elif drugi_ukaz == ZAMENJAJ_RAZDELEK:
                zamenjaj_razdelek()
            elif drugi_ukaz == PREBERI_KNJIGO:
                preberi_knjigo()
        elif model.aktualni_razdelek == V_BRANJU:
            predstavitev_aktualnega_razdelka()
            tretji_ukaz = izberi_moznost(moznosti_drugic)
            if tretji_ukaz == PREBERI_STRANI:
                preberi_strani()
            elif tretji_ukaz == PREBERI_KNJIGO:
                preberi_knjigo()
            elif tretji_ukaz == POBRISI_KNJIGO:
                pobrisi_knjigo_z_razdelka()
            elif tretji_ukaz == ZAMENJAJ_RAZDELEK:
                zamenjaj_razdelek()
        elif model.aktualni_razdelek == PREBRANE:
            predstavitev_aktualnega_razdelka()
            cetrti_ukaz = izberi_moznost(moznosti_tretjic)
            if cetrti_ukaz == ZAMENJAJ_RAZDELEK:
                zamenjaj_razdelek()
            elif cetrti_ukaz == POBRISI_KNJIGO:
                pobrisi_knjigo_z_razdelka()
                cetrti_ukaz
        elif model.aktualni_razdelek == IZHOD:
            break

def prikazi_pozdravno_sporocilo(): #DELA 
    print('Pozdravljeni v programu Moje knjige')

def predstavitev_aktualnega_razdelka():  #DELA 
    if model.aktualni_razdelek.stevilo_knjig_v_razdelku() == 0:
        print(f'Ste na razdelku: {model.aktualni_razdelek.ime}')
        print('V tem razdelku ni vnešene nobene knjige.') 
    else:
        print(f'{model.aktualni_razdelek.ime}: ' + model.aktualni_razdelek.naslovi_knjig_v_razdelku())

def predstavitev_vseh_razdelkov():
    print('V BRANJU: ' + V_BRANJU.naslovi_knjig_v_razdelku() + '\n' + 'ZELIM PREBRATI: ' + ZELIM_PREBRATI.naslovi_knjig_v_razdelku() + '\n' +'PREBRANE: ' + PREBRANE.naslovi_knjig_v_razdelku())

def zamenjaj_razdelek(): #DELA 
    print("Izberite željen razdelek")
    razdelek = izberi_moznost(razdelki)
    model.zamenjaj_razdelek(razdelek)

def dodaj_knjigo(): #DELA 
    """Na aktualni razdelek doda knjigo."""
    print('Vnesite naslednje podatke o knjigi: naslov, avtor, število strani.')
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    strani = input('Število strani> ')
    model.aktualni_razdelek.dodaj_knjige(Knjige(naslov, avtor, strani))
    
def pobrisi_knjigo_z_razdelka(): #DELA 
    """Na razdelku izberemo knjigo in jo zbrišemo."""
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        (model.aktualni_razdelek.knjige).remove(knjiga)

def zacni_brati_knjigo(): 
    """Prestavi knjigo iz razdelka ZELIM_PREBRATI na razdelek V_BRANJU"""
    if ZELIM_PREBRATI.stevilo_knjig_v_razdelku() == 0:
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(ZELIM_PREBRATI.knjige)
        V_BRANJU.knjige.append(knjiga)
        ZELIM_PREBRATI.knjige.remove(knjiga)
       
def preberi_strani():
    if prazen_razdelek(V_BRANJU):
        print('Ta razdelek je prazen, najprej dodajte knjigo!')
    else:
        print('Izberite knjigo, katero ste brali in vnesite število prebranih strani')
        knjiga = izberi_knjigo(V_BRANJU.knjige)
        n = input('število prebranih strani> ')
        try:
            if int(n) == n:
                knjiga.preberi_n_strani(n)
        except ValueError:
            print('Neveljaven vnos! Prosim vnesite celo število.')

def preberi_knjigo():
    """Prestavi knjigo iz razdelka V_BRANJU na razdelek PREBRANO, spremeni atribute knjige"""
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        PREBRANE.dodaj_knjige(knjiga)
        model.aktualni_razdelek.knjige.remove(knjiga)

tekstovni_vmesnik()





