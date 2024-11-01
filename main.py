import decimal

def calculate_pi(n):
    # Ställ in decimal precision
    decimal.getcontext().prec = n + 2  # +2 för att få rätt antal decimaler
    pi = decimal.Decimal(0)
    k = 0
    
    # Beräkning av pi med hjälp av Chudnovsky-algoritmen
    while k < n:
        numerator = decimal.Decimal((-1) ** k) * decimal.Decimal(factorial(6 * k)) * (13591409 + 545140134 * k)
        denominator = (decimal.Decimal(factorial(3 * k)) * decimal.Decimal(factorial(k) ** 3) * (640320 ** (3 * k)))
        pi += numerator / denominator
        k += 1

    pi = (pi * decimal.Decimal(12).sqrt()) / decimal.Decimal(640320 ** 1.5)
    pi = 1 / pi
    return str(pi)[:n + 2]  # Returnera pi som en sträng med n decimaler

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Exempel på användning
n = 100  # Antal decimaler av pi
pi_value = calculate_pi(n)
print(f"De första {n} decimalerna av π är: {pi_value}")
