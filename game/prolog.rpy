#Inhaltsverzeichnis:
#label prolog: Start-Label
#label prolog_duschen: gerade in der neuen Wohnung angekommen, Bernd ist dreckig, menu: Duschen? J/N -> J
#label prolog_dreckig: gerade in der neuen Wohnung angekommen, Bernd ist dreckig, menu: Duschen? J/N -> N
#label prolog_nimmGeld: Bernd ging nicht duschen, braucht Geld zum Einkaufen, menu: Geld nehmen? J/N -> J
#label prolog_nimmGeldNicht: Bernd ging nicht duschen, braucht Geld zum Einkaufen, menu: Geld nehmen? J/N -> N
#label prolog_nimmGeldDoch: Bernd hat das Geld nicht genommen, 2. menu: [S]pardose suchen oder [G]eld doch nehmen: G
#label prolog_suchSpardose: Bernd hat das Geld nicht genommen, 2. menu: [S]pardose suchen oder [G]eld doch nehmen: S
#label prolog_Einkaufen: Bernd geht nun einkaufen
#label prolog_EinkaufenLinks: Bernd biegt nach links ab und findet dort einen Aldi
#label prolog_EinkaufenRechts: Bernd biegt nach links ab und findet dort einen Lidl
#label prolog_EinkaufenWLAN: was im Supermarkt passiert, für Aldi & Lidl gleich
#label prolog_abend: Bernd hat sich WLan eingerichtet, er geht auf /b/


#Stats:
#$ sisLove =
    #Grundeinstellung = +40
    #prolog_duschen = +5
    #prolog_dreckig = -5
    #max. +45 / +35 möglich
#$ maLove =
    #Grundeinstellung = +20
    #prolog_duschen = +5
    #prolog_dreckig = -5
    #prolog_nimmGeld = -10
    #prolog_nimmGeldDoch = -10
    #max. +25 / +5 möglich
#$ friendLove =
    #Grundeinstellung = +-0
#$ yanLove = 
    #Grundeinstellung = +-0

#$ geld =
    #Grundeinstellung = +-0
    #prolog_duschen = +25
    #prolog_nimmGeld = +25
    #prolog_nimmGeldDoch = +25
    #prolog_suchSpardose = +20
    #prolog_EinkaufenWLAN = -15
    #max. +10 / +5 möglich

#-------------------------------------------------------------------------------



init:
    $ prolog_GeldGenommen = 0
    
label prolog:

    stop music

    scene splash splash_prolog
    with gradientTrans

    $ renpy.pause(5.0)

    scene black
    with gradientTrans

    "Stimme" "...fstehen!"
    
    "Eine Stimme weckt mich aus meinem unruhigen Schlaf."

    scene bg zuhause_draussen
    with flash

    play music m_bernd

    "Das Auto ist stehen geblieben."
    b "Lass mich schlafen."
    
    #show mutter neutral
    #Bild für Mutter existiert noch nicht
    #Ginga Ale
    
    ma "Nein, steh auf! Wir schauen uns die neue Wohnung an!"
    "Neue Wohnung?"
    b "Sind wir denn schon da?"
    ma "Ja, und jetzt steh endlich auf."

    "Wir sind heute nach Berlin umgezogen."

    scene bg zuhause_hausflur
    with fade

    "Ich folge meiner Mutter in die Wohnung."
    
    scene bg wohnung_innen
    with wooshTrans

    "Als wir durch die Tür kommen, läuft meine kleine Schwester bereits aufgeregt im Flur umher."

    play music m_laura fadein 0.3

    show laura happy
    with dissolve

    sis "Welches ist mein Zimmer, Mama? Welches?"
    "Wie kann sie nur so nervig sein? {w}Schrecklich."
    b "Du kriegst kein Zimmer."
    b "Du musst im Keller schlafen."
    "Ich ärgere meine Schwester gerne mit so was."
    
    #show laura happy at right
    #with move
    
    #show mutter at left
    #Bild existiert noch nicht
    #Ginga Ale

    ma "Eigentlich..."
    ma "...bist du es, der im Keller schlafen muss, %(berndName)s."

    stop music fadeout 0.4

    "Ungläubig sehe ich meine Mutter an."

    ma "Da dein Vater jetzt nicht mehr bei uns ist, können wir uns keine 3-Zimmer-Wohnung mehr leisten."
    ma "Und %(sisName)s ist schon 13."
    ma "Sie braucht auch mal ein eigenes Zimmer."
    ma "Da bleibt für dich nur noch der Keller."

    "Mein Blick wandert herüber zu meiner Schwester."
    "Sie grinst siegessicher."

    ma "Ach, komm schon! So schlimm wird es nicht sein."
    ma "Es ist doch nur für ein paar Wochen."
    ma "Wir bringen deinen Computer nach unten, dann wirst du dich gleich wie zu Hause fühlen"
    
    play music m_bernd
    
    scene bg keller_aus
    with fade

    "Etwas später..."
    "Nachdem ich mich damit abgefunden hatte, dass ich im Keller leben müsste, und mein Computer aufgebaut war, sofort die nächste Enttäuschung."
    #AE = Einziger langer Satz im kompletten Spiel...soll der Satz in kleinere Sätze aufgeteilt werden?
    "Kein Internet im Keller."
    "Das Kabel kann ich schlecht durch den Hausflur nach unten legen, also muss ich wohl einen Router kaufen."
    "W-LAN ist angesagt."
    "Ich gehe nach oben, um meine Mutter nach Geld zu fragen."
    
    scene bg wohnung_innen
    with fade
    
    play music m_wohnung
    
    #show mutter neutral
    #with dissolve
    #Ginga Ale
    
    ma "%(berndName)s! Wie siehst du denn aus?!"
    "Ich schaue an mir herunter."
    "Ein bisschen staubig, sonst nichts."
    b "Ist doch nur ein bisschen Staub."
    ma "Ein bisschen?!"
    ma "Sofort unter die Dusche mit dir!"
    ma "Und dann ziehst du dir was Frisches an."
    ma "Wir wollen gleich die neuen Nachbarn begrüßen."
    "Die neuen Nachbarn?"
    "Na toll."
    ma "Nun mach schon, %(berndName)s!"
    
    menu:
        "Soll ich duschen gehen?"
        
        "Ja, ich sollte auf sie hören.":
            jump prolog_duschen
            
        "Nein, die Alte kann mich mal!":
            jump prolog_dreckig
    
