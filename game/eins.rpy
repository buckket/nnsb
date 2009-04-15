#Kapitel 1
#Einen Monat nach den Ereignissen des Prologs
#max sisLove = 50

#---------------------------------------
#
#INHALT
#
#label eins
#start von kapitel 1, alles vor der entscheidung ob treffen oder nicht
#
#label eins_treffenBerndf
#erstes und zweites treffen mit abzweigung zu abholen
#
#label eins_accept_fBernd
#annehmen des angebots von Anja
#
#label eins_refuse_fBernd
#ablehnen des angebots von Anja
#
#label eins_sisAbholen_promise
#kurzer dialog wenn man der schwester versprochen hat sie abzuholen
#
#label eins_sisAbholen
#abholen der schwester am zweiten tag nach berndtreffen
#
#label eins_krautchanOff
#krautchan geht off
#
#label eins_sisAbholenZuerst
#abholen der schwester am ersten und zweiten tag + stalking
#
#label eins_ende
#sprung zu kapitel 2
#
#---------------------------------------
label eins:    
    
    stop music fadeout 1.0

    scene splash splash_eins
    with gradientTrans

    $ renpy.pause(5.0)

    scene black
    with gradientTrans
    
    "Einen Monat später..."
    
    play music "music/bernd_theme.ogg"
    
    scene bg keller_aus
    with spotTrans
    
    ma "%(berndName)s, willst du nicht aufstehen?"
    
    menu:
        " "
        
        "OK, ich steh' auf.":
            $ maLove += 5
            b "OK, ich steh' auf."
            "Scheiße, ich hab 'ne Morgenlatte."
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
            "Scheiße, ich hab 'ne Morgenlatte."
            "Wenn meine Mutter die sieht, gibt sie wieder 'nen blöden Kommentar ab."
            "Ich muss irgendwie Zeit rausschinden."
            b "Wie spät ist es denn?"
            ma "Viertel vor Zwölf."
            b "Es ist noch viel zu früh zum Aufstehen."
            ma "%(berndName)s!"
            "Jetzt ist sie sauer..."
           
    
    "Genau im richtigen Moment kommt %(sisName)s rein."
    
    play sound "sounds/door_1.wav"
    
    show laura happy
    with dissolve
    
    play music "music/laura_theme.ogg"
    
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
            "Was Jemand, der in meinem Alter noch Jungfrau ist, wohl jede Nacht träumt."
            show laura neutral
            with dissolve
            sis "Nur so."
            sis "Man sagt, dass das, was man in der ersten Nacht in einer neuen Wohnung träumt, in Erfüllung geht."
            "Davon hab' ich noch nie gehört."
            "Wer denkt sich sowas aus?"
            b "Tja, vielleicht hast du Recht."
            b "Was hast DU denn heute Nacht geträumt?"
            show laura embarrassed
            with dissolve
            sis "Ach..."
            sis "...nichts Besonderes."
            b "Sag schon!"
            show laura happy
            with dissolve
            sis "Ist doch sowieso nur ein dummer Aberglaube!"
            "Sie will es mir wohl nicht erzählen..."
            b "Ist es dir peinlich oder warum willst du es mir nicht sagen?"
            show laura emb_surprised
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
            b "Dann kann ich jetzt ja in Ruhe fap-"
            
            play sound "sounds/door_1.wav"
            
            show laura neutral
            with dissolve
            
            play music "music/laura_theme.ogg"
            
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
                    b "Da haben wir auch beide was von."
                    
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
            
            #sis beleidigt
            sis "Dann geh' ich halt!"
            sis "Bäh!"
            
            hide laura happy
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
    
    play music "music/bernd_theme.ogg"
    
    "Seit einem Monat denke ich immer an das Mädchen aus dem Supermarkt."
    
    "Warum musste sie auch so geil aussehen?"
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
    "Ich werde sie wohl niemals wiederseh-"
    
    stop music
    
    scene bg keller_aus
    with flash
    
    scene bg keller_aus
    with slowFlash
    $ renpy.pause(0.5)
    
    scene bg keller_aus
    with damnSlowFlash
    $ renpy.pause()
    
    "Ich kam."
    "Erschöpft lasse ich mich auf's Bett fallen."
    "Ich glaub', ich bin verliebt."
    "Dabei dachte ich immer..."
    "...Bernd braucht keine Liebe."
            
    play sound "sounds/error.wav"        
    
    "Ein Signalton befördert mich unsanft aus meinen Gedanken."
    
    play music "music/bernd_theme.ogg"
    
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
    
    scene bg badezimmer
    with fade



    #play sound "sound/dusche.wav"

    #muss noch gefunden werden
    play music "music/bernd_wohnung.mp3"


    b "So, fertig geduscht."

    "Jetzt muss ich erstmal meinen Hunger bekämpfen."

    scene bg kueche
    with fade

    b "Was ess' ich denn jetzt mal..."

    b "Mal gucken, was so im Kühlschrank ist."
    "Ich öffne die Kühlschranktür."
    $ renpy.music.play ("music/rugenwalder.ogg", channel=7, loop=False, fadeout=None, synchro_start=False, fadein=0, tight=False, if_changed=False)
    b "OH MEIN GOTT!"
    b "Das ist doch...!"
    b "RÜGENWALDER TEEWURST!"
    b "DIE MIT DER MÜHLE!"
    b "Wie viele nehm' ich denn?"
    b "ALLE!"
    #om nom nom sound
    #Sound
    b "RÜGENWALDER!"
    b "GROB ODER FEIN, DIE MIT DER MÜHLE MUSS ES SEIN!"

    b "Hm..."
    b "Lecker."
    stop music fadeout 0.5

    b "So, endlich kann ich Strike with Cheese schauen."
    
    scene bg keller_bluescreen
    with fade
   
    play music "music/bernd_theme.ogg"
    
    "Als ich wieder in den Keller komme, ist der ganze Raum in ein blaues Licht getaucht."
    "Sofort schaue ich auf den Bildschirm."
    
    b "OH MEIN GOTT, WAS IST GESCHEHEN!?"
    b "WAS IST DAS DENN!!?"
    b "DU HURENSOHN!"
    b "DIE RESET-TASTE..."
    b "WO IST DIE RESET-TASTE!?"
    b "STARTE DAS VERDAMMTE BETRIEBSSYSTEM!"
    
    show bg keller_aus
    
    $ renpy.pause(3.0)
    
    play sound "sounds/boot.wav"
    
    $ renpy.pause(2.0)
    
    show bg keller
    with dissolve
    
    b "Geht doch..."
    "Ich brauche wirklich mal einen neuen PC."
    "Dieses alte Teil ist wirklich zu nichts mehr gut."
    "Andauernd stürzt das Ding ab."
    #BUTTERGOTT hier noch eine zeile
    "Auf /b/ scheint wieder nichts los zu sein."
    "Krautchan saugt in letzter Zeit ziemlich."
    "Warum nur?"
    "Naja, wenigstens kann ich dann jetzt endlich Strike with Cheese gucken."
    
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
            ma "%(berndName)s!!"
            ma "Du kommst jetzt sofort hoch und hilfst deiner Schwester beim Tragen!"
            b "In Ordnung. Ich komme ja schon."
        
        
    "Ich stehe auf und gehe nach oben."
    
    stop music fadeout 0.4
    
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
    
    play music "music/bernd_theme.ogg"
    
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
            show laura neutral
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
    
    "Ungläubig sehe ich auf den Bildschirm."
    b "Das..."
    "Ich lese es noch einmal durch."
    "Noch einmal."
    "Und noch einmal."
    "Kein Zweifel."
    "Das..."
    b "Das sind ja MEINE Daten!"
    "Scheiße."
    "Wo hat der die her?"
    "Ich bin doch gerade erst hier eingezogen?"
    "Wie kommt der da überhaupt dran?"
    "Das war's."
    "Ich kann eigentlich gleich grillen gehen."
    "In einer Stunde stehen hier bestimmt 20 Bernds vor der Tür."
    b "Was mach ich nur...!?"
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
    
    #hier die email einblenden
    
    "Ich brauche deine Hilfe..."
    "...Krautchan nicht mehr geben."
    "Treffen morgen um 14 Uhr..."
    "...Alexanderplatz."
    
    b "Verarschen kann ich mich alleine!"
    "Wenn man jemanden mit sowas reinlegen will, sollte man sich wenigstens eine halbwegs glaubwürdige Geschichte ausdenken."
    "Bei so einer Nachricht würde doch niemand reagieren."
    "Andererseits..."
    "Ich will nicht den ganzen Tag zuhause sein, wenn die Gefahr besteht, dass ein Bernd vor der Tür auftaucht."
    "Warum also nicht hingehen..."
    "...und mich lächerlich machen?"
    "Nein, danke!"
    "So tief bin ich noch nicht gesunken."
    #BUTTERGOTT mehr
    "Scheiße, ich hab Kopfschmerzen."
    "Ich lege mich besser kurz hin."
    
    scene black
    with fade
    
    "Zwei Stunden später..."
    
    scene bg keller
    with fade
    
    play music "music/bernd_theme.ogg"
    
    "Das scheint nicht geholfen zu haben."
    "Im Gegenteil."
    "Die Kopfschmerzen sind schlimmer geworden."
    "Ich brauch 'ne Kopfschmerztablette."
    "Mühsam stehe ich auf und gehe nach oben."
    "Meine Mutter steht in der Küche und macht etwas zu essen."
    
    scene bg kueche
    with fade
    
    play music "music/bernd_wohnung.mp3"
    
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
    "Meine Kopf fühlt sich an, als würde er 20 Kilo wiegen."
    
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
    #with Dissolve(2.0)
    with noisetrans
    
    play music "music/bernd_theme.ogg"
    
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
    "Naja, ich kann mit beiden Händen fappieren, also ist es so schlimm nicht."
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
    "Sowas passiert mir doch sonst nicht."
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
    b "Ich halte sowas doch aus."
    show laura sad
    with dissolve
    sis "Aber..."
    sis "...ich hatte so Angst, dass dir was Schlimmes passiert ist und..."
    "Oh Mann."
    "Gleich heult sie los."
    show laura crying
    with dissolve
    sis "...versprich mir, dass du sowas nie wieder machst!"
    "Wenn meine Mutter jetzt reinkommt, glaubt sie wieder, ich wäre Schuld."
    "Naja..."
    "...bin ich ja auch indirekt."
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
    show laura sadsmile
    with dissolve
    sis "Ich hab dich gern, %(berndName)s."
    "Hey!"
    "So viel körperliche Nähe bin ich nicht gewohnt!"
    b "D- Du solltest jetzt wirklich schlafen gehen."
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
    
    scene black
    with fade
    
    "Was wohl aus dieser Sache mit dem Treffen wird..."
    "...ich habe immer noch keine Ahnung ob ich hingehen soll."
    "Vielleicht schlafe ich auch einfach..."
    "...den ganzen..."
    "...Tag..."
    "..."
    
    "Später..."
    
    scene bg keller
    with fade
   
    play music "music/bernd_theme.ogg"
   
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
            stop music fadeout 0.4
            
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
                    $ anjaTreffen = 0
                "Nein, ich gehe nicht.":
                    $ anjaTreffen = 1
        "Ich bin doch nicht blöd.":
            $ anjaTreffen = 0
            "Ha, wieso sollte ich da hingehen?"
            b "Ich hab wirklich Besseres zu tun."
            
            play sound "sounds/door_1.wav"
            
            ma "Richtig."
            "Meine Mutter steht im Zimmer."
            "Ich brauch' wirklich einen Schlüssel für diese Tür."
            ma "Ich möchte, dass du %(sisName)s von der Schule abholst, %(berndName)s."
            b "Muss ich?"
            ma "Ja."
            "Scheiße."
            b "Ich bin aber verletzt."
            ma "Deine Hand?"
            ma "Das wird dich nicht daran hindern deine Schwester abzuholen."
            ma "Geh' schon!"
            b "OK, OK."
            #jump eins_sisAbholen
    if anjaTreffen == 1:
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
        
    if anjaTreffen == 0:
        b "OK."
        b "Ich geh' ja schon."
        ma "Gut."
        ma "Beeil dich."
        "Ich packe alles zusammen und gehe nach oben."
        jump eins_sisAbholenZuerst
        
