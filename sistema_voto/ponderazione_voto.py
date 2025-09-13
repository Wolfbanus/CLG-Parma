import random
import math

class SistemaVoto:
    def __init__(self):
        self.associazioni = 0
        self.gruppi_informali = 0
        self.persone_singole = 0
        
        # Pesi base per ciascuna categoria
        self.PESO_ASSOCIAZIONE = 10
        self.PESO_GRUPPO = 7
        self.PESO_SINGOLO = 1
        
        # Numero di voti favorevoli (anziché percentuali)
        self.favorevoli_associazioni = 0
        self.favorevoli_gruppi = 0
        self.favorevoli_singoli = 0
        
    def aggiorna_soci(self, associazioni, gruppi, singoli):
        self.associazioni = associazioni
        self.gruppi_informali = gruppi
        self.persone_singole = singoli
    
    def calcola_pesi(self):
        # Calcola il potere di voto totale per ogni categoria
        potere_collettivi = (self.associazioni * self.PESO_ASSOCIAZIONE + 
                            self.gruppi_informali * self.PESO_GRUPPO)
        
        potere_singoli = self.persone_singole * self.PESO_SINGOLO
        
        # Applica il limite del 50/50 se necessario
        if potere_singoli > potere_collettivi:
            # Riduce il peso dei singoli per bilanciamento
            fattore_correttivo = potere_collettivi / potere_singoli
            peso_singolo_effettivo = self.PESO_SINGOLO * fattore_correttivo
        else:
            peso_singolo_effettivo = self.PESO_SINGOLO
        
        # Calcola i pesi normalizzati
        potere_singoli_effettivo = self.persone_singole * peso_singolo_effettivo
        peso_totale = potere_collettivi + potere_singoli_effettivo
        
        if peso_totale == 0:
            return 0, 0, 0, 0, 0, 0
            
        peso_associazione_norm = (self.associazioni * self.PESO_ASSOCIAZIONE) / peso_totale * 100
        peso_gruppo_norm = (self.gruppi_informali * self.PESO_GRUPPO) / peso_totale * 100
        peso_singolo_norm = potere_singoli_effettivo / peso_totale * 100
        
        return peso_associazione_norm, peso_gruppo_norm, peso_singolo_norm, potere_collettivi, potere_singoli_effettivo, peso_totale
    
    def simula_votazione(self, favorevoli_associazioni=None, favorevoli_gruppi=None, favorevoli_singoli=None):
        # Memorizza il numero di voti favorevoli (non più le percentuali)
        if favorevoli_associazioni is not None:
            self.favorevoli_associazioni = favorevoli_associazioni
        if favorevoli_gruppi is not None:
            self.favorevoli_gruppi = favorevoli_gruppi
        if favorevoli_singoli is not None:
            self.favorevoli_singoli = favorevoli_singoli
        
        # Calcola i pesi
        peso_a, peso_g, peso_s, potere_c, potere_s, peso_totale = self.calcola_pesi()
        
        # Calcola i voti favorevoli
        voti_favorevoli = (
            (self.favorevoli_associazioni * self.PESO_ASSOCIAZIONE) +
            (self.favorevoli_gruppi * self.PESO_GRUPPO) +
            (self.favorevoli_singoli * (potere_s / self.persone_singole if self.persone_singole > 0 else 0))
        )
        
        # Calcola la percentuale di voti favorevoli
        percentuale_favorevoli = (voti_favorevoli / peso_totale) * 100 if peso_totale > 0 else 0
        
        # Determina se la proposta è approvata (soglia al 50%)
        approvata = percentuale_favorevoli >= 50
        
        return {
            "voti_favorevoli": voti_favorevoli,
            "voti_totali": peso_totale,
            "percentuale_favorevoli": percentuale_favorevoli,
            "approvata": approvata,
            "dettaglio_favorevoli": {
                "associazioni": self.favorevoli_associazioni,
                "gruppi": self.favorevoli_gruppi,
                "singoli": self.favorevoli_singoli
            }
        }