label prolog_duschen:
    $ maLove += 5
    $ sisLove +=5
    
    "Widerwillig gehe ich ins Bad, ziehe mich aus und steige unter die Dusche."
    
    scene bg badezimmer
    with fade
    
    b "Wieso muss ich überhaupt mit?"
    b "Kann sie die Nachbarn nicht alleine begrüßen?"
    b "Soll sie doch %(sisName)s mitneh-{nw}"
    
    play sound "sounds/door_1.wav"
    
    show laura neutral
    with dissolve
    
    sis "Hey, %(berndName)s. Hast du mein-{nw}"
    
    show laura surprised
    with dissolve
    
    "Sie starrt mich an."
    "Ich hatte doch abgeschlossen."
    "Sie starrt weiter."
    b "Raus mit dir!"
    b "SOFORT!"
    b "Was fällt dir ein hier einfach reinzuplatzen?!"
    
    play music m_laura fadein 0.3
    
    show laura happy
    with dissolve
    
    sis "Hihi! {w}%(berndName)s hat einen Steifen!"
    "Na toll. Das hat mir gerade noch gefehlt."
    b "Hau ab!"
    "Sie verschwindet kichernd."   
    
    hide laura happy
    with dissolve
    
    "Das fängt ja gut an."
    
    stop music
    
    scene black
    with fade
    
    "Kurz darauf..."
    
    scene bg wohnung_innen
    with fade
    
    play music m_wohnung
    
    #show mutter neutral
    #with dissolve
    #Ginga Ale
    
    b "Muss ich wirklich mit?"
    ma "Ja, %(berndName)s!"
    ma "Ich will nicht, dass du direkt am ersten Tag wieder einen schlechten Eindruck bei den Nachbarn hinterlässt."
    b "Kannst du nicht %(sisName)s mitnehmen?"
    b "Dafür geh' ich heute auch einkaufen."
    
    #show mutter at left
    #with move
    #Ginga Ale
    
    show laura happy #at right
    with dissolve
    
    sis "Ja, Mama!"
    sis "Ich will die Nachbarn begrüßen!"    
    ma "Hm..."
    ma "In Ordnung."
    
    "Meine Mutter holt zwei Geldscheine aus der Tasche."
    ma "Hier hast du Geld, %(berndName)s."
    b "Ich brauch' auch noch einen WLAN-Adapter."
    b "Sonst habe ich unten kein Internet."
    ma "Na gut, hier hast du noch 25 Euro. Mehr kriegst du aber nicht!"
    
    $ geld += 25
    
    "25 Euro reichen völlig."
    "Glück gehabt."
    
    ma "Los, %(sisName)s, wir gehen und stellen uns den neuen Nachbarn vor."
    
    show laura neutral #at right
    with dissolve
    
    sis "OK!"
    
    show laura happy #at right
    with dissolve
    
    sis "Du schuldest mir was, %(berndName)s!"
    
    "Berechnend wie immer, die kleine Nervensäge."
    b "Schon gut, schon gut."
    
    hide laura happy
    with dissolve
    
    #hide mutter
    #with dissolve
    #Ginga Ale
    
    "Die Beiden verlassen die Wohnung."
    b "Ich sollte mich auch auf den Weg machen."
    
    $ Spardose = 0
    
    scene black
    with fade
      
    jump prolog_Einkaufen
    