label eins_treffenBerndf:
    scene bg zuhause_draussen
    with fade
    
    play music "music/bernd_wohnung.mp3"
    
    b "Wo lang jetzt...?"
    "Ich kenn mich hier ja überhaupt nicht aus."
    b "Zuerst mal zur nächsten, großen Straße."
    "Ich biege um die Ecke."
    "Eine alte Frau kommt mir entgegen."
    "Die könnte ich nach dem Weg fragen."
    "Ich gehe auf sie zu."
    "Als sie mich bemerkt, sieht sie mich an, aber ich drehe den Kopf weg und gehe an ihr vorbei."
    "Ich kann nichtmal jemanden nach dem Weg fragen."
    "Erbärmlich."
    "Ich gehe die Straße runter und blicke am Ende nach links und rechts."
    "Rechts ist eine Sackgasse, aber links scheint es auf eine größere Straße zuzugehen."
    "Also da lang."
    "Warum bin ich eigentlich nochmal losgegangen?"
    "Als würde dort ernsthaft ein Bernd auf mich warten, damit ich ihm helfe, Krautchan zu retten."
    "Das ist absurd."
    "In Gedanken versunken, laufe ich fast auf die Straße."
    "Zum Glück merke ich rechtzeitig, dass der Fußweg hier zu Ende ist."
    "Ich sehe mich um."
    b "OK."
    b "Das war leichter als gedacht."
    "In der Ferne sehe ich den Fernsehturm."
    "Wenn ich mich richtig erinnere, ist der direkt am Alexanderplatz."
    b "Also da lang..."
    
    scene black
    with fade
    
    "Einige Minuten später..."
    
    scene bg alexanderplatz_eins
    with fade
    
    b "Das ging schneller als ich dachte."
    "Jetzt muss ich warten."
    "Ich sehe auf die Uhr."
    "Genau zwei Minuten vor zwei."
    "Nirgendwo eine Spur von Bernd."
    "Aber der Platz ist groß."
    b "Am besten laufe ich ein wenig herum."
    
    scene bg alexanderplatz_zwei
    with fade
    
    "Jetzt ist es schon fünf Minuten nach zwei."
    "Wahrscheinlich hat mich Bernd doch nur verarscht und lacht sich jetzt tot."
    b "Scheiße."
    "Fünf Minuten warte ich noch, dann gehe ich."
    "Sicher sitzt er irgendwo an einer Ecke und macht grade Fotos."
    "Gab es hier nicht auch eine Live Webcam?"
    "Wahrscheinlich beobachtet mich schon ganz Krautchan."
    "Ich könnte versuchen, mich zu verstecken."
    "Zwischen den Menschen falle ich sicher nicht so auf, wie wenn ich alleine hier herumstehe."
    "..."
    "Wieso sind hier überhaupt so viele Leute?"
    "Haben die kein Zuhause?"
    "Was hier teilweise für Gestalten rumlaufen..."
    "Schrecklich."
    "Was wollen die alle h-"
    
    show anja neutral
    with flash
    
    hide anja neutral
    with dissolve
    
    b "Das war doch..."
    "Es war nur ein kurzer Augenblick, aber irgendwo in der Menge habe ich sie gesehen..."
    "Das Mädchen aus dem Supermarkt."
    "...aber warum sollte sie hier sein?"
    "Warum gerade jetzt?"
    "Ich schaue mich um, aber sie ist nirgends zu sehen."
    b "Wo ist sie hin?"
    "Da."
    "Sie ist in einer großen Menschenmenge."
    "Ein ganzes Stück weit weg, aber sie kommt in meine Richtung."
    "Oder ist sie das nicht?"
    "Ich gehe auf sie zu."
    "Was denke ich mir dabei?"
    "Will ich sie ansprechen?"
    "Das traue ich mich nicht."
    "Niemals."
    "Nur noch wenige Meter trennen uns."
    "Jetzt kann ich sie erkennen."
    "Das ist sie ganz sicher."
    
    show anja neutral
    with flash
    
    "Ich gehe an ihr vorbei und sehe sie an."
    "Nur keine Aufmerksamkeit erregen."
    "Sie dreht sich zu mir um."
    "Scheiße, jetzt hat sie mich bemerkt."
    "Ich hätte sie nicht so anstarren dürfen."
    "Schnell wende ich mich ab."
    
    u"Mädchen" "%(berndName)s?"
    
    play music "music/anja_theme.mp3"
    
    "Was...?"
    "Meint sie mich?"
    "Unmöglich."
    u"Mädchen" "Hey, %(berndName)s!"
    "Ich spüre eine Hand auf meiner Schulter und zucke zusammen."
    b "Was...?"
    "Woher kennt sie meinen Namen?"
    "Was soll das...?"
    u"Mädchen" "Du bist doch %(berndName)s, oder?"
    "Ich nicke verwirrt."
    u"Mädchen" "Na also."
    u"Mädchen" "Komm mit."
    u"Mädchen" "Wir gehen irgendwo hin, wo wir reden können."
    "Ich folge ihr."
    
    scene bg alexanderplatz_drei
    with fade
    
    show anja neutral
    with dissolve
    
    u"Mädchen" "Hier sind weniger Leute."
    u"Mädchen" "Das ist besser zum Reden."
    u"Mädchen" "Gut, dass du gekommen bist, %(berndName)s."
    b "Ich..."
    "Wovon redet sie?"
    
    show anja surprised
    with dissolve
    
    u"Mädchen" "Ah!"
    u"Mädchen" "Ich habe mich ja noch gar nicht vorgestellt!"
    
    show anja neutral
    with dissolve
    
    u"Mädchen" "Ich bin %(wBerndName)s."
    bw "Ich habe dir die E-Mail geschickt."
    bw "Deshalb bist du hier, oder?"
    "Was zum...?"
    "SIE ist der Bernd, der mir die Mail geschickt hat?"
    "Das ergibt keinen Sinn."
    "Verwundert sehe ich sie an."
    bw "Nicht?"
    bw "Hast du meine Mail nicht bekommen?"
    if berndName != "Bernd":
        bw "Aber du bist doch ein Bernd, oder?"
    else:
        bw "Aber du bist doch Stalkerbernds neuestes Opfer, oder?"
    "Ich nicke."
    b "J... ja."
    b "Ich bin wegen der E-Mail hier aber..."
    
    show anja surprised
    with dissolve
    
    bw "Ah!"
    bw "Jetzt versteh' ich!"
    bw "Du bist überrascht, dass ich ein Mädchen bin, richtig?"
    
    show anja neutral
    with dissolve
    
    b "Äh... ja."
    bw "Hihi."
    bw "Hätte ich das geschrieben, wärst du sicher nicht gekommen, oder?"
    "Sie hat recht."
    "Ich kann immer noch nicht glauben, dass sie ein Bernd ist."
    "Ich dachte immer, es gäbe keine Frauen im Internet."
    bw "War ja klar."
    bw "Du bist ein typischer Bernd."
    "Macht sie sich über mich lustig?"
    bw "Tut mir Leid."
    bw "Ich wollte dich nicht beleidigen oder so."
    "Anscheinend kann sie meine Gedanken lesen."
    bw "Ich brauche dich schließlich noch."
    "Sie braucht mich?"
    "Wofür?"
    b "Was meinst du...?"
    bw "Na wegen Krautchan!"
    "Achso wegen Krautchan."
    "Das erklärt..."
    "...nichts."
    bw "Wenn wir nichts unternehmen wird Krautchan untergehen!"
    "Was labert die denn da?"
    "Sind ALLE Frauen verrückt im Kopf?"
    b "Was redest du v-"
    
    show anja surprised
    with dissolve
    
    bw "OH!"
    bw "Ich muss nach Hause!"
    
    "Was zum...?"
    
    show anja neutral
    with dissolve
    
    bw "%(berndName)s."
    b "Ja?"
    bw "Wir treffen uns morgen wieder hier."
    bw "Um die gleiche Zeit."
    bw "Bis dann."
    
    hide blond
    with dissolve
    
    "Sie rennt zur Straßenbahn."
    "Bevor ich merke, was passiert ist, ist sie schon weg."
    
    stop music fadeout 0.4
    
    "Was sollte das?"
    "Morgen um die gleiche Zeit?"
    "Was glaubt sie, wer sie ist?"
    "Kommandiert mich hier herum."
    "Verwirrt trete ich den Heimweg an."
    
    scene black
    with fade
    
    scene bg keller
    with fade
    
    play music "music/bernd_theme.ogg"
    
    "Zuhause angekommen lasse ich mich auf meine Matratze fallen."
    "Noch einmal lasse ich mir die Geschehnisse des heutigen Tages durch den Kopf gehen."
    "Stalkerbernd hat meinen Namen, meine E-Mail Adresse und ein Foto von mir gepostet."
    "Ein Bernd hat mir daraufhin einen Hilferuf geschickt."
    "Am vereinbarten Treffpunkt traf ich das Mädchen aus dem Supermarkt."
    "Es stellt sich heraus, dass sie der Bernd mit dem Hilferuf ist."
    "Sie will, dass ich ihr helfe, Krautchan zu retten."
    b "..."
    b "wat"
    "Das ergibt alles keinen Sinn."
    "Je mehr ich darüber nachdenke, desto mehr tut mir der Kopf weh."
    b "Nicht schon wieder..."
    b "Vielleicht sollte ich was essen..."
    "Ich beschließe in die Küche zu gehen."
    
    scene bg kueche
    with fade
    
    play music "music/bernd_wohnung.mp3"
    
    "Ich öffne die Kühlschranktür."
    b "OH MEIN GOTT!"
    b "Das ist doch...!"
    b "Nichts."
    "Der Kühlschrank ist leer."
    "Ich höre, wie die Wohnungstür aufgemacht wird."
    ma "%(berndName)s! Wir sind wieder da!"
    ma "Bist du hier?"
    "Ich gehe in den Flur."
    
    scene bg wohnung_innen
    with fade
    
    b "Ja."
    b "Wo wart ihr?"
    ma "Ich war deine Schwester abholen."
    ma "Du wolltest ja anscheinend nicht."
    ma "Jetzt hängst du doch hier rum?"
    ma "Das muss aber ein kurzes Treffen gewesen sein."
    b "War es."
    
    show laura happy
    with dissolve
    
    sis "Hallo, %(berndName)s."
    b "Hi."
    
    hide laura happy
    with dissolve
    
    ma "Ich will, dass du %(sisName)s zum Einkaufen mitnimmst."
    ma "Der Kühlschrank ist leer."
   
    b "Ich will aber ni-"
    
    show laura happy
    with dissolve
    
    sis "OK!"
    sis "Komm, %(berndName)s!"
    "Sie nimmt meinen Arm und versucht mich nach draußen zu ziehen."
    b "Na gut, ich komm ja schon..."
    
    scene bg zuhause_draussen
    with fade
    
    if supermarkt == "":
        $ supermarkt = "Aldi"
    
    "Wir gehen in Richtung %(supermarkt)s."
    
    show laura neutral
    with dissolve
    
    sis "Sag mal %(berndName)s..."
    b "Ja?"
    sis "Wieso hast du mich heute nicht von der Schule abgeholt?"
    "Oh Mann."
    "Wie erklär' ich ihr das?"
    b "Ich... äh..."
    sis "Du hattest wieder keine Lust, oder?"
    b "Nein!"
    b "Das stimmt gar nicht!"
    sis "Ich wusste es."
    sis "Du bist hoffnungslos, %(berndName)s."
    
    show laura happy
    with dissolve
    
    sis "Aber ich hab dich trotzdem lieb!"
    "Sie hält immer noch meinen Arm fest."
    sis "Morgen kommst du mich abholen, ja?"
    "Erwartungsvoll sieht sie mich an."
    
    menu:
        " "
        "Auf jeden Fall!":
            $ sisLove += 20
            $ anjaTreffen2 = -1
            sis "Ich werde auf dich warten."
            sis "...und wehe du kommst nicht."
            b "Was dann?"
            sis "Das wirst du schon sehen..."
            sis "...und es wird dir nicht gefallen."
            b "Was meinst..."
            sis "Schau!"
            sis "Wir sind da."
        "Das kann ich nicht versprechen.":
            $ anjaTreffen2 = 0
            sis "Wie immer..."
            sis "Na wenigstens bist du ehrlich."
            sis "Ich hab von jemandem wie dir auch nichts anderes erwartet."
            b "Von jemandem wie mir?"
            b "Was soll das denn heißen?"
            sis "Das wirst du schon noch herausfinden."
            sis "Schau!"
            sis "Wir sind da."
            
    scene bg supermarkt
    with fade
    
    play music "music/shop.mp3"
    
    b "Was sollen wir nochmal einkaufen?"
    
    show laura neutral
    with dissolve
    
    sis "Hm..."
    
    show laura happy
    with dissolve
    
    sis "Keine Ahnung!"
    "Großartig..."
    b "Naja..."
    b "Kaufen wir halt Butter und Rügenwalder."
    
    show laura neutral
    with dissolve
    
    sis "Sicher, dass wir nicht mehr brauchen?"
    b "Nein, aber was sollen wir machen?"
    sis "Ich könnte Mama anrufen."
    sis "Ich hab' mein Handy dabei."
    b "Du hast ein Handy?"
    show laura happy
    with dissolve
    sis "Klar hab ich eins!"
    b "Na dann, ruf sie an."
    show laura neutral
    with dissolve
    sis "OK."
    "Sie zieht ein rosafarbenes Handy aus der Tasche."
    "Geschickt klickt sie sich durch das Menü bis sie die Nummer gefunden hat."
    "Wieso hat die in ihrem Alter schon ein Handy?"
    "Ist das normal heutzutage?"
    sis "Hallo Mama, ich bin's."
    sis "Wir haben vergessen dich zu fragen, was wir einkaufen sollen."
    sis "..."
    sis "OK."
    sis "Sonst noch was?"
    sis "..."
    sis "Alles klar!"
    show laura happy
    with dissolve
    sis "Bis gleich!"
    "Sie legt auf."
    show laura neutral
    with dissolve
    sis "Sie sagt, dass wir auch noch Milch und Brot brauchen."
    "Also Milch, Butter, Brot und Rügenwalder."
    b "OK."
    b "Dann besorgen wir das schnell und danach gehen wir nach Hause."
    sis "OK."
    hide laura neutral
    with dissolve
    "Nachdem wir alles gefunden haben, gehen wir zur Kasse."
    "Vor uns ist eine ältere Frau, die langsam einen Artikel nach dem anderen auf's Band legt."
    "Die Kassiererin ist sichtlich genervt."
    "Warum kaufen alte Leute immer so viel ein und brauchen dann eine halbe Stunde an der Kasse?"
    show laura neutral
    with dissolve
    sis "%(berndName)s?"
    b "Was denn?"
    sis "Bekomm' ich eine Packung Kaugummi?"
    b "Nein, die sind zu teuer."
    sis "Aber ich bezahl' es von meinem Taschengeld!"
    sis "Ich geb' es dir zuhause wieder!"
    sis "Ganz bestimmt!"
    "Hm..."
    b "Na gut, nimm dir eine Packung."
    show laura happy
    with dissolve
    sis "Danke, %(berndName)s."
    
    scene black
    with fade
    
    "Eine halbe Stunde später..."
    b "Endlich wieder zuhause."
    
    stop music fadeout 1.0
    
    scene bg keller
    with fade
    
    play music "music/bernd_theme.ogg"
    
    b "Mal schauen, ob der Faden mit meinen Daten noch auf /b/ ist..."
    scene bg keller_kc
    with dissolve
    "..."
    b "Nichts."
    b "Glück gehabt."
    "Es scheint, als wäre wirklich nichts weiter passiert..."
    "Bernd ist wohl wirklich völlig unfähig."
    
    #BUTTERGOTT MEHR DIALOG HIER
    
    play sound "sounds/door_1.wav"
    show laura neutral
    with dissolve
    
    sis "%(berndName)s?"
    "Was denn nun schon wieder?"
    "Kann ich nicht einmal im Keller meine Ruhe haben?"
    b "Was willst du?"
    sis "Ich wollte nur fragen, ob du mir bei den Hausaufgaben helfen kannst..."
    "Als ob ich sonst nichts zu tun hätte."
    "Oh warte..."
    "Ich habe sonst nichts zu tun."
    b "Na gut."
    b "Welches Fach denn?"
    sis "Mathematik."
    b "Na dann zeig doch mal her..."
    "Sie sieht sich um."
    sis "Hast du hier einen Stuhl?"
    sis "Im Sitzen kann man es besser erklären, oder?"
    b "Ich hol' dir eben einen von oben."
    "Ich will aufstehen, aber sie kommt mir zuvor."
    sis "Nicht nötig, %(berndName)s."
    sis "Ich kann ja hier sitzen."
    "Bevor ich etwas erwidern kann, klettert sie auf meinen Schoß."
    b "..."
    sis "Also."
    sis "Schau hier..."
    "Sie schlägt ihr Matheheft auf."
    sis "Wir sollen das hier ausrechnen."
    "Sie zeigt auf eine Aufgabe."
    b "sin(&#945;) = 1"
    b "Berechne &#945;."
    "Mal nachdenken..."
    
    menu:
        "Das ist..."
        
        "90°":
            b "Ich bin mir ziemlich sicher, dass es 90° sind."
            $ sisFrage = "richtig"
        "0°":
            b "Das müssten 0° sein."
            $ sisFrage = "falsch"
        "Globalisierung":
            b "Das ist ganz sicher Globalisierung."
            sis "Sicher?"
            b "Sicher."
            $ sisFrage = "richtigFalsch"
    
    show laura happy
    with dissolve
    
    sis "OK, danke %(berndName)s!"
    sis "Jetzt krieg ich sicher eine gute Note."
    b "Kein Problem."
    sis "Achso..."
    b "Ja?"
    "Was denn noch?"
    sis "Hier ist das Geld für die Kaugummis."
    sis "Ich hab dir ja versprochen, dass ich es dir zurückgebe."
    "Wow."
    "Daran habe ich gar nicht mehr gedacht."
    b "Äh... danke."
    sis "Bis morgen, %(berndName)s."
    b "Ja."
    b "Bis morgen."
    
    hide laura happy
    with dissolve
    
    b "Schon wieder so spät... ich lauer noch ein wenig auf /b/ und gehe dann schlafen."
    
    #random event
    
    scene black
    with fade
    
    "Am nächsten Morgen..."
    
    ma "%(berndName)s?"
    ma "Willst du nicht langsam mal aufstehen?"
    
    b "Wie spät ist es denn?"
    
    ma "Schon 13 Uhr."
    
    scene bg keller_aus
    with flash
    
    b "WAS!?"
    b "Ich wollte mich doch heute eventuell wieder mit %(wBerndName)s treffen."
    "Scheiße."
    "Jetzt hab' ich es laut gesagt."
    
    ma "Wer ist %(wBerndName)s?"
    ma "Deine imaginäre Freundin?"
    ma "Mach dich nicht lächerlich."
    
    if(anjaTreffen2 == -1):
        jump eins_sisAbholen_promise
    
    ma "Wirst du heute endlich deine Schwester abholen oder muss ich das wieder machen?"
    "Wieso soll ich das immer machen?"
    "Kann sie nicht einsehen, dass ich andere Dinge zu tun habe."
    
    menu:
        ""
        "Ich mach das schon.":
            b "Ich mach das schon."
            ma "Na dann beeil dich mal lieber."
            b "OK."
            jump eins_sisAbholen
        "Ich habe wieder eine Verabredung.":
            b "Nein, ich habe wieder eine Verabredung."
            ma "Was soll ich nur mit dir machen...?"
            "Sie verlässt das Zimmer."
    
    "Ich mache mich fertig, um mich mit %(wBerndName)s zu treffen."
    
    stop music fadeout 1.0
    
    scene bg zuhause_draussen
    with fade
    
    "Dieses Mal sollte der Weg leichter zu finden sein."
    "Tatsächlich, ich weiß noch genau, wo es lang geht."
    
    scene bg alexanderplatz_drei
    with fade
    
    "Als ich ankomme wartet %(wBerndName)s bereits auf mich."
    show anja neutral
    with dissolve
    
    play music "music/anja_theme.mp3"
    
    bw "Hey, %(berndName)s."
    b "H- Hi."
    bw "..."
    b "..."
    "Spannendes Gespräch."
    bw "...und?"
    b "Was?"
    bw "Na... wie gehts dir so?"
    b "Hm..."
    b "Ja."
    bw "Du bist ja nicht sehr gesprächig..."
    "Komm endlich zur Sache."
    b "..."
    b "Du wolltest mir erklären, warum du meine Hilfe brauchst."
    bw "Ja."
    bw "Also..."
    bw "Um es auf den Punkt zu bringen:"
    bw "Wir müssen Krautchan retten."
    "Krautchan retten."
    "Soso."
    b "Aha."
    b "Warte... was?"
    bw "Krautchan ist nicht mehr das, was es mal war."
    b "Du meinst die Neuschwuchteln."
    b "Die stören doch kaum noch."
    bw "Nein."
    bw "Wie erkläre ich das am besten..."
    bw "Krautchan wurde übernommen."
    b "lolwas?"
    "Wer würde denn Krautchan übernehmen?"
    "4chan?"
    "Oder ein anderes Imageboard?"
    bw "Der Server wurde beschlagnahmt."
    bw "Krautchan..."
    bw "...ist bereits tot."
    b "Was zum...?"
    "Server beschlagnahmt."
    "Von der Polizei?"
    "Warum das denn?"
    "Kinderpornografie?"
    "Wohl kaum..."
    bw "Die genauen Einzelheiten kenne ich auch nicht."
    bw "Ich weiß nur, dass der Server eines Morgens von der Polizei beschlagnahmt wurde."
    bw "Wir sind die Einzigen, die Krautchan retten können, %(berndName)s."
    bw "Deshalb brauch ich deine Hilfe."
    bw "Du bist der Einzige, dem ich vertrauen kann."
    b "..."
    "Was soll das?"
    "Sie trollt mich doch nur."
    "Ich wusste es von Anfang an."
    "Aber wie kann ich mir sicher sein?"
    "..."
    "Aha!"
    b "Aber Krautchan ist doch noch online?"
    b "0/10"
    b "Offensichtlicher Troll ist offensichtlich."
    "Der habe ich's gezeigt."
    "So leicht lasse ich mich nicht trollen."
    bw "Es scheint, als wäre Krautchan noch online, ja."
    bw "Aber die Realität sieht anders aus."
    b "Was soll das heissen?"
    "Willkommen in der Matrix oder was wird das hier?"
    bw "Die Seite wird von der Polizei benutzt um Bernds zu überwachen."
    bw "Es ist eine Falle!"
    "Oho!"
    "Totale Überwachung!"
    "Sowas glaubt doch kein Mensch."
    b "Wieso sollte ich dir das glauben?"
    b "Die Admins hätten doch schon längst-"
    bw "Die Admins?"
    bw "Tsaryu ist nach Japan ausgewandert."
    bw "Shaky wird von der Polizei verfolgt und ist nach Mexiko geflohen."
    bw "dergeneral ist untergetaucht."
    bw "Krautchan ist definitiv tot."
    "Da ist was dran..."
    "In letzter Zeit gab es auf KC wenig sichtbare Aktivität von Seiten der Mods."
    b "...und woher willst du das alles wissen?"
    bw "..."
    bw "Du vertraust mir nicht?"
    "Wieso sollte ich?"
    b "Bernd, das ist lächerlich!"
    b "Das klingt doch alles völlig absurd."
    bw "Hm..."
    bw "Ich habe mir wohl den falschen Bernd ausgesucht."
    bw "Ich kann also nicht auf deine Hilfe zählen?"
    b "Nicht, wenn du mir nicht erklärst, was das alles zu bedeuten hat."
    bw "Wenn ich es wüsste, würde ich es dir erklären."
    bw "Es liegt an uns, das herauszufinden."
    "Klingt wie der Plot eines schlechten Action-Adventures."
    bw "Wir müssen den Verantwortlichen finden und Krautchan retten!"
    b "Das ergibt doch alles keinen Sinn..."
    bw "Entweder du glaubst mir oder du glaubst mir nicht."
    bw "Was nun?"
    "So, %(berndName)s."
    "Jetzt musst du dich entscheiden."
    
    menu:
        "Ich..."
        
        "...glaube ihr.       ":
            $ friendLove += 10
            jump eins_accept_fBernd
        "...glaube ihr. NICHT.":
            $ friendLove -= 5
            jump eins_refuse_fBernd
            
