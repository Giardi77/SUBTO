
# Subto - Subdomain Takeover

## Panoramica

**Subto**  consente agli utenti di specificare i target direttamente o tramite un file, avviare scansioni, gestire la registrazione degli utenti e gestire i risultati delle scansioni. Lo strumento è particolarmente utile per identificare e mitigare il rischio di takeover di sottodomini.

## Installazione

```bash
git clone https://github.com/Giardi77/SUBTO.git
cd SUBTO
python -m venv subto_venv
source subto_venv/bin/activate
pip install -r requirements.txt
```

## Utilizzo

```bash
Subto [-h] [-t TARGET] [-f FILE] [-r] [-n NAME] [-ls] [-sr SCAN_RESULT]
```

### Opzioni

- **`-h, --help`**
  - Descrizione: Mostra il messaggio di aiuto ed esce.
  - Utilizzo: 
    ```bash
    python main.py --help
    ```

- **`-t TARGET, --target TARGET`**
  - Descrizione: Specifica i domini target direttamente. È possibile fornire più target separati da virgole.
  - Esempio: 
    ```bash
    python main.py -t esempio.com,esempio.org
    ```

- **`-f FILE, --file FILE`**
  - Descrizione: Specifica un file contenente un elenco di target, con un target per linea.
  - Esempio: 
    ```bash
    python main.py -f target.txt
    ```

- **`-r, --register`**
  - Descrizione: Registra un nuovo utente per lo strumento.
  - Utilizzo: 
    ```bash
    python main.py -r
    ```

- **`-ls, --list-scan`**
  - Descrizione: Elenca tutte le scansioni salvate in precedenza.
  - Utilizzo: 
    ```bash
    python main.py -ls
    ```

- **`-sr SCAN_RESULT, --scan-result SCAN_RESULT`**
  - Descrizione: Recupera i risultati di una specifica scansione per nome.
  - Esempio: 
    ```bash
    python main.py -sr <ID>
    ```

## Esempi

1. **Scansiona più target direttamente:**

   ```bash
   python main.py -t esempio.com,esempio.org
   ```

2. **Scansiona target da un file:**

   ```bash
   python main.py -f target.txt
   ```

3. **Registrare un nuovo utente:**

   ```bash
   python main.py -r
   ```

4. **Imposta un nome personalizzato per la scansione e avvia la scansione:**

   ```bash
   python main.py -n "Scansione_Agosto" -t esempio.com
   ```

5. **Elenca tutte le scansioni precedenti:**

   ```bash
   python main.py -ls
   ```

6. **Recupera il risultato di una scansione specifica:**

   ```bash
   python main.py -sr <ID>
   ```

