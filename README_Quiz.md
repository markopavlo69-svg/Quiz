# Quiz Game

Ein interaktives Quizspiel mit verschiedenen Kategorien und Highscore-System.

## Features

- Mehrere Kategorien (Gaming, Python)
- Punktesystem (+10 für richtig, -5 für falsch)
- Persistente Highscore-Liste (Top 5)
- Multiple-Choice-Fragen

## Verwendung

```bash
python quiz.py
```

## Spielablauf

1. Namen eingeben
2. Kategorie wählen (Gaming oder Python)
3. 3 Fragen beantworten (A, B oder C)
4. Ergebnis und Highscores anzeigen

## Beispiel

```
=== QUIZ GAME ===

Bitte Namen eingeben: Marko
Kategorien:
Gaming
Python
Wähle Kategorie: 1 für Gaming 2 für Python

1 von 3
Wie heißt der Electro Archon von Inazuma?

A: Raiden
B: Zhongli
C: Venti

Bitte auswählen: A
Deine Antwort: A Richtig! + 10 Punkte
```

## Datenspeicherung

Highscores werden in `highscores.txt` gespeichert.

## Technologien

- Python 3
- Listen und Dictionaries
- Dateioperationen
- Lambda-Funktionen für Sortierung

## Lernziele

- Funktionen definieren und aufrufen
- Verschachtelte Datenstrukturen
- Bedingte Logik und Schleifen
- Datei-I/O mit Fehlerbehandlung
