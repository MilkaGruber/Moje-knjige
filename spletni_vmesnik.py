import bottle
from model import Model, Razdelek, Knjige

IME_DATOTEKE = "stanje.json"
try:
    model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    model = Model()

RAZDELEK1 = model.razdelki[0]  # RAZDELEK Zelim prebrati
RAZDELEK2 = model.razdelki[1]  # RAZDELEK V branju
RAZDELEK3 = model.razdelki[2]  # RAZDELEK Prebrane
RAZDELEK4 = model.razdelki[3]  # RAZDELEK Izhod

@bottle.get('/')
def osnovna_stran():
    return bottle.template(
        'osnovna_stran.tpl',
        st_knjig_sez_zelja=RAZDELEK1.stevilo_knjig_v_razdelku(),
        knjige_sez_zelja=RAZDELEK1.knjige,
        st_knjig_v_branju=RAZDELEK2.stevilo_knjig_v_razdelku(),
        knjige_v_branju=RAZDELEK2.knjige,
        st_knjig_prebrano=RAZDELEK3.stevilo_knjig_v_razdelku(),
        prebrane_knjige=RAZDELEK3.knjige
    )

@bottle.post('/dodaj/')
def dodaj_knjigo():
    naslov = bottle.request.forms.getunicode("naslov")
    avtor = bottle.request.forms.getunicode("avtor")
    st_strani = bottle.request.forms.getunicode("st_strani")
    knjiga = Knjige(naslov, avtor, st_strani)
    RAZDELEK1.dodaj_knjigo(knjiga)
    model.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect('/')

bottle.run(debug=True, reloader=True) #poženemo strežnik