label eins_accept_fBernd:
    $ anjaAccept = 1
    $ anjaRoute = 1

    b "Das klingt zwar alles sehr merkwürdig aber..."
    b "Ich glaube dir."
    "Tue ich das?"
    bw "Gut."
    bw "Wir haben keine Zeit zu verlieren."
    bw "Wie gehen wir vor?"
    "Das fragt sie mich?"
    b "Woher soll ich das wissen?"
    b "Es war doch deine Idee."
    bw "Also gut dann..."
    bw "Versuch' so viele Informationen wie möglich zu finden."
    bw "Bleib' am besten zuhause und benutz' das INTERNET."
    "Das kann ich wenigstens."
    bw "Ich werde mich ein wenig umhören..."
    bw "Soziale Interaktion liegt mir wohl besser als dir."
    "Das merkt sie aber früh."
    b "In Ordnung."
    b "Ich werde sehen, was ich tun kann."
    bw "OK."
    bw "Dann sehen wir uns demnächst."
    bw "Ich werde dir eine E-Mail schreiben, wenn ich was herausfinde."
    b "Einverstanden."
    bw "Bis dann."
    b "OK..."
    "Sie bricht zur Straßenbahnhaltestelle auf."
    hide anja neutral
    with dissolve
    b "Am besten gehe ich nach Hause."
   
    stop music fadeout 0.4
   
    #random event
    
    scene black
    with fade
    
    "Später am Abend..."
    
    scene bg keller
    with fade
    
    play music "music/bernd_theme.ogg"
    
    "Ich setze mich vor meinen Rechner."
    b "Informationen sammeln..."
    b "Wo fange ich da an?"
    "Krautchan."
    "Wo sonst?"
    "www.krautchan.net"
    "..."
    "..."
    b "Warum dauert das so lange?"
    "Ah..."
    "Endlich lä-"
    "404"
    "File not found."
    b "Krautchan ist..."
    b "...tatsächlich offline."
    
    scene black
    with fade
    
    stop music fadeout 0.4
    
    #kapitel 2
    
    jump eins_ende
    
