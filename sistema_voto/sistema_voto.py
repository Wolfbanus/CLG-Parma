import math

class SistemaVoto:
    """
    Classe che gestisce il sistema di voto ponderato per associazioni, gruppi informali e persone singole.
    """
    def __init__(self):
        # Inizializza il numero di soci per ciascuna categoria
        self.associazioni = 0
        self.gruppi_informali = 0
        self.persone_singole = 0

        # Pesi base assegnati a ciascuna categoria
        self.PESO_ASSOCIAZIONE = 10
        self.PESO_GRUPPO = 7
        self.PESO_SINGOLO = 1

        # Inizializza il numero di voti favorevoli per ciascuna categoria
        self.favorevoli_associazioni = 0
        self.favorevoli_gruppi = 0
        self.favorevoli_singoli = 0

    def aggiorna_soci(self, associazioni, gruppi, singoli):
        """
        Aggiorna il numero di soci per ciascuna categoria.
        :param associazioni: numero di associazioni
        :param gruppi: numero di gruppi informali
        :param singoli: numero di persone singole
        """
        self.associazioni = associazioni
        self.gruppi_informali = gruppi
        self.persone_singole = singoli

    def calcola_pesi(self):
        """
        Calcola il potere di voto totale e la distribuzione percentuale per ciascuna categoria.
        Applica un limite: i singoli non possono superare il potere dei collettivi (associazioni + gruppi).
        :return: tuple con pesi normalizzati e valori assoluti
        """
        # Potere di voto totale per collettivi (associazioni + gruppi)
        potere_collettivi = (self.associazioni * self.PESO_ASSOCIAZIONE + 
                            self.gruppi_informali * self.PESO_GRUPPO)
        # Potere di voto totale per singoli
        potere_singoli = self.persone_singole * self.PESO_SINGOLO

        # Se i singoli superano i collettivi, si applica un fattore correttivo
        if potere_singoli > potere_collettivi:
            fattore_correttivo = potere_collettivi / potere_singoli
            peso_singolo_effettivo = self.PESO_SINGOLO * fattore_correttivo
        else:
            peso_singolo_effettivo = self.PESO_SINGOLO

        # Potere effettivo dei singoli dopo la correzione
        potere_singoli_effettivo = self.persone_singole * peso_singolo_effettivo
        # Potere totale
        peso_totale = potere_collettivi + potere_singoli_effettivo

        # Se non ci sono soci, restituisce zeri
        if peso_totale == 0:
            return 0, 0, 0, 0, 0, 0

        # Calcolo delle percentuali normalizzate
        peso_associazione_norm = (self.associazioni * self.PESO_ASSOCIAZIONE) / peso_totale * 100
        peso_gruppo_norm = (self.gruppi_informali * self.PESO_GRUPPO) / peso_totale * 100
        peso_singolo_norm = potere_singoli_effettivo / peso_totale * 100

        return peso_associazione_norm, peso_gruppo_norm, peso_singolo_norm, potere_collettivi, potere_singoli_effettivo, peso_totale

    def simula_votazione(self, favorevoli_associazioni=None, favorevoli_gruppi=None, favorevoli_singoli=None):
        """
        Simula una votazione, calcolando i voti favorevoli e la percentuale di approvazione.
        :param favorevoli_associazioni: voti favorevoli delle associazioni
        :param favorevoli_gruppi: voti favorevoli dei gruppi informali
        :param favorevoli_singoli: voti favorevoli delle persone singole
        :return: dizionario con risultati della votazione
        """
        # Aggiorna i voti favorevoli se forniti
        if favorevoli_associazioni is not None:
            self.favorevoli_associazioni = favorevoli_associazioni
        if favorevoli_gruppi is not None:
            self.favorevoli_gruppi = favorevoli_gruppi
        if favorevoli_singoli is not None:
            self.favorevoli_singoli = favorevoli_singoli

        # Calcola la distribuzione dei pesi
        peso_a, peso_g, peso_s, potere_c, potere_s, peso_totale = self.calcola_pesi()

        # Calcola i voti favorevoli totali, pesati per categoria
        voti_favorevoli = (
            (self.favorevoli_associazioni * self.PESO_ASSOCIAZIONE) +
            (self.favorevoli_gruppi * self.PESO_GRUPPO) +
            (self.favorevoli_singoli * (potere_s / self.persone_singole if self.persone_singole > 0 else 0))
        )

        # Calcola la percentuale di voti favorevoli
        percentuale_favorevoli = (voti_favorevoli / peso_totale) * 100 if peso_totale > 0 else 0

        # La proposta è approvata se la percentuale è almeno 50%
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
