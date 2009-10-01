label zwei_yasmin_Anfang:
    #kurz nachdem KC offline ist
    scene bg keller_aus
    with fade
    
    play music m_bernd
    
    "Ich liege auf meinem Bett und starre die Decke an."
    "Krautchan ist offline."
    "Was mach ich denn nun?"
    "Vielleicht sollte ich mich mal auf 4chan..."
    "Nein!"
    "So weit wird es nie kommen!"
    "Ich frage mich nur..."
    "Warum?"
    "Warum ist Krautchan von einem auf den anderen Tag verschwunden?"
    "Vielleicht trollt dergeneral auch einfach wieder alle?"
    "Eventuell sollte ich einfach mal bis morgen warten, und gucken ob es dann wieder online ist."
    "Es ist schon 2 Uhr nachts."
    "Ich geh besser mal schlafen."
    "..."
    "Es ist völlig ruhig."
    "Zum ersten mal, dass ich in dieser Stadt bin, höre ich kein Geräusch."
    "Normalerweise fährt immer irgendwo ein Auto, oder jemand geht am Fenster vorbei."
    "Manchmal läuft noch irgendwo ein Fernseher oder jemand hört mitten in der Nacht noch Musik."
    "Aber heute nicht."
    "Merkwürdig."
    "Vielleicht bilde ich mir das auch nur ein."
    
    stop music
    
    play sound "sounds/schraube.wav"
    
    "!!!"
    "Was war das?"
    "Ich habe ein Geräusch gehört."
    "Es war nur sehr leise, aber man konnte es deutlich hören."
    
    play sound "sounds/schraube.wav"
    
    "Da war es wieder."
    "Woher kommt das?"
    "Soll ich aufstehen und nachsehen?"
    "Ach, Quatsch."
    "Sicher ist es nur ein Zweig oder so, der gegen ein Fenster klopft."
    "Ein Zweig?"
    "Unsinn."
    "Der nächste Baum ist gute 10 Meter vom Haus entfernt."
    
    play sound "sounds/schraube.wav"
    
    "Was zum...?"
    "Es kommt von meinem Fenster."
    "Irgendetwas ist dort."
    "Ich will nicht nachsehen..."
    "...wenn es wieder Stalkerbernd ist?"
    "Was würde ich dann tun?"
    "Ich sollte versuchen, es zu ignorieren."
    
    play sound "sounds/schraube.wav"
    
    "Da war es wieder..."
    "Was macht er da?"
    "Ich ziehe mir mein Kissen über den Kopf und das Geräusch verstummt."
    "Es wird schon nichts Schlimmes passieren..."
    "Hier unten ist es so dunkel, dass er sowieso nicht reingucken kann."
    "Mit diesem Gedanken schlafe ich ein."

    jump zwei_yasmin_lauraTraum

label zwei_yasmin_lauraTraum:    
    scene black
    with fade

    "Stimme" "%(berndName)s."
    "Stimme" "Wach auf!"
    "Ich öffne die Augen, in der Erwartung %(sisName)s oder meine Mutter zu sehen, aber..."
    
    scene bg knastkeller
    with fade
    
    "Ich bin nicht in meinem Zimmer."
    "Der Raum in dem ich mich befinde sieht eher aus wie eine Art Zelle."
    "Nicht, dass ich das nicht aus meinem Keller schon kennen würde, aber irgendwas ist trotzdem anders."
    "Der Raum hat keine Tür."
    "Jedenfalls kann ich keine sehen."
    "Beleuchtet wird er nur durch das blasse Mondlicht, was durch ein Gitterfenster hinter mir dringt."
    "Ich versuche mich umzudrehen, aber es geht nicht."
    "Als ich an mir heruntersehe, stelle ich fest, dass ich an einen Stuhl gefesselt bin."
    "Super."
    "Stimme" "Scheint, als wärest du endlich wach."
    "Erschrocken blicke ich auf."
    
    show laura neutral
    with dissolve
    
    sis "Hallo %(berndName)s."
    b "%(sisName)s?"
    "Was macht sie denn hier?"
    b "Was soll das?"
    b "Wo sind wir hier?"
    b "Was ist das für ein Keller, und warum sind wir hier?"
    sis "Im Keller..."
    sis "...sind oft Leute eingesperrt, %(berndName)s."
    "Was zum...?"
    b "Was soll das bedeuten?"
    b "Mach mich los!"
    sis "Tut mir Leid, %(berndName)s."
    sis "Das kann ich nicht."
    b "Was soll denn das?"
    "So sehr ich auch an zerre und ziehe, ich kann mich nicht befreien."
    sis "Das bringt nichts."
    sis "Du wirst hier nicht rauskommen, wenn du nicht das tust, was ich von dir verlange."
    "Ich spüre wie mein Puls steigt."
    b "Mach mich los!"
    sis "Wie gesagt."
    sis "Du musst das tun, was ich sage."
    b "Und das wäre?"
    sis "Ich will, dass du mir zuhörst."
    sis "Ich möchte dir nur eine kleine Geschichte erzählen."
    sis "Wirst du mir zuhören?"
    
    menu:
        ""
        
        "In Ordnung. Ich höre zu.":
            b "Von mir aus."
            b "Ich höre dir zu. {w}Wenn du mir versprichst, dass du mich danach los machst."
            sis "Also gut."
            sis "Es war einmal ein Junge, der fuhr mit seiner Familie in den Urlaub."
            sis "Als sie ankamen, wollte er sofort an den großen Strand zu den anderen Kindern."
            sis "Er wollte mit ihnen spielen."
            sis "Der Vater jedoch verbat dem Sohne an den großen Strand zu gehen."
            sis "Das Kind durfte nur an den kleinen Strand abseits des großen Strandes."
            sis "Nach anfänglichem Schmollen hatte der Junge aber doch eine Menge Spaß mit den wenigen anderen Kindern am kleinen Strand."
            sis "Auch die Eltern hatten Spaß."
            sis "Es war eine schöne Zeit für die Familie."
            sis "Doch dies sollte sich bald ändern."
            sis "\"Aus rasestischen Grunden geschlossen - Die Stadtverwaltung\" stand auf dem Schild, das er eines Tages erblickte."
            sis "Der Strand wurde geschlossen."
            sis "Der Vater erlaubte ihm daraufhin mit den anderen Kindern am großen Strand zu spielen."
            sis "Nach einer Weile merkte der Junge aber, dass er nicht mehr so viel Spaß am grosen Strand hatte wie noch vor Kurzem am kleinen Strand."
            sis "Die Eltern hatten jedoch weiterhin jede Menge Spaß."
            sis "Ein paar Tage später wurde ein riesiger Krebs an den Strand gespült."
            sis "Der Junge wollte mit dem Krebs spielen."
            sis "Plötzlich schnappte der Krebs nach dem Kind und es fing an zu bluten."
            sis "Der Junge fiel in Ohnmacht."
            sis "Der Krebs hörte jedoch nicht mehr auf."
            sis "Und so kam es, dass der Junge starb."
            sis "Der Krebs war Schuld am Tod des Jungen."
            b "Und was willst du mir damit jetzt sagen?"
            sis "Du wirst es verstehen, wenn die Zeit reif ist."
            b "Aha..."
            "Ich verstehe nichts."
            sis "%(berndName)s..."
            show laura happy
            with dissolve
            sis "Danke, dass du mir zugehört hast."
            show laura embarrassed
            with dissolve
            sis "Dafür, dass du so lange ausgehalten hast, bekommst du eine Belohnung."
            "Was hat sie nun vor?"
            "Sie kommt näher..."
            b "Laura... {w}was wird das?"
            "Sie krabbelt auf meinen Schoß."
            "Ihr Gesicht kommt immer näher."
            b "Laura..."
            sis "Beruhig dich, %(berndName)s."
            sis "Mach die Augen zu..."
            "Ich schließe die Augen und..."
            scene black
            with dissolve
            "...sie küsst mich."
            
            $renpy.pause(2.0)
       
        "Nein! Mach mich los!":
            b "Nein!"
            b "Und jetzt mach mich los, verdammt nochmal."
            "Langsam kommt sie auf mich zu."
            sis "Du bist nicht in der Lage, mir irgendwelche Befehle zu geben."
            sis "Ich frage dich noch einmal."
            sis "Wirst du mir zuhören?"
            b "Nein!"
            sis "Schade."
            "Sie kommt noch näher."
            
            #ab hier nicht in demo
            
            #show laura knife
            #with dissolve
            #Bild existiert noch nicht
            
            #"EIN MESSER?"
            #sis "Dann habe ich wohl keine andere Wahl."
            #"Sie holt weit aus..."
            #-----------------------------------------------
            #if persistent.wieherbuhSprache is 0:
            #    "Leb wohl, schnöde Welt."
            #if persistent.wieherbuhSprache is 1:
            #    "Sayonara, asamashii Sekai."
            #if persistent.wieherbuhSprache is 2:
            #    "{=jp}さよなら、 浅ましい 世界。{/=jp}"
            #-----------------------------------------------
            #"Ich schließe meine Augen und lass es auf mich zukommen."
            
            #scene black
            #with dissolve
            
            #play sound "sounds/iit.wav"
            #Sound existiert noch nicht 
            #nicht mit dem Sound von unten verwechseln
            #Bernd wird hier von Laura befreit           

            #"Es tut gar nicht weh."
            #"Und es ist dunkel."
            #"Bin ich etwa schon in der Hölle?"
            
            #sis "Du kannst aufstehen."
            #"%(sisName)s?"
            #sis "Mach die Augen auf."
            #"Langsam öffne ich meine Augen."
            
            #sis "Leb wohl."
                        
            #play music m_kanashimi
            
            #play sound "sounds/iit.wav"
            #Sound existiert noch nicht
            #nicht mit dem Sound von oben verwechseln
            #Sound, wie Laura das Messer in Bernd hineinrammt
            #wer die letzte Folge von School Days gesehen hat, weiß, welchen Sound ich meine
            
            #sis "Du Mistkerl."
            #sis "Du denkst doch nur daran, {w}dich selbst glücklich zu machen!"
            #$ sisNameKurz = stringShorten(sisName,3)
            #b "%(sisNameKurz)s..."
            #$ sisNameEnde = stringEnde(sisName,2)
            #b "...%(sisNameEnde)s..."
            
            #BIS HIER
            #demoversion
            
            $ renpy.music.set_volume(0.5, .5, channel="music")
            play music m_kanashimi
            #eventuell die ganze szene lang?
            
            #eventuell wird Bernd belohnt, wenn er sich die geschichte anhört
            # KISU? :3            
            
            "Was hat sie vor?"
            "In diesem Moment..."
            
            play sound "sounds/messer.wav"
            
            scene black
            show splash slash_horizontal
            with flash
            
            scene black
            with fade
            "Eine einzige Bewegung... {w}viel zu schnell... {w}ich kann ihr nicht folgen."

            play sound "sounds/messer.wav"
            
            show splash slash_vertikal
            with flash
            
            scene black
            with fade
            
            "Ein stechender Schmerz in der Brust."
            
            show splash blood_blur
            with None
            
            scene black
            show splash blood
            with dissolve
            
            "Blut?"
            "...mein Blut?"
            "Mir ist plötzlich so kalt..."
            "...ich beginne zu verstehen."
            
            show splash blood_blur
            with dissolve
            
            show splash blood
            with dissolve
            
            "Meine Kraft schwindet langsam."
            "Viel Zeit bleibt nicht mehr."
            
            scene black
            with dissolve
            
            "Ich schließe die Augen und falle."

            stop music fadeout 2.0
            
            $renpy.pause(2.0)
            
            $renpy.music.set_volume(1.0,.5,channel="music")
            
            #ende demoversion
    
    scene bg keller_aus
    with flash
    
    play music m_bernd
    
    b "Was zum?!"
    "Durch das wenige Sonnenlicht, das durch mein Fenster fällt, geweckt, setze ich mich aufrecht auf's Bett."
    "Alles nur ein Traum...?"
    "Wie spät ist es?"
    "Wieso hat mich denn niemand geweckt?"
    "Sicher ist es schon Mittag."
    "Ich setze mich auf die Bettkante und schalte den PC ein."
    
    play sound "sounds/boot.wav"
    
    scene bg keller
    with dissolve
    
    "Der Boden unter meinen Füßen ist kalt."
    "Komisch."
    "Ich kann mich gar nicht daran erinnern, meine Socken ausgezogen zu haben."
    "Ich schlafe oft, ohne mich umzuziehen."
    "Wozu auch?"
    "Am nächsten Morgen ziehe ich mich doch eh wieder an."
    "Meine Socken sind verschwunden."
    "Dafür liegt auf dem Boden etwas anderes."
    "Etwas Kleines aus Metall."
    "Aber was...?"
    "Sieht aus wie..."
    "Eine Schraube?"
    "Aber wie kommt die hierher?"
    "Und von wo?"
    "Ich bücke mich runter und nehme sie hoch."
    "Vielleicht irgendwo aus dem PC Gehäuse gefallen?"
    "Wieso sollte sie?"
    "So was löst sich ja nicht einfach so."
    "Außerdem ist sie viel zu kurz."
    "Merkwürdig."
    "Ich habe überhaupt nichts, wo solche Schrauben drin sind."
    "Zumindest kann ich mich an nichts erinnern."
    "Es steht auch nichts drauf."
    "Sehr merkwürdig."
    
    play sound "sounds/error.wav"
    #Sound -> anderer Mailsound
    
    "Oh."
    "Eine Fehlermeldung?"
    "Ach so, nur eine E-Mail."
    "Spam."
    "Löschen."
    "Mal sehen, ob Krautchan schon wieder da ist."
    "..."
    "Nichts."
    "Immer noch offline."
    "Ich mache das Fenster zu und starre auf meinen Desktop."
    "Die Systemuhr verrät mir, dass es erst 10 Uhr morgens ist."
    "..."
    "Irgendwie ist mir langweilig."
    "Ohne Krautchan fehlt einfach irgendwas."
    "Vielleicht sollte ich mich einfach irgendwie ablenken."
    "Zur Bestätigung knurrt mein Magen."
    "Ich entscheide mich, nach oben zu gehen und etwas zu essen aufzutreiben."
    
    scene bg kellertreppe
    with fade
    
    scene bg wohnung_innen
    with fade
    
    "Komisch."
    "Es ist niemand hier."
    "%(sisName)s ist wohl noch in der Schule..."
    "Meine Mutter ist wohl einkaufen oder so."
    
    scene bg kueche
    with fade
    
    "In der Küche finde ich frische Brötchen und Rügenwalder."
    "Was will man mehr?"
    "Schnell gehe ich wieder nach unten."
    
    scene bg keller
    with fade
    
    "Neue E-Mails habe ich keine."
    "Und Krautchan ist auch offline."
    "Was nun?"
    
    menu:

        "Ich gehe auf 4chan.":
            "Ich öffne den Browser und tippe www.4chan.org in die Adresszeile."
            "Mal sehen, wie sich das im Laufe der Zeit verändert hat."
            "Vielleicht finde ich dort auch Hinweise."
            "Ich klicke auf /b/ - Random und fange an zu lauern..."
            scene black
            with fade
            stop music
            "Eine Woche später..."
            scene bg gameover_vierkanal
            with fade
            $ renpy.pause()
            jump ende

        "Ich gehe auf irgendeine Website.":
            "Auf welche Website geht man denn, wenn man Informationen sucht?"
            "Erschrocken stelle ich fest, dass ich das eigentlich noch nie gemacht habe."
            "Obwohl ich mal irgendwann gelernt habe, dass das Internet als weltweites Informationsnetzwerk gedacht ist..."
            "...habe ich es eigentlich immer nur zum Download von Pornos und illegalen Spielen und Filmen benutzt."
            "Naja... was soll's."
            "Google hat mich noch nie im Stich gelassen."
            "Nur was gebe ich ein?"
            "..."
            "\"Krautchan offline\""
            "..."
            "Das war nichts."
            
            jump zwei_yasmin_einbruch
            
        "Ich warte einfach ab.":
            "Frustriert werfe ich mich auf die Matratze und starre die Decke an."
            "Was mache ich denn jetzt den ganzen Tag lang?"
            "Wo soll ich nun lauern?"
            "4chan kommt nicht in Frage."
            "Eher gehe ich grillen."
            "...keine schlechte Idee."
            "Ach, Schwachsinn!"
            
            jump zwei_yasmin_einbruch
            