label prolog_dreckig:
    $ maLove -= 5
    $ sisLove -= 5
    b "Nö."
    b "Ich geh' hier niemanden begrüßen!"
    b "Gib mir mal lieber Geld."
    b "Ich brauch' einen WLAN-Adapter, damit ich ins Internet kann."
    ma "Wie redest du mit mir, %(berndName)s?!"
    ma "Ich geb' dir sicherlich kein Geld!"
    ma "Dann werd' ich halt deine Schwester mitnehmen."
    ma "Du solltest dir an ihr ein Beispiel nehmen!"
    
    #show mutter at left
    #with move
    #Ginga Ale
        
    show laura happy #at right
    with dissolve
    
    sis "Genau!"
    
    hide laura happy
    with dissolve
    
    #hide mutter
    #with dissolve
    #Ginga Ale
    
    "Die Beiden verlassen die Wohnung."
    b "Na toll."
    b "Jetzt hab' ich kein Internet."
    
    stop music
    
    "Da sehe ich es."
    "Meine Mutter hat ihr Geld hiergelassen."
    menu:
        "Soll ich es nehmen?"
        
        "Ja. Das merkt sie nicht.":
            jump prolog_nimmGeld
            
        "Nein. Das wäre falsch.":
            jump prolog_nimmGeldNicht
    
label prolog_nimmGeld:
    "Ohne weiter nachzudenken, nehme ich mir 25 Euro und verlasse das Haus..."
    $ maLove -= 10
    $ prolog_GeldGenommen = 1
    
    $ geld += 25
    
    $Spardose = 0
    
    jump prolog_Einkaufen
    
label prolog_nimmGeldNicht:
    "Wenn ich es nehme, merkt sie das."
    "Ich lass es lieber."
    "Vielleicht kann ich ja noch woanders etwas auftreiben."
    "Ich denke nach."
    "Vielleicht ist noch etwas in meiner Spardose."
    "Aber die unter den ganzen Sachen zu finden dürfte nicht einfach werden."
    "In welchem Karton könnte sie sein..?"
    
    menu:
        "Soll ich sie suchen?"
        
        "Ja.":
            jump prolog_suchSpardose
        
        "Nein. Ich nehme doch das Geld von meiner Mutter.":
            jump prolog_nimmGeldDoch
    
label prolog_suchSpardose:
    b "Na gut, dann mal los."
    "Ich durchsuche am besten zuerst die Kartons unten im Keller."
    
    play music m_bernd
    
    scene bg keller
    with fade
        
    b "Hm... in diesem Karton ist sie nicht."
    "Also ein Anderer."
    "Wieso habe ich überhaupt so viele Kartons?"
    "Ich brauch doch nur mein Bett und den Computer."
    "Ich sollte dieses alte Zeug mal wegwerfen."
    "Zumindest das, was ich nicht mehr brau..."
    b "Hab' sie!"
    "Das ging schneller als erwartet."
    "Nur noch 20 Euro drin."
    "Na ja, das muss reichen."
    "Es wird schon spät, ich sollte besser losgehen."
    
    $ geld += 20
    $ Spardose = 1
    
    jump prolog_Einkaufen
    
label prolog_nimmGeldDoch:
    b "Mir doch egal."
    "Ich nehme mir 25 Euro von meiner Mutter und verlasse das Haus."
    $ geld += 25
    $ maLove -= 10
    $ prolog_GeldGenommen = 1
    
    $Spardose = 0
    
    jump prolog_Einkaufen
    
label prolog_Einkaufen:

    if Spardose == 1:
        play music m_wohnung
        pass
    
    else:
        pass
   
   
    scene bg zuhause_draussen
    with fade
   
    "Ich verlasse das Haus und sehe mich um."
    "Toll. Ich soll einkaufen gehen und habe keine Ahnung, wo ich bin, oder wo der nächste Supermarkt ist."
    b "Na super..."
   
    menu:
        "Egal. Ich gehe nach..."
       
        "...links.":
            $ supermarkt = "Aldi"
           
            jump prolog_EinkaufenLinks
       
        "...rechts.":
            $ supermarkt = "Lidl"
           
            jump prolog_EinkaufenRechts
           
