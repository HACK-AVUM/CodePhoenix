# Refactoring del programma COBOL in Java

## Modifiche apportate

1. **Linguaggio di Programmazione**: 
   - Il codice è stato convertito da COBOL a Java.

2. **Struttura del Programma**:
   - La struttura di base è stata mantenuta, ma adattata alla sintassi di Java.
   - È stata creata una classe `RaddoppiaNumero`.

3. **Input e Output**:
   - In COBOL, l'input era gestito con `ACCEPT`. In Java, abbiamo utilizzato la classe `Scanner` per leggere l'input dell'utente.
   - L'output è stato realizzato con `System.out.println` invece di `DISPLAY`.

4. **Logica di Raddoppio**:
   - La logica di raddoppio è stata estratta in un metodo privato `raddoppia`, migliorando la modularità e la leggibilità del codice.

5. **Chiusura dello Scanner**:
   - È stato aggiunto `scanner.close()` per chiudere il `Scanner` e liberare risorse.

## Conclusioni

Il programma mantiene la stessa funzionalità del codice COBOL originale, ma sfrutta le caratteristiche moderne di Java, come la modularità e una gestione più efficiente dell'input/output.
