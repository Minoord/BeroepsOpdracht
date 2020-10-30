import time 
print("-- Computer: In deze textbased applicatie speel je als een vluchteling Aladin.")
print("Hij is 35 jaar en woont in Marokko. Hij lijdt twee levens eentje die hij liever geheim houd en zijn normale leven.")
print("Het verhaal begint als hij net thuis komt van zijn werk. Voordat we beginnen moet ik wel iets mededelen, dit verhaal is gebaseerd op twee echte vluchtelingen verhalen, maar ook een gedeeld ")
print("is verzonnen. Laten we nu beginnen --")
print("")

Stuk0 = True


while Stuk0 == True:
    #Stukje 0 t/m 5 --- Einde moet nog worden gemaakt----
    print("Je komt je huis binnen en loopt de woonkamer in waar je jouw vrouw ziet zitten met een bezorgd gezicht.")
    print("---Computer: Je krijgt nu een keuze voor je. Een keuze bestaat uit A en B. Je moet daarom a of b invullen, als je iets anders invult wordt je antwoord standaard B. ---")
    print("A= Vraag wat er mis is")
    print("B= Vraag of het eten al klaar is")
    stuk0 = input()
    if stuk0 == "A" or stuk0 == "a":
        #stukje 1 -- Klaar
        print("Je vraagt je vrouw wat er mis is. Ze kijkt je aan met een bang gezicht. Vervolgens staat ze op en vertelt ze dat ze jouw tweede leven heeft gevonden.")
        print("Waarneer ze dit zegt voel je een koude rilling over je rug lopen. Je vraagt of ze het tegen iemand heeft vertelt, waarop ze ja knikt. Wat ga je doen?")
        print("A= Word boos op haar")
        print("B= De kamer verlaten om je gedachten op een rijtje te zetten ")
        stuk1 = input()
        if stuk1 == "A" or stuk1 == "a":
            #Stukje 3-- klaar
            print("Je voelt je langzaam boos worden op je vrouw. Je begint tegen haar te schreeuwen en geeft haar vervolgens een klap in haar gezicht.")
            print("je beseft wat je hebt gedaan en loopt vervolgens naar je kamer. Op je kamer begin je na te denken.")
            print("Ze heeft je leven nu een stuk moeilijker gemaakt. Je weet wat die gasten kunnen doen en ze zijn niet bang om mensen te vermoorden. Je besluit te vluchten")
            
        else:
            #Stukje 4---- klaar
            print("Je loopt snel naar je kamer toe en je gaat bedenken wat je nu gaat doen.")
            print("Je kan gewoon door blijven leven en hopen dat er niks gebeurd of je kan gaan vluchten, want je weet dat als ze hier achter komen, dat je dood bent.")
            print("A= Vluchten")
            print("B= Afwachten")
            stuk4 = input()
            if stuk4 == "A" or stuk4 == "a":
                Stuk6 = True
            else:
                #Stukje 5-- Alleen einde---
                print("5 weken zijn er voor bij gegaan. Je ontvangt steeds dreigbrieven en jij en je huis worden af en toe belaagd met stenen.")
                print("Je overweegt om te vluchten of te blijven. Als je vlucht moet je jouw familie achterlaten, maar als je hier blijft word het je dood.")
                print("Je zit de opties te overwegen als je een brief binnen krijgt. Je vermoedt dat het een dreigbrief is, maar je opent hem alsnog.")
                print("Je komt erachter dat het weer een dreigbrief is. In de dreigbrief staat dat je nog maar 2 dagen te leven hebt voor dat je executie begint.")
                print("Je weet dat de politie je niet kan helpen. Je besluit om nog af te wachten.")
                print("Op een nacht als je ligt te slapen hoor je beneden veel geluid. Je besluit om te gaan kijken.")
                print("Als je beneden komt zie je jouw heel woonkamer in puin. Je wilt je omdraaien, maar voelt een pijnscheut in je zij en vervolgens volgt er nog een in je rug.")
                print("Je draait je om en ziet iemand staan met een mes met bloed. De persoon met het mes steekt je in je ribbenkast.")
                print("Je smeekt naar god dat je familie ongedeerd is en daarna gaan alle lichten uit.")
                print("")
                print("Wil je verder gaan met het verhaal vanaf het moment dat je vlucht of wil je stoppen ")
                print("A= Verder")
                print("B= Stoppen")
                einde1 = input()
                if einde1 == "A" or einde1 == "a":
                    print("")
                else:
                    print("Bedankt voor het testen!")
                    time.sleep(1) 
                    exit()
                    

            
    else:
        #Stukje 2 -- Klaar
        print("Je vraagt aan je vrouw of het eten al klaar is en ze kijkt je aan met een bang gezicht. Vervolgens staat ze op een loopt naar de keuken.")
        print("Even later hoor je veel lawaai uit de keuken komen en je rent naar de keuken toe, waar je ziet dat het raam is ingegooid met stenen.")
        print("Je ziet je vrouw met glas stukjes in haar gezicht op de grond liggen. Je belt een ambulance en niet veel later word je vrouw  meegenomen naar het ziekenhuis.")
        print("")
        #Stukje 5-- Alleen einde---
        print("5 weken zijn er voor bij gegaan. Je ontvangt steeds dreigbrieven en jij en je huis worden af en toe belaagd met stenen.")
        print("Je overweegt om te vluchten of te blijven. Als je vlucht moet je jouw familie achterlaten, maar als je hier blijft word het je dood.")
        print("Je zit de opties te overwegen als je een brief binnen krijgt. Je vermoedt dat het een dreigbrief is, maar je opent hem alsnog.")
        print("Je komt erachter dat het weer een dreigbrief is. In de dreigbrief staat dat je nog maar 2 dagen te leven hebt voor dat je executie begint.")
        print("Je weet dat de politie je niet kan helpen. Je besluit om nog af te wachten.")
        print("Op een nacht als je ligt te slapen hoor je beneden veel geluid. Je besluit om te gaan kijken.")
        print("Als je beneden komt zie je jouw heel woonkamer in puin. Je wilt je omdraaien, maar voelt een pijnscheut in je zij en vervolgens volgt er nog een in je rug.")
        print("Je draait je om en ziet iemand staan met een mes met bloed. De persoon met het mes steekt je in je ribbenkast.")
        print("Je smeekt naar god dat je familie ongedeerd is en daarna gaan alle lichten uit.")
        print("")
        print("Wil je verder gaan met het verhaal vanaf het moment dat je vlucht of wil je stoppen of wil je helemaal op nieuw beginnen?")
        print("A= Vluchten")
        print("B= Stoppen")
        einde2 = input()
        if einde2 == "A" or einde2 == "a":
            print("")
        else:
            print("Bedankt voor het testen!")
            time.sleep(1) 
            exit()
        


    #stukje 6 t/m 8--- klaar  
    print("Je hebt besloten te vluchten. Je pakt je spullen en vertrekt midden in de nacht. Je wilt je familie niet achterlaten,")
    print("maar je hebt geen keuze, want de smokkelaar die je naar Engeland  brengt vraagt je teveel om je familie mee te nemen. Je komt op de plek aan, waar je met de smokkelaar hebt afgesproken.")
    print("Je ziet hem daar al staan bij een busje. Hij vraagt je om het busje in te stappen en dat doe je ook. Niet veel later zijn jullie onderweg naar een vliegveld")
    print("Ga je met de smokkelaar praten of blijf je stil?")
    print("A= Praten")
    print("B= stil blijven")
    stuk6 = input()
    if stuk6 == "A" or stuk6 == "a":
        #Stukje 7-- klaar
        print("Je vraagt de smokkelaar waarom hij mensen over de grens heen smokkelt. De smokkelaar zucht en vraagt je om stil te blijven. Je wilt ja zeggen, maar besluit om niets te zeggen.")
        print("")

    else:
        #Stukje 8-- klaar
        print("Je besluit om niets te zeggen. Je kijkt wat naar buiten en hoopt dat je snel bij het vliegtuig aan komt.")
        print("")


    #stukje 9 t/m 16-- Alleen nog de eindes--
    #Stukje 9--klaar
    print("Je komt op het vliegveld. Tot nu toe is alles soepel gegaan. Je hebt geen gesprek met de smokkelaar gehad, dus je weet ook niet wat er gaat gebeuren.")
    print("Blijkbaar heeft hij een nep paspoort voor je gemaakt en voordat je het weet zit je in het vliegtuig. Het vliegtuig landt in Turkije en je begint twijfels te krijgen over het vluchten,")
    print("maar je gaat verder. In Turkije brengt de smokkelaar je naar een garage. Waar je samen met hem in een auto gaat zitten en jullie beginnen te rijden.")
    print("")
    print("Na een paar dagen rijden komen jullie aan in Nederland. Jullie stopen voor een tankstation, omdat de smokkelaar iets moet doen.")
    print("Je blijft een tijdje wachten en je begint jezelf af te vragen waar de smokkelaar blijf. Wat ga je doen?") 
    print("A= Blijf wachten")
    print("B= Ga naar hem opzoek")
    stuk9 = input()
    if stuk9 == "A" or stuk9 == "a":
        #Stukje 10-- Alleen nog het einde---
        print("Je besluit om een nog even te wachten. Na 1 uur begin je weer te twijfelen, maar je besluit om toch te blijven te wachten.")
        print("Het begint ook al aardig koud te worden. Het is namelijk al winter.")
        print("")
        print("Voordat je het weet val je in slaap en je begint te dromen. Je droomt over je leven wat er gebeurd is, de fouten die je hebt gemaakt, de leuke herinneringen en de stomme.")
        print("Opeens begint je droom te veranderen en je ziet jezelf andere keuzes maken met andere uitkomsten. De uitkomsten zijn niet altijd zo leuk, andere wel.")
        print("Nadat je alle opties hebt gezien ben je blij dat je gevlucht bent en daarna werd alles zwart. Je vraagt je af wat er gebeurd.")
        print("Je voelde jezelf steeds meer verlammen en niet veel later stopt alles. Je bent dood gevroren")
        print("EINDE: BEVROREN") 
        print("")
        print("Wil je verder gaan met het verhaal vanaf het moment dat je hem gaat zoeken of wil je stoppen? ")
        print("A= Zoeken")
        print("B= Stoppen")
        einde3 = input()
        if einde3 == "A" or einde3 == "a":
            print("")
        else:
            print("Bedankt voor het testen!")
            time.sleep(1) 
            exit()        

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
    else:
        #Stukje 11--klaar
        print("Je gaat naar hem opzoek. Je begint met het rondkijken op de parkeerplaats, maar je ziet hem niet.")
        print("Je gaat bij de tankstation naar binnen. Je kijkt daar goed rond, maar ziet hem daar ook niet.")
        print("Je gaat vervolgens weer na buiten en ziet de auto van de smokkelaar weg is.")
        print("Je raakt lichtelijk in paniek. Had je toch maar moeten wachten of was dit het plan van te voren al zo bedacht.")
        print("Je gaat heel even op de stoep rand zitten en begint na te denken. Wat ga je doen?")
        print("A= Je gaat weer na binnen en vraagt in je best Engels of ze je kunnen helpen.")
        print("B= Je kijkt nog een keer goed rond.")
        stuk11 =input() 
        if stuk11 == "A" or stuk11 == "a":
            #Stukje 12--klaar--
            print("Je loopt het Tankstation binnen en vraagt in je beste Engels waar het dichtsbijzijnde politiebureau is.")
            print("Het winkelpersoneel verteld je dat het meer dan 10 km vanaf het tankstation ligt.")
            print("Een klant in de winkel die jullie gesprek hoorde biedt je aan om je er naar toe te brengen.")
            print("A= Accepteer de aanbod")
            print("B= Zeg beleefd dat het niet hoeft")
            stuk12 =input()
            if stuk12 == "A" or stuk12 == "a":
                #Stukje 14--klaar--
                print("Je accepteert het aanbod van de klant en voordat je het weet zitten jullie samen in de auto naar het politiestation.")
                print("De klant vraagt onderweg in het Engels waar je vandaan komt, hoe je hier bent gekomen en waarom je hier bent gekomen enzovoort.")
                print("Je vind het fijn om weer eens met iemand een langdurig gesprek te houden, maar je voelt je niet comfortabel bij de vragen die hij stelt. ")
                print("Toch beantwoord je de vragen, want je vind dat je hem het schuldig bent nadat hij zo aardig was om je naar het politiebureau te brengen. ")
                print("Na wat vragen eindigt de rit. Hij wijst naar een groot gebouw en zegt dat dat het politiebureau was.")
                print("Je bedankt hem uit de grond van je hart en je gaat de auto uit op weg naar het politiebureau. Opeens zie je een portemonnee op de grond liggen.")
                print("Je pakt de portemonnee op en je ziet dat er 500 euro in zit. Dat is precies genoeg om de boot naar Engeland te nemen en een taxi daarnaar toe.")
                print("Neem je de portemonnee mee en ga je naar Engeland toe of lever je de portemonnee in bij de politie?")
                print("A= Naar Engeland")
                print("B= Naar Politiebureau ")
                stuk14 =input()
                if stuk14 == "A" or stuk14 == "a":
                    #Stukje 16--Alleen nog het einde--
                    print("Je kiest er voor om het geld te pakken en naar Engeland te gaan.")
                    print("Je pakt de eerste taxi die je ziet. Hij brengt je naar de haven, waar je een kaartje koopt voor de eerste beste boot naar Engeland.")
                    print("Daarna wacht je op de boot. Na een tijdje komen twee politie-agenten langs lopen. Ze zien je wachten en vragen om je ID.")
                    print("Je zegt dat je geen ID bij je heb en precies op dat moment valt de portemonnee op de grond. Een van de agent pakt de portemonnee op en ziet een Identiteitskaart zitten.")
                    print("Hij pak de ID en ziet dat het niet jouw ID is en vraagt of je de persoon op de ID kent.")
                    print("Je knikt ja, maar ze kijken je nog steeds verdacht aan. Ze vragen of het familie van je is en je knikt weer ja.")
                    print("Dan nemen ze je mee naar het politiebureau. Je moest heel even wachten in een kamer. Na 20 minuten wachten komen er twee agenten binnen.")
                    print("Ze zeggen dat je wordt gearresteerd voor diefstal en omdat ze je niet konden vinden in de database willen ze een uitleg over wie je bent.")
                    print("Je legt je verhaal uit en de agenten begrijpen het.")
                    print("Helaas omdat je iets hebt gestolen, moet je twee nachten doorbrengen in de cel en daarna werd je terug gestuurd naar je thuisland.")
                    print("Hier word je binnen een week neergeschoten. Al die moeite voor niks omdat je naar Engeland wilde.")
                    print("EINDE: DIEF!")
                    print("")
                    print("Wil je verder gaan met het verhaal vanaf het moment dat je op het politiebureau komt met de portemonnee of wil je stoppen?")
                    print("A= Politiebureau")
                    print("B= Stoppen")
                    einde4 = input()
                    if einde4 == "A" or einde1 == "a":
                        print("")
                    else:
                        print("Bedankt voor het testen!")
                        time.sleep(1) 
                        exit()                   
                else:
                    print("") 
                    
            else:
                #Stukje 15--klaar--
                print("Je zegt heel beleefd dat het niet hoeft en je loopt de tankstation uit. Waarneer je buiten komt begin je in de richting te lopen waar de kassière heen wees.")
                print("Terwijl je loopt wordt het langzaam donker en steeds kouder. Gelukkig ben je een snelle loper en ben je zo in de stad.")
                print("Je loopt wat rond totdat je een portemonnee op de grond ziet liggen. Je pakt de portemonnee op en je ziet dat er 500 euro in zit.")
                print("Dit is precies genoeg om de boot naar Engeland te nemen en een taxi daarna toe.")
                print("Neem je de portemonnee mee en ga je naar Engeland toe of lever je de portemonnee in bij de politie?")
                print("A= Naar Engeland")
                print("B= Naar Politiebureau")
                stuk15 =input()
                if stuk15 == "A" or stuk15 == "a":
                    #Stukje 16--Alleen nog het einde--
                    print("Je kiest er voor om het geld te pakken en naar Engeland te gaan.")
                    print("Je pakt de eerste taxi die je ziet. Hij brengt je naar de haven, waar je een kaartje koopt voor de eerste beste boot naar Engeland.")
                    print("Daarna wacht je op de boot. Na een tijdje komen twee politie-agenten langs lopen. Ze zien je wachten en vragen om je ID.")
                    print("Je zegt dat je geen ID bij je hebt en precies op dat moment valt de portemonnee op de grond. Een van de agent pakt de portemonnee op en ziet een Identiteitskaart zitten.")
                    print("Hij pak de ID en ziet dat het niet jouw ID is en vraagt of je de persoon op de ID kent.")
                    print("Je knikt ja, maar ze kijken je nog steeds verdacht aan. Ze vragen of het familie van je is en je knikt weer ja.")
                    print("Dan nemen ze je mee naar het politiebureau. Je moet heel even wachten in een kamer. Na 20 minuten wachten komen er twee agenten binnen.")
                    print("Ze zeggen dat je wordt gearresteerd voor diefstal en omdat ze je niet konden vinden in de database wilden ze een uitleg wie je was.")
                    print("Je legt je verhaal uit en de agenten begrijpen het.")
                    print("Helaas omdat iets hebt gestolen, moet je twee nachten doorbrengen in de cel en daarna word je terug gestuurd naar je thuisland.")
                    print("Hier word je binnen een week neergeschoten. Al die moeite voor niks omdat je naar Engeland wilde.")
                    print("EINDE: DIEF!")
                    print("")
                    print("Wil je verder gaan met het verhaal vanaf het moment dat je op het politiebureau komt met de portemonnee of wil je stoppen?")
                    print("A= politiebureau")
                    print("B= Stoppen")
                    einde5 = input()
                    if einde5 == "A" or einde5 == "a":
                        print("")
                    else:
                        print("Bedankt voor het testen!")
                        time.sleep(1) 
                        exit()
                else:
                    print("")
        else:
            #Stukje 13--klaar--
            print("Je kijkt nog een keertje rond, maar je ziet hem niet. ")
            print("Je loopt naar zijn auto toe en kijkt naar binnen, maar ziet niks.")
            print("Je loopt weg van de auto en gaat vervolgens het Tankstation binnen en vraagt in je beste Engels waar het dichtsbijzijnde politiebureau is.")
            print("Het winkelpersoneel verteld je dat het meer dan 10 km vanaf het tankstation ligt.")
            print("Een klant in de winkel die jullie gesprek hoort biedt je aan om je er naar toe te brengen.")
            print("A= Accepteer de aanbod")
            print("B= Zeg beleefd dat het niet hoeft")
            stuk12 =input()
            if stuk12 == "A" or stuk12 == "a":
                #Stukje 14--klaar--
                print("Je accepteer het aanbod van de klant en voordat je het weet zitten jullie samen in de auto naar het politiestation.")
                print("De klant vraagt onderweg in het Engels waar je vandaan komt, hoe je hier bent gekomen en waarom je hier bent gekomen enzovoort.")
                print("Je vind het fijn om weer eens met iemand een langdurig gesprek te houden, maar je voelt je niet comfortabel bij de vragen die hij stelt. ")
                print("Toch beantwoordt je de vragen, want je vind dat je hem het verschuldigd bent nadat hij zo aardig was om je naar het politiebureau te brengen. ")
                print("Na wat vragen eindigt de rit. Hij wijst naar een groot gebouw en zegt dat dat het politiebureau is.")
                print("Je bedankte hem uit de grond van je hart en je gaat de auto uit op weg naar het politiebureau. Opeens zie je een portemonnee op de grond liggen.")
                print("Je pakt de portemonnee op en je ziet dat er 500 euro in zit. Dat is precies genoeg om de boot naar Engeland te nemen en een taxi daarnaar toe.")
                print("Neem je de portemonnee mee en ga je naar Engeland toe of lever je de portemonnee in bij de politie?")
                print("A= Naar Engeland")
                print("B= Naar Politiebureau ")
                stuk14 =input()
                if stuk14 == "A" or stuk14 == "a":
                    #Stukje 16--Alleen nog het einde--
                    print("Je kiest er voor om het geld te pakken en naar Engeland te gaan.")
                    print("Je pakt de eerste taxi die je ziet. Hij brengt je naar de haven, waar je een kaartje koopt voor de eerste beste boot naar Engeland.")
                    print("Daarna wacht je op de boot. Na een tijdje komen twee politie-agenten langs lopen. Ze zien je wachten en vragen om je ID.")
                    print("Je zegt dat je geen ID bij je hebt en precies op dat moment valt de portemonnee op de grond. Een van de agent pakt de portemonnee op en ziet een Identiteitskaart zitten.")
                    print("Hij pak de ID en ziet dat het niet jouw ID is en vraagt of je de persoon op de ID kent.")
                    print("Je knikt ja, maar ze kijken je nog steeds verdacht aan. Ze vragen of het familie van je is en je knikt weer ja.")
                    print("Dan nemen ze je mee naar het politiebureau. Je moet heel even wachten in een kamer. Na 20 minuten wachten komen er twee agenten binnen.")
                    print("Ze zeggen dat je wordt gearresteerd voor diefstal en omdat ze je niet konden vinden in de database wilden ze een uitleg wie je was.")
                    print("Je legt je verhaal uit en de agenten begrijpen het.")
                    print("Helaas omdat iets hebt gestolen, moet je twee nachten doorbrengen in de cel en daarna word je terug gestuurd naar je thuisland.")
                    print("Hier word je binnen een week neergeschoten. Al die moeite voor niks omdat je naar Engeland wilde.")
                    print("EINDE: DIEF!")
                    print("")
                    print("Wil je verder gaan met het verhaal vanaf het moment dat je op het politiebureau komt met de portemonnee of wil je stoppen ")
                    print("A= Politiebureau")
                    print("B= Stoppen")
                    einde6= input()
                    if einde6 == "A" or einde6 == "a":
                        print("")
                    else:
                        print("Bedankt voor het testen!")
                        time.sleep(1) 
                        exit()
                 
                else:
                    print("") 
                    
            else:
                #Stukje 15--klaar--
                print("Je zegt heel beleefd dat het niet hoeft en je loopt de tankstation uit. Waarneer je buiten komt begin je in de richting te lopen waar de kassière heen wees.")
                print("Terwijl je loopt wordt het langzaam donker en steeds kouder. Gelukkig ben je een snelle loper en ben je zo in de stad.")
                print("Je loopt wat rond totdat je een portemonnee op de grond ziet liggen. Je pakt de portemonnee op en je ziet dat er 500 euro in zit.")
                print("Dit is precies genoeg om de boot naar Engeland te nemen en een taxi daarna toe.")
                print("Neem je de portemonnee mee en ga je naar Engeland toe of lever je de portemonnee in bij de politie?")
                print("A= Naar Engeland")
                print("B= Naar Politiebureau")

                stuk15 =input()
                if stuk15 == "A" or stuk15 == "a":
                    #Stukje 16--Alleen nog het einde--
                    print("Je kiest er voor om het geld te pakken en naar Engeland te gaan.")
                    print("Je pakt de eerste taxi die je ziet. Hij brengt je naar de haven, waar je een kaartje koopt voor de eerste beste boot naar Engeland.")
                    print("Daarna wacht je op de boot. Na een tijdje komen twee politie-agenten langs lopen. Ze zien je wachten en vragen om je ID.")
                    print("Je zegt dat je geen ID bij je hebt en precies op dat moment valt de portemonnee op de grond. Een van de agent pakt de portemonnee op en ziet een Identiteitskaart zitten.")
                    print("Hij pak de ID en ziet dat het niet jouw ID is en vraagt of je de persoon op de ID kent.")
                    print("Je knikt ja, maar ze kijken je nog steeds verdacht aan. Ze vragen of het familie van je is en je knikt weer ja.")
                    print("Dan nemen ze je mee naar het politiebureau. Je moet heel even wachten in een kamer. Na 20 minuten wachten komen er twee agenten binnen.")
                    print("Ze zeggen dat je wordt gearresteerd voor diefstal en omdat ze je niet konden vinden in de database wilden ze een uitleg wie je was.")
                    print("Je legt je verhaal uit en de agenten begrijpen het.")
                    print("Helaas omdat iets hebt gestolen, moet je twee nachten doorbrengen in de cel en daarna word je terug gestuurd naar je thuisland.")
                    print("Hier word je binnen een week neergeschoten. Al die moeite voor niks omdat je naar Engeland wilde.")
                    print("EINDE: DIEF!")
                    print("")
                    print("Wil je verder gaan met het verhaal vanaf het moment dat je op het politiebureau komt met de portemonnee of wil je stoppen?")
                    print("A =Vluchten")
                    print("B= Stoppen")
                    einde7 = input()
                    if einde7 == "A" or einde7 == "a":
                        ("Restarting the program")
                    else:
                        print("Bedankt voor het testen!")
                        time.sleep(1) 
                        exit()
                    
                else:
                    print("") 
        


    #Stukje 17 t/m 19---klaar
    print("Je besloot om de portemonnee mee te nemen naar het politiebureau. Na een tijdje heb je het politiebureau gevonden. Je loopt naar binnen en je gaat naar de balie.")
    print("Vandaar af gaat alles heel snel. De agenten daar zijn heel aardig en begrijpen meteen je situatie")
    print("Ze pakken de portemonnee aan en ze wijzen je meteen door naar een stichting die vluchtelingen helpt en voordat je het weet heb je een dak boven je hoofd.")
    print("Een paar dagen later krijg je een bedankbrief van de persoon van de portemonnee met een doos chocola.")
    print("")
    print("Je blijft in het asielzoeker centrum voor 2 maanden en krijgt vervolgens een verblijfsvergunning. In de tussen tijd heb je ook alweer je bankrekening heropend en Nederlands geleerd.")
    print("Nu je dit alles hebt, begin je met het nadenken over waar je wilt wonen. Het enigste wat je kan betalen is een appartement of een klein huis buiten de stad. Waar wil je wonen?")
    print("A= Appartement")
    print("B= Klein huis")
    stuk17 = input()
    if stuk17 == "A" or stuk17 == "a":
        print("Je kiest om in het appartement te gaan wonen. Je krijgt alles rond met de bank en de vorige eigenaar en je hebt eindelijk je eigen woonplek.")
    else:
        print("Je kiest om in een klein huis te gaan wonnen. Je krijgt alles rond met de bank en de vorige eigenaar en je hebt eindelijk je eigen woonplek.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------        

    #Stukje 20 t/m 30
    #Stukje20
    print("Nu je een huis hebt gekregen maak je wel meer kosten en heb je dus een baan nodig. Je gaat online kijken of je een boekhouder kan worden. ")
    print("Je had in Marokko daar al een opleiding voor gedaan, maar je wist niet of die geldig is in Nederland. ")
    print("Je zoekt het op en je ziet dat het geldig is, maar je moes nog wel cursussen volgen voor een maand.")
    print("Je gaat kijken welke banen er zijn en vind een bedrijf die je aanspreekt, Boekhouders en Co. Daarnaast vind je ook nog een schoonmaakbedrijf die nog schoonmakers vragen.")
    print("Wat kies je?")
    print("A= Boekhouders en Co ")
    print("B= Schoonmaakbedrijf ")
    stuk20 = input()
    if stuk20 == "A" or stuk20 == "a":
        #Stukje 21
        print("Je besluit om te solliciteren bij het bedrijf Boekhouders en Co. Niet veel dagen later krijg je een email, je mag op gesprek komen.")
        print("Je was super blij en besluit meteen voor nieuwe kleding te gaan kijken. Voordat je het weet is het de dag van het sollicitatiegesprek ")
        print("en daar zit je dan recht tegenover een lang, bruinharige meneer. Hij begint je vragen te stellen en je beantwoordt ze allemaal.")
        print("Aan het einde van het gesprek wordt er gezegd dat je wordt aangenomen en dat je al je gegevens die ze nodig hebben moet mailen.")
        print("Je zegt meteen ja en je gaat met een blij gevoel naar huis. Als je thuis bent stuur je meteen al je gegevens door en ga je met een gelukkig gevoel naar bed.")
        print("De volgende dag bekijk je jouw email en je ziet een email er tussenstaan van Boekhouders en Co. Je opent de email en leest er in dat je toch niet bent aangenomen,")
        print("omdat je niet had gezegd dat je een vluchteling bent. Je voelt je zelf langzaam boos worden.")
        print("Ze hadden je niet aangenomen, omdat je een vluchteling bent, belachelijk!")
        print("Ga je weer op zoek naar een nieuwe baan of toch solliciteren bij het schoonmaakbedrijf?")
        print("A= Nieuwe baan")
        print("B= Schoonmaakbedrijf")
        stuk21= input()
        if stuk21 == "A" or stuk21 == "a":
            #Stukje 23
            print("Je gaat opzoek naar een nieuw baan en je vindt er een. Je solliciteert bij het bedrijf en je wordt aangenomen.")
            print("Al je collega’s zijn super aardig en je geniet van je werk.")
            
        else:
            #Stukje 22--klaar
            print("Je kiest er voor om te solliciteren bij het schoonmaakbedrijf en binnen een paar dagen hoor je dat je bent aangenomen.")
            print("Je bekijkt het salaris en komt er achter dat het niet genoeg is om van te leven. Je gaat weer voor een andere baan kijken.")
            print("wat voor een baan kies je?")
            print("A= Taxichauffeur")
            print("B= Winkelpersoneel")
            stuk22 = input()
            if stuk22 == "A" or stuk22 == "a":
                #Stukje 24--klaar
                print("Je kiest er voor om taxichauffeur te worden. Je word aangenomen en met twee banen tegelijke tijd krijg je genoeg geld om jezelf te onderhouden.")
                print("Helaas niet genoeg geld om je familie naar Nederland te halen, maar dat kan ook later nog.") 
                print("Op een nacht sta je te wacht op een nieuwe klant voor je taxi, een man komt naar je toe lopen en vraagt je om ergens heen te rijden.")
                print("Je zegt ja en jullie stappen beide in de auto. Voordat je begint te rijden vraagt de man of je wilde helpen in een drugs deal in ruil voor wat geld. Wat ga je zeggen?")
                print("A=Ja")
                print("B=Nee")
                stuk24 = input()
                if stuk24 == "A" or stuk24 == "a":
                   #Stukje 28--klaar
                    print("Je zegt ja tegen de man en de man geeft je wat plaatsen waar je heen moet gaan.")
                    print("Je gaat naar die plaatsen en zet daarna de man op zijn eindlocatie af. Voordat de man weg gaat geeft hij een je een envelop met geld en bedankt je.") 
                    print("")
                    print("Waarneer je thuis komt open je de envelop en ziet dat er wat geld in zat. Het was niet veel geld, maar je was er al blij mee.")
  
                else:
                    #Stukje 29--klaar
                    print("Je zegt nee en de man stapt uit, voordat hij wegloopt schopt hij  tegen je auto aan. ") 
                    print("Je wilde boos worden, maar je vind dat geen goed idee. Je ziet de man weglopen en je besluit om  je avond veder te gaan")

            else:
                #Stukje 25
                print("Je kiest er voor om in een winkel te werken. Je word aangenomen en met twee banen krijg je genoeg geld om jezelf te onderhouden.") 
                print("Je kan niet met elke collega om gaan, maar je geniet wel van je werk. Op een dag komt er een klant naar je toe en vraagt uit welk land je komt. Wat zeg je?")
                print("A= Wees eerlijk en beantwoord de vraag")
                print("B= vraag waarom hij dat moet weten")
                stuk25 = input()
                if stuk25 == "A" or stuk24 == "a":
                   #Stukje 26--klaar
                    print("Je vertelt de klant dat je uit Marokko komt en de man begint je uitschelden. ")
                    print("Een collega van je komt aan lopen en vraagt aan de klant of er een probleem is.") 
                    print("De man begint nu ook tegen je collega te schreeuwen.")
                    print("Niet veel later wordt de klant uit de winkel gezet en gaat alles gewoon weer door. Je voelt je wel rot, maar je kon er niks aan doen.")
  
                else:
                    #Stukje 27--klaar
                    print("Je vraagt aan de klant waarom hij dat wilt weten. De klant antwoord dat hij dat gewoon wilt weten. ") 
                    print("Je zegt dat je er niet comfortabel bij voelt en de klant loopt mompelend weg. Je vraagt je af waarom hij dat wilde weten, maar je laat het er bij.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    else:
        #Stukje 22--klaar
        print("Je kiest er voor om te solliciteren bij het schoonmaakbedrijf en binnen een paar dagen hoor je dat je bent aangenomen.")
        print("Je bekijkt het salaris en komt er achter dat het niet genoeg is om van te leven. Je gaat weer voor een andere baan kijken.")
        print("wat voor een baan kies je?")
        print("A= Taxichauffeur")
        print("B= Winkelpersoneel")
      
        stuk22 = input()
        if stuk22 == "A" or stuk22 == "a":
            #Stukje 24--klaar
            print("Je kiest er voor om taxichauffeur te worden. Je word aangenomen en met twee banen tegelijke tijd krijg je genoeg geld om jezelf te onderhouden.")
            print("Helaas niet genoeg geld om je familie naar Nederland te halen, maar dat kan ook later nog.") 
            print("Op een nacht sta je te wacht op een nieuwe klant voor je taxi, een man komt naar je toe lopen en vraagt je om ergens heen te rijden.")
            print("Je zegt ja en jullie stappen beide in de auto. Voordat je begint te rijden vraagt de man of je wilde helpen in een drugs deal in ruil voor wat geld. Wat ga je zeggen?")
            print("A=Ja")
            print("B=Nee")
            stuk24 = input()
            if stuk24 == "A" or stuk24 == "a":
               #Stukje 28--klaar
                print("Je zegt ja tegen de man en de man geeft je wat plaatsen waar je heen moet gaan.")
                print("Je gaat naar die plaatsen en zet daarna de man op zijn eindlocatie af. Voordat de man weg gaat geeft hij een je een envelop met geld en bedankt je.") 
                print("")
                print("Waarneer je thuis komt open je de envelop en ziet dat er wat geld in zat. Het was niet veel geld, maar je was er al blij mee.")

  
            else:
                #Stukje 29--klaar
                print("Je zegt nee en de man stapt uit, voordat hij wegloopt schopt hij  tegen je auto aan. ") 
                print("Je wilde boos worden, maar je vind dat geen goed idee. Je ziet de man weglopen en je besluit om  je avond veder te gaan")
                

        else:
            #Stukje 25
            print("Je kiest er voor om in een winkel te werken. Je word aangenomen en met twee banen krijg je genoeg geld om jezelf te onderhouden.") 
            print("Je kan niet met elke collega om gaan, maar je geniet wel van je werk. Op een dag komt er een klant naar je toe en vraagt uit welk land je komt. Wat zeg je?")
            print("A= Wees eerlijk en beantwoord de vraag")
            print("B= vraag waarom hij dat moet weten")
            stuk25 = input()
            if stuk25 == "A" or stuk25 == "a":
               #Stukje 26--klaar
                print("Je vertelt de klant dat je uit Marokko komt en de man begint je uitschelden. ")
                print("Een collega van je komt aan lopen en vraagt aan de klant of er een probleem is.") 
                print("De man begint nu ook tegen je collega te schreeuwen.")
                print("Niet veel later wordt de klant uit de winkel gezet en gaat alles gewoon weer door. Je voelde je wel rot, maar je kon er niks aan doen.")
  
            else:
                #Stukje 27--klaar
                print("Je vraagt aan de klant waarom hij dat wilt weten. De klant antwoorde dat hij dat gewoon wilde weten. ") 
                print("Je zegt dat je er niet comfortabel bij voelt en de klant loopt mompelend weg. Je vraagt je af waarom hij dat wilde weten, maar je laat het er bij.")



        

    #Stukje 30 t/m 32--Alleen nog eindes--
    print("Na eentje tijdje gewerkt te hebben heb je genoeg geld om je gezin naar Nederland te halen, maar je weet het niet zeker of je dat wilt.")
    print("Je had dankzij je vrouw wel moeten vluchten. Wat ga je doen? ")
    print("A= Familie naar Nederland brengen")
    print("B= Hier alleen blijven")
    stuk30 = input()
    if stuk30 == "A" or stuk30 == "a":
        print("Je besluit toch om je gezin naar Nederland te halen. Wanneer je ze weer ziet wordt je zo gelukkig.")
        print("Je had ze heel erg gemist. Je was nog nooit zo gelukkig geweest.")
        print("Je hebt nu je eigen huis, een goedlopend baan en nu je gezin weer terug. Wat wil je nog meer?")
        print("EINDE: EEN GELUKKIGE MAN")
        print("")
        print("Wil je het verhaal opnieuw spelen of wil je stoppen?")
        print("A= Opnieuw")
        print("B= Stoppen")
        einde8 = input()
        if einde8 == "A" or einde8 == "a":
            print("")
        else:
            print("Bedankt voor het testen!")
            time.sleep(1) 
            exit()
        
    else:
        print("Je besluit dat je geen zin had om je gezin te zien en je begint een eigen leven te leiden. ")
        print("Na een jaar vind je een leuk meisjes en begin je met haar te daten.")
        print("Na een paar jaar samen te zijn trouw je haar en beginnen jullie een gezin. ")
        print("Je leeft een gelukkig leven, maar soms vraag je jezelf af wat er met je andere familie is gebeurd.")
        print("EINDE: DE ACHTERGELATEN FAMILIE")
        print("")
        print("Wil je het verhaal opnieuw spelen of wil je stoppen?")
        print("A= Opnieuw")
        print("B= Stoppen")
        einde9 = input()
        if einde9 == "A" or einde9 == "a":
            print(" ")
        else:
            print("Bedankt voor het testen!")
            time.sleep(1) 
            exit()
    
   
    
 
    
