import matplotlib.pyplot as plt

tipos = ["Original", "Optimizado"]

tiempos = [25, 2]

plt.figure(figsize=(6,4))

plt.bar(tipos, tiempos)

plt.xlabel("Version")
plt.ylabel("Tiempo")
plt.title("Comparacion de tiempos")

plt.savefig("grafica.png")

print("Grafica generada correctamente")