label zwei_yasmin_einbruch:
    "Es ist hoffnungslos."
    "Ich muss mir wohl ein Leben ohne Krautchan aufbauen..."
    "Vielleicht wird ja doch noch was aus mir."
    "Gibt es denn wirklich nichts, was ich tun kann?"
    "Vielleicht sollte ich raus und ein bisschen frische Luft schnappen..."
    "Eine Runde um den Block zu gehen wird mir gut tun."
    
    scene bg zuhause_draussen
    with fade
    
    play music m_wohnung
    
    "Ich verlasse das Haus und gehe um die Ecke."
    "Hier habe ich Stalkerbernd getroffen."
    "Mein Blick wandert nach unten zu meinem Kellerfenster."
    "Man kann nichts sehen."
    "Das Gitter ist zu dicht."
    "Ich bücke mich runter und sehe durch das Gitter, aber auch so sieht man nicht viel."
    "Zufrieden stehe ich auf und gehe weiter."
    "Stalkerbernd kann mich drinnen nicht gesehen haben."
    "Er hatte ja kein Nachtsichtgerät oder so was."
    "Ich biege um die Ecke."
    "Um irgendetwas persönliches von mir zu bekommen, müsste er schon einbrechen."
    
    stop music
    
    "Moment mal...!"
    "Ich renne zurück zum Fenster und bücke mich runter."
    
    play music m_psycho
    
    "Zu meinem Entsetzen bestätigt sich meine Vermutung."
    "Die Schraube, die ich unten gefunden hatte, stammt von meinem Fenster."
    "Eine fehlt."
    "Das Geräusch, was ich gestern gehört habe."
    "Die Schraube auf meinem Fußboden."
    "Jemand ist bei mir eingebrochen."
    "Jemand ist eingebrochen und ich habe es nicht gemerkt."
    "Irgendwer war heute Nacht bei mir im Zimmer."
    "Stalkerbernd war heute Nacht bei mir im Zimmer."
    "Ich bekomme es mit der Angst zu tun."
    "So unauffällig wie möglich stehe ich auf und sehe mich um."
    "Unsinn."
    "Das bringt jetzt auch nichts mehr."
    "Hm..."
    "Anscheinend ist niemand hier."
    "Die Straßen sind leer."
    "Es ist ruhig hier."
    "Viel zu ruhig."
    "Wo sind alle hin?"
    "Was ist mit %(sisName)s und %(maName)s?"
    "Ich habe sie heute noch nicht gesehen."
    "Was ist wenn Stalkerbernd ihnen was angetan hat?"
    "Womöglich haben sie ihn heute Nacht erwischt und er hat sie niedergeschlagen oder sonstwas mit ihnen angestellt?!"
    
    scene bg zuhause_hausflur
    with fade
    
    scene bg wohnung_innen
    with fade
    
    scene bg lauraszimmer 
    with fade
    
    "So schnell ich kann renne ich in die Wohnung und reiße die Tür zu %(sisName)ss Zimmer auf."
    "Leer."
    "Niemand hier."
   
    scene bg wohnung_innen
    with fade
   
    "Systematisch durchkämme ich jeden Winkel der Wohnung, aber es ist niemand hier."
    "Sie sind wie vom Erdboden verschluckt."
    "Was geht hier vor?"
    "Wieso ist niemand da?"
    "Wo sind die denn?"
    "Ich rufe %(sisName)s einfach an."
    "Sie hat ja ein Handy."
    "Aber wie ist ihre Nummer?"
    "Neben dem Telefon liegt ein Notizblock mit wichtigen Nummern."
    "Ich suche ihre Nummer raus und wähle..."
    "..."
    "Es klingelt."
    "Sie hat ihr Handy also an."
    "..."
    
    stop music
    
    sis "Ja?"
    b "Hi, %(sisName)s. Ich bin es."
    sis "%(berndName)s?"
    b "Ja."
    b "Wo bist du?"
    sis "Im Unterricht! Wieso rufst du mich an?!"
    sis "Mein Lehrer hat mich vor die Tür geschickt, weil das Handy geklingelt hat."
    sis "Ist es so wichtig?"
    "Das hätte ich ja wissen müssen."
    b "Nein, ich..."
    sis "Was ist denn?"
    sis "Beeil dich!"
    "Was soll ich ihr nur erzählen?"
    menu:
        "Ich fühlte mich einsam.":
            sis "Du fühltest dich einsam?"
            sis "Deshalb rufst du mich in der Schule an?"
            sis "Du bist doch bescheuert!"
        "Ich wollte nur wissen, wie es dir geht.":
            sis "Du wolltest wissen, wie es mir geht?"
            sis "Nur dafür rufst du mich an?"
            sis "Hättest du nicht warten können bis ich nach Hause komme?"
            sis "Nur zu deiner Information:"
            sis "Es geht mir überhaupt nicht gut!"
            sis "Deinetwegen bin ich aus dem Unterricht geflogen!"
        "Telefonstreich!":
            sis "..."
    "Sie legt auf."
    "Ich hätte wirklich wissen sollen, dass sie noch in der Schule ist."
    "Jetzt ist sie total sauer auf mich..."
    "Das gibt sicher Ärger."
    "Bleibt noch zu klären, wo meine Mutter ist."
    "Zu Hause ist sie nicht."
    "Einkaufen?"
    "Es ist 10:30 Uhr."
    "Ich bin um 10 Uhr aufgestanden, also ist sie schon mindestens eine halbe Stunde weg."
    "So lange braucht sie sonst nie."
    "In diesem Moment öffnet sich die Wohnungstür."
    
    play music m_wohnung
    
    ma "%(berndName)s?"
    ma "Was machst du denn hier oben?"
    "Sie hat zwei Plastiktüten in der Hand."
    "Also war sie wohl doch einkaufen."
    b "Darf ich nicht mehr in die Wohnung, oder wieso fragst du?"
    ma "Unsinn."
    ma "Man sieht dich hier oben nur so selten."
    ma "Den ganzen Tag hockst du im Keller."
    ma "Andere Männer in deinem Alter sind verheiratet und verdienen Geld."
    ma "Du hattest bisher nicht einmal eine Freundin."
    ma "Immer sitzt du vor deinem PC."
    "Na toll."
    "Immer fängt sie damit an."
    ma "Ach, ist ja auch egal."
    ma "Ich höre ja schon auf, wenn du nicht gern darüber redest."
    "Warum hat sie überhaupt angefangen?"
    ma "Willst du mir nicht in der Küche helfen?"
    ma "Es gibt heute Spaghetti."
    b "Nein ich..."
    "...habe zu tun, wollte ich sagen, aber was soll ich schon zu tun haben?"
    "Krautchan ist ja offline."
    "Wenn ich mich sonst nur langweilen würde, kann ich ihr auch helfen."
    b "...ich helfe gern."
    ma "Nanu?"
    ma "Was ist denn in dich gefahren?"
    ma "So kenne ich dich gar nicht."
    ma "Aber ich werde mich sicherlich nicht beschweren."
    "Lachend geht sie in die Küche."
    
    stop music fadeout 0.5
    
    scene black
    with fade
    
    "Eine halbe Stunde später klingelte das Telefon."
    "Anscheinend hatte %(sisName)s in der Schule ziemlichen Ärger bekommen, als ich sie angerufen habe."
    "Jetzt musste sie jemand abholen, und dieser jemand war ich."
    
    scene bg schulweg1
    #with fade
    
    show laura mad
    with fade
    
    play music m_drama
    #hier fehlt passende musik
    
    "Ich bin also mit %(sisName)s im Schlepptau auf dem Rückweg von der Schule nach Hause."
    "Bisher haben wir kein Wort gesprochen."
    "Anscheinend ist sie ziemlich sauer."
    "Kein Wunder."
    "Meinetwegen wurde sie für eine Woche von der Schule suspendiert."
    "Wir sind schon fast zu Hause."
    
    scene bg zuhause_draussen
    with fade
    
    show laura mad
    with dissolve
    
    sis "%(berndName)s!"
    sis "Hörst du mir überhaupt zu?"
    b "W... was?"
    "Ich hatte ihr natürlich nicht zugehört."
    sis "Du könntest dich doch wenigstens mal entschuldigen!"
    sis "Meinst du nicht?"
    "Ich?"
    "Mich entschuldigen?"
    "Bei meiner kleinen Schwester?"
    "Kommt gar nicht in Frage!"
    sis "Nun?"
    
    #######################################################
    #Je nachdem, ob Bernd sich nun bei Laura entschuldigt,#
    #verrät sie der Mutter, dass er sie angerufen hat.----#
    #Dies ist die erste wichtige Entscheidung.------------#
    #######################################################
    
    menu:
        "Ich entschuldige mich nicht!":
            $ zwei_entschuldigt = 0
            "Ich werde niemals so tief sinken."
            "Mich bei meiner kleinen Schwester zu entschuldigen."
            "Was glaubt sie wer sie ist?"
            b "Du bist doch selbst Schuld."
            sis "W... was?"
    
            show laura mad_talk
            with dissolve
    
            sis "Jetzt willst du mir die Schuld in die Schuhe schieben, oder was?"
            b "Hättest du dein Handy im Unterricht ausgeschaltet, so wie es sich gehört, dann wäre das sicher nicht passiert!"
            show laura sad
            with dissolve
            sis "Aber..."
            b "Jetzt heul hier nicht rum!"
            b "Akzeptiere einfach, dass du Schuld bist!"
    
            show laura crying
            with dissolve
    
            sis "Aber ich bin nicht Schuld!"
            sis "Du hast mich angerufen also bist du Schuld!"
    
            hide laura crying
            with dissolve
    
            "Weinend rennt sie nach Hause."
            "Jetzt wird sie sicher alles erzählen und ich krieg dafür Ärger."
            "Dabei bin ich nicht Schuld."
    
        "Ich entschuldige mich bei ihr.":
            $ zwei_entschuldigt = 1
            "Eigentlich hat sie ja Recht."
            "Hätte ich sie nicht angerufen, wäre das nie passiert."
            "Aber entschuldigen..."
            "Naja, bringe ich es halt hinter mich."
            b "{size=-12}'Tschuldigung.{/size}" #geiler effekt imho
            sis "Ich kann dich nicht hören."
            b "{size=-8}Entschuldigung.{/size}"
            sis "Ich hab es leider immer noch nicht verstanden."
            b "Es tut mir Leid, ok?"
            show laura happy
            with dissolve
            sis "Geht doch."
            "Anscheinend hat das gereicht, um sie wieder fröhlich zu stimmen."
            "In diesem Moment klingelt ihr Handy."
            
            play music m_laura
            
            sis "Oh!"
            sis "Das ist meine Freundin."
            sis "Wir wollten uns ja heute treffen."
            sis "Ich geh schon mal nach Hause vor, %(berndName)s!"
            b "Wie du meinst."
     
            hide laura happy
            with dissolve
     
            "Wahrscheinlich würde sie zu Hause alles erzählen."
            "Scheiße."
    "Ich verwerfe den Gedanken und gehe weiter."
    "%(sisName)s ist schon außer Sichtweite."
    "Für ihr Alter ist sie ganz schön schnell."
    "Ich erinnere mich wieder an Stalkerbernd und instinktiv sehe ich mich um."
    "Nichts."
    "Niemand ist zu sehen."
    "Ich biege um die Ecke und komme an meinem Fenster vorbei."
    "Die Schraube fehlt immer noch."
    "Das sollte ich wohl oder übel mal beheben."
    "Ich drehe mich um und will reingehen, als mir etwas ins Auge sticht."
    
    stop music fadeout 0.5
    
    scene bg lieferwagen
    with fade
  
    "Direkt gegenüber steht ein weißer Lieferwagen mit getönten Scheiben."
    "War der eben auch schon da?"
    "Ich kann mich nicht erinnern."
    "Wahrscheinlich bilde ich mir das nur ein."
    "Etwas verunsichert gehe ich rein."
  
    scene black
    with wooshTrans
  
    scene bg wohnung_innen
    with wooshTrans
    
    play music m_wohnung
  
    "%(sisName)s hat natürlich schon alles erklärt."
    b "...und?"
    b "Hat sie dir alles erzählt?"
    ma "Ja."
    ma "...und ich finde es unerhört, jemandem einfach so im Unterricht anzurufen!"
    "Jetzt gehts los."
    ma "...wie kann man so was nur machen?"
    ma "Ist doch klar, dass das Ärger gibt!"
  
    if(zwei_entschuldigt): #wenn bernd sich entschuldigt hat
        ma "...und so was nennt sich Freundin."
        "Freundin?"
        b "Was meinst du...?"
        b "Freundin?"
        "Fragend sieht mich meine Mutter an."
        "Ich schau zu %(sisName)s, aber sie grinst nur und nickt mir zu."
        b "Ach, ja!"
        b "Freundin!"
        b "Ich verstehe schon."
        "Meine Mutter sieht verwirrt aus."
        b "Ich gehe besser runter in den Keller..."
        ma "Alles in Ordnung, %(berndName)s?"
        b "Ich bin nur ein wenig unkonzentriert."
        b "Schlecht geschlafen und so."
        ma "Na dann..."
        ma "...sollte ich mich wohl um das Mittagessen kümmern."
        sis "...und ich mache mich fertig für meine Verabredung."
        "Die beiden verlassen das Zimmer."
        "Ich beschließe, nach unten zu gehen."
    else: #wenn bernd sich nicht entschuldigt hat
        ma "...und so was nennt sich Bruder."
        ma "Ich bin enttäuscht, %(berndName)s!"
        ma "Du hattest ja nicht einmal einen richtigen Grund!"
        ma "Du solltest dich wirklich schämen!"
        "Das Gequatsche halte ich nicht mehr aus."
        "Ich ignoriere sie und verziehe mich in meinen Keller."
  
    scene black
    with wooshTrans
    
    stop music fadeout 0.5
  
    scene bg keller
    with wooshTrans
    
    play music m_bernd
  
    "Unten angekommen, sehe ich aus dem Fenster."
  
    scene bg lieferwagen
    with fade
  
    "Der Lieferwagen steht immer noch draußen."
    "Direkt gegenüber."
  
    scene bg keller
    with fade
  
    "Merkwürdig, dass ich ihn noch nie hier gesehen habe."
    "Ich vertreibe den Gedanken und setze mich an meinen Rechner."
  
    scene bg desktop_none
    with dissolve
  
    "Nichts neues."
    "Es muss doch mehr im Leben geben, als Krautchan, oder?"
    "...aber spontan fällt mir kein anderer Zeitvertreib ein."
    "Games habe ich alle schon durch."
    "Fappiert habe ich heute morgen."
    "Arbeit oder Schule habe ich nicht."
    "Was machen denn andere Leute so, wenn sie nicht lauern?"
  
    scene bg keller
    with dissolve
  
    show laura happy
    with dissolve
  
    sis "Hey, %(berndName)s."
    sis "Ich gehe jetzt rüber zu meiner Freundin."
    sis "Wollte dir nur Bescheid sagen."
  
    hide laura happy
    with dissolve
  
    b "..."
    "Meine Schwester hat anscheinend Freunde und so was."
    "...aber sie geht ja auch zur Schule."
    "Da findet man leicht nette Menschen."
    "Wenn ich mich an meine Schulzeit erinnere..."
    "...fällt mir auf, dass ich selbst damals keine Freunde hatte."
    b "Verdammt."
    "Vielleicht ist ja inzwischen das Essen fertig."
    "Ich gehe am besten hoch und frage wie lange es noch dauert."
  
    scene bg wohnung_innen
    with fade
    
    play music m_wohnung fadein 0.5
 
    ma "Ah, %(berndName)s!"
    ma "Du kommst grade richtig."
    ma "Ich wollte dir dein essen runterbringen, aber wenn du schon hier bist, kannst du es selbst mitnehmen."
    b "Ich glaube, ich esse heute hier oben."
    "Erstaunt sieht sie mich an."
    ma "Sicher, dass mit dir alles ok ist?"
    ma "Du isst sonst nie oben."
    b "Irgendwann ist immer das erste Mal."
    ma "Du hast ja recht."
    ma "Vielleicht wird ja doch noch was aus dir."
    "Bla. Bla. Bla."
    "Wenn sie glaubt, dass ich mir eine Arbeit suche und in eine eigene Wohnung ziehe, dann hat sie sich getäuscht."
    "Dafür ist es zu Hause viel zu bequem."
    ma "Du kannst nicht ewig von Hartz IV leben, %(berndName)s."
    ma "Willst du denn nicht..."
    ma "...ach vergiss es."
    ma "Essen wir lieber."
    scene black
    with fade
    stop music fadeout 0.5
    "Nach dem Essen kam auch irgendwann %(sisName)s nach Hause und hat vom Treffen mit ihrer Freundin erzählt."
    "Ich ging nach unten und verbrachte den Rest des Tages damit, alte Spiele nochmal durchzuspielen und schaute ab und zu nach Krautchan."
    "An der 404-Seite hatte sich den ganzen Tag über nichts geändert, also gab ich auf und ging ins Bett."
 
    scene bg keller_aus
    with fade
 
    "Ob jetzt wohl jeder Tag so ablaufen wird?"
    "Vielleicht sollte ich Krautchan einfach vergessen und mich den wichtigen Dingen im Leben zuwenden."
    "Ich könnte ja einen Job suchen."
    "Vielleicht finde ich dort auch Freunde oder zumindest Bekannte."
    "Einfach Menschen, mit denen ich sprechen kann."
    "Immer nur alleine im Keller zu hocken ist auch irgendwie langweilig."

    play sound "sounds/schraube.wav"
    "...!"
    "Da ist es wieder."
    "Das gleiche Geräusch wie gestern Abend."

    play sound "sounds/schraube.wav"

    "Das Geräusch, von dem ich nicht wusste, woher es kommt."

    play sound "sounds/schraube.wav"

    "Jetzt weiss ich es."

    play sound "sounds/schraube.wav"

    "Jemand sitzt bei mir am Kellerfenster und öffnet das Gitter."

    play sound "sounds/schraube.wav"

    "Ich habe total vergessen, die Schraube wieder einzudrehen."

    play sound "sounds/schraube.wav"

    "Was soll ich machen?"

    play sound "sounds/schraube.wav"

    "Aufspringen und ihn erschrecken?"

    play sound "sounds/schraube.wav"

    "Nein, das traue ich mich nicht."

    play sound "sounds/schraube.wav"

    "Ich werde einfach die Augen zu machen und so tun, als würde ich schlafen."

    scene black
    with fade

    "..."
    "Das Geräusch ist verstummt."
    "Das kann nur bedeuten, dass er das Fenster schon geöffnet hat."
    "...aber jetzt höre ich nichts mehr."
    "Ist er wieder gegangen?"
    "Nein..."
    "Ich spüre ihn neben meinem Bett."
    play music m_yasminStalk fadein 0.5
    "Er ist verdammt leise."
    "Ich öffne die Augen nur ein wenig, und sehe ihn."

    scene bg keller_aus
    with fade

    show yasmin stalker
    with dissolve

    "Der gleiche schwarze Mantel."
    "Kein Zweifel."
    "Das ist Stalkerbernd."
    "Stalkerbernd ist bei mir im Keller."
    "Was hat er vor?"
    "Gibt es bei mir irgendetwas von Wert?"
    "Nein."
    "Hier unten steht nur mein PC."
    "Wenn er da ran will, muss er mein Passwort knacken."
    
    "Sollte ich nicht eingreifen?"

    menu:
        "Ja, ich muss was tun!":
            "Ich muss jetzt eingreifen!"
            "Wenn ich ihn noch länger in Ruhe lasse..."
            "Nicht auszudenken, was er anstellen könnte."
            "Ich spanne all meine Muskeln an und bereite mich auf den Angriff vor."
            "..."
            "Jetzt!"
            "Blitzschnell werfe ich die Bettdecke zur Seite und springe auf."
            "Ich werfe mich mit meinem gesamten Gewicht in seine Richtung."
            show yasmin stalker at right
            with fastMove
            show yasmin stalker at center
            with fastMove
            "Ich bin zu langsam."
            "Er weicht aus und ich knalle gegen die harte Wand."
            "Schnell richte ich mich auf und setze zum zweiten Angriff an."
            show bg keller_aus
            with vpunch
            "Etwas hartes trifft mich am Kopf und mir wird kurz schwarz vor Augen."
            show black
            with fade
            "Ich darf jetzt nicht die Kontrolle verlieren."
            "Mit aller Kraft raffe ich mich auf."
            hide yasmin stalker
            #with fade
            hide black
            with fade
            "Er ist weg...?"
            "Wenn ich mich beeile erwische ich ihn noch!"
            scene bg kellertreppe
            with fastFade
            scene bg wohnung_innen
            with fastFade
            scene bg zuhause_hausflur
            with fastFade
            scene bg zuhause_draussen
            with fastFade
            "..."
            "Niemand da."
            "Verwirrt sehe ich mich um."
            "So weit kann er nicht sein!"
            "Der Lieferwagen auf der anderen Straßenseite springt mir ins Auge."
            scene bg lieferwagen
            with fade
            "Jemand sitzt am Steuer und startet den Wagen."
            "So schnell ich kann, renne ich los, aber das Auto rast an mir vorbei auf die nächste Kreuzung zu."
            scene bg zuhause_draussen
            with fade
            "Ich laufe hinterher auf die offene Kreuzung, als die Ampel auf rot springt."
            "Der Lieferwagen biegt ohne abzubremsen um die Ecke."
            "Ich versuche, das Kennzeichen zu erkennen, aber er ist schon zu weit weg."
            "Ich muss ihn fassen!"
            "Wenn ich ihn jetzt nicht schnappen kann, wird er mich mein Leben lang verfolgen."
            "Von diesem Gedanken besessen laufe ich auf die Kreuzung."
            "Zu spät bemerke ich die Lichter des Autos, das von links auf die Kreuzung fährt."
            scene white
            with dissolve
            jump ende #Bernd stirbt hier!
            
        "Nein, ich warte noch ab.":
            "Ich muss noch warten!"
    
    "Ich werde ihn einfach noch ein wenig beobachten."
    "Notfalls kann ich dann immer noch eingreifen."
    "Er setzt sich an meinen Rechner."
    "Naja, da kommt er nicht rein."
    "Mein Passwort ist so siche-{nw}"
    "Er ist drin."
    "Ich kann es nicht wirklich glauben, aber über seine Schulter sehe ich eindeutig mein Wallpaper."
    "Er hat mein Passwort geknackt."
    "Innerhalb weniger Sekunden hat er es geschafft mein Passwort zu knacken."
    "Das ist kein Anfänger."
    "Ich habe es hier mit einem Expertenhacker zu tun."
    "Ein Expertenhacker, der es auf mich abgesehen hat."
    "Ich kann nicht sehen, was er am Computer macht, und wenn ich mich bewege, schöpft er vielleicht Verdacht."
    "Andererseits kann ich hier auch nicht einfach liegen und warten, bis er von alleine weggeht."
    "Ich muss langsam etwas tun..."
    
    menu:
        "Ich sollte eingreifen!":
            "Ich sollte nicht unüberlegt handeln, aber ich muss etwas tun."
            "Was macht der dort?"
            "Er holt einen kleinen Kasten unter dem Mantel hervor."
            "Eine externe Festplatte, die er per USB anschließt."
            "Er will ein Backup machen."
            "Diesen Moment muss ich nutzen."
            "Jetzt ist er abgelenkt."
            "Wenn ich noch etwas zögere, verpasse ich meine Chance."
            "Ich spanne jede einzelne Muskelfaser meines Körpers an."
            "Obwohl ich damals in Sport immer beim Bodenturnen versagt habe, gelingt mir die nahezu perfekte Hechtrolle."
            "Ich werfe den erschrockenen Stalkerbernd zu Boden."
            "Mit einer fließenden Bewegung greife ich ihn an beiden Handgelenken und drücke die Arme auf den Boden."
            b "Hab ich dich!"
            #BUTTERGOTT:
            #hier wäre ein großes CG cool!
            "Er starrt mich schweigend an."
            b "Jetzt bist du fällig, Stalkerbernd!"
            jump zwei_yasmin_geschnappt
 
        "Nein, ich warte nur noch ein bisschen...":
            "Ich sollte wirklich nicht unüberlegt handeln."
            "Vielleicht sollte ich doch versuchen, mich ein wenig zu bewegen?"
            "Nur ein kleines Stück den Kopf drehen, damit ich den Monitor sehen kann."
            "Vielleicht durchsucht er meine Dateien, oder installiert irgendeinen Virus?"
            "Plötzlich holt er einen kleinen Kasten unter dem Mantel hervor."
            "Eine externe Festplatte, die er per USB anschließt."
            "Ich nutze den kurzen Moment, um mich ein wenig zu drehen, so dass ich den Monitor sehen kann."
            "Er macht ein Backup meiner Daten, um dann zu Hause alles in Ruhe durchzugehen."
            "Clever."
            "Wenn ich daran denke, dass er zu Hause in Seelenruhe durch meine persönlichsten Informationen stöbert..."
            "Mein Hals fühlt sich an, als würde mich jemand erwürgen wollen."
            "Als würde ein ungeheurer Druck ihn zusammenschnüren."
            "Ich will husten, aber ich muss mich zusammenreißen und den Reflex unterdrücken."
            "Lange halte ich es nicht mehr aus."
            "Ich muss irgendwas tun."
            "Die Ladeleiste auf dem Monitor verrät mir, dass das Backup noch 15 Minuten braucht."
            "Das halte ich auf keinen Fall so lange durch."
            "Das drückende Gefühl wird stärker."
            "Ich bekomme keine Luft mehr."
            "Nicht in der Lage, den Reflex weiter zu unterdrücken, platzt es aus mir heraus."
            "Tränen schießen mir in die Augen, während ich hustend nach Luft schnappe."
            
            scene black
            with dissolve
            
            "Jetzt ist alles zu spät."
            "Er hat mich bemerkt und wird mich umbringen oder so was."
            "Er darf ja keine Spuren hinterlassen."
            "Ich warte auf seine Reaktion."
            "Ich warte, aber es passiert nichts."
            "Warum passiert nichts?"
            "Will er mich nicht irgendwie loswerden oder so?"
            
            scene bg keller_blur
            with dissolve
            
            "Ich kann nichts erkennen."
            "Mit der Hand wische ich mir die Tränen aus den Augen."
            
            scene bg keller
            with wooshTrans
            
            "..."
            "Er ist weg."
            "Einfach verschwunden."
            "Die Fehlermeldung auf dem Bildschirm lässt mich wissen, dass das externe Gerät unerwartet entfernt wurde, und dass das Backup nicht fertiggestellt werden konnte."
            "Ein Glück."
            "Zu schwach, heute Abend noch irgendetwas zu tun, lasse ich mich ins Bett fallen und schlafe ein."
     
            scene black
            with fade
 
            jump ende

            
