import time

inicio = time.time()

numeros_primos = []

for n in range(2, 100000):
    es_primo = True

    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        numeros_primos.append(n)

fin = time.time()

print("Cantidad de números primos:", len(numeros_primos))
print("Tiempo de ejecución:", fin - inicio, "segundos")