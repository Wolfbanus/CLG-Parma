
# Regolamento CLG

Questo repository contiene documenti, regolamenti e strumenti per il Consiglio Locale Giovani (CLG) di Parma.

## Come è organizzata la repository

All’interno di questa cartella troverai:

- **sistema_voto/**: una cartella che contiene strumenti per simulare e capire il sistema di voto del CLG.
	- `animazione_pesi.py`: un programma che mostra, tramite animazione, come funzionano i "pesi" dei voti.
	- `ponderazione_voto.py`: un programma che calcola come vengono pesati i voti delle associazioni.
	- `32-associazioni_1-gruppo-singolo.mp4`: un video che spiega visivamente il sistema di voto.

- **STATUTO CLG CON EMENDAMENTI APPROVATI.pdf**: il documento ufficiale dello statuto, in formato PDF.

- **voting_software_links.md**: un file con link a software di voto (per ora non fateci caso)

## Come usare i file

### 1. Leggere i documenti

- I file con estensione `.md` (Markdown) sono documenti di testo. Puoi leggerli in vari modi:
    - **Su GitHub**: se stai guardando la repo su GitHub, i file `.md` sono già visualizzati in modo leggibile.
	- **Su computer**: aprili con un editor di testo (come Notepad, Blocco Note, TextEdit, o programmi come Visual Studio Code, Atom, ecc.).
	- **Online**: puoi caricarli su [Dillinger](https://dillinger.io/) o [StackEdit](https://stackedit.io/).

- I file `.pdf` si aprono con qualsiasi lettore PDF (come [Okular](https://okular.kde.org/it/), browser web, Adobe Reader, ecc.).

### 2. Guardare il video

- I file `.mp4` si possono aprire con qualsiasi programma per video (VLC, Windows Media Player, ecc.).

### 3. Eseguire i programmi Python

I file `animazione_pesi.py` e `ponderazione_voto.py` sono programmi scritti in Python. Per eseguirli:

1. **Installa Python**
	 - **Windows**: Vai su [python.org](https://www.python.org/downloads/windows/) e scarica l'installer per Windows. Durante l'installazione, **spunta la casella "Add Python to PATH"** prima di cliccare su "Install Now".
	 - **macOS**: Su molti Mac recenti Python è già installato, ma spesso è una versione vecchia. Per una versione aggiornata, scarica l'installer da [python.org](https://www.python.org/downloads/macos/) oppure installa [Homebrew](https://brew.sh/) e poi esegui `brew install python` dal Terminale.
	 - **Linux**: Su molte distribuzioni Python è già installato. Per installare o aggiornare Python:
		 - **Ubuntu/Debian**: apri il Terminale e scrivi `sudo apt update && sudo apt install python3`
		 - **Fedora**: `sudo dnf install python3`
		 - **Altre distro**: consulta la documentazione della tua distribuzione.

2. **Apri il terminale o prompt dei comandi**
	 - **Windows**: cerca "Prompt dei comandi" o "cmd".
	 - **macOS/Linux**: cerca "Terminale".

3. **Vai nella cartella dove si trova il file**
	 - Usa il comando `cd` per entrare nella cartella, ad esempio:
		 ```
		 cd percorso/della/cartella/sistema_voto
		 ```

4. **Esegui il programma**
	 - Scrivi:
		 ```
		 python nomefile.py
		 ```
	 - Se su Linux/macOS il comando `python` non funziona, prova con `python3`:
		 ```
		 python3 nomefile.py
		 ```
	 - Sostituisci `nomefile.py` con `animazione_pesi.py` o `ponderazione_voto.py`.

5. **Dipendenze**
	 - Prima di eseguire i programmi, installa tutte le dipendenze necessarie con il comando:
		 ```
		 pip install -r requirements.txt
		 ```
		 (Se su Linux/macOS il comando `pip` non funziona, prova con `pip3`)
	 - Questo installerà automaticamente le librerie necessarie (ad esempio: `matplotlib`, `numpy`).

## Domande o problemi?

Se hai dubbi, difficoltà o vuoi suggerire modifiche, puoi:
- Scrivere una email ai responsabili del CLG
- Aprire una "issue" su GitHub (serve creare un account)

## Licenza

Questo progetto è distribuito con licenza [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.it).

Se utilizzi, modifichi o redistribuisci i contenuti di questo repository, attribuisci la paternità agli autori originali.
