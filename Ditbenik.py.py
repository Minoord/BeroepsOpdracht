# Michelle's beroepsopdracht code
 
print("Hello You!, ik ben Michelle" + ". " + "Wie ben jij?") 
naam = input() 
print("Hello" + " " + naam)
print("Het is vandaag:")

from datetime import datetime
datum = datetime.now()
print( datum)

print(" Er komt nu een quiz over mij als een nieuwkomer op het Mediacollege Amsterdam . je krijgt de keuzes A,B,C schrijf deze graag in hoofdletters letters op. Als je iets verkeerd type is je antwoord gelijk C ")
print(" Nu je weet wat je moet doen, laten we dan nu beginnen!")

print(" ")
print(" Wat voor een opleiding heb ik hiervoor gedaan?")
print(" A = Havo")
print(" B = Mavo ")
print(" C = Vwo ")
choice = input()
if choice == 'A' :
     print(" Sorry, het was B Mavo")
elif choice == 'B' : 
     print(" Gefeliciteerd, je hebt het goed!")
else: 
     print(" Sorry, het was B Mavo")
   

print(" ")
print(" Welke opleiding wilde ik doen voor dat ik deze opleiding had gezien?")
print(" A = Politie Acedemy ")
print(" B =  De zelfde opleiding alleen dan op het ROC ")
print(" C = Dit was mijn eerste keuze ")
choice = input()
if choice == 'A' :
     print(" Sorry,  Het was C: dit was mijn eerste keuze")
     print(" Ik heb wel er over na gedacht, maar het was niks voor mij")
elif choice == 'B' : 
     print(" Sorry, Het C: dit was mijn eerste keuze")
     print(" Het ROC sprak mij niet aan als school zijnde")
else: 
     print(" Gefeliciteerd, je hebt het goed!")
     print("Ik had deze opleiding gezien en wilde het meteen doen.")  


print(" ")
print(" Welke bewering over mij is FOUT?")
print(" A = Ik was de eerste dag in de verkeerde trein gestapt. ")
print(" B = Ik heb tot nu toe alle lokalen kunnen vinden")
print(" C = Ik had hiervoor geen progameer skills")
choice = input()
if choice == 'A' :
     print(" Gefeliciteerd, je hebt het goed!")
     print("Ik heb tot nu toe, telkens in de goede trein gezeten.")
     print("  ") 
     print(" Bonus vraag!: ")
     print(" Welke trein neem ik op de heen reis")
     print(" A = De intercity naar Amsterdam Centraal" ) 
     print(" B = De sprinter naar Leiden Centraal" ) 
     print(" C = De intercity naar Enkhuizen") 
     choice = input()
     if choice == 'A': 
        print(" Gefeliciteerd, je hebt het goed!")
     elif choice =='B': 
          print(" Sorry, ik neem nooit de sprinter. Ik neem A de intercity naar Amsterdam Centraal")
     else:
          print( " Sorry, ik neem deze trein soms op de terug weg. Het was A de intercity naar Amsterdam Centraal")
elif choice == 'B' : 
     print(" Sorry, Ik heb tot nu toe elke lokaal gevonden")
     print(" Het was A, Ik heb wel telkens in de goede trein gezeten")
     print("  ") 
     print(" Bonus vraag!: ")
     print("Ken ik het heel school gebouw uit mijn hoofd? ")
     print(" A = Ja" ) 
     print(" B = Nope" ) 
     print(" C = Welke school gebouw?") 
     choice = input()
     if choice == 'A': 
        print(" Sorry, het was B. Ik ben alleen boven geweest en als je binnenkomt rechts voor de rest ken ik het gebouw niet.")
     elif choice =='B': 
          print("Gefeliciteerd, je hebt het goed!")
     else:
          print( " Dit antwoord is niet goed en niet fout. Je hebt de vraag niet begrepen en dat is niet jouw fout. Ik had het over het schoolgebouw waar ik in studeer of te wel Ma contactweg 36 ")
          print(" Mijn exuses dat ik de vraag niet duidelijk had gesteld") 
else: 
     print( " Sorry, ik neem deze trein soms op de terug weg. Het was A de intercity naar Amsterdam Centraal")
     print(" Sorry, Ik heb tot nu toe elke lokaal gevonden")
     print(" Het was A, Ik heb wel telkens in de goede trein gezeten")
     print("  ") 
     print(" Bonus vraag!: ")
     print("Waarom wilde ik leren te progameren? ")
     print(" A = Omdat ik het makkelijk vind" ) 
     print(" B = Mijn droom is om een game te maken" ) 
     print(" C = Omdat mijn ouders het ook doen en het mij leuk leek") 
     choice = input()
     if choice == 'A': 
        print(" Sorry, het was B. Ik vind het soms nog moeilijk en ik heb het nooit makkelijk gevonden .")
     elif choice =='B': 
          print("Gefeliciteerd, je hebt het goed!")
          print("Ik heb al sinds ongeveer 5 jaar die droom, alleen nooit iets meegedaan") 
     else:
          print( " Sorry, het was B. Mijn ouders toen iets totaal anders. ")
   

print(" ")
print("Creator: Dit is het einde van de quiz. Ik hoop dat je mij beter heb leren kennen en dat je het leuk vond" +" " + naam + "!")