label eins_refuse_fBernd:
    $ anjaAccept = 0
    b "Ich kann das irgendwie nicht glauben."
    b "Das ist doch völliger Unsinn."
    bw "Aber %(berndName)s!"
    bw "An wen soll ich mich sonst wenden?"
    bw "Bitte!"
    bw "Hilf mir!"
    menu:
        "..."
        "OK.":
            $ friendLove += 10
            jump eins_accept_fBernd
        "Nein.":
            $ friendLove -= 20
            b "Tut mir Leid, aber ich denke, ich gehe besser."
    "Ohne ein weiteres Wort zu sagen, drehe ich mich um und gehe."
    hide anja neutral
    with dissolve
    
    bw "%(berndName)s!!"
    bw "Du kannst mich doch nicht im Stich lassen!"
    
    "Doch."
    "Das kann ich."
    "Verarschen kann ich mich nämlich selbst."
    
    stop music fadeout 0.4
    
    scene black
    with fade
    
    "Wieder zuhause..."
    
    jump eins_krautchanOff
    
label eins_sisAbholen_promise:
    $ lauraRoute = 1
    ma "Du hast versprochen deine Schwester abzuholen."
    "Mist."
    "Ich will gar nicht..."
    "Da treffe ich mich lieber mit dem Mädchen von gestern..."
    "Wie heisst sie noch..."
    "%(wBerndName)s."
    "Ein schöner Name..."
    ma "Langsam müsstest du losgehen."
    b "Aber ich will nicht..."
    ma "%(berndName)s!"
    ma "Du hast es versprochen, also gehst du auch!"
    "Sie hat recht..."
    "Ich habe es ihr wirklich versprochen."
    "Dreck."
    "Ich habe wohl keine andere Wahl."
    "%(wBerndName)s muss wohl warten..."
    b "In Ordnung..."
    b "Ich gehe."
    "Ich packe meine sieben Sachen und mache mich auf den Weg."
    
