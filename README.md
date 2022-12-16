# Unit testing!
I denne oppgaven skal du skrive unittests for å avdekke og korrigere feil i funksjoner som du finner i `src/main.py`! En unittest er en metode for å teste om en funksjon oppfører seg som den skal. I motsetning til brukertesting, krever en unittest ingen menneskelig input. La maskinen gjøre jobben for deg!

Merk at du skal kun teste funksjonene `multiply_numbers`, `sum_3_nums`, `purchase` og `sell`, ikke selve programmet (alt under `if __name__ == "__main__":`).

Start med å kjøre koden i `src/main.py` for å se hva den gjør (den kommer til å feile!). Deretter navigerer du deg til `tests/test_main.py` og leser gjennom. Skriv tester der du sammenligner resultatet av funksjonen med det du forventer at den skal returnere. Du kan bruke `assert` for å sammenligne to verdier. Noen tester ligger der allerede. For eksempel:

```python
assert 2+2 == 4
assert sum_3_nums(1, 2, 3) == 6
assert sum_3_nums('1', '2', '3') == 6
```

Men du må også huske tilfeller der brukeren gjør feil!
```python
assert sum_3_nums('a', 'b', 'c') == ???  # hva skjer her?
```

Du kan kjøre testene ved å kjøre `pytest` i terminalen, eller ved å trykke på `Run`-knappen på testen i PyCharm.

> **OBS:** Oppgaven retter seg selv, sjekk at du får en grønn checkmark på GitHub for å se at du har løst oppgaven riktig.
> Merk at du må også korrigere feilene i `src/main.py` for at oppgaven skal bli godkjent, slik at testene ikke feiler.
> 
> Du må ha testet alle funksjonene i `src/main.py` for at oppgaven skal bli godkjent. Dette kalles for 100% code coverage (Minst èn test for alle funksjoner). Du kan se hvor mye code coverage du har ved å høyreklikke `tests`-mappen og velge More Run/Debug` og velge `Run ... with Coverage`. (Eller ved at GitHub godkjenner oppgaven din.)

## Eksempel på testing
Hvis en funksjon forventer 2 tall, og du gir den 2 bokstaver, så er det ikke sikkert at funksjonen vil fungere som forventet. Da må du skrive en test som tester dette scenariet.

## Var noe vanskelig å forstå? Fant du ut av det selv?
[Skriv dine tanker her]

## Nevn noen grunner om hvorfor det kan være viktig å teste kode!
[Skriv noen grunner her]