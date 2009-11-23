#Inhaltsverzeichnis:
#label eins = Start von Kapitel 1, alles vor der Entscheidung, ob Treffen oder nicht
#label eins_treffenBerndf = Erstes und zweites Treffen mit Abzweigung zu Abholen
#label eins_accept_fBernd = Annehmen des Angebots von Anja
#label eins_refuse_fBernd = Ablehnen des Angebots von Anja
#label eins_sisAbholen_promise = Kurzer Dialog, wenn man der Schwester versprochen hat sie abzuholen
#label eins_sisAbholen = Abholen der Schwester am zweiten Tag nach Berndtreffen
#label eins_krautchanOff = Krautchan geht off
#label eins_sisAbholenZuerst = Abholen der Schwester am ersten und zweiten Tag + Stalking


#Stats:
#$ sisLove =
    #Begrüßung am Morgen: "Guten Morgen, Laura" = +5
    #Begrüßung am Morgen: "Geh weg, Nervensäge" = -5
    #Kondome werden nur mitgebracht, wenn sisLove > 50
    #Bernd bedankt sich für die Kondome/Gummibärchen = +5
    #Bernd bedankt sich nicht für die Kondome/Gummibärchen = -5    
    #Laura: "Morgen holst du mich aber ab, oder?" - Bernd: "Klar." = +15
    #Laura: "Morgen holst du mich aber ab, oder?" - Bernd: "Nein." = -15    
    #max. +65 / +10 möglich
#$ maLove =
    #Mutter: "Willst du nicht aufstehen?" - Bernd: "OK." = +5
    #Mutter: "Willst du nicht aufstehen?" - Bernd: "Nein." = -5
    #Mutter: "Kommst du beim Tragen helfen?" - Bernd: "OK." = +5
    #Mutter: "Kommst du beim Tragen helfen?" - Bernd: "Nein." = -5    
    #max. +35 / -5 möglich
#$ friendLove =
    #Anja: "Mit KC ist das und das passiert. Glaubst du mir?" - Bernd: "Ja." = +10
    #Anja: "Mit KC ist das und das passiert. Glaubst du mir?" - Bernd: "Nein." = -5
    #Anja: "Hilfst du mir denn?" - Bernd: "Ja." = +10
    #Anja: "Hilfst du mir denn?" - Bernd: "Nein." = -10
    #max. +10 / -15 möglich
#$ yanLove = 
#$ geld =
    #Döner kaufen = -3,5
    #Eis für Laura kaufen = -1,5
    #max. +5 / +-0 möglich

#-------------------------------------------------------------------------------
#Kapitel 1
#Einen Monat nach den Ereignissen des Prologs
#-------------------------------------------------------------------------------