label zwei_yasmin_geschnappt:
    "Stalkerbernd" "Stalkerbernd?"
    
    stop music fadeout 0.5
    
    "!"
    "Es hat gesprochen."
    "Stalkerbernd" "Wer soll das sein?"
    "Diese Stimme...?"
    "Ich lasse seine Arme los, und setze mich auf's Bett."
    "Ich bin verwirrt."
    "Seine Stimme klingt wie..."
    b "...du bist ein Mädchen?"
    
    show yasmin stalker_shy
    with dissolve
    
    play music m_yasmin
    
    "Wow."
    "Ich habe mit allem gerechnet, aber damit nicht."
    b "...aber."
    b "Ich dachte doch..."
    b "Du..."
    
    show yasmin stalker_neutral
    with dissolve
    
    u"Mädchen" "Was?"
    u"Mädchen" "Was hast du gedacht?"
    u"Mädchen" "Und was wirst du nun mit mir machen?"
    u"Mädchen" "Wirst du jetzt die Polizei rufen?"
    u"Mädchen" "Ja, ich geb es ja zu."
    u"Mädchen" "Ich bin ein Stalker."
    u"Mädchen" "Ich hab dich gestalkt."
    u"Mädchen" "Du hast ja Recht."
    u"Mädchen" "Also."
    u"Mädchen" "Ruf die Polizei schon an, ich habe es verdient."
    "Ich kann ihr irgendwie nicht folgen..."
    b "Du bist kein Bernd?"
    
    #show yasmin confused
    #with dissolve
    #Bild existiert noch nicht
    
    u"Mädchen" "Bernd?"
    if berndName == "Bernd":
        u"Mädchen" "Ich dachte, du wärst %(berndName)s."
        b "Ja, der bin ich auch."
        u"Mädchen" "Und wie kommst du dann drauf, dass ich Bernd sei?"
        b "Ach, schon gut."
    "Habe ich mich geirrt?"
    "Ist sie wirklich kein Bernd?"
    "Andererseits kann sie mir hier auch nur einen vorspielen."
    "Aber warum sollte mich sonst jemand stalken?"
    b "Mach dich nicht über mich lustig!"
    b "Warum solltest du mich sonst stalken?!"
    
    show yasmin stalker_shy
    with dissolve
    
    u"Mädchen" "..."
    b "..."
    "Vielleicht ist sie wirklich kein Bernd?"
    "...aber ist das nicht egal?"
    "Sie ist bei mir eingebrochen."
    "Mehrmals."
    b "Warum bist du bei mir eingebrochen?"
    u"Mädchen" "..."
    b "Warum hast du mich verfolgt?"
    u"Mädchen" "..."
    b "Wer bist du?"
    u"Mädchen" "..."
    b "Was willst du von mir?"
    $ yanNameKurz = stringShorten(yanName,2)
    u"Mädchen" "%(yanNameKurz)s- %(yanName)s."
    b "Wa- wie bitte?"
    "%(yanName)s?"
    u"Mädchen" "Ich heiße %(yanName)s."
    $ yanKennen = 1
    b "..."
    yan "..."
    "%(yanName)s also..."
    "Ich habe keine Ahnung, was ich sagen soll..."
    "...aber wenn man sie so ansieht, könnte man meinen, ihr ginge es genauso."
    yan "..."
    b "..."
    "Was soll ich denn nun mit ihr machen?"
    "Die Polizei rufen?"
    
    show yasmin stalker_neutral
    with dissolve
    
    yan "%(berndName)s... ich..."
    "Woher kennt sie meinen Namen überhaupt?"
    b "Woher kennst du meinen Namen?"
    
    show yasmin stalker_shy
    with dissolve
    
    yan "..."
    "Jetzt schweigt sie wieder."
    "Ich sollte nicht dazwischen reden, wenn ich etwas von ihr erfahren will."
    b "Sprich ruhig weiter."
    yan "..."
    yan "Ich..."
    
    #show yasmin stalker_cry #braucht noch besseres bild für wenn sie RICHTIG heult
    #with dissolve
    
    yan "...es tut mir so Leid!"
    yan "*schluchz*"
    "Warum weint sie denn jetzt!?"
    "Ist das nur Show?"
    "Will sie mich auf den Arm nehmen?"
    "Nur um dann einen überraschenden Fluchtversuch zu starten?"
    "Oder ist es echt?"    
    yan "*schluchz*"
    b "Beruhig dich doch erst mal!"
    b "Ich werde schon nicht die Polizei rufen."
    b "Allerdings musst du mir schon erklären, was es mit dieser ganzen Sache auf sich hat."
    
    #show yasmin stalker_cry
    #with dissolve
    
    yan "..."
    b "Nun?"
    yan "..."
    b "..."
    "Das kann ja heiter werden."
    "Wie lange will sie noch hier sitzen und schweigen?"
    yan "..."
    "Vielleicht sollte ich sie irgendwas fragen?"
    "...aber was?"
    "Warum sie mich verfolgt hat, und was das alles überhaupt soll, will sie mir anscheinend nicht sagen..."
    "Was mach ich denn jetzt mit ihr?"
    "Ich kann sie ja nicht einfach hier sitzen lassen?"
    "Irgendwie muss ich sie zum Reden bringen..."
    "...aber wie?"
    b "Fangen wir noch mal ganz von vorne an."
    
    show yasmin stalker_neutral
    with dissolve
    
    yan "..."
    "Zuerst frage ich sie, warum sie mich verf-... nein."
    "Das ist zu direkt."
    "Ich muss das langsamer angehen."
    "Aber wie?"
    "Was weiß ich denn bisher über sie?"
    "Hmm..."
    "Ich kenne nur ihren Namen."
    "Fangen wir damit an."
    b "Dein Name ist also %(yanName)s?"
    "Sie nickt."
    "Das ist doch schon mal ein Anfang."
    "...aber..."
    
    #hier folgt nun ein dialog, bei dem verschiedene fragen gestellt werden können,
    #wobei jede Frage den Spieler weiterbringen kann, aber nicht muss
    
