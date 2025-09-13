import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Funzione didattica per calcolare pesi e fattore correttivo
def calcola_pesi_anim(associazioni, gruppi, singoli, PESO_ASSOCIAZIONE=10, PESO_GRUPPO=5, PESO_SINGOLO=1):
    potere_collettivi = (associazioni * PESO_ASSOCIAZIONE + gruppi * PESO_GRUPPO)
    potere_singoli = singoli * PESO_SINGOLO
    if potere_singoli > potere_collettivi and potere_singoli > 0:
        fattore_correttivo = potere_collettivi / potere_singoli
        peso_singolo_effettivo = PESO_SINGOLO * fattore_correttivo
    else:
        fattore_correttivo = 1.0
        peso_singolo_effettivo = PESO_SINGOLO
    potere_singoli_effettivo = singoli * peso_singolo_effettivo
    peso_totale = potere_collettivi + potere_singoli_effettivo
    if peso_totale == 0:
        return 0, 0, 0, fattore_correttivo
    peso_associazione_norm = (associazioni * PESO_ASSOCIAZIONE) / peso_totale * 100
    peso_gruppo_norm = (gruppi * PESO_GRUPPO) / peso_totale * 100
    peso_singolo_norm = potere_singoli_effettivo / peso_totale * 100
    return peso_associazione_norm, peso_gruppo_norm, peso_singolo_norm, fattore_correttivo


# Input utente
print("Animazione didattica distribuzione pesi di voto")
while True:
    try:
        a = int(input("Numero di associazioni: "))
        if a < 0:
            print("Il numero deve essere >= 0")
            continue
        break
    except ValueError:
        print("Inserisci un numero intero valido.")
while True:
    try:
        b = int(input("Numero di gruppi informali: "))
        if b < 0:
            print("Il numero deve essere >= 0")
            continue
        break
    except ValueError:
        print("Inserisci un numero intero valido.")
while True:
    try:
        singoli_max = int(input("Numero massimo di persone singole da visualizzare (es: 200): "))
        if singoli_max < 0:
            print("Il numero deve essere >= 0")
            continue
        break
    except ValueError:
        print("Inserisci un numero intero valido.")

singoli_range = np.arange(0, singoli_max+1, 1)

# Precalcolo per animazione
pesi_associazioni = []
pesi_gruppi = []
pesi_singoli = []
fattori = []
pesi_collettivi_list = []
for s in singoli_range:
    pa, pg, ps, f = calcola_pesi_anim(a, b, s)
    pesi_collettivi = pa + pg
    pesi_singoli.append(ps)
    pesi_associazioni.append(pa)  # mantenuto per eventuali debug
    pesi_gruppi.append(pg)        # mantenuto per eventuali debug
    pesi_collettivi_list.append(pesi_collettivi)
    fattori.append(f)


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Linee vuote da aggiornare
line_c, = ax1.plot([], [], label="Soci collettivi", color="blue")
line_s, = ax1.plot([], [], label="Persone singole", color="orange")
ax1.axvline(x=(a*10+b*5), color='red', linestyle='--', alpha=0.5, label="Soglia 50/50")
ax1.set_ylabel("Peso percentuale (%)")
ax1.set_ylim(0, 100)
ax1.legend(loc="upper right")
ax1.set_title("Distribuzione pesi di voto e soglia 50/50")
ax1.grid(True)

line_f, = ax2.plot([], [], color="purple", label="Fattore correttivo")
ax2.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5)
ax2.set_ylabel("Fattore correttivo")
ax2.set_xlabel("Numero di persone singole")
ax2.set_ylim(0, 1.05)
ax2.legend(loc="upper right")
ax2.grid(True)

# Testo dinamico
fattore_text = ax2.text(0.02, 0.85, '', transform=ax2.transAxes, fontsize=12, color='purple')


# Funzione di animazione
def animate(i):
    x = singoli_range[:i+1]
    # Plotta soci collettivi e singoli
    line_c.set_data(x, pesi_collettivi_list[:i+1])
    line_s.set_data(x, pesi_singoli[:i+1])
    line_f.set_data(x, fattori[:i+1])
    fattore_text.set_text(f"Fattore correttivo: {fattori[i]:.2f}")
    return line_c, line_s, line_f, fattore_text

ax1.set_xlim(0, singoli_max)

ani = FuncAnimation(fig, animate, frames=len(singoli_range), interval=40, blit=True, repeat=False)
plt.tight_layout()

# Salvataggio video opzionale
salva = input("Vuoi salvare l'animazione come video mp4? (s/N): ").strip().lower()
if salva == 's' or salva == 'si' or salva == 'y':
    nome_file = input("Nome file (es: animazione_pesi.mp4): ").strip()
    if not nome_file:
        nome_file = "animazione_pesi.mp4"
    print("Salvataggio in corso... (potrebbe richiedere qualche secondo)")
    try:
        ani.save(nome_file, writer='ffmpeg', fps=25)
        print(f"Animazione salvata come {nome_file}")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}\nAssicurati che ffmpeg sia installato nel sistema.")

plt.show()

print("Animazione: la parte superiore mostra la variazione dei pesi percentuali tra Soci collettivi e Persone singole, la parte inferiore il fattore correttivo. Quando il fattore scende sotto 1, il limite 50/50 è attivo.")
