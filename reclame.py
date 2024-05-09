from algemene_functies import mijn_functie_2
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer 
    

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return laagste, hoogste

def gemiddelde(mijn_lijst):
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)




    