label yasmin_befragung_eins:
    python:
        try:
            y_bef_11
        except NameError:
            y_bef_11 = 0
        try:
            y_bef_12
        except NameError:
            y_bef_12 = 0
    menu:
        "Wie soll ich jetzt weiterfragen?"
        
        "Was willst du hier?" if y_bef_11 == 0:
            $ y_bef_11 = 1
            b "Was willst du hier?"
            yan "..."
            "Keine Antwort..."
            jump yasmin_befragung_eins
      
        "Warum verfolgst du mich?" if y_bef_12 == 0:
            $ y_bef_12 = 1
            b "Warum verfolgst du mich?"
            yan "Ich..."
            b "Ja?"
            yan "..."
            "Keine Antwort..."
            jump yasmin_befragung_eins
      
        "Willst du vielleicht erst mal was trinken?": #wird immer angezeigt
            b "Willst du vielleicht erst mal was trinken?"
            "Sie nickt."
            "...aber kann ich sie hier einfach alleine lassen?"
            "Eigentlich nicht..."
            yan "Ich..."
            yan "Ich lauf nicht weg!"
            yan "Ganz bestimmt!"
            yan "Ich kann auch mitkommen!"
            yan "Aber ich laufe bestimmt nicht weg!"
            "Sieh an."
            "Plötzlich redet sie."
            "Sie mit nach oben zu nehmen ist keine gute Idee."
            "Nachher sieht sie noch jemand."
            "Ich werde mich einfach beeilen, dann kann sie nicht entkommen."
            b "Warte hier, ich bin gleich wieder da."
            yan "...ok."
            b "Was möchtest du denn trinken?"
            yan "..."
            "Sie sagt wieder nichts."
            b "Na gut dann bringe ich di-"
            yan "Traubensaft."
            "Traubensaft?"
            "Hat hier jemals einer Traubensaft getrunken?"
            b "Ich weiß nicht, ob wir welchen hier haben."
            yan "..."
            yan "Im Kühlschrank."
            yan "Dritte Flasche von hinten."
            b "..."
            "Woher will sie das wissen?!"
            "Sie wird doch nicht die Wohnung durchsucht haben?"
            "Ich sag lieber nichts."
            b "Bin gleich wieder da."
            
            $renpy.music.set_volume(0.5,0.5,channel="music")
            
            scene bg kueche
            with fade
            
            "Tatsächlich."
            "Wir haben Traubensaft."
            "Genau da, wo sie gesagt hat."
            "Das ist nicht normal!"
            "Die ist ja völlig krank."
            "Ich sollte mich lieber beeilen."
            "Hastig fülle ich zwei Gläser und begebe mich so schnell es geht wieder nach unten."
            
            $renpy.music.set_volume(1.0,0.5,channel="music")

            
            scene bg keller_aus
            

            
            show yasmin stalker_neutral
            with fade
            
            "Sie sitzt noch genau so da, wie ich sie verlassen habe."
            "Anscheinend hat sie wirklich nicht vor abzuhauen."
            "...oder ist das ein Trick?"
            "Ich reiche ihr ein Glas und setze mich wieder hin."
            yan "..."
            yan "Danke."
            "Also..."
            "Was nun?"
            
