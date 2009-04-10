init:
    $ prolog_GeldGenommen = 0
    
label prolog:

    scene bg splash_prolog
    with gradientTrans

    $ renpy.pause(5.0)

    scene black
    with gradientTrans


    "\"Aufwachen, %(berndName)s!\""
    
    scene bg zuhause_draussen
    with fade

    play music "music/1.ogg"

    "Eine Stimme weckte mich aus meinem unruhigen Schlaf."

    "Das Auto ist stehen geblieben, also sind wir da."

    b "Sind wir da, Mama?"

    ma "Ja, steh auf! Komm, wir schauen uns die neue Wohnung an!"

    "Neue Wohnung?"
    "Langsam kommt die Erinnerung wieder."
    "Wir sind heute nach Berlin umgezogen."

    scene bg zuhause_hausflur
    with fade

    "Ich folge meiner Mutter in die Wohnung."
    
    scene bg zuhause_drinnen
    with wooshTrans

    "Als wir durch die Tür kommen, läuft meine kleine Schwester bereits aufgeregt im Flur umher."

    play music "music/schwester.ogg"

    show laura happy
    with dissolve

    sis "Welches ist mein Zimmer, Mama? Welches?"

    "Wie kann sie nur so nervig sein? Schrecklich."

    b "Du kriegst kein Zimmer, du musst im Keller schlafen."

    "Ich ärgere meine Schwester gerne mit sowas."
    
    hide laura happy
    with dissolve

    ma "Eigentlich..."
    ma "...bist du es, der im Keller schlafen muss, %(berndName)s."


    stop music fadeout 0.4

    "Ungläubig sehe ich meine Mutter an."

    ma "Da dein Vater jetzt nicht mehr bei uns ist, können wir uns keine 3-Zimmer-Wohnung leisten."
    ma "%(sisName)s ist schon 13. Sie braucht ein eigenes Zimmer."
    ma "Da bleibt für dich nur noch der Keller."
    
    show laura happy
    with dissolve

    "Mein Blick wandert herüber zu meiner Schwester."
    "Sie grinst siegessicher."
    
    hide laura happy
    with dissolve

    ma "Ach, komm schon! So schlimm wird es nicht sein."
    ma "Es ist doch nur für ein paar Wochen."
    ma "Los! Wir bringen deinen Computer nach unten."

    #hier keller einblenden
    play music "music/1.ogg"
    
    scene bg keller_aus
    with fade

    "Etwas später..."
    
    "Nachdem ich mich damit abgefunden hatte, dass ich im Keller leben würde, und mein Computer aufgebaut war, sofort die nächste Enttäuschung."
    
    "Kein Internet im Keller."
    
    "Das Kabel kann ich schlecht durch den Hausflur nach unten legen, also muss ich wohl einkaufen."
    
    "W-LAN ist angesagt."
    
    "Ich gehe nach oben, um meine Mutter nach Geld zu fragen."
    
    scene bg zuhause_drinnen
    with fade
    
    play music "music/2.mp3"
    
    #mutter einblenden
    ma "%(berndName)s! Wie siehst du denn aus?!"
    
    "Ich schaue an mir herunter."
    
    "Ein bisschen staubig, sonst nichts."
    
    b "Ist doch nur ein bisschen Staub."
    
    ma "Ein bisschen?!"
    ma "Sofort unter die Dusche mit dir!"
    ma "Und dann ziehst du dir was frisches an."
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
    $ sisLove +=10
    stop music
    
    scene black
    with fade
    
    "Missmutig gehe ich ins Bad, ziehe mich aus und steige unter die Dusche."
    
    scene bg badezimmer
    with fade
    
    b "Wieso muss ich überhaupt mit?"
    b "Kann sie die Nachbarn nicht alleine begrüßen?"
    b "Soll sie doch %(sisName)s mitnehm-"
    
    play sound "sounds/door_1.wav"
    
    show laura neutral
    with dissolve
    
    sis "Hey, %(berndName)s. Hast du mein-"
    
    show laura surprised
    with dissolve
    
    "Sie starrt mich an."
    "Scheiße, ich hatte doch abgeschlossen."
    
    "Sie starrt weiter."
    
    b "Scheiße! Raus mit dir! Was fällt dir ein hier einfach reinzuplatzen?!"
    
    play music "music/schwester.ogg"
    
    show laura happy
    with dissolve
    
    sis "Hihi! %(berndName)s hat einen Steifen!"
    
    "Na toll. Das hat mir gerade noch gefehlt."
    
    b "Verpiss dich!"
    
    "Sie verschwindet kichernd."   
    
    hide laura happy
    with dissolve
    
    "Das fängt ja gut an."
    stop music
    
    scene black
    with fade
    
    "Etwas später..."
    
    scene bg zuhause_drinnen
    with fade
    
    play music "music/2.mp3"
    
    b "Muss ich wirklich mit?"
    
    ma "Ja, %(berndName)s!"
    ma "Ich will nicht, dass du direkt am ersten Tag wieder einen schlechten Eindruck auf die Nachbarn machst."
    
    b "Kannst du nicht %(sisName)s mitnehmen?"
    b "Dafür geh' ich heute auch einkaufen."
    
    show laura happy
    with dissolve
    
    sis "Ja, Mama!"
    sis "Ich will die Nachbarn begrüßen!"
    
    hide laura happy
    with dissolve
    
    ma "Hm..."
    ma "In Ordnung."
    
    "Meine Mutter holt einen 20 Euro Schein aus der Tasche."
    
    ma "Hier hast du Geld, %(berndName)s."
    
    b "Ich brauch' auch noch einen W-LAN Adapter."
    b "Sonst habe ich unten kein Internet."
    
    ma "Na gut, hier hast du noch 20. Mehr kriegst du nicht."
    
    $ geld += 20
    
    "20 Euro reichen völlig."
    "Glück gehabt."
    
    ma "Los, %(sisName)s, wir gehen und stellen uns den neuen Nachbarn vor."
    
    show laura neutral
    with dissolve
    
    sis "OK!"
    
    show laura happy
    with dissolve
    
    sis "Du schuldest mir was, %(berndName)s!"
    
    "Berechnend wie immer, die kleine Nervensäge."
    
    b "Schon gut, schon gut."
    b "Danke."
    
    hide laura happy
    with dissolve
    
    "Die Beiden verlassen die Wohnung."
    
    b "Ich sollte mich auch auf den Weg machen."
    
    stop music
    
    scene black
    with fade
    
    jump prolog_Einkaufen
    
