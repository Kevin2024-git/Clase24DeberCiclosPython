n = int(input("¿Cuántos términos de la serie Fibonacci quieres ver? "))
a, b = 0, 1
contador = 0

while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1