label yasmin_befragung_zwei:
    python:
        try:
            y_bef_21
        except NameError:
            y_bef_21 = 0
        try:
            y_bef_22
        except NameError:
            y_bef_22 = 0
   
    menu:
        "Wie soll ich weiter vorgehen?"
        
        "Was willst du von mir?" if y_bef_21 == 0:
            b "Was willst du von mir?"
            b "Warum bist du hier?"
            yan "..."
            b "Es muss doch einen Grund geben?"
            yan "..."
            yan "Nein."
            yan "Ich..."
            yan "Ich weiß nicht..."
            "So kommen wir nicht weiter."
            $ y_bef_21 = 1
            jump yasmin_befragung_zwei
            
        "...und was soll ich jetzt mit dir machen?": #immer anzeigen
            b "...und was soll ich jetzt mit dir machen?"
            yan "..."
            b "Ich kann dich ja nicht einfach laufen lassen."
            "Nein, das geht auf keinen Fall."
            "...aber ans Weglaufen scheint sie ja auch gar nicht zu denken."
            b "Warum bist du nicht weggelaufen?"
            b "Ich habe dir genug Zeit gegeben, oder?"
            
            show yasmin stalker_surprised
            with dissolve
            
            yan "..."
            b "Was willst du denn von mir?"
            b "Wenn du nicht sprichst, kann ich dir nicht helfen."
            
            show yasmin stalker_embarrased
            with dissolve
            
            yan "..."  
            "Sie will jedenfalls nicht weglaufen."
            "Irgendetwas muss es noch geben, was sie davon abhält."
            jump yasmin_befragung_drei
            
        "Wie schmeckt der Traubensaft?" if y_bef_22 == 0:
            b "Wie schmeckt der Traubensaft?"
            
            show yasmin stalker_neutral
            with dissolve
            
            yan "...gut."
            b "..."
            yan "..."
            $ y_bef_22 = 1
            jump yasmin_befragung_zwei
            
            