label prolog_dreckig:
    $ maLove -= 5
    $ sisLove -= 2
    b "Nö. Ich geh' hier niemanden begrüßen!"
    b "Gib mir mal lieber Geld."
    b "Ich brauch' einen W-LAN Adapter, damit ich ins Internet kann."
    
    ma "Wie redest du mit mir, %(berndName)s?!"
    ma "Ich geb dir sicherlich kein Geld!"
    ma "Dann werd' ich halt deine Schwester mitnehmen."
    ma "Du solltest dir an ihr ein Beispiel nehmen!"
    
    show laura happy
    with dissolve
    
    sis "Genau!"
    
    hide laura happy
    with dissolve
    
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
    "Ohne weiter nachzudenken, nehme ich mir 20 Euro und verlasse das Haus..."
    $ maLove -= 10
    $ prolog_GeldGenommen = 1
    
    $ geld += 20
    
    jump prolog_Einkaufen
    
label prolog_nimmGeldNicht:
    "Wenn ich es nehme, merkt sie das."
    "Ich lass es lieber."
    "Vielleicht kann ich ja noch woanders etwas auftreiben."
    "Ich denke nach."
    "Vielleicht ist noch etwas in meiner Spardose."
    "Sie zu finden sollte nicht leicht sein."
    "Sicher ist sie in einem der vielen Kartons."
    
    menu:
        "Soll ich sie suchen?"
        
        "Ja.":
            jump prolog_suchSpardose
        "Nein. Ich nehme doch das Geld von meiner Mutter.":
            jump prolog_nimmGeldDoch
    
label prolog_suchSpardose:
    b "Na gut, dann mal los."
    "Ich durchsuche am Besten zuerst die Kartons unten im Keller."
    
    stop music
    #keller szene
    scene bg keller
    with fade
    
    b "Hm... in diesem Karton ist sie nicht."
    "Also ein anderer."
    "Wieso habe ich überhaupt so viele Kartons?"
    "Ich brauch doch nur mein Bett und den Computer."
    "Ich sollte dieses alte Zeug mal wegwerfen."
    "Zumindest das, was ich nicht mehr bra..."
    b "Hab sie!"
    "Das ging schneller als erwartet."
    "Nur noch 15 Euro drin."
    "Naja, muss reichen."
    "Es wird schon spät, ich sollte besser losgehen."
    
    $ geld += 15
    
    jump prolog_Einkaufen
    
