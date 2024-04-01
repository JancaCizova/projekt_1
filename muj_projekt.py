print("projekt_1.py: první projekt do Engeto Online Python Akademie")
print("author: Jana Čížová")
print("email: janca.cizova@seznam.cz")
print("discord: Janča Č. - janca_15997")

uzivatele = {'bob': '123', 'ann': 'pass123',  'mike': 'password123','liz': 'pass123'}

texty = [ '''Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.''']

def prihlaseni():
    while True:
        jmeno = input("Zadejte uživatelské jméno: ")
        heslo = input("Zadejte heslo: ")
        if jmeno in uzivatele and uzivatele[jmeno] == heslo:
            print(f"Vítejte v aplikaci, {jmeno}!")
            return True
        else:
            print("Chybné uživatelské jméno nebo heslo!")
            return False
def analyzuj_text(text):
    slova = text.split()
    pocet_slov = len(slova)
    pocet_slov_velka_prvni = sum(1 for slovo in slova if slovo.istitle())
    pocet_slov_velka = sum(1 for slovo in slova if slovo.isupper())
    pocet_slov_mala = sum(1 for slovo in slova if slovo.islower())
    cisla = [slovo.strip(".,!?") for slovo in slova if slovo.isdigit()]
    pocet_cisel = len(cisla)
    soucet_cisel = sum(int(cislo) for cislo in cisla)
    delky_slov = {}
    for slovo in slova:
        delka = len(slovo.strip(".,!?"))
        delky_slov[delka] = delky_slov.get(delka, 0) + 1

    return { "pocet_slov": pocet_slov,
        "pocet_slov_velka_prvni": pocet_slov_velka_prvni,
        "pocet_slov_velka": pocet_slov_velka,
        "pocet_slov_mala": pocet_slov_mala,
        "pocet_cisel": pocet_cisel,
        "soucet_cisel": soucet_cisel,
        "delky_slov": delky_slov}

def tisk_statistik(statistiky):
    print(f"Ve vybraném textu je {statistiky['pocet_slov']} slov.")
    print(f"Z toho je {statistiky['pocet_slov_velka_prvni']} slov začínajících velkým písmenem.")
    print(f"Z toho je {statistiky['pocet_slov_velka']} slov napsaných velkými písmeny.")
    print(f"Z toho je {statistiky['pocet_slov_mala']} slov napsaných malými písmeny.")
    print(f"V textu je celkem {statistiky['pocet_cisel']} čísel.")
    print(f"Celkový součet všech čísel je {statistiky['soucet_cisel']}.")
    print("DÉLKA| VÝSKYT")
    print("----------------------------------------")
    for delka, vyskyt in statistiky['delky_slov'].items():
        print(f"{delka:5}| {'*' * vyskyt}")

def hlavni():
    if prihlaseni():
        print(f"K dispozici máme {len(texty)} textů k analýze.")
        while True:
            try:
                vyber = int(input("Zadejte číslo od 1 do 3 pro výběr textu: "))
                if 1 <= vyber <= len(texty):
                    break
                else:
                    print("Zadejte prosím číslo od 1 do 3.")
            except ValueError:
                print("Zadejte prosím platné číslo.")

        vybrany_text = texty[vyber - 1]
        statistiky = analyzuj_text(vybrany_text)
        tisk_statistik(statistiky)

if __name__ == "__main__":
    hlavni()
