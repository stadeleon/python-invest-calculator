class InvestCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_compound_interest(principal, annual_rate, capitalization, years, monthly_deposit):
        n = capitalization
        r = annual_rate / 100
        t = years
        d = monthly_deposit
        return principal * (1 + r/n)**(n*t) + (d * (((1 + r/n)**(n*t) - 1) / (r/n)))