label yasmin_befragung_drei:
    python:
        try:
            y_bef_31
        except NameError:
            y_bef_31 = 0
        try:
            y_bef_32
        except NameError:
            y_bef_32 = 0
    
    menu:
        "Nach was frage ich sie jetzt?"
        
        "Warum antwortest du mir nicht?":
             b "Warum antwortest du mir nicht?"
             b "Es muss doch einen Grund geben, sonst wären wir jetzt nicht hier."
             
             show yasmin stalker_embarrased
             with dissolve
             
             yan "..."
             b "Kannst du es mir nicht sagen, oder willst du es mir nicht sagen?"
             yan "..."
             
        "Soll ich dich einfach gehen lassen, oder was?":
             b "Soll ich dich einfach gehen lassen, oder was?"
             yan "..."
             b "Willst du gehen?"
             "Inzwischen ist es mir egal."
             b "Ich gebe auf."
             b "Geh."
             yan "..."
             "Sie geht nicht."
             "Sie rührt sich keinen Zentimeter."
             
        "Antworte mir, sonst kann ich für nichts garantieren!":
             b "Antworte mir, sonst kann ich für nichts garantieren!"
             yan "..."
             b "Ich rufe die Polizei!"
             yan "..."
             b "Ich warne dich zum letzen Mal!"
             yan "..."
    
    play music m_psycho
    
    b "{size=32}Verdammt!{/size}"
    
    show yasmin stalker_surprised
    with dissolve
    
    b "Was willst du nur von mir!?"
    "Ich springe auf und drücke sie gegen die Wand."
    b "{size=32}ANTWORTE!{/size}"
    yan "..."
    
    "Stimme" "%(berndName)s?"
    "Das ist %(sisName)s!"
    "Verdammt, was mache ich jetzt?"
    "Ich hätte nicht so laut sein sollen." 
    sis "Alles ok da unten?"
    "Scheiße!"
    b "J- Ja!"
    b "Alles ok!"
    b "Nicht reinkommen!"
    "Ich muss dieses Mädchen loswerden!"
    b "Versteck dich!"
    yan "..."
    "Warum macht sie denn nichts!?"
    b "Du sollst dich verstecken!"
    yan "...wo denn?"
    "Stimmt ja."
    "Hier unten ist ja nichts, wo man sich verstecken könnte."
    sis "%(berndName)s? Wieso soll ich nicht reinkommen?"
    "Sie ist schon direkt vor der Tür."
    b "Warte nur kurz, ja?"
    "%(yanName)s sitzt immer noch da und rührt sich nicht."
    b "Los!"
    b "Irgendwo!"
    sis "Mit wem sprichst du?"
    b "Mit niemandem!"
    b "Mit wem sollte ich denn sprechen?"
    "Ich packe %(yanName)s an den Armen und werfe sie auf's Bett."
    b "Los, unter die Decke!"
    
    show yasmin stalker_embarrased
    with dissolve
    
    yan "...!"
    b "Los!"
    sis "Ich komme jetzt rein, %(berndName)s!"
    
    hide yasmin stalker_embarrased
    with dissolve
    
    stop music fadeout 0.5
    
    show laura neutral
    with dissolve
    
    sis "Was machst du denn hier?"
    sis "Wieso bist du so laut?"
    b "N-nichts!"
    "Ich stelle mich vorsichtshalber vor das Bett."
    sis "Ist wirklich alles ok?"
    b "Ja!"
    b "Alles ok!"
    "Hoffentlich merkt sie nichts."
    b "Wieso?"
    sis "Du bist anders als sonst."
    b "Tja."
    "Mehr bringe ich nicht hervor."
    b "D- Du kannst jetzt gehen."
    sis "In Ordnung."
    b "..."
    sis "..."
    b "Worauf wartest du?"
    sis "...ganz sicher, dass alles ok ist?"
    b "Ja."
    sis "Mit wem hast du dann eben gesprochen?"
    b "Ich..."
    b "Das war online!"
    "Perfekte Ausrede ist perfekt!"
    sis "Ach so!"
    
    show laura happy
    with dissolve
    
    sis "Da habe ich nicht dran gedacht!"
    sis "Dann ist ja alles ok."
    b "Sag ich doch."
    
    show laura neutral
    with dissolve
    
    sis "Gute Nacht, %(berndName)s!"
    b "Gute Nacht."
    
    hide laura neutral
    with dissolve
    
    "Sie geht schon so früh schlafen?"
    "Das wusste ich gar nicht."
    "...aber in ihrem Alter musste ich wahrscheinlich auch so früh ins Bett."
    "..."
    "Ah!"
    "Ich drehe mich zum Bett und schlage die Decke zurück."
    
    show yasmin stalker_happy
    with dissolve
    
    "Nanu?"
    "Warum ist sie denn so fröhlich?"
    
    b "Warum so grinsend?"
    
    show yasmin stalker_surprised
    with dissolve
    
    show yasmin stalker_shy
    with dissolve
    
    b "Hm...?"
    yan "..."
    "Ich habe es genau gesehen."
    "Sie kann mir nichts vormachen."
    b "Also...?"
    b "Weswegen grinst du so?"
    yan "..."
    
    play music m_yasmin
    
    yan "...deine... {w=1}Bettwäsche."
    "Meine Bettwäsche?"
    "Was ist daran so besonders?"
    "..."
    "Oh."
    "Wahrscheinlich ist es für einen Mann in meinem Alter nicht normal, Animebettwäsche zu besitzen."
    "Kein Wunder, dass sie sich darüber lustig macht."
    show yasmin stalker_happy
    with dissolve
    yan "Das ist Lucky Star, richtig?"
    "Was zum...?"
    "Woher kennt sie Lucky Star?"
    b "J-Ja."
    yan "Ist es lustig?"
    yan "Ich bin noch nicht dazu gekommen, es zu sehen."
    yan "{=slow}Also ich wollte eigentlich schon die ganze Zeit, aber dann kam immer was dazwischen und es hat ja auch nicht gerade wenig Folgen und dann haben so viele Leute erzählt wie schlecht die Serie sei und irgendwie fand ich dann aber manche Bilder doch recht lustig und hab dann mal in die ersten beiden Folgen reingeschaut aber die waren nicht so gut also{/=slow}{nw}"
    b "Stop!"
    show yasmin stalker_surprised
    with dissolve
    yan "T-Tut mir Leid..."
    "Ich bin verwirrt."
    "Was war das gerade?"
    "Sie hat den Spieß komplett umgedreht."
    "Erst spricht sie kein Wort und dann redet sie wie ein Wasserfall..."
    "...und das auch noch über Anime!"
    "Mein Spezialgebiet!"
    "Was bildet die sich ein?"
    "Wütend balle ich meine Fäuste."
    show yasmin stalker_shy
    with dissolve
    yan "T-Tut mir wirklich Leid!"
    yan "Ich wollte nicht so viel reden, aber..."
    show yasmin stalker_embarrased
    with dissolve
    yan "..."
    b "..."
    "Anscheinend habe ich sie erschreckt."
    "Vielleicht sollte ich mich entschuldigen."
    yan "W-Wenn..."
    "Oh, sie spricht?"
    yan "Wenn ich über etwas rede, was mich interessiert, kann ich gar nicht mehr aufhören..."
    b "..."
    "Sie will mir also erzählen, dass sie Lucky Star mag?"
    "...ist das nur ein Trick?"
    yan "...du magst Anime, oder?"
    b "Sieht man das nicht?"
    b "Mein ganzes Zimmer ist voll mit Postern!"
    yan "...ja."
    show yasmin stalker_shy
    with dissolve
    yan "Das war eine dumme Frage."
    yan "Entschuldigung."
    b "Ja, ich mag Anime."
    b "Ist das so schlimm?"
    b "Darf man in meinem Alter so was nicht mehr gucken, oder was?"
    show yasmin stalker_surprised
    with dissolve
    yan "Nein, nein!"
    yan "D-Das meinte ich nicht."
    show yasmin stalker_shy
    with dissolve
    yan "Ich war nur... {w}überrascht."
    "Hm..."
    "Irgendwie verständlich."
    "..."
    "Aber eine Lösung für dieses Problem finden wir so nicht."
    "Ich muss sie immer noch irgendwie loswerden."
    "...aber ich habe keine Lust mehr, die Polizei zu rufen."
    yan "%(berndName)s...?"
    yan "Wenn du willst...{w} gehe ich einfach."
    b "..."
    "Kann ich sie einfach gehen lassen?"
    "Ich will doch wissen, warum sie überhaupt hier ist!"
    "Nein. {w}Bevor ich das nicht herausgefunden habe, bleibt sie hier!"
    b "Willst du mir nicht erst erzählen, was das hier alles soll?"
    yan "..."
    b "Du brichst in meine Wohnung ein, versuchst meine Festplatte zu kopieren..."
    b "...du wusstest sogar, wo im Kühlschrank die Saftflasche steht!"
    yan "..."
    b "Wieviel weißt du noch über mich, hä?"
    yan "..."
    yan "Nicht viel..."
    yan "D-Dein Name ist %(berndName)s."
    yan "Du magst Anime."
    yan "Du hast eine kleine Schwester...{w} %(sisName)s."
    yan "Das war alles...{w} denke ich."
    "Sie weiß wirklich nicht viel."
    b "Aber was willst du denn dann von mir?"
    b "Sag es mir doch einfach!"
    yan "Ich würde es dir sagen... {w}wenn ich könnte."
    b "Was soll das denn bedeuten?"
    b "Wieso solltest du es nicht können?"
    yan "Weil..."
    show yasmin stalker_neutral
    with dissolve
    yan "...ich es nicht weiß."
    b "Also nochmal..."
    yan "Warte, %(berndName)s..."
    yan "...egal, wie oft du fragen wirst, ich kann es dir nicht sagen."
    yan "Du wirst keine Antwort bekommen, weil ich dir keine Antwort geben kann."
    yan "Ich kann nicht, obwohl ich will."
    show yasmin stalker_shy
    with dissolve
    yan "...das ist alles, was ich dir noch sagen wollte."
    yan "Darf ich nun gehen?"
    b "..."
    "Ich kann sie nicht gehen lassen."
    b "Nein, bleib hier."
    yan "..."
    yan "Warum?"
    yan "Es wird nichts ändern."
    "Ich darf sie nicht entkommen lassen."
    "Ich muss sie irgendwie davon überzeugen, zu bleiben."
    b "I-Ich werde dich nichts mehr fragen."
    yan "...?"
    b "Ich..."
    "Was jetzt?"
    b "Du sagtest, du magst Lucky Star... oder?"
    yan "Was?"
    yan "Wieso spielt das jetzt eine Rolle?"
    b "Ich..."
    b "Ich will dich einfach ein bisschen... {w}besser kennenlernen."
    show yasmin stalker_surprised
    with dissolve
    "Habe ich das wirklich gesagt?"
    "Zu einem Mädchen?"
    "Mir ist auf die Schnelle nichts Besseres eingefallen."
    "Ob sie mir das abnimmt?"
    yan "..."
    "Anscheinend nicht."
    b "Also... was ist nun?"
    b "Magst du Lucky Star?"
    yan "..."
    show yasmin stalker_shy
    with dissolve
    yan "Naja..."
    yan "Ich habe nur die ersten beiden Folgen gesehen, und die haben mir nicht wirklich gefallen."
    yan "Aber... was soll das denn plötzlich?"
    "Ich muss sie ablenken..."
    b "Lucky Star wird erst nach der vierten Folge richtig gut!"
    yan "%(berndName)s?"
    "Wenn ich einfach weiter rede, kann sie gar nicht anders, als mir zuzuhören."
    "Dann habe ich sie, wo ich sie haben will."
    b "Die ersten vier Folgen sind ziemlich schlecht und langweilig."
    b "Danach wird es besser."
    b "Du solltest unbedingt weiterschauen."
    yan "%(berndName)s...?"
    "Ich weiß genau, wie solche Leute drauf sind."
    "Das habe ich mal in einem Anime gesehen."
    "Man muss nur ein wenig dominant sein, und sie tun alles, was man von ihnen will."
    b "Ich habe eine Idee!"
    b "Warum schauen wir es nicht jetzt?"
    yan "...jetzt?"
    b "Ja."
    yan "Sofort?"
    b "Ja."
    yan "..."
    b "Willst du Folge eins und zwei noch mal sehen, oder überspringen wir die?"
    show bg keller
    with dissolve
    "Ich öffne meinen Animeordner und suche das entsprechene Unterverzeichnis."
    yan "..."
    b "Was nun?"
    yan "...ich möchte sie noch mal sehen."
    yan "Es ist schon etwas her."
    "Ja!"
    "Mission erfolgreich!"
    "Jetzt habe ich sie."
    b "Gut!"
    "Mit einem Doppelklick starte ich die erste Folge von Lucky Star."
    #stop music fadeout 0.5
    "Ich setze mich auf's Bett und genieße den Vorspann."
    b "Jetzt steh da nicht so rum."
    b "Setz dich!"
    "Ich signalisiere ihr, dass sie sich hinsetzen soll."
    "Sie gehorcht ohne Widerworte."
    "Genau nach Plan."
    "..."
    "Moment mal!"
    "Ich war so sehr darin vertieft, sie dazu zu überreden, nicht zu gehen, dass ich gar nicht realisiert habe, in welcher Situation ich mich befinde."
    "Ich sitze mitten in der Nacht neben einem fremden Mädchen auf meinem Bett und wir sind am Anfang eines Animemarathons."
    "Ich schaue aus den Augenwinkeln zu ihr herüber."
    show yasmin stalker_happy
    with dissolve
    "Sie schaut lächelnd auf den Monitor und tippt mit den Finger im Takt zum Vorspann."
    "Ich rücke ein Stück weiter von ihr weg."
    "Zu viel menschliche Nähe kann für jemanden wie mich nicht gut sein."
    "...aber hauptsache sie ist noch da."
    "Irgendwie werde ich noch alles aus ihr rausquetschen."
    
    stop music fadeout 0.5
    
    scene black
    with fade
    
    $ renpy.pause(1.0)
    
    jump yasmin_zwei_derMorgenDanach

