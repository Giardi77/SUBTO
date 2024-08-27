
# Subto Tool

## Panoramica

**Subto** è un potente strumento progettato per aiutare i professionisti della sicurezza a scoprire possibili takeover di sottodomini. Questo strumento offre diverse opzioni per specificare i target, gestire le scansioni e gestire i risultati delle scansioni.

## Utilizzo

```bash
Subto [-h] [-t TARGET] [-f FILE] [-r] [-n NAME] [-ls] [-sr SCAN_RESULT]
```

## Descrizione

Subto consente agli utenti di specificare i target direttamente o tramite un file, avviare scansioni, gestire la registrazione degli utenti e gestire i risultati delle scansioni. Lo strumento è particolarmente utile per identificare e mitigare il rischio di takeover di sottodomini.

### Opzioni

- **`-h, --help`**
  - Descrizione: Mostra il messaggio di aiuto ed esce.
  - Utilizzo: 
    ```bash
    Subto --help
    ```

- **`-t TARGET, --target TARGET`**
  - Descrizione: Specifica i domini target direttamente. È possibile fornire più target separati da virgole.
  - Esempio: 
    ```bash
    Subto -t esempio.com,esempio.org
    ```

- **`-f FILE, --file FILE`**
  - Descrizione: Specifica un file contenente un elenco di target, con un target per linea.
  - Esempio: 
    ```bash
    Subto -f target.txt
    ```

- **`-r, --register`**
  - Descrizione: Registra un nuovo utente per lo strumento.
  - Utilizzo: 
    ```bash
    Subto -r
    ```

- **`-n NAME, --name NAME`**
  - Descrizione: Imposta il nome per la scansione. Utile per organizzare e identificare diverse scansioni.
  - Esempio: 
    ```bash
    Subto -n "Scansione_Agosto"
    ```

- **`-ls, --list-scan`**
  - Descrizione: Elenca tutte le scansioni salvate in precedenza.
  - Utilizzo: 
    ```bash
    Subto -ls
    ```

- **`-sr SCAN_RESULT, --scan-result SCAN_RESULT`**
  - Descrizione: Recupera i risultati di una specifica scansione per nome.
  - Esempio: 
    ```bash
    Subto -sr "Scansione_Agosto"
    ```

## Esempi

1. **Scansiona più target direttamente:**

   ```bash
   Subto -t esempio.com,esempio.org
   ```

2. **Scansiona target da un file:**

   ```bash
   Subto -f target.txt
   ```

3. **Registrare un nuovo utente:**

   ```bash
   Subto -r
   ```

4. **Imposta un nome personalizzato per la scansione e avvia la scansione:**

   ```bash
   Subto -n "Scansione_Agosto" -t esempio.com
   ```

5. **Elenca tutte le scansioni precedenti:**

   ```bash
   Subto -ls
   ```

6. **Recupera il risultato di una scansione specifica:**

   ```bash
   Subto -sr "Scansione_Agosto"
   ```

## Informazioni aggiuntive

Subto è uno strumento versatile per i ricercatori di sicurezza e i penetration tester focalizzati sull'identificazione dei takeover di sottodomini, una vulnerabilità comune in molte applicazioni web. Un utilizzo corretto delle opzioni fornite aiuterà a gestire e organizzare le tue scansioni in modo efficiente.

Per ulteriori informazioni o supporto, fare riferimento alla documentazione ufficiale o contattare il team di supporto dello strumento.
