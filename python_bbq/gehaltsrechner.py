class Person:

    def __init__(self, salary, marital_status, church_tax):
        self.salary = salary
        self.marital_status = {1:'ledig', 2:'bla', 3:'blabla'}
        self.church_tax = church_tax
        self.tax_class = marital_status

    def get_kv(self):
        kv = round((self.salary * 7.3)/100, 2)
        return kv

    def get_pv(self):
        pv = round((self.salary * 1.5)/100, 2)
        return pv

    def get_rv(self):
        rv = round((self.salary * 9.3)/100, 2)
        return rv

    def get_av(self):
        av = round((self.salary * 1.25)/100, 2)
        return av


    def get_sum_sozial(self):
        sa = [self.get_kv(), self.get_pv(), self.get_rv(), self.get_av()]
        sum_sa = sum(sa)
        return round(sum_sa, 2)

    def calculate_tax(self):
        if self.tax_class == 1:
            if self.salary > 1029:
                if self.salary > 4000:
                    return round(((self.salary - 1029) * 26) / 100, 2)
                if self.salary <= 4000:
                    return round(((self.salary - 1029) * 22) / 100, 2)
            elif self.salary <= 1029:
                return 0

        elif self.tax_class == 2:
            if self.salary > 1225:
                if self.salary > 4000:
                    return round(((self.salary - 1225) * 22)/100, 2)
                if self.salary <= 4000:
                    return round(((self.salary - 1225) * 18)/100, 2)
            elif self.salary <= 1225:
                return 0

        elif self.tax_class == 3:
            if self.salary > 1952:
                if self.salary > 4000:
                    return round(((self.salary - 1952) * 22)/100, 2)
                if self.salary <= 4000:
                    return round(((self.salary - 1952) * 18)/100, 2)
            elif self.salary <= 1952:
                return 0

    def get_sol_zuschlag(self):
        if self.tax_class == 1:
            if self.salary > 1029:
                sz = round(((self.salary - 1029) * 5.5)/100, 2)
                return sz
            elif self.salary <= 1029:
                sz = float(0)
                return sz
        elif self.tax_class == 2:
            if self.salary > 1225:
                sz = round(((self.salary - 1225) * 5.5)/100, 2)
                return sz
            elif self.salary <= 1225:
                sz = float(0)
                return sz
        elif self.tax_class == 3:
            if self.salary > 1952:
                sz = round(((self.salary - 1952) * 5.5)/100, 2)
                return sz
            elif self.salary <= 1952:
                sz = float(0)
                return sz

    def get_ks(self):
        if self.church_tax == 2:
            ks = float(0)
            return ks
        elif self.church_tax == 1:
            if self.tax_class == 1:
                if self.salary > 1029:
                    ks = round(((self.salary - 1029) * 4) / 100, 2)
                    return ks
                elif self.salary <= 1029:
                    ks = 0
                    return ks
            if self.tax_class == 2:
                if self.salary > 1225:
                    ks = round(((self.salary - 1225) * 4) / 100, 2)
                    return ks
                elif self.salary <= 1225:
                    ks = 0
                    return ks
            if self.tax_class == 3:
                if self.salary > 1925:
                    ks = round(((self.salary - 1925) * 4) / 100, 2)
                    return ks
                elif self.salary <= 1925:
                    ks = 0
                    return ks

    def get_all_taxes(self):
        all_taxes = [self.calculate_tax(), self.get_sol_zuschlag(), self.get_ks()]
        sum_all_taxes = sum(all_taxes)
        return round(sum_all_taxes, 2)

    def calc_netto_salary(self):
        all_expendatures = [self.get_all_taxes(), self.get_sum_sozial()]
        return self.salary - sum(all_expendatures)


gehat_input = float(input("Gehalt: "))
familienstand_input = int(input(
    '''Familienstand: 
1: lediag /n
2: alleinerziehnd
3: verheiratet'''))

kirchensteuer_input = int(input(
'''Kirchensteuer: 
1 - ja, 2 - nein
'''))

person = Person(gehat_input, familienstand_input, kirchensteuer_input)
print("Gehalt(brutto) : ", person.salary)
print("Familienstand : ", person.marital_status.get(familienstand_input))
print("Steuerklasse : ", person.tax_class)
print("KV Betrag: ", person.get_kv())
print("PV Betrag: ", person.get_pv())
print("AV Betrag: ", person.get_av())
print("Summe Sozialausgaben: ", person.get_sum_sozial())
print()
print("Lohnsteuer: ", person.calculate_tax())
print("Solid. Zuschlag Betrag: ", person.get_sol_zuschlag())
print("Kirchensteuer: ", person.get_ks())
print("Summe Steuer: ", person.get_all_taxes())
print()
print("Gehalt (netto): ", person.calc_netto_salary())