#---------------------------------------    
label yasmin_zwei_derMorgenDanach:
    
    scene bg keller
    with fade
    
    play music m_bernd
    
    b "Mhm..."
    "Nanu, wie spät ist es?"
    "Ist ja auch egal, ich bin sowieso noch müde, also kann ich mich ruhig wieder hinlegen."
    "Ich lasse meinen Kopf auf das Kissen fallen, und mache die Augen zu."
    
    scene black
    with fade
    
    "Irgendwas ist komisch."
    "Aber was?"
    
    scene bg keller
    show yasmin happy
    with fade
    
    play music m_yasmin fadein 0.2
    
    yan "Guten Morgen, %(berndName)s."
    b "Oh, guten Morgen, %(yanName)s."
    "..."
    b "W-w-w-w-as machst du hier?!"
    "%(yanName)s sitzt neben mir im Bett."
    "Wieso sitzt sie da?"
    
    show yasmin embarrassed
    with dissolve
    
    yan "Aber..."
    yan "...erinnerst du dich nicht mehr?"
    b "Woran sollte ich mich... {w}Oh."
    "Ich erinnere mich tatsächlich an etwas."
    "Wir haben die ganze Nacht Lucky Star geguckt."
    "Wieso habe ich mich auf so was eingelassen?"
    b "Wie lange haben wir gestern geguckt?"
    
    show yasmin happy
    with dissolve
    
    yan "Bis Folge 9."
    "Folge 9."
    "Das sind fast fünf Stunden."
    b "Und dann?"
    yan "Wir sind wohl eingeschlafen."
    "Verständlich."
    "Es war wahrscheinlich ein harter Tag für uns beide."
    "Kein Wunder, dass wir dann irgendwann eingeschla-"
    "Wir sind zusammen eingeschlafen."
    "Ich erinnere mich wieder."
    "Ihre Augen sind langsam zugefallen, und bevor ich was machen konnte, lag sie neben mir im Bett."
    "In meinem Bett."
    "Ein Mädchen."
    "Das ist fast wie Sex."
    "..."
    "Heißt das, ich habe die ganze Nacht mit ihr im Bett gelegen...?!"
    "...was sonst?"
    "..."
    "Ich habe die ganze Nacht neben einem Mädchen geschlafen."
    "Und jetzt?"
    yan "Ich muss mal kurz nach oben..."
    b "Was?"
    "Will sie nun doch endlich abhauen?"
    show yasmin shy
    with dissolve
    yan "Na... du weißt schon..."
    yan "Ich müsste eben mal... nach oben."
    "Hä?"
    b "Was denn?"
    show yasmin embarrassed
    with dissolve
    yan "Naja, ich muss eben mal... {w=1}für kleine Mädchen."
    "Oh, jetzt verstehe ich, was sie meint."
    "Drücken sich alle Frauen so umständlich aus?"
    b "Ja, äh..."
    b "...du kennst dich aus, oder... {w}muss ich dir den Weg zeigen?"
    show yasmin smile
    with dissolve
    yan "Nein, nein. Ich find es schon."
    hide yasmin smile
    with dissolve
    "..."
    "Jetzt ist sie weg."
    "Das ist gut."
    "Ich kann nun in Ruhe überlegen, wie ich weiter verfahren soll."
    "Sie kann auf keinen Fall bleiben."
    "Nachher sieht sie noch jemand."
    "...!"
    "Ist es nicht gefährlich, sie nach oben gehen zu lassen?"
    "Was ist, wenn jemand anders sie sieht?"
    "...andererseits wird sie schon aufpassen, oder?"
    "Und wenn."
    "Ich wäre sie los."
    "Hätte ich nicht wirklich ein Problem mit."
    "Im Gegenteil."
    "Ich kann sie ja auf keinen Fall hier unten verstecken."
    "Außerdem muss sie ja sicher auch mal nach Hause."
    "Ich muss sie also irgendwie davon überzeugen, zu gehen."
    "Aber wie mache ich das?"
    "Ich kann ihr ja nicht einfach sagen, dass sie abhauen soll."
    "...oder?"
    menu:
        "Ich muss es ihr irgendwie nett sagen.":
            "Ich will sie nicht kränken."
            "Auch wenn ich sie gar nicht kenne."
            "So was tut man einfach nicht."
            "Ich muss mir also am Besten irgendwie überlegen, wie ich sie möglichst taktvoll abwimmeln kann, ohne dass sie sich verletzt fühlt."
            "...aber wie?"
            '"Hey, ich muss gleich los, also solltest du besser gehen."'
            "...nein."
            "Das wird sie mir nicht abnehmen."
            "Sie wird wissen wollen, wohin ich denn muss, und was soll ich da sagen?"
            "Schule?"
            "Training?"
            "Nicht um die Uhrzeit."
            "...und nachher will sie dann mitkommen oder so."
            "Nein, das geht nicht."
            "..."
            '"Ich glaube du solltest lieber gehen, bevor dich noch jemand sieht."'
            "Das könnte klappen."
            "Wenn das kein Grund ist..."
            "OK, das wäre geschafft."
            "Ich muss also nur noch warten, bis sie wieder da ist, dann sage ich es ihr."
            "Ich lasse mich auf's Kissen fallen und warte ab."
            "Es ist ganz warm."
            "Ich rolle mich ein Stück weiter dorthin, wo sie gelegen hat."
            "Auch warm."
            "..."
            "Es fühlt sich genau so an, wie auf meiner Seite, aber doch irgendwie anders."
            "Ich rolle mich abwechselnd vor und zurück."
            "Irgendwas ist anders, aber ich kann nicht sagen, was es ist."
            "..."
            "Wieso denke ich über so was nach?"
            "So ein Schwachsinn!"
            "...trotzdem bleibe ich am Ende auf \"ihrer\" Seite liegen."
            
        "Ich sag es so, wie es ist!":
            "Was interessiert mich, was sie denkt?"
            "Ich werde ihr einfach ins Gesicht sagen, was ich denke."
            '"Hau ab und lass mich in Ruhe!"'
            "Sie wird gehen und ich werde wieder meine Ruhe haben."
            "Endlich."
            "Sie hat mir nur Ärger bereitet."
            "...und ich weiß immer noch nicht, warum."
            "Das ist ganz schön frustrierend."
            "Ich vergrabe den Kopf im Kissen und warte ab."
            
        
    scene black
    with fade
    
    scene bg keller
    with fade
    
    "Wieso braucht sie denn so lange?"
    "Hat sie es doch nicht gefunden?"
    "Oder ist sie vielleicht doch abgehauen?"
    "Das wäre vielleicht gar nicht so schlecht."
    "Vielleicht kehrt dann endlich mein normaler Tagesablauf wieder zurück."
    "In diesem Moment höre ich die Tür aufgehen."
    "Jetzt muss ich es ihr sagen."
    "Ich richte mich auf und..."
    show yasmin happy
    with dissolve
    "...vor mir steht %(yanName)s."
    "In den Händen trägt sie ein Tablett."
    "Der sonst muffige Keller füllt sich mit dem Geruch frischer Brötchen."
    yan "Ich hab uns Frühstück gemacht."
    #KAWAII! (''° ω°)
    #Yasmin ist Bernds waifu!!
    b "..."
    #fragezeichenmächen
    yan "Hast du etwa keinen Hunger?"
    b "D-Doch."
    b "Ich habe nur nicht damit gerechnet."
    "Sie stellt das Tablett auf die Matratze und hockt sich neben mich."
    "Belegte Brötchen mit Käse, Wurst, Salat, Gurke, Tomate..."
    "Sogar Rührei hat sie gemacht."
    yan "Guten Appetit!"
    b "G-Guten Appetit..."
    "Sie nimmt sich ein Brötchen mit Käse und beißt hinein."
    "Ich nehme mir ein Wurstbrötchen."
    "Eine Weile sitzen wir kauend und schweigend nebeneinander."
    "Ich traue mich nicht, etwas zu sagen."
    "Ihr geht es sicher genauso."
    "Ich denke noch einmal über das nach, was geschehen ist."
    "In der Hoffnung, dass alles am Ende irgendwie Sinn ergibt, gehe ich in Gedanken die Ereignisse der letzten Tage immer und immer wieder durch."
    "Am Ende bin ich nicht schlauer als zuvor."
    "..."
    "Wir haben nun seit einigen Minuten kein Wort mehr gewechselt."
    "Sie sitzt einfach schweigend da und sieht mich an."
    "Wenn ich mich zu ihr drehe, wendet sie den Blick ab."
    "Irgendwie muss ich es ihr jetzt sagen."
    "Wenn ich noch länger warte, überlege ich es mir vielleicht."
    "Ich atme tief durch."
    stop music fadeout 0.5
    "Also jetzt oder nie!"
    show yasmin neutral
    with dissolve
    yan "%(berndName)s."
    yan "Ich weiß, was du mir sagen willst."
    b "Ich..."
    yan "Lass mich ausreden."
    yan "Du willst mir sagen, dass ich gehen soll."
    yan "Du verstehst nicht, warum ich überhaupt hier bin."
    yan "Du möchtest, dass alles wieder so wird wie vorher."
    yan "Du glaubst, ich wäre verrückt.{w} Vielleicht hast du sogar recht."
    yan "Du hasst mich."
    yan "Aber..."
    yan "Es gibt eine ganz simple Erklärung für alles."
    yan "Ich..."
    
    play sound "sounds/hit_1.wav"
    
    scene bg keller
    show yasmin neutral
    with vpunch

    
    show laura neutral at Position(xpos=0.0,xanchor="right")
    with None
    
    show yasmin surprised at right
    show laura happy at left
    with move
    
    play music m_laura
    
    sis "Hey, %(berndName)s!"
    "Oh, verflucht!"
    "Wie immer platzt sie genau dann rein, wenn es den meisten Schaden anrichtet."
    
    show laura neutral at left
    with dissolve
    
    sis "Nanu?"
    sis "Wer ist das?"
    sis "Deine Freundin?"
    
    show laura neutral at center
    with move
    show yasmin embarrassed at rightedge
    with fastMove
    
    "Blitzschnell weicht sie aus und versteckt sich hinter meinem Rücken."
    
    show laura happy
    with dissolve
    
    sis "Oh, sie ist schüchtern!"
    sis "Bist du %(berndName)ss Freundin?"
    sis "Wie heißt du?"
    
    yan "..."
    
    "Die Situation ist außer Kontrolle geraten."
    "Ich muss eingreifen."
    
    b "%(sisName)s..."
    sis "Hm...?"
    b "Könntest du eventuell... {w}gehen?"
    
    show laura surprised
    with dissolve
    
    sis "..."
    
    show laura happy
    with dissolve
    
    sis "Verstehe schon."
    sis "Ihr zwei wollt alleine sein."
    sis "Keine Sorge, ich erzähle es niemandem, wenn es dir peinlich ist."
    sis "Viel Spaß noch euch beiden."
    
    hide laura happy
    with dissolve
    
    b "..."
    "Sie hat es völlig falsch verstanden."
    "Aber Hauptsache sie ist weg."
    
    show yasmin embarrassed at center
    with move
    
    yan "...ich sollte lieber gehen."
    "Sie ergibt zum ersten Mal Sinn."
    "Aber sie wollte mir doch eben noch irgendwas sagen, bevor %(sisName)s hier reingestürmt ist."
    b "Willst du nicht deinen Satz noch beenden?"
    b "\"Ich...\”?"
    yan "..."
    
    show yasmin smile
    with dissolve
    
    yan "Das erzähle ich dir ein anderes Mal."
    yan "Ich muss wirklich weg hier."
    "Sie nimmt ihren Mantel und wirft ihn sich über."
    
    show yasmin stalker_smile
    with dissolve
    
    b "Ein anderes Mal?"
    b "Warum sollte ich mich wieder mit dir treffen wollen?"
    
    show yasmin stalker_happy
    with dissolve
    
    yan "Wir haben noch 15 Folgen Lucky Star vor uns, schon vergessen?"
    b "..."
    "Mit diesen Worten dreht sie sich um und geht."
    
    hide yasmin stalker_happy
    with dissolve
    
    "Ich bleibe allein und verwirrt zurück."
    
    scene black
    with dissolve
    
    #OK HIER IST SCHLUSS
    jump ende
    
    jump drei_yasmin