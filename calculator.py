
def calc_simple_interest(principal, annual_rate, years):
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    return principal * annual_rate * years / 100


def calc_compound_growth(initial_amount, annual_rate, years, periods_per_year=1):
    if initial_amount < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    if not isinstance(periods_per_year, int) or periods_per_year <= 0:
        raise ValueError("periods_per_year должно быть целым положительным числом")
    return initial_amount * (1 + annual_rate / (100 * periods_per_year)) ** (periods_per_year * years)


def calc_tax_deduction(income, tax_percent):
    if not (0 <= tax_percent <= 100):
        raise ValueError("tax_percent должен быть от 0 до 100")
    return income * tax_percent / 100