label eins_sisAbholen:

    scene bg zuhause_hausflur
    with fade
    
    "Ich sollte mich mal langsam aber sicher auf den Weg machen."
    "Sonst muss ich gleich so hetzen."
    "Aber noch habe ich ja Zeit."
    
    scene bg schulweg1
    with fade
    
    play music "music/schulweg.mp3"
    
    "Noch zwanzig Minuten, bis die Schule vorbei ist und bis ich da bin brauche ich noch knapp eine viertel Stunde."
    "Gut, dass meine Mutter mir rechtzeitig Bescheid gesagt hat, sonst wäre ich nie pünktlich gekommen."
    "...und wer weiss, was %(sisName)s dann mit mir gemacht hätte."
    
    scene bg schulweg2
    with fade
    
    "Puh, das ist weiter als ich dachte."
    "Ich sehe mich um."
    "Irgendwie habe ich das Gefühl, dass ich einen Umweg gegangen bin."
    "Und..."
    "Ich hätte jetzt *wirklich* Lust auf einen Döner."
    "Auf der anderen Straßenseite sehe ich einen Dönerladen."
    "Die scheint es hier an jeder Straßenecke zu geben."
    "Naja, mir soll es Recht sein."
    
    scene bg donerladen
    with fade
    
    play music "music/donerladen.ogg"
    
    show salih neutral
    with dissolve
    
    "Salih" "Hallo."
    b "Hallo."
    b "Einen Döner bitte."
    "Salih" "nomal oda schicken?"
    b "Normal... bitte."
    "Salih" "welches sosse?"
    b "Äh... Knoblauchsoße."
    "Salih" "mit alle?"
    b "Ja."
    "Salih" "Auch sviebel?"
    b "Bitte?"
    "Salih" "sviebel"
    b "Ja..."
    b "Zwiebeln auch."
    "Salih" "drai oiro funfzisch dann bittä"
    "Ich gebe ihm das Geld."
    "Salih" "döner dauerd noch minude ja?"
    b "Ja, ist ok."

    hide salih neutral
    with dissolve

    "Wieso können die nicht mal jemanden einstellen, der ordentlich Deutsch redet?"
    "Hier braucht man ja zum Bestellen länger als die Zubereitung dauert."
    "Macht nichts, ich bin noch gut in der Zeit."
    "Solange ich pünktlich bin, ist alles ok."
    "Ich sehe mich nach dem Dönerverkäufer um, aber der ist nirgendwo zu sehen."
    "Seltsam..."
    "Irgendwie kommt er mir bekannt vor."
    "Wo treibt der sich denn rum?"
    "Der soll mal lieber meinen Döner machen, sonst komme ich zu spät."
    "5 Minuten vergehen, bevor er zurückkommt und endlich anfängt zu arbeiten."
    "Faules Pack."
    "Ich sehe auf die Uhr."
    "Noch bin ich pünktlich, aber wenn der sich noch mehr Zeit lässt, wird %(sisName)s mich umbringen."
    "Ich will gar nicht daran denken..."
    
    stop music fadeout 2.0
    
    scene black
    with fade
    
    "Später..."
    
    scene bg schulweg2
    with fade
    
    play music "music/schulweg.mp3"
    
    b "OH SCHEI-"
    b "In 5 Minuten ist die Schule vorbei."
    b "Der Typ hat 10 Minuten für einen einzigen Döner gebraucht."
    b "Inkompetentes Pack."
    "Jetzt muss ich mich richtig beeilen..."
    "Ich renne in Richtung Schule."
    "Aber moment..."
    "Wo IST die Schule?"
    "Ich bleibe stehen und sehe mich um."
    "Wunderbar."
    "Ich habe mich verlaufen."
    "Frustriert beisse ich in meinen Döner."
    "Wo jetzt hin?"
    "Mal überlegen..."
    "Ich habe keine Ahnung, aus welcher Richtung ich gekommen bin."
    "Wieso hat das echte Leben keine Minimap?"
    "Da fällt mir ein, dass ich einen Stadtplan dabei habe."
    "Den hatte ich ja extra für diesen Fall eingesteckt."
    "Ich krame den Stadtplan raus und klappe ihn auf."
    "Nach einigen Sekunden weiss ich, wo ich lang muss."
    "Ich falte den Plan wieder zusammen und sprinte los."
    "Meinen Döner habe ich zum Glück schon aufgegessen, was das Rennen um einiges erleichtert."
    "Ich biege nach links ab."
    "Da vorne ist ihre Schule."
    "Endspurt ist angesagt."
    "Völlig außer Atem erreiche ich den Schulhof."
    
    scene bg schulhof
    with fade
    
    stop music fadeout 0.4
    
    "Schon zehn Minuten zu spät."
    "Sie wird mich umbringen wollen."
    "Da hinten steht sie."
    
    show laura sad
    with dissolve
    
    sis "Da bist du ja endlich!"
    b "Entschuldigung, %(sisName)s."
    b "Es..."
    "Ich schnappe nach Luft."
    b "...ging nicht früher."
    b "Du musstest doch nicht lange warten, oder?"
    sis "Doch."
    sis "Alle meine Freundinnen sind schon nach Hause gegangen."
    sis "Nur ich stehe hier noch."
    b "T- Tut mir Leid."
    "Gleich passiert es..."
    
    show laura crying
    with dissolve
    
    sis "Wieso bist du immer so gemein zu mir?!"
    sis "Du magst mich nicht, stimmts?"
    sis "Du hasst mich!"
    
    b "Stimmt doch gar nicht!"
    b "Natürlich mag ich dich."
    b "Ich bin doch dein großer Bruder."
    "Hauptsache sie hört auf zu weinen..."
    "Ich hasse es, wenn sie weint."
    
    show laura sad
    with dissolve
    
    sis "..."
    sis "Du magst mich wirklich?"
    
    b "Ja."
    b "Und wenn du jetzt aufhörst zu weinen, kauf ich dir ein Eis."
    "...wenn ich noch genug Geld habe."
    
    show laura happy
    with dissolve
    
    sis "OK!"
    "Das war einfach..."
    b "Na dann."
    b "Gehen wir."
    
    scene bg schulweg1
    with fade
    
    play music "music/schulweg.mp3"
    
    "Irgendwo war hier doch ein Eiswagen..."
    "Ah! Da ist er."
    
    scene bg eiswagen
    with fade
    
    show salih neutral
    with dissolve
    
    "Salih" "Guten Tag."
    "Salih" "Was darfs denn sein?"
    "Den kenn ich doch..."
    
    show salih neutral at right
    with move
    
    show laura neutral at left
    with dissolve
    
    sis "3 Kugeln bitte."
    "Salih" "Im Becher oder im Hörnchen?"
    sis "Hörnchen."
    "Salih" "Und welche Sorten?"
    sis "Banane, Schoko und Stracciatella."
    "Salih" "Hier, bitte sehr."
    "Salih" "Das macht dann 1,80€."
    "Das ist zwar mein letztes Geld, aber was tut man nicht alles für seine kleine Schwester."
    b "Hier."
    "Salih" "Dankeschön."
    "Salih" "Schönen Tag noch."
    
    hide salih neutral
    with dissolve
    
    show laura happy at center
    with move
    
    sis "Danke, %(berndName)s."
    b "Hey, ich habs doch versprochen."
    sis "Das tust du oft."
    sis "Aber wenn du mal ein Versprechen hältst, ist das etwas besonderes."
    b "Hey!"
    b "Was soll das heissen!"
    "... aber sie rennt bereits vorraus."
    b "Warte doch...!"
    
    scene black
    with fade
    
    "Endlich wieder zuhause..."
    
    jump eins_krautchanOff

label eins_krautchanOff:
    scene bg keller
    with fade
    
    stop music fadeout 0.4
    
    b "Jetzt erstmal auf Krautchan."
    "Da war ich lange genug nicht mehr."
    "..."
    "Verbindung wird hergestellt."
    "..."
    b "Warum dauert das so lange?"
    "Ist es etwa wieder GET-Zeit?"
    "Nein, kann nicht sein."
    "Ah..."
    "Endlich lä-"
    "404"
    "File not found."
    b "Krautchan ist..."
    b "...offline."
    
    jump eins_ende

