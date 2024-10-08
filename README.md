# Guida all'Installazione e Avvio dell'Applicazione

## Prerequisiti

1. Docker
2. Docker Compose
3. Un account Together AI

## Passi per l'Installazione

### 1. Installare Docker

Se non hai già Docker installato sul tuo sistema, segui questi passaggi:

1. Visita il [sito ufficiale di Docker](https://www.docker.com/get-started)
2. Scarica e installa Docker Desktop per il tuo sistema operativo (Windows, macOS, o Linux)
3. Segui le istruzioni di installazione fornite per il tuo sistema operativo

### 2. Generare la Chiave API di Together AI

1. Accedi al tuo account [Together AI](https://www.together.ai/) o creane uno nuovo
2. Vai alla sezione delle impostazioni del tuo account
3. Cerca l'opzione per generare una nuova chiave API
4. Copia la chiave API generata

### 3. Configurare il File .env

1. Nella directory principale del progetto, crea un file chiamato `.env` se non esiste già
2. Apri il file `.env` con un editor di testo
3. Aggiungi la seguente riga, sostituendo `<TUA_CHIAVE_API>` con la chiave API di Together AI che hai copiato:

   ```
   TOGETHERAI_API_KEY=<TUA_CHIAVE_API>
   ```

4. Salva e chiudi il file

### 4. Costruire l'Immagine Docker

Nella directory principale del progetto, esegui il seguente comando per costruire l'immagine Docker:

```bash
docker compose build
```

Questo comando costruirà tutte le immagini Docker necessarie per l'applicazione come specificato nel file `docker-compose.yml`.

### 5. Avviare l'Applicazione

Una volta completata la costruzione dell'immagine, puoi avviare l'applicazione con il seguente comando:

```bash
docker compose up
```

Questo comando avvierà tutti i servizi definiti nel file `docker-compose.yml`.

## Accesso all'Applicazione

Dopo aver avviato l'applicazione, puoi accedere al frontend navigando nel tuo browser web a:

```
http://localhost:3000
```

## Note Aggiuntive

- Per arrestare l'applicazione, premi `Ctrl+C` nel terminale dove hai eseguito `docker compose up`.
- Per eseguire l'applicazione in background, usa il comando `docker compose up -d`.
- Per visualizzare i log dell'applicazione in esecuzione in background, usa `docker compose logs -f`.

Congratulazioni! Hai completato con successo l'installazione e l'avvio dell'applicazione.
