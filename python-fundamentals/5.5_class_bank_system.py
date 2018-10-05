from decimal import Decimal
from operator import attrgetter


class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance

    def get_info(self):
        return f'{self.name} -> {self.balance:.2f} ({self.bank})'


def create_accounts(storage):
    line = input()
    while line != 'end':
        bank, name, balance = line.split(' | ')
        storage.append(BankAccount(name, bank, Decimal(balance)))
        line = input()
    return storage

# ordered by their balance, in descending order, and then by length of the bank name, in ascending order.
def sort_accounts(storage):
    sorted_accounts = sorted(storage, key=lambda x: (x.balance, -len(x.bank)), reverse=True)
    return sorted_accounts


def print_info(accounts):
    for account in accounts:
        print(account.get_info())


data_base = []
create_accounts(data_base)

print_info(sort_accounts(data_base))

'''
Create a class BankAccount which has a Name (string), Bank (string) and Balance (decimal). 
You will receive several input lines, containing information in the following way:
{bank} | {accountName} | {accountBalance}
You need to store every given Account. When you receive the command “end” you must stop the input sequence.
Then you must print all Accounts, ordered by their balance, in descending order, 
and then by length of the bank name, in ascending order.
The accounts must be printed in the following way “{accountName} -> {balance} ({bank})”.
Note: Numbers must be printed rounded to the 2nd decimal digit.

Input
DSK | Ivan | 504.403
DSK | Pesho | 2000.4031
DSK | Aleksander | 20000.0001
Piraeus | Ivan | 504.403
Piraeus | Aleksander | 20000.0001
end

Output
Aleksander -> 20000.00 (DSK)
Aleksander -> 20000.00 (Piraeus)
Pesho -> 2000.40 (DSK)
Ivan -> 504.40 (DSK)
Ivan -> 504.40 (Piraeus)





'''