def minimo_multiplicador(n):
    m = 1
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count % 2 != 0:
            m *= i
        i += 1
    if n > 1:
        m *= n
    return m
def main():
    n = int(input("Ingrese un número: "))
    resultado = minimo_multiplicador(n)
    print("Debe ser multiplicado por", resultado)
main()