label prolog_EinkaufenLinks:
    "Spontan gehe ich nach links."
    "Es muss hier ja irgendwo einen Supermarkt geben."
    
    scene bg aldi
    with fade
    
    "Tatsächlich finde ich nach etwa zehn Minuten einen Aldi."
    
    scene bg supermarkt
    with fade
    
    play music m_shop
    
    if (prolog_GeldGenommen):
        jump prolog_EinkaufenWLAN
    "Was soll ich hier überhaupt kaufen?"
    "Ich habe keine Ahnung."
    "Ich nehme ein Paket Deutsche Markenbutter und mache mich auf den Weg zur Kasse."
   
    jump prolog_EinkaufenWLAN       
    
label prolog_EinkaufenWLAN:
    b "WLAN-Adapter haben die hier sicher nicht..."
    "Obwohl ich nur leise vor mich hin gemurmelt habe, hat mich wohl jemand gehört."
    
    show salih neutral
    with dissolve
    
    "Salih" "Doch, haben wir. Zweite Reihe, drittes Regal."
    b "Äh... ja."
    "Tatsächlich finde ich dort einen WLAN-Adapter für nur 15 Euro."
    $ geld -= 15
    "Das muss fürs Erste reichen."
    "Hauptsache raus hier."
    "So schnell es geht gehe ich zur Kasse und bezahle."
    b "Ich sollte mich wirklich beeil-{nw}"
    
    stop music
    
    scene bg supermarkt
    with vpunch
    
    play sound "sounds/hit_1.wav"
    
    show anja weird_n
    with dissolve
    
    u"Mädchen" "Autsch..."
    "Verdammt."
    "Jetzt hab ich ein Mädchen umgelaufen."
    "Warum passiert so was immer mir?"
    b "Al-alles in O-Ordnung?"
    
    show anja surprised_n
    with dissolve
    
    play music m_anja fadein 0.3
    
    u"Mädchen" "Ähm...ja."
    u"Mädchen" "Alles bestens."
    
    show anja neutral_n
    with dissolve
    
    "Verdammt."
    "Die sieht auch noch gut aus."
    "Wieso immer ich?"
    u"Mädchen" "Meine Brille...?"
    "Ihre Brille liegt auf dem Boden."
    "Schnell hebe ich sie auf."
    b "Hier."
    
    show anja shy
    with dissolve
    
    u"Mädchen" "Oh, danke."
    b "..."
    u"Mädchen" "Tut mir wirklich leid."
    "Was?"
    "Das war doch meine Schuld."
    b "Ähm... kein Problem."
    u"Mädchen" "Na gut... ähm..."
    
    show anja neutral
    with dissolve
    
    u"Mädchen" "Tschüss."
    b "..."

    hide anja neutral
    with dissolve
   
    stop music fadeout 1.0
   
    "Sie dreht sich um und geht."
    "Ich verlasse den Laden."
    "Man, war das peinlich."
    "Typisch für jemanden wie mich."
    "Ich kann einfach nicht mit Frauen umgehen."
    "Und genau deswegen werde ich auch als Jungfrau sterben."
    "Ich seufze und trete den Weg nach Hause an."
    
    jump prolog_abend

label prolog_EinkaufenRechts:
    "Spontan gehe ich nach rechts."
    "Es muss hier ja irgendwo einen Supermarkt geben."
    
    scene bg lidl
    with fade
    
    "Tatsächlich finde ich nach etwa zehn Minuten einen Lidl."
    
    play music m_shop
    
    scene bg supermarkt
    with fade
    
    if (prolog_GeldGenommen):
        jump prolog_EinkaufenWLAN
    "Was soll ich hier überhaupt kaufen?"
    "Ich habe keine Ahnung."
    "Ich nehme ein Paket Deutsche Markenbutter und mache mich auf den Weg zur Kasse."
    
    jump prolog_EinkaufenWLAN
    
label prolog_abend:

    scene bg keller_aus
    with fade

    play music m_bernd
    
    "Später am Abend..."
    "Nachdem ich den neu erstandenen WLAN-Adapter angeschlossen und konfiguriert habe..."

    scene bg keller_aus
    with fade
    
    play sound "sounds/boot.wav"
    
    $ renpy.pause(1.5)
    
    "Wie ich diese Stimme vermisst habe..."
    
    scene bg keller
    with fade    
    
    "www.krautchan.net"
    "Enter."
    
    scene bg keller_kc
    with dissolve
    
    "Erstmal auf /b/ gucken."
    "Wieder nur Krebs."
    "Typisch."
    
    scene bg keller
    with dissolve

    "Ich schließe das Browserfenster und lasse mich auf meine Matratze fallen."
    "Nun bin ich also ein echter Bernd."
    
    stop music fadeout 1.0
    
    scene black
    with gradientTrans
    
    $ renpy.pause(2.0)
    
    jump eins