label eins:    
    
    stop music fadeout 1.0

    #scene splash splash_eins
    #with gradientTrans

    $ renpy.pause(5.0)

    scene black
    with gradientTrans
    
    "Einen Monat später..."
    
    play music m_bernd
    
    scene bg keller_aus
    with spotTrans
    
    ma "%(berndName)s, willst du nicht aufstehen?"
    
    menu:
        " "
        
        "OK, ich steh' auf.":
            $ maLove += 5
            b "OK, ich steh' auf."
            "Verdammt, ich hab 'ne Morgenlatte."
            "Wenn meine Mutter die sieht, gibt sie wieder 'nen blöden Kommentar ab."
            "Ich muss irgendwie Zeit rausschinden."
            b "Wie spät ist es denn?"
            ma "Viertel vor Zwölf."
            b "Warum weckst du mich so früh?"
            ma "Weil du nicht den ganzen Tag im Bett liegen kannst."
            ma "Jetzt steh auf."
            "Dreck."
            "Ich setze mich vorsichtig hin und achte darauf, dass die Bettdecke keine verräterischen Falten wirft."
            "Meine Mutter scheint nichts gemerkt zu haben."
        
        "Lass mich schlafen!":
            $ maLove -= 5
            b "Lass mich schlafen!"
            ma "Komm, %(berndName)s, jetzt stell dich nicht so an."
            b "Lass mich in Ruhe, ich will noch schlafen."
            ma "%(berndName)s, du stehst jetzt gefälligst auf, oder es setzt was."
            "Verdammt, ich hab 'ne Morgenlatte."
            "Wenn meine Mutter die sieht, gibt sie wieder 'nen blöden Kommentar ab."
            "Ich muss irgendwie Zeit rausschinden."
            b "Wie spät ist es denn?"
            ma "Viertel vor Zwölf."
            b "Es ist noch viel zu früh zum Aufstehen."
            ma "%(berndName)s!"
            "Jetzt ist sie sauer..."
           
    
    "Genau im richtigen Moment kommt %(sisName)s rein.{nw}"
    
    play sound "sounds/door_1.wav"
    
    show laura happy
    with dissolve
    
    play music m_laura fadein 0.3
    
    sis "Guten Morgen, %(berndName)s."
    
    menu:
        " "
        
        "Guten Morgen, %(sisName)s.":
            $ sisLove += 5
            b "Guten Morgen, %(sisName)s."
            "Na toll."
            "Als wäre meine Mutter nicht genug..."
            "Jetzt hab ich schon zwei Weiber in meinem Zimmer und ein Ende dieser Erektion ist nicht in Sicht."
            sis "Hast du gut geschlafen, %(berndName)s?"
            b "Naja, es geht."
            sis "Was hast du geträumt?"
            "Was habe ich geträumt?"
            "Gute Frage."
            b "Wieso willst du das wissen?"
            "Was soll ich schon geträumt haben?"
            "Was Jemand, der in meinem Alter noch Jungfrau ist, wohl jede Nacht träumt..."
            
            show laura neutral
            with dissolve
            
            sis "Nur so."
            b "Was hast DU denn heute Nacht geträumt?"
            
            show laura embarrassed
            with dissolve
            
            sis "Ach..."
            sis "...nichts Besonderes."
            b "Sag schon!"
            
            show laura happy
            with dissolve
            
            sis "Das ist ein Geheimnis."
            "Sie will es mir wohl nicht erzählen..."
            b "Ist es dir peinlich oder warum willst du es mir nicht sagen?"
            
            show laura surprised_drop
            with dissolve
            
            sis "Peinlich?"
            
            show laura embarrassed
            with dissolve
            
            sis "W- wieso das denn?"
            sis "Was soll ich denn Peinliches träumen?"
            b "Da könnte ich dir einige Beispiele nennen."
            ma "Genug, %(berndName)s!"
            ma "Deine Schwester und ich gehen jetzt eben einkaufen."
            ma "Ich will, dass du fertig angezogen bist und gefrühstückt hast, wenn wir wiederkommen."
            b "Geht in Ordnung."
            
            show laura neutral
            with dissolve
            
            sis "Bis gleich, %(berndName)s!"
            
            hide laura neutral
            with dissolve
            
            "Die beiden verlassen endlich das Zimmer."
            
            stop music fadeout 0.4
            
            b "Endlich sind sie weg."
            b "Dann kann ich jetzt ja in Ruhe fap-{nw}"
            
            play sound "sounds/door_1.wav"
            
            show laura neutral
            with dissolve
            
            play music m_laura
            
            sis "Soll ich dir irgendwas mitbringen?"
            
            menu:
                " "
                
                "Kondome.":
                    $ mitbringen = "kondome"
                    b "Kondome."
                    b "Da haben wir beide was von."
                    
                    show laura surprised
                    with dissolve
                    
                    sis "Aber %(berndName)s!"
                    "Sie rennt aus dem Zimmer."
                    
                    hide laura surprised
                    with dissolve
                    
                    stop music fadeout 0.4
                    
                    b "Hey, war doch nur Spaß!"
                    "Sie hört mich schon nicht mehr."
                
                "Gummibärchen.":
                    $ mitbringen = "gummi"
                    b "Ich hätte mal wieder Lust auf Gummibärchen."
                    b "Da haben wir beide was von."
                    
                    show laura happy
                    with dissolve
                    
                    sis "Oh, ja!"
                    sis "Dann bis gleich, %(berndName)s!"
                    
                    b "Ja, bis gleich." 
                    
                    hide laura neutral
                    with dissolve
                    
                    stop music fadeout 0.4
            "So."
            "Jetzt aber."
         
        "Geh' weg, Nervensäge.":
            $ sisLove -= 5
            b "Geh' weg, Nervensäge!"
            "Warum müssen die jetzt beide hier rumstehen?"
            "Das ist MEIN Keller!"
            
            show laura pissed
            with dissolve
            
            sis "Dann geh' ich halt!"
            sis "Bäh!"
            
            hide laura pissed
            with dissolve
            
            ma "Aber %(berndName)s, wie redest du denn mit deiner Schwester?"
            b "Ist mir doch egal, ich will schlafen."
            ma "Also ich will, dass du jetzt aufstehst und gleich frühstückst."
            ma "Wenn du nicht in zehn Minuten oben bist, kannst du deinen Internetanschluss selbst bezahlen."
            "Wütend knallt sie die Tür hinter sich zu."
            "Sie sagt so was oft."
            "Nachher ist alles wieder ok."
            
            stop music fadeout 0.4
            
    "Endlich bin ich allein und kann in Ruhe fappieren."
    
    play music m_bernd
    
    "Seit einem Monat denke ich immer an das Mädchen aus dem Supermarkt."
    
    "Warum musste sie auch so gut aussehen?"
    "Die würde ich auch ungewaschen lecken."
    "(Nur sie müsste sich vorher waschen.)"
    "Ich fange an wild zu fappieren."
    
    ma "%(berndName)s, wir sind dann jetzt weg."
    ma "Kommst du gleich hoch und frühstückst?"
    b "Ja, ich komme gleich!"
    "Die Wohnungstür fällt ins Schloss."
    "Ob ich sie wohl jemals wiedersehen werde?"
    "Wahrscheinlich wohnt sie ganz hier in der Nähe."
    "Warum sollte sie sonst hier einkaufen?"
    "Oder war sie nur zufällig in der Gegend?"
    "Ich will sie wiedersehen!"
    "...aber was würde ich ihr sagen?"
    "\"Hallo, mein Name ist %(berndName)s und ich will dich ficken!\""
    "Hey..."
    "Das könnte sogar funktionieren."
    "...oder auch nicht."
    "Ich werde sie wohl niemals wiederseh-{nw}"
    
    $ renpy.music.set_volume(0.0, .5, channel="music")
    
    scene bg keller_aus
    with flash
    
    scene bg keller_aus
    with slowFlash
    $ renpy.pause(0.5)
    
    scene bg keller_aus
    with damnSlowFlash
    $ renpy.pause(0.5)
    
    "Ich kam."
    "Erschöpft lasse ich mich auf's Bett fallen."
    
    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    "Ich glaub', ich bin verliebt."
    "Dabei dachte ich immer..."
    "...Bernd braucht keine Liebe."
            
    play sound "sounds/error.wav"        
    
    "Ein Signalton befördert mich unsanft aus meinen Gedanken."
    
    "Oh, scheint als wäre ein Download fertig."
    "Ich zieh' mir meine Unterhose hoch und sehe nach."

    scene bg keller
    with dissolve

    "Tatsächlich."
    "Die neue Folge von Strike with Cheese ist unten, aber ich muss erst was essen."
    "Und fappiert habe ich eh gerade erst, also hat das noch Zeit."
    "Ich könnte auch mal wieder duschen gehen."
    "Monatsanfang, frische Unterwäsche."
    "Ich gehe nach oben und ins Bad."
    
    scene black
    with fade

    play music m_wohnung
    
    scene bg badezimmer
    with fade    

    b "So, fertig geduscht."

    "Jetzt muss ich erstmal meinen Hunger bekämpfen."

    scene bg kueche
    with fade

    b "Was ess' ich denn jetzt mal..."

    b "Mal gucken, was so im Kühlschrank ist."
    "Ich öffne die Kühlschranktür."
    
    stop music fadeout 0.2
    
    $ renpy.music.play ("music/rugenwalder.ogg", channel=7, loop=False, fadeout=None, synchro_start=False, fadein=0, tight=False, if_changed=False)
    $ renpy.music.queue(["sounds/omnomnom.mp3"], loop=True)

    b "OH MEIN GOTT!"
    b "Das ist doch...!"
    b "RÜGENWALDER TEEWURST!"
    b "DIE MIT DER MÜHLE!"
    b "Wie viele nehm' ich denn?"
    b "ALLE!"
    
    $ renpy.pause(5)

    b "RÜGENWALDER!"
    b "GROB ODER FEIN, DIE MIT DER MÜHLE MUSS ES SEIN!"

    b "Hm..."
    b "Lecker."
    
    stop music fadeout 0.5

    b "So, endlich kann ich Strike with Cheese schauen."
    
    scene bg keller_bluescreen
    with fade
   
    play music m_bernd
    
    "Als ich wieder in den Keller komme, ist der ganze Raum in ein blaues Licht getaucht."
    "Sofort schaue ich auf den Bildschirm."
 
    b "OH MEIN GOTT, WAS IST GESCHEHEN!?"
    b "WAS IST DAS DENN!!?"
    b "DU HURENSOHN!"
    b "DIE RESET-TASTE..."
    b "WO IST DIE RESET-TASTE!?"
    b "STARTE {w}DAS {w}VERDAMMTE {w}BETRIEBSSYSTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEM!"

    show bg keller_aus
    
    $ renpy.pause(3.0)
    
    play sound "sounds/boot.wav"
    
    $ renpy.pause(2.0)
    
    show bg keller
    
    b "Geht doch..."
    "Ich brauche wirklich mal einen neuen PC."
    "Dieses alte Teil ist wirklich zu nichts mehr gut."
    "Andauernd stürzt das Ding ab."
    "Erstmal auf Krautchan..."

    scene bg keller_kc
    
    "Auf /b/ scheint wieder nichts los zu sein."
    "Krautchan saugt in letzter Zeit ziemlich."
    "Warum nur?"
    "Na ja, wenigstens kann ich dann jetzt endlich Strike with Cheese gucken."
    
    play sound "sounds/door_1.wav"

    "Ich will die Datei öffnen, als ich höre, wie sich die Wohnungstür öffnet." 
    ma "%(berndName)s, wir sind wieder da!"
    "Na toll."
    "Das ging schnell."
    ma "Kommst du hoch und hilfst uns eben?"
    ma "Wir haben 'ne Menge zu tragen."
    
    menu:
        " "
        
        "Klar!":
            $ maLove += 5
            b "OK, bin schon auf dem Weg!"
        
        "Haha, als ob!":
            $ maLove -= 5
            b "Warum ich?"
            $ berndNameCaps = berndName.upper()
            ma "%(berndNameCaps)s!"
            ma "DU KOMMST JETZT SOFORT HOCH UND HILFST DEINER SCHWESTER BEIM TRAGEN!"
            b "In Ordnung. Ich komme ja schon."
        
    "Ich stehe auf und gehe nach oben."
    
    play music m_wohnung
    
    scene bg zuhause_hausflur
    with fade
    
    "Als ich den Hausflur betrete, sehe ich, wie sich %(sisName)s mit einer schweren Tasche abmüht."
    "Wie haben die in so kurzer Zeit so viel eingekauft?"
    "Ich denke, das werde ich nie verstehen."
    b "Lass mich das tragen, %(sisName)s."
    sis "Danke, %(berndName)s."
    b "Ich tue nur meine Pflicht als großer Bruder."
    
    scene black
    with fade
    
    scene bg keller
    with fade
    
    play music m_bernd
    
    if mitbringen == "kondome":
        if sisLove < 50:
            $ mitbringen = "nichts"
        
    if mitbringen != "nichts":
    
        b "Endlich kann ich Strike with Cheese guck-"
        
        play sound "sounds/door_1.wav"
    
        show laura happy
        with dissolve
    
        sis "%(berndName)s, ich hab dir was mitgebracht!"
        
        if mitbringen == "gummi":
        
            "Sie hat eine Packung Gummibärchen in der Hand."
            show laura neutral
            with dissolve
            sis "Bitte."
        
        if mitbringen == "kondome":

            show laura embarrassed
            with dissolve
            
            sis "Hier..."
            "Sie hat eine Packung Kondome in der Hand."
            "Hätte nicht gedacht, dass sie das tatsächlich macht."
            
        menu:
            "Ich nehme die Packung und..."
            "...bedanke mich.":
                b "Danke, %(sisName)s."
                $ sisLove += 5
                show laura neutral
                with dissolve
                
                sis "Für dich mach' ich das doch gerne, %(berndName)s."
                
                hide laura neutral
                with dissolve
            
            "...bedanke mich nicht.":
                "Ohne Worte nehme ich die Packung."
                "Mit einer Handbewegung signalisiere ich %(sisName)s, dass sie jetzt gehen kann."
                $ sisLove -= 5
                hide laura neutral
                with dissolve
    
    "Endlich kann ich Strike with Cheese gucken."
    "Wurde aber auch Zeit."
        
    scene black
    with fade
    
    scene bg keller
    with fade
    
    "Epische Folge war episch."
    "Mal gucken, ob schon ein Faden drüber auf /a/ ist."
    "Ich rufe Krautchan auf und klicke auf /a/."
    
    scene bg desktop_a
    with dissolve
    
    $ renpy.pause(2.5)
    
    "Kein Faden."
    "Dann mach' ich halt einen auf..."
    "..."
    "So."
    "Jetzt auf /b/ lauern gehen."
    "Scheint als würde mein Leben genauso weitergehen wie bisher."
    "Warum sollte sich auch etwas ändern?"
    "Heutzutage ist eh jede Stadt gleich."
    "Es ist völlig egal, wo man wohnt."
    "Mal sehen, was so los ist auf /b/."

    $ renpy.pause(2.5)
    
    scene bg desktop_b
    with dissolve
    
    "Gore."
    "Langweilig."
    "Hentai."
    "Alles schon gesehen."
    "Irgendein Faden, wo einer seinen positiven HIV-Test gepostet hat."
    "Ich sehe Pixel."
    "Langweilig."
    "Seite 2."
    "Das könnte interessant werden."
    "Stalkerbernd hat mal wieder zugeschlagen."
    "Sicher hat wieder so ein Versager irgendwo seine persönlichen Daten gepostet."
    "Selbst Schuld."
    "Den mach' ich fertig!"
    
    stop music fadeout 0.4
    
    b "Was zum...?!"
    
    #hier den bildschirm mit dem kc thread einblenden
    #Stepmania???
    
    "Ungläubig sehe ich auf den Bildschirm."
    b "Das..."
    "Ich lese es noch einmal durch."
    "Noch einmal."
    "Und noch einmal."
    "Kein Zweifel."
    "Das..."
    "Das sind ja MEINE Daten!"
    "Scheiße."
    "Wo hat der die her?"
    "Verzweifelt lasse ich mich auf mein Bett fallen."
    "Ich bin doch gerade erst hier eingezogen!"
    "Wie kommt der da überhaupt dran?"
    "Das war's."
    "Ich kann eigentlich gleich grillen gehen."
    "In einer Stunde stehen hier bestimmt 20 Bernds vor der Tür."
    "Was mach ich nur...!?"
    "AHHHHHHHHHHHH!"
    $ n(wS("Ich bin verzweifelt!","ZETSUBOU SHITA!","絶望したっ!"),interact=True)
    $ n(WS("Das Internet lässt mich verzweifeln!","NETTO SHAKAI NI ZETSUBOU SHITA!","ネット 社会 に 絶望したっ!"),interact=True)
    #Gibt es entsprechende Kanji für "shikai" in diesem Kontext?
    #Ich habe jetzt erst einmal Hiragana genommen...    
    "Was mache ich denn jetzt?"
    "Regungslos sitze ich vor dem Rechner."
    "Zuerst mal meine E-Mails abrufen..."
    
    scene bg desktop_email
    with dissolve
    
    "Die Adresse hat er auch gepostet."
    "..."
    "Wie erwartet."
    "Massenhaft Müll."
    "\"Hallo Bernd\""
    "Löschen."
    "\"lol internet\""
    "Löschen."
    "\"penispenispenispenis\""
    "Löschen."
    "\"HILFE\""
    "Lösch-"
    b "Hilfe?"
    b "wzf"
    b "Sinnvolle Mails?"
    b "In MEINEM Postfach?"
    b "Mal lesen..."
    
    scene bg desktop_hilfe
    with dissolve
    
    "Ich brauche deine Hilfe..."
    "...Krautchan nicht mehr geben."
    "Treffen morgen um 14 Uhr..."
    "...Alexanderplatz."
    
    b "Schlechter Witz!"
    "Wenn man jemanden mit so was reinlegen will, sollte man sich wenigstens eine halbwegs glaubwürdige Geschichte ausdenken."
    "Bei so einer Nachricht würde doch niemand reagieren."
    "Andererseits..."
    "Ich will nicht den ganzen Tag zu Hause sein, wenn die Gefahr besteht, dass ein Bernd vor der Tür auftaucht."
    "Warum also nicht hingehen..."
    "...und mich lächerlich machen?"
    "Nein, danke!"
    "So tief bin ich noch nicht gesunken."
    "Verdammt, ich hab Kopfschmerzen."
    "Ich lege mich besser kurz hin."
    
    scene black
    with fade
    
    $ renpy.music.set_volume(0.0, .5, channel="music")
    
    "Zwei Stunden später..."
    
    scene bg keller
    with fade
    
    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    "Das scheint nicht geholfen zu haben."
    "Im Gegenteil."
    "Die Kopfschmerzen sind schlimmer geworden."
    "Ich brauch 'ne Kopfschmerztablette."
    "Mühsam stehe ich auf und gehe nach oben."
    "Meine Mutter steht in der Küche und macht etwas zu essen."
    
    scene bg kueche
    with fade
    
    play music m_wohnung
    
    ma "%(berndName)s!"
    ma "Was ist denn passiert?"
    ma "Du bist ja total blass!"
    "Wenn sie wüsste..."
    b "Ich hab' nur Kopfschmerzen."
    b "Keine Ahnung wovon."
    ma "Vielleicht war das mit dem Keller doch keine so gute Idee."
    ma "Die Luft da unten ist sicherlich nicht gut für dich."
    b "Nein, daran liegt es nicht."
    "Das fehlt mir gerade noch."
    "Der Keller ist doch perfekt."
    "Da kann kein Bernd von außen reingucken und Fotos machen."
    b "Ich habe kein Problem damit, im Keller zu wohnen."
    b "So schlimm ist es ja nicht."
    b "Ich glaube einfach, dass mich der Umzug ein wenig mitgenommen hat."
    b "Es liegt bestimmt nicht an der Luft."
    ma "Möchtest du eine Kopfschmerztablette?"
    ma "Die müssen hier irgendwo sein."
    b "Ja, das wäre gut."
    "Sie wühlt in einer Kiste herum."
    ma "Komisch."
    ma "Die müssten hier sein."
    ma "%(sisName)s!"
    ma "Hast du eine Ahnung, wo die Kopfschmerztabletten sein könnten?"
    "Meine Schwester kommt aus ihrem Zimmer."
    
    show laura neutral
    with dissolve
    
    sis "Die was?"
    ma "So eine kleine, runde Packung."
    sis "Diese hier?"
    "Sie hat die Packung in der Hand?"
    ma "Wo hast du die denn her?"
    
    show laura happy
    with dissolve
    
    sis "Die standen direkt hier im Schrank."
    sis "Da, wo sie hingehören."
    
    ma "Was würde ich nur ohne dich machen?"
    
    hide laura happy
    with dissolve
    
    "Meine Mutter füllt ein Glas mit Wasser und lässt eine Tablette hineinfallen."
    ma "Warte, bis sie sich aufgelöst hat, bevor du trinkst."
    "Glaubt sie, dass ich das nicht weiß?"
    ma "In einer halben Stunde gibt es Essen."
    ma "Soll ich dich rufen oder hast du keinen Hunger?"
    "Natürlich hab' ich Hunger."
    b "Ich gehe nach unten und lege mich ein wenig hin."
    b "Sag dann einfach Bescheid, wenn das Essen fertig ist."
    ma "Natürlich."
    ma "Wenn du was gegessen hast, geht es dir sicher besser."
    b "Ja..."
    "Ich nehme das Glas und gehe nach unten."
    
    scene bg kellertreppe
    with fade
    
    "Die Kellertreppe kommt mir irgendwie länger vor als vorher."
    "Merkwürdig."
    "Liegt wahrscheinlich an den Kopfschmerzen."
    "Langsam und vorsichtig steige ich die Stufen hinab."
    "Mein Kopf fühlt sich an, als würde er 20 Kilo wiegen."
    
    stop music fadeout 0.4
    
    show bg kellertreppe_blur
    with cloudtransSlow
    
    "Die Kellertreppe verschwimmt vor meinen Augen."
    "Ich verliere das Gleichgewicht."
    
    scene black
    with cloudtrans
    
    play sound "sounds/hit_1.wav"
    $ renpy.pause(0.5)
    play sound "sounds/glass.wav"
    
    "Ein Glas zersplittert irgendwo."
    "Ein dumpfer Schmerz am Hinterkopf."
    ma "W.. wa. ..s .ür ein Ger...."
    "Irgendwo in der Ferne ruft meine Mutter..."
    ma "Oh G...!"
    "Ihre Stimme ist lauter als vorher."
    ma "%(sisName)s!"
    ma "Komm schnell!"
    "Jetzt höre ich sie nicht mehr."
    
    $ renpy.pause(1.0)
    
    ma "%(berndName)s!"
    ma "Hörst du mich?"
    ma "Geht's dir gut?"
    
    scene bg keller_blur
    with fade
    
    "Wo bin ich?"
    "Mein Zimmer..."
    "Mein Kopf."
    ma "%(berndName)s!!"
    "Meine Mutter."
    
    show bg keller
    with noisetrans
    
    play music m_bernd
    
    b "Was..."
    b "...ist passiert?"
    ma "Du warst bewusstlos."
    "Ich erinnere mich."
    "Ich habe auf der Treppe das Gleichgewicht verloren und bin gestürzt."
    ma "Bin ich froh, dass du nicht ernsthaft verletzt worden bist."
    "Nicht ernsthaft?"
    b "Was meinst du mit \"nicht ernsthaft\"?"
    ma "Deine Hand..."
    "Ich versuche die Finger meiner rechten Hand zu bewegen, aber mehr als ein Zucken kriege ich nicht zustande."
    "Sie sind völlig taub."
    b "Was ist mit meiner Hand?"
    ma "Du hattest das Glas in der Hand, als du gefallen bist."
    ma "Anscheinend ist es beim Aufprall in deiner Hand zerbrochen."
    ma "Keine Sorge."
    ma "Das sind nur kleine Schnittwunden."
    ma "Es ist nichts Ernsthaftes."
    ma "...hoffe ich."
    "Nichts Ernsthaftes?"
    "Ich kann meine Hand nicht bewegen."
    "Na ja, ich kann mit beiden Händen fappieren, also ist es so schlimm nicht."
    ma "Ich hab' dir Pflaster drauf gemacht."
    ma "In ein paar Tagen ist das wieder ok."
    ma "Sei froh, dass es nur die Hand ist und kein Auge."
    "Sie hat Recht."
    b "...wie lange war ich bewusstlos?"
    ma "Ein paar Stunden."
    ma "Es ist 22 Uhr."
    "Mein Magen knurrt."
    ma "Hast du Hunger?"
    ma "Ich kann dir dein Essen nochmal warm machen."
    b "Ja, das wäre gut."
    "Ich habe wirklich Hunger."
    ma "Na gut."
    ma "Ich bin gleich wieder da."
    "Sie geht nach oben."
    "Ich versuche einen klaren Gedanken zu fassen, aber mein Kopf hat wohl etwas dagegen."
    "Warum bin ich überhaupt die Treppe runtergefallen?"
    "So was passiert mir doch sonst nicht."
    "Ich höre Schritte auf der Treppe."
    "Das wird meine Mutter mit dem Essen sein."
    "Ich setze mich aufrecht auf meine Matratze."
    "Überraschenderweise ist es %(sisName)s, die das Zimmer betritt."
    
    show laura neutral
    with dissolve
    
    b "Was machst du denn hier?"
    b "Müsstest du nicht schon längst schlafen?"
    "Sie setzt sich neben mich auf die Matratze."
    
    show laura embarrassed
    with dissolve
    
    sis "Aber..."
    sis "...ich hab' mir solche Sorgen um dich gemacht, dass ich nicht schlafen konnte."
    b "Dummkopf."
    b "Um mich musst du dir keine Sorgen machen."
    b "Ich halte so was doch aus."
    
    show laura sad
    with dissolve
    
    sis "Aber..."
    sis "...ich hatte so Angst, dass dir was Schlimmes passiert ist und..."
    "Oh Mann."
    "Gleich heult sie los."
    
    show laura crying
    with dissolve
    
    sis "...versprich mir, dass du so was nie wieder machst!"
    "Wenn meine Mutter jetzt reinkommt, glaubt sie wieder, ich wäre Schuld."
    "Eigentlich...{w}bin ich das ja auch indirekt."
    b "Hör auf zu weinen."
    b "Dafür bist du doch schon viel zu alt."
    sis "Versprich es mir erst!"
    sis "Sonst höre ich nicht auf!"
    "Was ich nicht alles mache, damit sie aufhört zu weinen..."
    b "Ist ja gut."
    b "Ich verspreche es."
    "Ich bin zu nett zu ihr..."
    b "Ich passe auf mich auf."
    show laura sad
    with dissolve
    sis "Wenn du das so sagst..."
    sis "...klingt das nicht sehr überzeugend."
    "Was soll ich denn noch sagen?"
    sis "Versprichst du es mir ganz ehrlich?"
    b "Ja."
    b "Ganz ehrlich."
    "Sie legt ihren Kopf an meine Schulter."
    
    show laura sad_smile
    with dissolve
    
    sis "Ich hab dich gern, %(berndName)s."
    "Hey!"
    "So viel körperliche Nähe bin ich nicht gewohnt!"
    b "D-Du solltest jetzt wirklich schlafen gehen."
    b "Ich brauche meine Ruhe."
    
    show laura happy
    with dissolve
    
    sis "OK!"
    sis "Gute Nacht, %(berndName)s!"
    b "Schlaf gut."
    "Sie dreht sich um und läuft die Treppe nach oben."
    
    hide laura happy
    with dissolve
    
    "Manchmal ist sie total nervig und manchmal total nett."
    "Ich verstehe sie einfach nicht."
    "Sind alle kleinen Schwestern so?"
    "In Hentaigames sind die ganz anders..."
    "...immer nett und freundlich..."
    "...hilfsbedürftig..."
    "...würden alles für einen tun..."
    "...ich wünschte %(sisName)s wäre wenigstens ein bisschen so."
    "Aber so was gibt es wohl nur in 2D-Form."
    
    play sound "sounds/door_1.wav"
    
    ma "Dein Essen ist fertig."
    "Meine Mutter betritt den Raum."
    ma "War deine Schwester gerade hier oder warum war die Tür zu?"
    ma "Die müsste doch schon längst im Bett sein."
    b "N- Nein."
    b "Die war nicht hier."
    b "Die schläft bestimmt schon."
    ma "Na dann."
    "Sie stellt mir einen Teller hin."
    "Kartoffelsalat und Würstchen."
    b "Danke."
    ma "Brauchst du sonst noch etwas?"
    "Brauche ich sonst noch etwas?"
    b "Nein."
    b "Ich hab alles."
    ma "OK."
    ma "Am besten schläfst du, wenn du fertig gegessen hast."
    ma "Ich wünsch' dir schon mal eine gute Nacht."
    b "Gute Nacht."
    "Sie verlässt das Zimmer."
    "Ich wende mich meinem Kartoffelsalat zu."
    "Ich überlege, ob ich noch auf Krautchan gehen soll, aber verwerfe den Gedanken schnell wieder."
    "Erstmal brauche ich jetzt Schlaf."
    "Nachdem ich das letzte Würstchen gegessen habe, schalte ich den Monitor aus und lege mich hin."
    "Was wohl aus dieser Sache mit dem Treffen wird..."
    "...ich habe immer noch keine Ahnung ob ich hingehen soll."
    "Vielleicht schlafe ich auch einfach..."
    "...den ganzen..."
    "...Tag..."
    "..."
    
    $ renpy.music.set_volume(0.0, .5, channel="music")
        
    scene black
    with fade

    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    "Am nächsten Tag..."
    
    scene bg keller
    with fade
   
    "Als ich aufwache, sehe ich auf die Uhr."
    "Es ist bereits 13 Uhr."
    "Ich habe lange geschlafen."
    b "Oh Mann..."
    b "Mein Kopf..."
    "Da fällt mir alles wieder ein."
    "Stalkerbernd."
    "Die E-Mail."
    "Meine Verletzung."
    "Ich versuche, meine Finger zu bewegen."
    "Langsam kehrt das Gefühl zurück, aber benutzen kann ich sie noch nicht."
    "Die E-Mail."
    "Sollte ich mich wirklich mit einem Bernd treffen?"
    "Was, wenn niemand da ist?"
    "Sicher lauert er dann irgendwo an einer Ecke und macht Fotos von mir."
    "Ich mach mich doch nicht zum Affen."
    "...aber was ist, wenn die Mail wirklich ernst gemeint war?"
    "\"Es wird Krautchan nicht mehr geben.\"..."
    "Was soll das überhaupt?"
    "Wen interessiert das denn?"
    "Wenn es KC nicht mehr gibt, wird es ein neues, deutsches Imageboard geben."
    "4chan-Style."
    "...aber ein Leben ohne KC..."
    "Verdammt..."
    "Was soll ich tun?"
    
    menu:
        " "
        "Ich gehe hin.":
            "Was hab ich schon zu verlieren...?"
            "Ich gehe einfach hin."
            "Ich sehe auf die Uhr."
            b "Noch 45 Minuten..."
            
            play sound "sounds/door_1.wav"
            
            ma "Noch 45 Minuten bis...?"
            "Meine Mutter steht im Zimmer."
            "Ich brauch wirklich einen Schlüssel für diese Tür."
            ma "Ich möchte, dass du %(sisName)s von der Schule abholst, %(berndName)s."
            "Ausgerechnet jetzt..."
            b "Ich hab aber gleich 'ne Verabredung."
            ma "Ja klar."
            ma "Du."
            ma "Soll das ein Witz sein?"
            b "Nein."
            b "Ich treffe mich gleich mit jemandem am Alexanderplatz."
            ma "Nein, tust du nicht."
            ma "Du wirst jetzt deine Schwester abholen."
            b "Aber ich bin verletzt!"
            ma "Das ist nur deine Hand."
            ma "Die brauchst du nicht, um deine Schwester abzuholen."
            b "Mir ist aber immer noch schwindelig."
            ma "Schluss mit den Ausreden."
            ma "Ich hab keine Lust sie abzuholen, also musst du gehen."
            ma "Ende der Durchsage."
            
            menu:
                " "
                "OK. Ich gehe.":
                    b "OK."
                    b "Ich geh' ja schon."
                    ma "Gut."
                    ma "Beeil dich."
                    "Ich packe alles zusammen und gehe nach oben."
                    
                    jump eins_sisAbholen
                    
                "Nein, ich gehe nicht.":
                    b "Nein."
                    b "Ich habe doch gesagt, dass ich eine Verabredung habe."
                    ma "Du willst doch nur deine Schwester nicht abholen!"
                    b "Nein, verdammt!"
                    b "Ich muss jetzt los, sonst komme ich zu spät."
                    ma "Was soll ich mit dir nur machen?"
                    "Sie verlässt das Zimmer."
                    "Ich stehe auf und überlege, was ich alles brauche."
                    "Handy, Schlüssel, Geld."
                    "Moment..."
                    "Mein Geld ist weg."
                    "Naja, das kann ich nachher suchen."
                    "Ich werde es unterwegs nicht brauchen."
                    "Schnell packe ich alles zusammen und gehe nach oben."
                    
                    scene black
                    with fade
                    
                    jump eins_treffenBerndf
                    
        "Ich bin doch nicht blöd.":
            "Wieso sollte ich da hingehen?"
            b "Ich hab wirklich Besseres zu tun."
            
            play sound "sounds/door_1.wav"
            
            ma "Richtig."
            "Meine Mutter steht im Zimmer."
            "Ich brauch' wirklich einen Schlüssel für diese Tür."
            ma "Ich möchte, dass du %(sisName)s von der Schule abholst, %(berndName)s."
            b "Muss ich?"
            ma "Ja."
            "Verdammt."
            b "Ich bin aber verletzt."
            ma "Deine Hand?"
            ma "Das wird dich nicht daran hindern deine Schwester abzuholen."
            ma "Geh' schon!"
            b "OK, OK."
            b "OK."
            b "Ich geh' ja schon."
            ma "Gut."
            ma "Beeil dich."
            "Ich packe alles zusammen und gehe nach oben."
           
            jump eins_sisAbholen