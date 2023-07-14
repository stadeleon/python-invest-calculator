def calculate_compound_interest(principal, annual_rate, capitalization, years, monthly_deposit):
    n = capitalization
    r = annual_rate / 100
    t = years
    d = monthly_deposit
    A = principal * (1 + r/n)**(n*t) + (d * (((1 + r/n)**(n*t) - 1) / (r/n)))
    return A

principal = 0
annual_rate = 10
capitalization = 12
monthly_deposit = 5000

years = [5, 10, 15, 20, 25, 30]
for year in years:
    total_amount = calculate_compound_interest(principal, annual_rate, capitalization, year, monthly_deposit)
    income = total_amount * 0.06 / 12
    payments = monthly_deposit * 12 * year
    print(f"Сума накопичень за {year} роки: {total_amount:,.2f} USD  з пасивним прибутком у 6% = {income:.2f} USD при вкладеннях "
          f"{payments:,.2f}" )
