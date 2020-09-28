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
elif choice == 'B' : 
     print(" Sorry, Ik heb tot nu toe elke lokaal gevonden")
     print(" Het was A, Ik heb wel telkens in de goede trein gezeten")
else: 
     print(" Sorry , ik had hiervoor nog nooit geprogammeerd")
     print(" Het was A Ik heb tot nu toe elke keer in de goede trein gezeten")
   

print(" ")
print("Creator: Dit is het einde van de quiz. Ik hoop dat je mij beter heb leren kennen en dat je het leuk vond" +" " + naam + "!")

