"""
=====================
Oppgave, Unit testing
=====================
Skriv tester for funksjonene i main.py, og få 100% dekning av koden.
Du må skrive tester for alle funksjonene i main.py, og avdekke feilene i koden.
Se under for eksempler på tester, du må sørge for at testene sjekker alle mulige tilfeller.

Det er viktig å ta høyde for rare input verdier, og at koden ikke krasjer når den får ugyldige verdier.
(F.eks. hva skjer om du tar input('Tall 1: ') og brukeren skriver 'hei' eller 'quit' i stedet for et tall?)

Tips:
- Bruk PyCharm sin innebygde test runner
- Kjør testene med "Run" i PyCharm

For å opprette en test:
- Lag en ny funksjon som starter med "test_"
- Skriv en assert som sjekker at koden din fungerer som den skal (f.eks. assert multiply_numbers(2, 3) == 6)
"""
import os, sys, pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import *


# Eksempel på en test
def test_sum_3_nums():
    # Sjekk at sum_3_nums kan summere tall
    assert sum_3_nums('1', '2', '3') == 6

    # Sjekk at sum_3_nums kan summere tall med desimaler
    assert sum_3_nums('1.1', '2.0', '3.0') == 6.1

    # Osv...


def test_multiply_numbers():
    # Her må du skrive egne tester!
    assert 2 * 2 == 4


def test_purchase():
    # Her må du skrive egne tester!
    assert 100 - 50 == 50


def test_sell():
    # Her må du skrive egne tester!
    assert 100 + 50 == 150


# Avansert testing med Exception handling
# =======================================
@pytest.mark.skip
def test_sum_3_nums_avansert():
    """
    Denne type testing er mer avansert å korrigere, så den er ikke obligatorisk.
    Du kan fikse og teste for denne type feil hvis du vil ha en ekstra utfordring. (fjern @pytest.mark.skip)
    """
    # Sjekk at sum_3_nums kaster en TypeError hvis den får inn bokstaver
    # (Tips: sum_3_nums må inneholde koden "raise TypeError('Melding')")
    with pytest.raises(TypeError):
        sum_3_nums('a', 'b', 'c')