def stampa_risultati(sistema, risultati):
    print("=" * 60)
    print("RISULTATI DELLA VOTAZIONE")
    print("=" * 60)
    
    # Informazioni sui soci
    print("COMPOSIZIONE DEI SOCI:")
    print(f"  Associazioni: {sistema.associazioni}")
    print(f"  Gruppi informali: {sistema.gruppi_informali}")
    print(f"  Persone singole: {sistema.persone_singole}")
    print()
    
    # Numero di voti favorevoli
    print("NUMERO DI VOTI FAVOREVOLI:")
    print(f"  Associazioni: {sistema.favorevoli_associazioni} su {sistema.associazioni}")
    print(f"  Gruppi informali: {sistema.favorevoli_gruppi} su {sistema.gruppi_informali}")
    print(f"  Persone singole: {sistema.favorevoli_singoli} su {sistema.persone_singole}")
    print()
    
    # Distribuzione dei pesi
    peso_a, peso_g, peso_s, potere_c, potere_s, peso_totale = sistema.calcola_pesi()
    print("DISTRIBUZIONE DEL POTERE DI VOTO:")
    print(f"  Associazioni: {peso_a:.2f}%")
    print(f"  Gruppi informali: {peso_g:.2f}%")
    print(f"  Persone singole: {peso_s:.2f}%")
    print()
    
    # Risultati della votazione
    print("RISULTATO DELLA VOTAZIONE:")
    print(f"  Voti favorevoli: {risultati['voti_favorevoli']:.2f} / {risultati['voti_totali']:.2f}")
    print(f"  Percentuale favorevoli: {risultati['percentuale_favorevoli']:.2f}%")
    print(f"  Esito: {'APPROVATA' if risultati['approvata'] else 'RESPINTA'}")
    print()

def genera_random():
    sistema = SistemaVoto()
    
    # Genera numeri casuali per i soci
    associazioni = random.randint(1, 20)
    gruppi = random.randint(1, 30)
    singoli = random.randint(0, 1000)
    
    sistema.aggiorna_soci(associazioni, gruppi, singoli)
    
    # Genera numeri casuali di voti favorevoli (non più percentuali)
    favorevoli_associazioni = random.randint(0, associazioni)
    favorevoli_gruppi = random.randint(0, gruppi)
    favorevoli_singoli = random.randint(0, singoli) if singoli > 0 else 0
    
    # Simula la votazione
    risultati = sistema.simula_votazione(favorevoli_associazioni, favorevoli_gruppi, favorevoli_singoli)
    
    return sistema, risultati

def input_manuale():
    sistema = SistemaVoto()
    
    print("Inserisci il numero di soci per ogni categoria:")
    associazioni = int(input("Associazioni: "))
    gruppi = int(input("Gruppi informali: "))
    singoli = int(input("Persone singole: "))
    
    sistema.aggiorna_soci(associazioni, gruppi, singoli)
    
    print("\nInserisci il numero di voti favorevoli per ogni categoria:")
    
    # Solo se ci sono associazioni, chiedi i voti favorevoli
    if associazioni > 0:
        favorevoli_associazioni = int(input(f"Voti favorevoli associazioni (0-{associazioni}): "))
        # Controllo che il valore sia valido
        while favorevoli_associazioni < 0 or favorevoli_associazioni > associazioni:
            print(f"Valore non valido. Inserisci un numero tra 0 e {associazioni}.")
            favorevoli_associazioni = int(input(f"Voti favorevoli associazioni (0-{associazioni}): "))
    else:
        favorevoli_associazioni = 0
    
    # Solo se ci sono gruppi, chiedi i voti favorevoli
    if gruppi > 0:
        favorevoli_gruppi = int(input(f"Voti favorevoli gruppi (0-{gruppi}): "))
        # Controllo che il valore sia valido
        while favorevoli_gruppi < 0 or favorevoli_gruppi > gruppi:
            print(f"Valore non valido. Inserisci un numero tra 0 e {gruppi}.")
            favorevoli_gruppi = int(input(f"Voti favorevoli gruppi (0-{gruppi}): "))
    else:
        favorevoli_gruppi = 0
    
    # Solo se ci sono singoli, chiedi i voti favorevoli
    if singoli > 0:
        favorevoli_singoli = int(input(f"Voti favorevoli singoli (0-{singoli}): "))
        # Controllo che il valore sia valido
        while favorevoli_singoli < 0 or favorevoli_singoli > singoli:
            print(f"Valore non valido. Inserisci un numero tra 0 e {singoli}.")
            favorevoli_singoli = int(input(f"Voti favorevoli singoli (0-{singoli}): "))
    else:
        favorevoli_singoli = 0
    
    # Simula la votazione
    risultati = sistema.simula_votazione(favorevoli_associazioni, favorevoli_gruppi, favorevoli_singoli)
    
    return sistema, risultati

def main():
    print("SISTEMA DI VOTO PONDERATO PER ASSOCIAZIONE")
    print("=" * 50)
    
    # Mostra la formula utilizzata
    # stampa_formula() rimossa perché non definita
    
    while True:
        print("\nScegli una modalità:")
        print("1. Generazione randomica")
        print("2. Inserimento manuale")
        print("3. Esci")
        
        scelta = input("Scelta: ")
        
        if scelta == "1":
            sistema, risultati = genera_random()
            stampa_risultati(sistema, risultati)
        elif scelta == "2":
            sistema, risultati = input_manuale()
            stampa_risultati(sistema, risultati)
        elif scelta == "3":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()