"""
Kan du fikse denne appen?
Den fungerer ikke som den skal, og det er din jobb å fikse den.

Bruk pytest for å opprette tester som tester funksjonene i main.py
Målet er å få 100% dekning av koden i main.py ved å skrive tester,
det kan hende testene gir deg noen hints om hva som er feil.
"""


def multiply_numbers(a, b):
    """
    Multipliserer to tall og returnerer resultatet
    """
    total = a * b
    return total


def sum_3_nums(a, b, c):
    """
    Summerer tre tall og returnerer resultatet
    """
    total = a + b + c
    return total


def purchase(price, wallet):
    """
    Kjøp noe for en viss sum penger, og returner den nye lommebok-verdien
    Eksempel: purchase(100, 200) -> 100
              purchase(99, 100) -> 1
    """
    new_wallet = wallet - price
    return new_wallet


def sell(price, wallet):
    """
    Selg noe for en viss sum penger, og returner den nye lommebok-verdien
    Eksempel: sell(100, 200) -> 300
              sell(99, 100) -> 199
    """
    new_wallet = wallet + price
    return new_wallet


# __Hovedprogrammet__
# Denne funksjonen skal ikke endres, bare kjøres. Sørg for at den kjører uten feil.
if __name__ == '__main__':  # pragma: no cover
    """# pragma: no cover sier at denne koden ikke skal dekkes av tester"""
    while True:
        print('Velkommen til appen min!')
        print('1. Multipliser to tall')
        print('2. Summer 3 tall')
        print('3. Kjøp noe')
        print('4. Selg noe')
        print('Q. Avslutt')
        command = input('Skriv inn en kommando: ')
        if command == '1':
            print('Du valgte å multiplisere to tall')
            tall1 = input('Skriv inn et tall: ')
            tall2 = input('Skriv inn et annet tall: ')
            total = multiply_numbers(tall1, tall2)
            print(f'Total: {total}')
        elif command == '2':
            print('Du valgte å summere 3 tall')
            tall1 = input('Tall 1: ')
            tall2 = input('Tall 2: ')
            tall3 = input('Tall 3: ')
            total = sum_3_nums(tall1, tall2, tall3)
            print(f'Total: {total}')
        elif command == '3':
            print('Du valgte å kjøpe noe')
            pris = input('Hva koster varen? ')
            lommebok = input('Hvor mye penger har du? ')
            rest = purchase(pris, lommebok)
            print(f'Du har {rest} igjen')
        elif command == '4':
            print('Du valgte å selge noe')
            pris = input('Hva koster varen? ')
            lommebok = input('Hvor mye penger er det i lommeboken din? ')
            rest = sell(pris, lommebok)
            print(f'Du har nå {rest} i lommeboken')
        elif command.lower() == 'q':
            print('Ha en fin dag!')
            break