label eins_sisAbholenZuerst:
    $ lauraRoute = 1
    $ stalker = 1
    #AB HIER LAURA ROUTE MIT STALKER
    scene bg zuhause_draussen
    with fade
    
    "Ich sollte mich mal langsam aber sicher auf den Weg machen."
    "Sonst muss ich gleich so hetzen."
    "Aber noch habe ich ja Zeit."
    "..."
    "Irgendwas stimmt hier nicht."
    "Ich werde beobachtet."
    "Quatsch."
    "Wer soll mich schon beobachten?"
    "Das ist sicher nur Einb-"
    "Stalkerbernd."
    "Es muss Stalkerbernd sein."
    "Oh Scheiße..."
        
    menu:
        "Am besten..."
        
        "...drehe ich mich um.":
            "Ich werde mich umdrehen und mich ihm stellen."
            "Mein ganzer Körper ist angespannt."
            "Nur nicht die Nerven verlieren..."
            "Jetzt!"
            "Blitzschnell drehe ich mich um."
            "..."
            "Nichts."
            "Niemand zu sehen."
            "Aber das Gefühl ist immer noch da."
            "Ich werde beobachtet."
            "Nirgendwo ist jemand zu sehen, der Stalkerbernd sein könnte."
            "Auf der anderen Straßenseite geht eine ältere Frau mit ihrem Hund spazieren und schaut mich merkwürdig an."
            "Kann es sein, dass sie...?"
            "Schwachsinn."
            "Wahrscheinlich werde ich einfach nur verrückt..."
            b "Ha."
            b "Hahaha."
            "Ich trete den Weg zur Schule an."
            
            scene bg schulweg1
            with fade
            
            play music "music/schulweg.mp3"
            
            "Nachdem ich einige Zeit gelaufen bin, verschwindet das beklemmende Gefühl."
            "Wahrscheinlich habe ich mir alles nur eingebildet."
            b "Kranker Scheiß."
            "Ich sehe auf die Uhr."
        
        "...lasse ich mir nichts anmerken.":
            "Wenn ich mich jetzt umdrehe, hat er sein Ziel erreicht."
            "Den Gefallen werde ich ihm nicht tun."
            "Ich gehe in richtung Schule."
            "Das unangenehme Gefühl beobachtet zu werden bleibt auch nachdem ich um die Ecke gebogen bin."
            "Meine Schritte beschleunigen sich."
            "Anstatt den direkten Weg zu nehmen, biege ich in eine Seitengasse."
            
            scene bg gasse1
            with fade
            
            "Schneller."
            "Ich muss hier weg."
            "Unbewusst fange ich an zu rennen."
            "Die Gasse biegt nach links ab."
            "Ohne abzubremsen renne ich um die Ecke und..."
            
            scene bg gasse2
            with fade
            
            "...lande in einer Sackgasse."
            "Vor mir eine Hauswand."
            "Hinter mir Stalkerbernd."
            "Das wars."
            "Hier komme ich nie wieder raus."
            "Ich setze mich in die Ecke und mache mich so klein wie möglich."
            "Jetzt ist es aus."
            "Was wird Stalkerbernd mit mir machen, wenn er mich gefunden hat?"
            "Ich will es nicht wissen."
            "Verzweifelt sehe ich mich um."
            "Es muss doch einen Ausweg geben."
            "Da sehe ich es."
            "Im ersten Stock ist ein offenes Fenster."
            "Wenn ich es dahin schaffe, kann ich vielleicht entkommen."
            "Nur wie komme ich da hoch...?"
            "Ich stehe auf und untersuche die Wand."
            "Klettern kann ich hier sicher nicht."
            "Erstens ist die Wand viel zu glatt, und zweitens bin ich unsportlich."
            b "Es muss einen anderen Weg geben."
            "...aber es gibt keinen."
            "Ich suche mit meinen Händen die Wand nach halt ab."
            "An einer Stelle werde ich fündig."
            "Ein Stein ist herausgebrochen und die enstandene Öffnung ist grade groß genug für beide Hände."
            "Ich versuche mich hochzuziehen."
            "Wenn ich nur damals nicht immer Sport geschwänzt hätte..."
            "Mit aller Kraft ziehe ich mich hoch."
            "Über mir sehe ich das offene Fenster."
            "Jetzt nur nicht schlapp machen..."
            "Ich strecke eine Hand nach dem Fenster aus und..."
            "...fast..."
            "Geschafft!"
            "Jetzt hänge ich ca. 4 Meter über dem Boden vor einem Fenster."
            "Meine Finger geben langsam nach."
            "Sicher steht Stalkerbernd unten und schaut mir zu."
            "Er wartet nur drauf, dass ich falle."
            "Nein."
            "Ich kann jetzt nicht verlieren."
            "Mit aller Kraft ziehe ich mich hoch und..."
            scene black
            with fade
            "...lande in einem dunklen Raum."
            "Das Haus ist verlassen?"
            "Mitten in Berlin?"
            "Merkwürdig."
            "Egal."
            "Das erleichtert einiges."
            "Zum Glück bin ich diese Lichtverhältnisse gewohnt, und finde schnell den Ausgang."
            
            scene bg schulweg1
            with fade
            
            "Als ich das Gebäude verlasse, ist von Stalkerbernd nichts zu sehen."
            "Auch das beklemmende Gefühl ist weg."
            "Oh Mann..."
            "Wahrscheinlich habe ich mir alles nur eingebildet."
            "Plötzlich merke ich, wie lächerlich ich mich verhalten habe."
            "*gesichtspalme*"
            "Ich schaue auf die Uhr."
    
    "Noch zwanzig Minuten, bis die Schule vorbei ist und bis ich da bin brauche ich noch knapp eine Viertelstunde."
    
    scene bg schulweg2
    with fade
    
    "Puh, das ist weiter als ich dachte."
    "Und..."
    "Ich hätte jetzt *wirklich* Lust auf einen Döner."
    "Auf der anderen Straßenseite sehe ich einen Dönerladen."
    "Die scheint es hier an jeder Straßenecke zu geben."
    "Naja, mir soll es Recht sein."
    
    scene bg donerladen
    with fade
    
    play music "music/donerladen.ogg"
    
    show salih neutral
    with dissolve
    
    "Salih" "Hallo."
    b "Hallo."
    b "Einen Döner bitte."
    "Salih" "nomal oda schicken?"
    b "Normal... bitte."
    "Salih" "welches sosse?"
    b "Äh... Knoblauchsoße."
    "Salih" "mit alle?"
    b "Ja."
    "Salih" "Auch sviebel?"
    b "Bitte?"
    "Salih" "sviebel"
    b "Ja..."
    b "Zwiebeln auch."
    "Salih" "drai oiro funfzisch dann bittä"
    "Ich gebe ihm das Geld."
    "Salih" "döner dauerd noch minude ja?"
    b "Ja, ist ok."
    
    hide salih neutral
    with dissolve
    
    "Wieso können die nicht mal jemanden einstellen, der ordentlich Deutsch redet?"
    "Hier dauert die Bestellung länger als die eigentliche Zubereitung."
    "Macht nichts, ich bin noch gut in der Zeit."
    "Solange ich pünktlich bin, ist alles ok."
    "Ich sehe mich nach dem Dönerverkäufer um, aber der ist nirgendwo zu sehen."
    "Seltsam..."
    "Irgendwie kommt er mir bekannt vor."
    "Wo treibt der sich denn rum?"
    "Der soll mal lieber meinen Döner machen, sonst komme ich zu spät."
    "5 Minuten vergehen, bevor er zurückkommt und endlich anfängt zu arbeiten."
    "Faules Pack."
    "Ich sehe auf die Uhr."
    "Noch bin ich pünktlich, aber wenn der sich noch mehr Zeit lässt, wird %(sisName)s mich umbringen."
    "Ich will gar nicht daran denken..."
    
    stop music fadeout 2.0
    
    scene black
    with fade
    
    "Später..."
    
    scene bg schulweg2
    with fade
    
    play music "music/schulweg.mp3"
    
    b "OH SCHEI-"
    b "In 5 Minuten ist die Schule vorbei."
    b "Der Typ hat 10 Minuten für einen einzigen Döner gebraucht."
    b "Inkompetentes Pack."
    "Jetzt muss ich mich richtig beeilen..."
    "Ich renne in Richtung Schule."
    "Aber Moment..."
    "Wo IST die Schule?"
    "Ich bleibe stehen und sehe mich um."
    "Wunderbar."
    "Ich habe mich verlaufen."
    "Frustriert beiße ich in meinen Döner."
    "Wohin jetzt?"
    "Mal überlegen..."
    "Ich habe keine Ahnung, aus welcher Richtung ich gekommen bin."
    "Wieso hat das echte Leben keine Minimap?"
    "Da fällt mir ein, dass ich einen Stadtplan dabei habe."
    "Den hatte ich ja extra für diesen Fall eingesteckt."
    "Ich krame den Stadtplan raus und klappe ihn auf."
    "Nach einigen Sekunden weiß ich, wo ich lang muss."
    "Ich falte den Plan wieder zusammen und sprinte los."
    "Meinen Döner habe ich zum Glück schon aufgegessen, was das Rennen um einiges erleichtert."
    "Ich biege nach links ab."
    "Da vorne ist ihre Schule."
    "Endspurt ist angesagt."
    "Völlig außer Atem erreiche ich den Schulhof."
    
    scene bg schulhof
    with fade
    
    stop music fadeout 0.4
    
    "Schon zehn Minuten zu spät."
    "Sie wird mich umbringen wollen."
    "Da hinten steht sie."
    
    show laura sad
    with dissolve
    
    sis "Da bist du ja endlich!"
    b "Entschuldigung, %(sisName)s."
    b "Es..."
    "Ich schnappe nach Luft."
    b "...ging nicht früher."
    b "Du musstest doch nicht lange warten, oder?"
    sis "Doch."
    sis "Alle meine Freundinnen sind schon nach Hause gegangen."
    sis "Nur ich stehe hier noch."
    b "T- Tut mir Leid."
    "Gleich passiert es..."
    
    show laura crying
    with dissolve
    
    sis "Wieso bist du immer so gemein zu mir?!"
    sis "Du magst mich nicht, stimmts?"
    sis "Du hasst mich!"
    
    b "Stimmt doch gar nicht!"
    b "Natürlich mag ich dich."
    b "Ich bin doch dein großer Bruder."
    "Hauptsache sie hört auf zu weinen..."
    "Ich hasse es, wenn sie weint."
    
    show laura sad
    with dissolve
    
    sis "..."
    sis "Du magst mich wirklich?"
    
    b "Ja."
    b "Und wenn du jetzt aufhörst zu weinen, kauf ich dir ein Eis."
    "...wenn ich noch genug Geld habe."
    
    show laura happy
    with dissolve
    
    sis "OK!"
    "Das war einfach..."
    b "Na dann."
    b "Gehen wir."
    
    scene bg schulweg1
    with fade
    
    play music "music/schulweg.mp3"
    
    "Irgendwo war hier doch ein Eiswagen..."
    "Ah! Da ist er."
    
    scene bg eiswagen
    with fade
    
    show salih neutral
    with dissolve
    
    "Salih" "Guten Tag."
    "Salih" "Was darfs denn sein?"
    "Den kenn ich doch..."
    
    show salih neutral at right
    with move
    
    show laura neutral at left
    with dissolve
    
    sis "3 Kugeln bitte."
    "Salih" "Im Becher oder im Hörnchen?"
    sis "Hörnchen."
    "Salih" "Und welche Sorten?"
    sis "Banane, Schoko und Stracciatella."
    "Salih" "Hier, bitte sehr."
    "Salih" "Das macht dann 1,80€."
    "Das ist zwar mein letztes Geld, aber was tut man nicht alles für seine kleine Schwester."
    b "Hier."
    "Salih" "Dankeschön."
    "Salih" "Schönen Tag noch."
    
    hide salih neutral
    with dissolve
    
    show laura happy at center
    with move
    
    sis "Danke, %(berndName)s."
    b "Hey, ich hab's doch versprochen."
    sis "Das tust du oft."
    sis "Aber wenn du mal ein Versprechen hältst, ist das etwas Besonderes."
    b "Hey!"
    b "Was soll das heißen!"
    "... aber sie rennt bereits voraus."
    b "Warte doch...!"
    
    scene black
    with fade
    
    stop music fadeout 0.4
    
    "Endlich wieder zuhause..."
    
    scene bg keller
    with fade
    
    play music "music/bernd_theme.ogg"
    
    "Komisch..."
    "Auf dem Rückweg hatte ich nicht mehr das Gefühl beobachtet zu werden."
    "Wahrscheinlich habe ich mir alles nur eingebildet."
    $ berndNameCaps = berndName.upper()
    ma "%(berndNameCaps)s!"
    "Was denn jetzt?"
    ma "GEH MAL EINKAUFEN, ICH HAB' HUNGER!"
    "Muss sie denn immer so schreien?"
    "Kann sie nicht runterkommen, wenn sie was will?"
    ma "HAST DU GEHÖRT!?"
    b "JAAAAA!"
    "Ich gehe lieber nach oben, bevor ich noch taub werde von ihrem Geschrei."
    
    scene bg kueche
    with fade
    
    b "Was denn?"
    ma "Ich hab' Hunger."
    b "Ja, und?"
    "Ist das denn mein Problem?"
    ma "Du musst einkaufen."
    b "Nein, du!"
    ma "Nein, du!"
    ma "Das ist ja wohl das Mindeste, was ich von dir erwarten kann."
    ma "Du machst ja sonst nichts im Haushalt."
    ma "Immer sitzt du nur vor deinem Computer und schaust diese Animefilme."
    b "Ist ja schon gut, ich gehe."
    "Blöde Kuh."
    "Aufgeregt kommt meine Schwester in die Küche gerannt."
    show laura neutral
    with dissolve
    sis "Darf ich auch mit, Mama?"
    ma "Ja, ja."
    ma "Wenigstens hab' ich dann für ein paar Minuten meine Ruhe."
    sis "Komm, %(berndName)s, wir gehen!"
    "Womit habe ich das verdient?"
    "Da ich im Moment nichts an dieser Situation ändern kann, sollte ich das Beste draus machen."
    
    scene bg zuhause_draussen
    with fade
    
    play music "music/bernd_wohnung.mp3"
    
    if supermarkt == "":
        $ supermarkt = "Aldi"
    
    "Wir gehen in Richtung %(supermarkt)s."
    
    show laura neutral
    with dissolve
    
    sis "Du, %(berndName)s?"
    b "Ja?"
    "Das hört sich nicht gut an..."
    sis "Ich..."
    show laura happy
    with dissolve
    sis "Danke, dass du mich heute von der Schule abgeholt hast!"
    "Wow."
    "Unerwartetes Lob von meiner Schwester?"
    "Was ist hier los?"
    b "Hm... ja."
    
    show laura neutral
    with dissolve
    
    sis "Man merkt es mir vielleicht nicht an, aber ich freue mich immer, wenn du mich abholen kommst."
    "Mehr wie: \"Ich freue mich, wenn du mir ein Eis kaufst.\", hab ich recht?"
    b "Hm... ja."
    sis "Manchmal kannst du echt nett sein, %(berndName)s."
    "Manchmal?"
    b "Hm... ja."
    sis "Du kommst mich doch morgen sicher wieder abholen, oder?"
    b "Hm... ja."
    "Warte... was?"
    
    show laura happy
    with dissolve
    
    sis "OK, dann ist es abgemacht!"
    b "Hey, ich hab morgen aber..."
    
    show laura neutral
    with dissolve
    
    sis "Was?"
    sis "Was hast du morgen?"
    
    b "..."
    b "...nichts."
    b "Ich komme dich abholen."
    
    show laura happy
    with dissolve
    
    sis "Na dann ist ja alles klar!"
    sis "Los, beeilen wir uns!"
    b "..."
    
    scene bg supermarkt
    with fade
    
    play music "music/shop.mp3"
    
    b "Was sollen wir nochmal einkaufen?"
    
    show laura neutral
    with dissolve
    
    sis "Hm..."
    
    show laura happy
    with dissolve
    
    sis "Keine Ahnung!"
    "Großartig..."
    b "Naja..."
    b "Kaufen wir halt Butter und Rügenwalder."
    
    show laura neutral
    with dissolve
    
    sis "Sicher, dass wir nicht mehr brauchen?"
    b "Nein, aber was sollen wir machen?"
    sis "Ich könnte Mama anrufen."
    sis "Ich habe mein Handy dabei."
    b "Du hast ein Handy?"
    show laura happy
    with dissolve
    sis "Klar hab ich eins!"
    b "Na dann, ruf' sie an."
    show laura neutral
    with dissolve
    sis "OK."
    "Sie zieht ein rosafarbenes Handy aus der Tasche."
    "Geschickt klickt sie sich durch das Menü, bis sie die Nummer gefunden hat."
    "Wieso hat die in ihrem Alter schon ein Handy?"
    "Ist das normal heutzutage?"
    sis "Hallo Mama, ich bin's."
    sis "Wir haben vergessen dich zu fragen, was wir einkaufen sollen."
    sis "..."
    sis "OK."
    sis "Sonst noch was?"
    sis "..."
    sis "Alles klar!"
    show laura happy
    with dissolve
    sis "Bis gleich!"
    "Sie legt auf."
    show laura neutral
    with dissolve
    sis "Sie sagt, dass wir auch noch Milch und Brot brauchen."
    "Also Milch, Butter, Brot und Rügenwalder."
    b "OK."
    b "Dann besorgen wir das schnell und danach gehen wir nach Hause."
    sis "OK."
    hide laura neutral
    with dissolve
    "Nachdem wir alles gefunden haben, gehen wir zur Kasse."
    "Vor uns ist eine ältere Frau, die langsam einen Artikel nach dem anderen auf's Band legt."
    "Die Kassiererin ist sichtlich genervt."
    "Warum kaufen alte Leute immer so viel ein und brauchen dann eine halbe Stunde an der Kasse?"
    show laura neutral
    with dissolve
    sis "%(berndName)s?"
    b "Was denn?"
    sis "Bekomm' ich eine Packung Kaugummi?"
    b "Nein, die sind zu teuer."
    sis "Aber ich bezahl' es von meinem Taschengeld!"
    sis "Ich geb' es dir zuhause wieder!"
    sis "Ganz bestimmt!"
    "Hm..."
    b "Na gut, nimm dir eine Packung."
    show laura happy
    with dissolve
    sis "Danke, %(berndName)s."
    
    scene black
    with fade
    
    "Eine halbe Stunde später..."
    b "Endlich wieder zuhause."
    
    stop music fadeout 1.0
    
    scene bg keller
    with fade
    
    play music "music/bernd_theme.ogg"
    
    b "Mal schauen, ob der Faden mit meinen Daten noch auf /b/ ist..."
    "..."
    b "Nichts."
    b "Glück gehabt."
    "Es scheint als wäre wirklich weiter nichts passiert..."
    "Bernd ist wohl wirklich völlig unfähig."
    
    #BUTTERGOTT MEHR DIALOG HIER
    
    play sound "sounds/door_1.wav"
    show laura neutral
    with dissolve
    
    sis "%(berndName)s?"
    "Was denn nun schon wieder?"
    "Kann ich nicht einmal im Keller meine Ruhe haben?"
    b "Was willst du?"
    sis "Ich wollte nur fragen, ob du mir bei den Hausaufgaben helfen kannst..."
    "Als ob ich sonst nichts zu tun hätte."
    "Oh warte..."
    "Ich habe sonst nichts zu tun."
    b "Na gut."
    b "Welches Fach denn?"
    sis "Mathematik."
    b "Na dann zeig mal her..."
    "Sie sieht sich um."
    sis "Hast du hier einen Stuhl?"
    sis "Im Sitzen kann man es besser erklären, oder?"
    b "Ich hol' dir eben einen von oben."
    "Ich will aufstehen, aber sie kommt mir zuvor."
    sis "Nicht nötig, %(berndName)s."
    sis "Ich kann ja hier sitzen."
    "Bevor ich etwas erwidern kann, klettert sie auf meinen Schoß."
    b "..."
    sis "Also."
    sis "Schau hier..."
    "Sie schlägt ihr Matheheft auf."
    sis "Wir sollen das hier ausrechnen."
    "Sie zeigt auf eine Aufgabe."
    b "sin(α) = 1"
    b "Berechne α."
    "Mal nachdenken..."
    
    menu:
        "Das ist..."
        
        "90°":
            b "Ich bin mir ziemlich sicher, dass es 90° sind."
            $ sisFrage = "richtig"
        "0°":
            b "Das müssten 0° sein."
            $ sisFrage = "falsch"
        "Globalisierung":
            b "Das ist ganz sicher Globalisierung."
            sis "Sicher?"
            b "Sicher."
            $ sisFrage = "richtigFalsch"
    
    show laura happy
    with dissolve
    
    sis "OK, danke %(berndName)s!"
    sis "Jetzt krieg ich sicher eine gute Note."
    b "Kein Problem."
    
    show laura neutral
    with dissolve
    
    sis "Achso..."
    b "Ja?"
    "Was denn noch?"
    sis "Hier ist das Geld für die Kaugummis."
    sis "Ich hab dir ja versprochen es zurückzugeben."
    "Wow."
    "Daran habe ich gar nicht mehr gedacht."
    b "Äh... danke."
    sis "Bis morgen, %(berndName)s."
    b "Ja."
    b "Bis morgen."
    
    hide laura happy
    with dissolve
    
    b "Schon wieder so spät... ich lauer noch ein wenig auf /b/ und gehe dann schlafen."
    "Ich öffne den Browser und gehe auf Krautchan."
    "..."
    "Nichts tut sich."
    "Krautchan ist heute mal wieder langsam."
    "..."
    "Endlich geladen."
    "Nachdem ich mich kurz durch alle wichtigen Boards gelesen habe, beschließe ich, dass es Schlafenszeit ist."
    "Morgen steht mir wieder ein normaler, langweiliger Tag bevor..."
    
    scene black
    with fade
    
    # ENDE TAG 1
    "Am nächsten Morgen..."

    ma "%(berndName)s?"
    ma "Willst du nicht langsam mal aufstehen?"
    b "Wie spät ist es denn?"
    ma "Schon 13 Uhr."

    scene bg keller
    with flash

    b "WAS!?"
    b "Ich wollte doch heute wieder %(sisName)s abholen."
    "Mist."
    "Jetzt hab ich es laut gesagt."
    "Ich wollte meine Verspätung gestern doch wieder gut machen."
    ma "Soso, du wolltest %(sisName)s abholen?"
    ma "Als ob!"
    ma "Das würdest du doch nie freiwillig machen."
    ma "Mach' dich nicht lächerlich."
    b "Ich kann nicht anders."
    b "Ich hab' es ihr versprochen."
    ma "Na dann beeil' dich mal lieber."
    ma "Du weißt, dass sie es hasst, wenn man zu spät kommt."
    b "Jaja."
    "Hektisch ziehe ich mich an, packe alles ein und mache mich auf den Weg."

    #insgesamt noch sehr ausbaufähig

    scene bg schulweg1
    with fade

    "Hmm..."
    "Irgendwie habe ich kein gutes Gefühl."
    "Das gleiche Gefühl hatte ich gestern auch schon."
    "Ich kann mich doch nicht zweimal so irren."
    "Irgendjemand verfolgt mich doch."
    "Es ist bestimmt irgendein Bernd, der heimlich Fotos von mir macht und dann auf Krautchan veröffentlicht."
    "Das Treffen war wahrscheinlich nur eine Falle, um mich aus meinem Haus zu locken."
    "Gut, dass ich nicht hingegangen bin."
    "Sowas würde total zu Bernd passen."
    "Anstatt geradeaus weiterzugehen, biege ich nach links ab."
    "Hoffentlich kann ich ihn so abhängen."

    scene bg schulwegPano at right
    with fade

    "Wenn ich mich jetzt umdrehe, hat er eigentlich keine Zeit mehr, um sich zu verstecken."
    "3..."
    "2..."
    "1..."
    "Jetzt!"

    scene bg schulwegPano at left
    with move
    "..."
    "..."
    "Wo ist der Typ?"
    "Ich sehe ihn nicht."
    "Vielleicht bilde ich mir das auch alles nur ein..."
    "In so einer großen Stadt wird man anscheinend schnell verrückt."
    "Ja."
    "So wird es wohl sein."
    "In letzter Zeit ist ja auch einiges geschehen."
    "Ich schaue auf die Uhr."
    "13:45 Uhr."
    "Ich hab noch eine Viertelstunde bis Schulschluss."
    "Gott sei Dank weiß ich den Weg jetzt auswendig."

    scene bg schulhof
    with fade

    "Ein Blick auf meine Uhr verrät mir, dass es kurz vor zwei ist."
    "Diesmal bin ich pünktlich."
    "Die Schule ist noch nicht aus."
    "Aber ich werde das Gefühl einfach nicht los."
    "Wenn mich doch jemand verfolgt...?"

    play sound "sounds/schulglocke.wav"
    #Sound

    "Das war die Schulglocke."
    "Wenn ich %(sisName)s da nicht mit reinziehen will, muss ich hier weg."
    "Ganz egal, wie nervig sie ist, sie ist immer noch meine kleine Schwester!"
    "Am besten stelle ich mich direkt an den Eingang, damit ich so schnell wie möglich verschwinden kann."
    "Stimme" "%(berndName)s!"
    $ berndNameUpper = berndName.upper()
    "Stimme" "%(berndNameUpper)s!"
    "Das ist %(sisName)s."
    "Dahinten kommt sie."

    show laura happy
    with dissolve

    sis "Hi."
    b "Hi."
    b "Wir müssen hier schleunigst weg."
    "Ich packe sie am Handgelenk."

    show laura surprised
    with dissolve
    
    sis "Hey, das tut weh!"
    sis "Was soll das!?"
    "Ich ignoriere sie und zerre sie von der Schule weg."

    scene bg schulweg2
    with fade
    
    show laura mad
    with dissolve

    sis "Hey, warum ziehst du mich so?"
    b "Ich erklär' dir gleich alles."
    sis "Aber du tust mir weh."
    b "Ahh, da vorne."
    "Ich ziehe sie in eine Seitengasse."

    show bg gasse1
    with fade
    
    show laura mad
    with dissolve

    sis "Was soll das alles?"
    b "Hör mir gut zu."
    sis "Ja...?"
    b "Wir werden verfolgt."

    show laura surprised
    with dissolve

    sis "Was?"
    b "Eigentlich werde nur ich verfolgt."
    b "Aber du bist nunmal hier, also bist du auch in Gefahr."
    b "Wer weiß, was mit dir passiert."
    sis "Weswegen wirst du verfolgt?"
    sis "Und von wem?"
    "Wie soll ich das erklären?"
    b "Ich..."
    b "Pass auf."
    b "Ich erklär' das später."
    sis "Was?"
    sis "Wieso denn?"
    b "Das ist schwer zu erklären..."
    b "Wir müssen hier zuerst weg."
    b "Bitte %(sisName)s, höre nur einmal auf deinen großen Bruder."
    
    show laura pissed
    with dissolve
    
    sis "So ein Schwachsinn!"
    sis "Du willst mich ja nur ärgern!"
    sis "Bleib' du meinetwegen hier in der Gasse sitzen."
    sis "Ich gehe nach Hause, so!"
    "Wütend dreht sie sich um und will gehen, aber ich halte sie fest und ziehe sie zurück in die Gasse."
    b "Du musst mir glauben."
    b "Wenn da draußen wirklich einer ist..."
    sis "Lass mich los, %(berndName)s."
    b "...und er Fotos von dir macht..."
    
    show laura mad
   
    sis "Lass mich los."
    b "...und sie ins Internet stellt..."

    show laura mad_talk
    with dissolve
    
    sis "Du sollst mich loslassen!"
    "Sie versucht ihren Arm zu befreien, aber ich lasse nicht los."
    "Mit meiner freien Hand greife ich nach ihrem anderen Arm, aber sie weicht aus."
    b "Jetzt hör' mir doch mal zu!"
    sis "Nein!"
    sis "Du sollst mich loslassen!"
    "Ich ziehe sie näher an mich ran und greife ihren freien Arm."
    sis "Aua!"
    sis "Du tust mir weh!"
    
    show laura mad
    with dissolve
    
    sis "Lass mich los, ich will nach Hause!"
    b "Nur, wenn du mir glaubst."
    sis "In Ordnung, in Ordnung."
    sis "Ich glaube dir."
    sis "Kannst du mich jetzt endlich loslassen?"
    "Ich lockere meinen Griff und sie geht einen Schritt zurück."
    
    show laura pissed
    with dissolve
    
    sis "Was ist denn los mit dir, %(berndName)s?"
    sis "Du bist doch sonst nicht so?"
    sis "Seit wir in Berlin wohnen, bist du immer so komisch."
    b "Ich..."
    
    show laura neutral
    with dissolve
    
    sis "Können wir jetzt einfach nach Hause gehen?"
    sis "Ich habe Hunger."
    b "Na gut."
    b "Aber wenn du jemanden siehst, der verdächtig aussieht, sag' mir Bescheid."
    
    show laura pissed
    with dissolve
    
    sis "Ist ja gut, ist ja gut."
    "Bevor wir auf die offene Straße hinausgehen, spähe ich vorsichtig nach links und rechts."
    
    show laura neutral
    with dissolve
    
    sis "...und?"
    b "Nichts."
    b "Lass uns gehen."
    
    show laura embarrassed
    with dissolve
    
    sis "Ach %(berndName)s..."
    b "Hm? Was ist denn?"
    
    show laura neutral
    with dissolve
    
    sis "Danke, dass du mich heute von der Schule abgeholt hast."
    b "Äh..."
    b "OK?"
    sis "Nein, wirklich."
    sis "Ich hab mich total gefreut."
    b "Ich hab's dir doch versprochen."
    b "Was man verspricht, muss man halten, oder nicht?"
    
    show laura happy
    with dissolve
    
    sis "Komisch, dass gerade du das sagst."
    
    show laura neutral
    with dissolve
    
    sis "Komm, beeilen wir uns."
    "Wir treten aus der Gasse auf die offene Straße."
    
    scene bg schulweg1
    with fade
    
    "Nachdem wir eine Weile still nebeneinander gelaufen sind, spüre ich, wie %(sisName)s mich antippt."
    
    show laura neutral
    with dissolve
    
    sis "Du, %(berndName)s?"
    b "Was ist denn?"
    b "Hast du etwas Verdächtiges bemerkt?"
    "Ich sehe mich um, aber es ist niemand da."
    
    show laura embarrassed
    with dissolve
    
    sis "Ich..."
    sis "Kannst du mich vielleicht an die Hand nehmen?"
    
    "Was zum...?"
    "Ich?"
    "Mitten in der Stadt?"
    "Hand in Hand mit einem kleinen Mädchen?"
    "Wie sieht das denn aus?"
    b "Bist du dafür nicht schon etwas zu alt?"
    sis "Aber..."
    sis "Du hast mir Angst gemacht mit deinen Verfolgungsgeschichten."
    sis "Ich glaube, dass du Recht haben könntest."
    sis "Wenn du meine Hand halten würdest..."
    sis "Ich würde mich sicherer fühlen, weißt du?"
    "*seufz*"
    b "Na gut."
    "Ich greife nach ihrer Hand."
    
    show laura happy
    with dissolve
    
    sis "Danke, %(berndName)s."
    sis "Ich hab dich lieb."    
    "Gemeinsam treten wir den Weg nach Hause an."

    scene black
    with fade
    
    "Zuhause..."
    
    scene bg keller_aus
    with fade

    "Endlich bin ich wieder in meinem Zimmer."
    "Hier kann mich niemand mehr beobachten."
    "Nur im Keller bin ich vor anderen Bernds sicher."
    "Erstmal den Computer starten."

    scene bg keller
    with dissolve

    "Erstmal ein bisschen im Internet brausen."
    "Ich öffne meinen Browser."
    "Automatisch drücke ich die Tastenkombination Strg + L."
    "Aus Reflex tippe ich \"kr\" ein, geh einmal runter, betätige die Enter-Taste und lande auf /b/."

    scene bg keller_kc
    with dissolve

    "Ein Japperfaden."
    "Nicht schon wieder."
    "Thread ausblenden."
    "Gurofaden."
    "NEIN!"
    "Thread ausblenden."
    "Fleshlightfaden."
    "Thread ausblenden."
    "/b/ ist schon seit ein paar Wochen der Krebs."
    "Zum Glück haben die Admins diese Funktion eingeführt."
    "Dafür hat dergeneral echt mal ein Lob verdient."
    "Ich gehe auf /kc/ und mache einen neuen Thread auf."
    "\"Heil dir, General.\""
    "\"Bernd dankt für die Thread-ausblenden-Funktion.\""
    "So, das wäre erledigt."
    "Ohhhhhhhhhhhhhh."
    "Nach /w/ - Wissenschaft und Ecchi soll es jetzt auch /t/ - Technik und Tentakel geben?"

    menu:
        " "

        "Ja!":
            "Fick ja, Tentakel."
            "Ich kontributierte."

        "Nein.":
            "NEIN!"
            "SAGE."


