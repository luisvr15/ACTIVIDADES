import numpy as np


arrCandidatos = np.arange(1,31)

votos = np.random.randint(1,30,5000)

contarVotos = np.bincount(votos,minlength=31)[1:]

indicesOrdenados = np.argsort(contarVotos)[::-1]

print("Resultados de la elección:")
print("Candidato | Votos")
print("------------------")
for i in indicesOrdenados:
    print(f"{arrCandidatos[i]} | {contarVotos[i]}")
