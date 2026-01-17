highscores = []
try:
    with open("highscores.txt", "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split(",")
            highscores.append({"name": teile[0], "punkte": int(teile[1])})
except FileNotFoundError:
    pass
kategorien = ["Gaming", "Python"]
print ("=== QUIZ GAME === \n")
name = input("Bitte Namen eingeben: \n")
print ("Kategorien : \n")
for kategorie in kategorien:
    print (kategorie)
auswahl = input( "Wähle Kategorie: 1 für Gaming 2 für Python \n ")
auswahl = int(auswahl)
fragen = [
        {"Frage " : "Wie heißt der Electro Archon von Inazuma? ", "antworten": ["A: Raiden", "B: Zhongli", "C: Venti"], "richtig" : "A"},
         {"Frage " : "Wer ist der Antoganist in FF7? ?", "antworten": ["A: Cloud","B: Sephiroth", "C: Barett" ], "richtig": "B"},
         {"Frage " : "Was ist der höchste Rank in RL? ", "antworten": ["A: SSL","B: Holz", "C: Platin" ], "richtig": "A"}
         ]    

def quiz(fragen):
    num = 1
    punkte = 0
    for frage in fragen:
        
        print(num, "von 3","\n", frage["Frage "], "\n", "\n")
        
        for antwort in frage["antworten"]:
            print(antwort, "\n")
        eingabe = input("Bitte auswählen: ")
        
        
        if eingabe == frage["richtig"]:
            punkte = punkte + 10
           

            print ("Deine Antwort: ", eingabe, "Richtig! ", "+", punkte, "Punkte \n")
        elif eingabe != frage["richtig"]:
             punkte = max(0,punkte - 5)
             
             print ("Deine Antwort: ", eingabe, "Falsch! ", "-", punkte, "Punkte \n")
                
        num = num + 1
    
        
    print("=== ERGEBNIS === \n",punkte, "Punkte: ", "von 30", "Punkten", "\n" )
    return punkte

if auswahl == 1:
    punkte = quiz(fragen)
elif auswahl == 2:
    python_fragen = [
        {"Frage " : "Was gibt print() aus?", "antworten": ["A: Nichts", "B: Text auf Konsole", "C: Eine Datei"], "richtig" : "B"},
        {"Frage " : "Was ist eine Liste?", "antworten": ["A: Eine Zahl", "B: Ein Text", "C: Eine Sammlung"], "richtig" : "C"},
        {"Frage " : "Was macht len()?", "antworten": ["A: Länge zählen", "B: Löschen", "C: Addieren"], "richtig" : "A"}
    ]
    punkte = quiz(python_fragen)
highscores.append({"name": name, "punkte": punkte})
highscores.sort(key=lambda x: x["punkte"], reverse=True)
highscores = highscores[:5]
print("\n=== HIGHSCORES ===")
for i, score in enumerate(highscores):
    print(f"{i+1}. {score['name']} - {score['punkte']} Punkte")
with open("highscores.txt", "w") as datei:
    for score in highscores:
        datei.write(f"{score['name']},{score['punkte']}\n")
print("Spiel beendet!")
    
   

    