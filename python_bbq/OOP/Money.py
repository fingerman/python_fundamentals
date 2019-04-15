class Money:
    def __init__(self, amount):
        self.exchange_rate = {'EUR to USD': 1.1227,
                              'USD to EUR': 0.89075,
                              'EUR to GBP': 0.8579,
                              'GBP to EUR': 1.16564,
                              'USD to GBP': 0.76435,
                              'GBP to USD': 1.3083
                              }
        self.amount = amount


class Account(Money):
    def __init__(self, amount, country):
        super().__init__(amount)
        self.country = country
        self.curr_exc_rate = self.travel_to(country)

    def travel_to(self, new_country):
        if self.country == new_country:
            self.curr_exc_rate = 1.00
        elif self.country == 'DE' and new_country == 'US':
            self.curr_exc_rate = self.exchange_rate.get('EUR to USD')
        elif self.country == 'DE' and new_country == 'UK':
            self.curr_exc_rate = self.exchange_rate.get('EUR to GBP')
        elif self.country == 'UK' and new_country == 'US':
            self.curr_exc_rate = self.exchange_rate.get('GBP to USD')
        elif self.country == 'UK' and new_country == 'DE':
            self.curr_exc_rate = self.exchange_rate.get('GBP to EUR')
        elif self.country == 'US' and new_country == 'DE':
            self.curr_exc_rate = self.exchange_rate.get('USD to EUR')
        elif self.country == 'US' and new_country == 'UK':
            self.curr_exc_rate = self.exchange_rate.get('USD to GBP')

        self.country = new_country
        self.amount *= self.curr_exc_rate
        return self.curr_exc_rate

    def check_account(self):
        currency = {'UK': 'GBP', 'US': 'USD', 'DE': 'EUR'}
        for k, v in currency.items():
            if self.country == k:
                currency = v
        print("Current Account: {:.2f}".format(self.amount), currency)

    def spend_money(self, new_amount):
        self.amount -= new_amount

    def get_money(self, new_amount):
        self.amount += new_amount
# ------------------------------------------------


nick = Account(500, 'UK')
nick.check_account()
nick.travel_to('UK')
nick.check_account()
nick.travel_to('DE')
nick.check_account()
nick.travel_to('US')
nick.check_account()
nick.travel_to('UK')
nick.check_account()
nick.travel_to('US')
nick.check_account()
nick.spend_money(54.33)
nick.check_account()
nick.get_money(300)
nick.check_account()