#menu ist entscheidend dafür, ob am Ende,
#wenn KC wieder on ist, es /t/ - Technik oder /t/ - Technik und Tentakel gibt

    "Dann wollen wir doch mal schauen, was Bernd von der neuen Episode von Strike with Cheese hält."
    "...das Übliche halt."
    "Hmm..."
    "Was mache ich jetzt?"
    
    scene bg desktop_none
    with fade
    
    "Woah..."
    "Ich erblicke das Icon von \"Wolfgang no haraise\" auf meinem Desktop."
    "Das habe ich lang nicht mehr gespielt."
    "Es wird mal wieder Zeit."
    "Ich starte das Spiel."
    "Ein Klick auf \"Spielstand laden\"."
    "Was war noch gleich der richtige Spielstand..."
    "Ach, was soll's."
    "Neues Spiel."

    scene bg keller_aus
    with fade

    "Was denn jetzt?"
    "Achso, der Ladebildschirm."
    "Schwarzes Bild und Ladebalken."
    "Wie einfallsreich."
    "Diese Ladezeiten sind wirklich unerträglich."
    "Ich muss mir einen neuen Computer anschaffen."
    "Mit diesem alten Ding kann man ja nichts mehr anfangen."
    "Der Bildschirm ist auch schon wieder dreckig."
    "Ich wische den Bildschirm mit meinem Ärmel ab, aber der Dreck geht nicht weg."
    "Egal wie sehr ich es versuche, eine Stelle verändert sich nicht."
    "..."
    "Oh."
    "Das ist kein Dreck."
    "Das ist das Fenstergitter, was sich im Monitor spiegelt."
    "Obwohl man das eigentlich nicht Fenster nennen kann."
    "Moment mal..."
    "...!"
    "In der Spiegelung kann ich es deutlich erkennen."
    "Da ist jemand vor'm Fenster."
    "Ich wusste es doch!"
    "Jemand beobachtet mich."
    "Ich hab mir das nicht eingebildet."
    "Es ist ganz sicher jemand dort."
    "Das muss Stalkerbernd sein."
    "Niemand anders hätte Grund mich zu verfolgen."
    "Ich kenne hier ja niemanden."
    "Was mach ich jetzt...?"
    "Die Gestalt am Fenster bewegt sich nicht von der Stelle."
    "In der Spiegelung kann ich kein Gesicht erkennen."
    "..."
    "Wenn ich mich umdrehe, ist er schneller weg als ich gucken kann."
    "Am besten überrasche ich ihn."
    "Ich muss irgendwie aus dem Zimmer kommen, ohne dass er Verdacht schöpft."
    "Hm..."
    "Aha!"
    b "Ich hol' mir mal lieber was zu trinken."
    "Ich sage es extra laut, damit er es ganz sicher hört."
    "Das Gesicht am Fenster macht keine Anstalten sich zu bewegen."
    "Langsam stehe ich auf und gehe die Treppe nach oben und nach draußen."
    
    scene bg kellertreppe
    with fade
    
    scene bg wohnung_innen
    with fade
    
    scene bg zuhause_hausflur
    with fade
    
    scene bg zuhause_draussen_dunkel
    with fade
    
    "In der Dunkelheit kann ich kaum was erkennen..."
    "Da sitzt jemand..."
    "Direkt vor meinem Fenster."
    
    show yasmin stalker
    with dissolve
    
    "Jetzt nur kein Geräusch machen..."
    "Langsam schleiche ich mich in seine Richtung."
    "..."
    "Er dreht sich um."
    "Verdammt."
    "Jetzt oder nie."
    "Blitzschnell richte ich mich auf und setze zum Sprint an."
    "Er dreht sich um und will weglaufen, aber so leicht entkommt er mir nicht!"
    "Ich bin noch nie so schnell gerannt, wie in diesem Moment, aber trotzdem ist er schneller als ich."
    "Warum mache ich auch nie Sport?"
    "Er läuft ohne abzubremsen um die Ecke."
    
    hide yasmin stalker
    with dissolve
    
    "Ich bin schon total fertig vom Rennen, aber ich muss durchhalten."
    "Mit letzter Kraft schaffe ich die Kurve."
    "Ich sehe ihn rennen, aber er ist schon mindestens 200 Meter weit weg."
    "Den hole ich nie ein."
    "Frustriert bleibe ich stehen und sehe zu, wie er um die Ecke biegt und verschwindet."
    "Den sehe ich hoffentlich nicht mehr so schnell wieder."
    "Immer noch außer Atem begebe ich mich auf den Rückweg in meinen Keller."
    
    scene black
    with fade
    
    scene bg keller_aus
    with fade

    "Wenigstens habe ich jetzt erstmal meine Ruhe."
    "Ein Blick zum Fenster bestätigt das."
    "Niemand da."
    "Ich blicke auf den Bildschirm."
    "Immer noch nicht geladen."
    "Da vergeht einem echt die Lust."
    "Wütend drücke ich Strg + Alt + Entf."

    scene bg keller
    with dissolve

    "Prozess beenden."
    "Ich schau mal, was auf Krautchan los ist."
    "Da war ich lange genug nicht mehr."
    "..."
    "Verbindung wird hergestellt."
    "..."
    b "Warum dauert das so lange?"
    "Ist es etwa wieder GET-Zeit?"
    "Nein, kann nicht sein."
    "Ah..."
    "Endlich lä-"
    "404"
    "File not found."
    b "Krautchan ist..."
    b "...offline."
    
    stop music fadeout 0.4
    
    jump eins_ende
    
label eins_ende:

    scene black
    with fade
    jump zwei