from sistema_voto import SistemaVoto
from utils import stampa_risultati, genera_random, input_manuale

print("SISTEMA DI VOTO PONDERATO PER ASSOCIAZIONE")
print("=" * 50)

while True:
    print("\nScegli una modalità:")
    print("1. Generazione randomica")
    print("2. Inserimento manuale")
    print("3. Esci")
    scelta = input("Scelta: ")
    if scelta == "1":
        sistema, risultati = genera_random(SistemaVoto)
        stampa_risultati(sistema, risultati)
    elif scelta == "2":
        sistema, risultati = input_manuale(SistemaVoto)
        stampa_risultati(sistema, risultati)
    elif scelta == "3":
        print("Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")