label prolog_nimmGeldDoch:
    b "Scheiß doch drauf."
    "Ich nehme mir 20 Euro von meiner Mutter und verlasse das Haus."
    $ geld += 20
    $ maLove -= 10
    $ prolog_GeldGenommen = 1
    jump prolog_Einkaufen
    
label prolog_Einkaufen:

   play music "music/1.ogg"
   scene bg zuhause_draussen
   with fade
   
   "Ich verlasse das Haus und sehe mich um."
   "Toll. Ich soll einkaufen gehen und habe keine Ahnung wo ich bin, oder wo der nächste Supermarkt ist."
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
    play music "music/3.mp3"
    scene bg supermarkt_innen
    with fade
    if (prolog_GeldGenommen):
        jump prolog_EinkaufenWLAN
    "Was soll ich hier überhaupt kaufen?"
    "Ich habe keine Ahnung."
    "Ich nehme ein Paket Deutsche Markenbutter und mache mich auf den Weg zur Kasse."
    jump prolog_EinkaufenWLAN
        
    
label prolog_EinkaufenWLAN:
    b "W-LAN Adapter haben die hier sicher nicht..."
    "Obwohl ich nur leise vor mich hin gemurmelt habe, hat mich wohl jemand gehört."
    u"Verkäuferin" "Doch, haben wir. Zweite Reihe, drittes Regal."
    b "Äh... ja."
    "Tatsächlich finde ich dort einen W-LAN Adapter für nur 15 Euro."
    $ geld -= 15
    "Das muss fürs erste reichen."
    "Hauptsache raus hier."
    "So schnell es geht gehe ich zur Kasse und bezahle."
    b "Ich sollte mich wirklich beeil-"
    stop music
    scene bg supermarkt_innen
    with vpunch
    play sound "sounds/hit_1.wav"
    show anja weird_n
    with dissolve
    u"Mädchen" "Autsch..."
    "Scheiße."
    "Jetzt hab ich ein Mädchen umgelaufen."
    "Warum passiert sowas immer mir?"
    b "Äh... alles in Ordnung?"
    show anja surprised_n
    with dissolve
    play music "music/bernd_anja_theme.mp3"
    u"Mädchen" "Äh... ja."
    u"Mädchen" "Alles ok."
    show anja neutral_n
    with dissolve
    "Scheiße."
    "Die sieht auch noch geil aus."
    "Wieso immer ich?"
    u"Mädchen" "Meine Brille...?"
    "Ihre Brille liegt auf dem Boden."
    "Schnell hebe ich sie auf."
    b "Hier."
    show anja shy
    with dissolve
    u"Mädchen" "Oh, danke."
    b "Ja."
    b "Kein Problem."
    u"Mädchen" "Tut mir wirklich Leid."
    "Was?"
    "Das war doch meine Schuld."
    b "Ähm... kein Problem."
    u"Mädchen" "Na gut... ähm..."
    show anja neutral
    with dissolve
    u"Mädchen" "Tschüss."
    b "Ja."
    b "Tschüss."
    hide anja neutral
    with dissolve
    stop music fadeout 1.0
    "Sie dreht sich um und geht."
    "Ich verlasse den Laden."
    "Scheiße, das war peinlich."
    "Typisch für jemanden wie mich."
    "Ich kann einfach nicht mit Frauen umgehen."
    "Genau deswegen werde ich als Jungfrau sterben."
    "Ich seufze und trete den Weg nach Hause an."
    
    jump prolog_abend

label prolog_EinkaufenRechts:
    "Spontan gehe ich nach rechts."
    "Es muss hier ja irgendwo einen Supermarkt geben."
    scene bg lidl
    with fade
    "Tatsächlich finde ich nach etwa zehn Minuten einen Lidl."
    play music "music/3.mp3"
    scene bg supermarkt_innen
    with fade
    if (prolog_GeldGenommen):
        jump prolog_EinkaufenWLAN
    "Was soll ich hier überhaupt kaufen?"
    "Ich habe keine Ahnung."
    "Ich nehme ein Paket Deutsche Markenbutter und mache mich auf den Weg zur Kasse."
    
    jump prolog_EinkaufenWLAN
    
label prolog_abend:

    scene bg keller
    with fade

    play music "music/1.mp3"
    
    "Später am Abend..."
    
    "Nachdem ich den neu erstandenen W-LAN Adapter angeschlossen und konfiguriert habe, schalte ich meinen Computer ein."
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