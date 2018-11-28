import pytest


class NoEnoughMoney(ValueError):
    pass


class AmountNotDividedbyten(ValueError):
    pass


class CountofNotes(ValueError):
    pass


class CashMachine:
    def __init__(self):
        self._banknoty = []

    @property
    def is_available(self):
        if self._banknoty:
            return True
        return False

    def put_money(self, banknoty):
        if len(banknoty)+len(self._banknoty)>10:
            raise CountofNotes("BŁĄD: Liczba wplacanych banknotow nie powinna byc wieksza niz 10")
        self._banknoty.extend(banknoty)


    def withdraw_money(self, to_withdraw):

        if to_withdraw % 10 != 0:
            raise AmountNotDividedbyten("BLAD: Kwota powinna być wielokrotnoscia 10")

        zabrane = []
        for banknot in sorted(self._banknoty, reverse=True):
            if sum(zabrane) + banknot <= to_withdraw:
                zabrane.append(banknot)

        if sum(zabrane) != to_withdraw:
            raise NoEnoughMoney("BŁAD: brak wystarczajace liczby banknotow dla kwoty 150!")

        for banknot in zabrane:
            self._banknoty.remove(banknot)

        return zabrane


def main():
    bankomat = CashMachine()
    while True:
        operacja = input("Podaj typ operacji w - wplata , y - wyplata, k-zakoncz:")
        # wplata
        if operacja == "w":
            money = input("Podaj jakie banknoty wplacasz - wpisz je rozdzielajac spacją: ")
            money = money.split()
            money = [int(x) for x in money]
            try:
                bankomat.put_money(money)
            except ValueError as e:
                print(e)

    #   wyplata
        if operacja == "y":
            kwota_do_wyplaty = int(input("Jaką kwotę chcesz wyplacic: "))
            try:
                wyplacone = bankomat.withdraw_money(kwota_do_wyplaty)
            except ValueError as e:
                print(e)
        if operacja == "k":
            print("Dziekujemy za skorzystanie z naszych uslug")
            break

main()


def test_cash_machine_not_avaiable():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_cashmachine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50])
    cash_machine.put_money([50])
    assert cash_machine.is_available


def test_cash_machine_withdraw_banknoty():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]
    with pytest.raises(ValueError):
        wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]


def test_cash_machine_withdraw_banknoty_sort_is_important():
    cash_machine = CashMachine()
    cash_machine.put_money((200, 100, 20, 50))
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]


def test_cash_machine_withdraw_banknoty_value_is_not_divided_by_10():
    cash_machine = CashMachine()
    with pytest.raises(AmountNotDividedbyten) as e:
        cash_machine.withdraw_money(123)


def test_cash_machine_put_money_more_than_ten_notes():
    bankomat = CashMachine()
    with pytest.raises(CountofNotes) as e:
        bankomat.put_money([50,50,50,50,50])
        bankomat.put_money([50, 50, 50, 50, 50, 50])