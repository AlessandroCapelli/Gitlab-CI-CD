# Gitlab CI/CD
## Alessandro Capelli

Implementazione di un'applicazione web che consiste nella possibilità di inserire, in un database, utenti (rappresentati come <id, email, password>) ed effettuare semplici operazioni sugli stessi. L'applicazione web è stata sviluppata in Python (utilizzando il framework Flask), ispirandosi al paradigma REST, ed implementa un database relazionale PostgreSQL per il salvataggio dei dati. Per quanto riguarda il file YML per l'implementazione della pipeline, è stato scelto l'utilizzo dell'immagine "python", e le fasi scelte sono state le seguenti:

- Build
- Verify
- Unit-Test
- Integration-Test
- Deploy

E' stato scelto l'utilizzo di un ambiente virtuale (virtualenv) per l'esecuzione degli script Python su GitLab e l'utilizzo di cache globali per il salvataggio delle dipendenze Python, così da evitare l'installazione delle stesse ad ogni job.

### Build

La fase di build consiste nell'installazione delle dipendenze Python (tramite comando "pip install -r requirements.txt") necessarie all'esecuzione dell'applicazione vera e propria (app.py).

### Verify

La fase di verifica consiste nell'installazione e successiva esecuzione di Flake8, utilizzato per effettuare un controllo sul codice (analisi statica del codice sorgente di app.py e dei test) Python in termini di stile e qualità.

### Unit-Test

La fase di unit-test consiste nell'esecuzione di un programma di test che, tramite l'utilizzo della libreria UnitTest, effettua un test sul corretto funzionamento dell'applicazione in termini di singole unità. E' stato scelto il test della funzione che non si connette al database (che rientrerebbe nell'integration-test) ma che gestisce la richiesta GET del default path.

### Integration-Test

La fase di integration-test consiste nell'esecuzione di un programma di test che, tramite l'utilizzo della libreria UnitTest, effettua una serie di test sul corretto funzionamento dell'applicazione in termini di integrazione tra l'applicativo e il database. Per poter effettuare un test di integrazione, è stato necessario l'utilizzo del servizio "postgres" così da poter simulare una reale connessione al database che risiede sulla stessa macchina dell'applicazione.

### Deploy

Per la fase di deploy è stato scelto l'utilizzo del servizio Heroku su cui effettuare il rilascio dell'applicazione web. Per effettuare il caricamento dei files necessari, si è scelto di utilizzare Git.

### Problematiche

La pipeline durante l'esecuzione dei vari stages produce il seguente warning:
`WARNING: venv/include/python3.8: chmod venv/include/python3.8: no such file or directory (suppressing repeats) `
Come riportato nella seguente discussione: [https://gitlab.com/gitlab-org/gitlab-foss/issues/19770] non è al momento presente un'effettiva soluzione al problema; inoltre, la documentazione ufficiale di gitlab specifica di utilizzare un ambiente virtuale in aggiunta alla cache [https://docs.gitlab.com/ee/ci/caching/#caching-python-dependencies]. Essendo un problema riscontrato da molti utenti, legato ai symlink, non abbiamo avuto modo di risolverlo all'interno del nostro progetto.
