def stampa_risultati(sistema, risultati):
    print("=" * 60)
    print("RISULTATI DELLA VOTAZIONE")
    print("=" * 60)
    print("COMPOSIZIONE DEI SOCI:")
    print(f"  Associazioni: {sistema.associazioni}")
    print(f"  Gruppi informali: {sistema.gruppi_informali}")
    print(f"  Persone singole: {sistema.persone_singole}")
    print()
    print("NUMERO DI VOTI FAVOREVOLI:")
    print(f"  Associazioni: {sistema.favorevoli_associazioni} su {sistema.associazioni}")
    print(f"  Gruppi informali: {sistema.favorevoli_gruppi} su {sistema.gruppi_informali}")
    print(f"  Persone singole: {sistema.favorevoli_singoli} su {sistema.persone_singole}")
    print()
    peso_a, peso_g, peso_s, potere_c, potere_s, peso_totale = sistema.calcola_pesi()
    print("DISTRIBUZIONE DEL POTERE DI VOTO:")
    print(f"  Associazioni: {peso_a:.2f}%")
    print(f"  Gruppi informali: {peso_g:.2f}%")
    print(f"  Persone singole: {peso_s:.2f}%")
    print()
    print("RISULTATO DELLA VOTAZIONE:")
    print(f"  Voti favorevoli: {risultati['voti_favorevoli']:.2f} / {risultati['voti_totali']:.2f}")
    print(f"  Percentuale favorevoli: {risultati['percentuale_favorevoli']:.2f}%")
    print(f"  Esito: {'APPROVATA' if risultati['approvata'] else 'RESPINTA'}")
    print()

def genera_random(SistemaVoto):
    import random
    sistema = SistemaVoto()
    associazioni = random.randint(32, 35)
    gruppi = random.randint(1, 5)
    singoli = random.randint(0, 50)
    sistema.aggiorna_soci(associazioni, gruppi, singoli)
    favorevoli_associazioni = random.randint(0, associazioni)
    favorevoli_gruppi = random.randint(0, gruppi)
    favorevoli_singoli = random.randint(0, singoli) if singoli > 0 else 0
    risultati = sistema.simula_votazione(favorevoli_associazioni, favorevoli_gruppi, favorevoli_singoli)
    return sistema, risultati

def input_manuale(SistemaVoto):
    sistema = SistemaVoto()
    print("Inserisci il numero di soci per ogni categoria:")
    associazioni = int(input("Associazioni: "))
    gruppi = int(input("Gruppi informali: "))
    singoli = int(input("Persone singole: "))
    sistema.aggiorna_soci(associazioni, gruppi, singoli)
    print("\nInserisci il numero di voti favorevoli per ogni categoria:")
    if associazioni > 0:
        favorevoli_associazioni = int(input(f"Voti favorevoli associazioni (0-{associazioni}): "))
        while favorevoli_associazioni < 0 or favorevoli_associazioni > associazioni:
            print(f"Valore non valido. Inserisci un numero tra 0 e {associazioni}.")
            favorevoli_associazioni = int(input(f"Voti favorevoli associazioni (0-{associazioni}): "))
    else:
        favorevoli_associazioni = 0
    if gruppi > 0:
        favorevoli_gruppi = int(input(f"Voti favorevoli gruppi (0-{gruppi}): "))
        while favorevoli_gruppi < 0 or favorevoli_gruppi > gruppi:
            print(f"Valore non valido. Inserisci un numero tra 0 e {gruppi}.")
            favorevoli_gruppi = int(input(f"Voti favorevoli gruppi (0-{gruppi}): "))
    else:
        favorevoli_gruppi = 0
    if singoli > 0:
        favorevoli_singoli = int(input(f"Voti favorevoli singoli (0-{singoli}): "))
        while favorevoli_singoli < 0 or favorevoli_singoli > singoli:
            print(f"Valore non valido. Inserisci un numero tra 0 e {singoli}.")
            favorevoli_singoli = int(input(f"Voti favorevoli singoli (0-{singoli}): "))
    else:
        favorevoli_singoli = 0
    risultati = sistema.simula_votazione(favorevoli_associazioni, favorevoli_gruppi, favorevoli_singoli)
    return sistema, risultati
