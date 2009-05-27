
#--------------------------------------------------------------------------------------------------#
#Dieser kleine Codeabschnitt entscheidet, ob Bernd auf die Anja- oder die Laura-/Yasminroute kommt.#
#--------------------------------------------------------------------------------------------------#

label zwei:
    python:
        try:
            stalker
        except NameError:
            stalker = 0
    if(lauraRoute):
        if(stalker):
            jump zwei_laura_stalk_entscheid
        jump zwei_laura
    if(anjaRoute):
        jump anja_anfang
    else:
        jump bernd_anfang


  
#---------------------------------------------------------------------------------------------------------------#
#Folgende Szene tritt ein, wenn Bernd sich nie mit Anja getroffen hat und stattdessen von Yasmin verfolgt wurde.#
#---------------------------------------------------------------------------------------------------------------#

label zwei_laura_stalk_entscheid:
    #kurz nachdem KC offline ist
    scene bg keller_aus
    with fade
    
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
    "Es wird schon nichts schlimmes passieren..."
    "Hier unten ist es so dunkel, dass er sowieso nicht reingucken kann."
    "Mit diesem Gedanken schlafe ich ein."
    
    scene black
    with fade
    
    "Stimme" "%(berndName)s."
    "Stimme" "Wach auf!"
    "Ich öffne die Augen, in der Erwartung %(sisName)s oder meine Mutter zu sehen aber..."
    
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
    sis "Das bringt nicht."
    sis "Du wirst hier nicht rauskommen, wenn du nicht das tust, was ich von dir verlange."
    "Ich spüre wie mein Puls steigt."
    b "Mach mich los!"
    sis "Wie gesagt."
    sis "Du musst das tun, was ich sage."
    b "Und das wäre?"
    sis "Ich will, dass du mir zuhörst."
    sis "Ich möchte dir nur eine kleine Geschichte erzählen."
    menu:
        ""
        "In Ordnung. Ich höre zu.":
            #BUTTERGOTT
            #braucht noch dialog
            pass
        "Nein! Mach mich los!":
            sis "Du willst deiner Schwester nicht zuhören?"
            b "Nein!"
            sis "Schade."
            sis "Dann habe ich wohl keine andere Wahl."
            sis "Es tut mir Leid, %(berndName)s."
            #BUTTERGOTT
            #BILD von Laura mit Messer
    scene bg keller_aus
    with flash
    
    b "Was zum?!"
    "Durch das wenige Sonnenlicht, das durch mein Fenster fällt, geweckt, setze ich mich aufrecht aufs Bett."
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
    "Sowas löst sich ja nicht einfach so."
    "Außerdem ist sie viel zu kurz."
    "Merkwürdig."
    "Ich habe überhaupt nichts, wo solche Schrauben drin sind."
    "Zumindest kann ich mich an nichts erinnern."
    "Es steht auch nichts drauf."
    "Sehr merkwürdig."
    play sound "sounds/error.wav"
    "Oh."
    "Eine Fehlermeldung?"
    "Achso, nur eine E-Mail."
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
            "Eine Woche später..."
            scene gameover_vierkanal
            with fade
            $ renpy.pause()
            jump ende

        "Ich gehe auf irgendeine Website.":
            "Auf welche Website geht man denn, wenn man Informationen sucht?"
            "Erschrocken stelle ich fest, dass ich das eigentlich noch nie gemacht habe."
            "Obwohl ich mal irgendwann gelernt habe, dass das Internet als weltweites Informationsnetzwerk gedacht ist..."
            "...habe ich es eigentlich immer nur zum Download von Pornos und illegalen Spielen und Filmen benutzt."
            "Naja... was solls."
            "Google hat mich noch nie im Stich gelassen."
            "Nur was gebe ich ein?"
            "..."
            "\"Krautchan offline\""
            "..."
            "Das war nichts."
            "Dafür bietet mir Google einen kostenlosen E-Mail-Zugang an."
            "Wer hat schon seine E-Mail bei Google?"
            "..."
            
            jump zwei_email_erinnerung
            
        "Ich warte einfach ab.":
            "Frustriert werfe ich mich auf die Matratze und starre die Decke an."
            "Ist Krautchan wirklich untergegangen?"
            "Dann hatte der Bernd, der mir die Mail geschickt hat, recht."
            "..."
            
            jump zwei_email_erinnerung



#----------------------------------------------------------------------------#
#Dieser Abschnitt tritt auf wenn Bernd abwartet oder im Internet sucht.------#
#Er stellt einen möglichen Übergang zur Anjaroute dar, sollte Bernd annehmen.#
#----------------------------------------------------------------------------#

label zwei_email_erinnerung:
    "Die E-Mail!"
    "Sofort stürze ich an meinen Rechner und öffne meine alten Mails."
    
    scene bg desktop_hilfe
    with dissolve
    
    "Die ist von ???."
    "Wenn die tatsächlich ernst gemeint ist..."
    "...sollte ich..."
    "...vielleicht..."
    "...antworten?"
    
    if lauraRoute :
        jump laura_anja_mail_vonLaura
    else:
        "blablabla"
        pass
    
    menu:
        ""
        "Ich sollte eine Antwort schreiben.":
          
            jump laura_anja_mail
            pass
            
        "Ich werde sie einfach ignorieren.":
            
            jump zwei_weiter_entscheid
            pass

 
label laura_anja_mail:
    "Ich klicke auf \"Antworten\"."
    
    scene bg desktop_mail_leer
    with dissolve
    #Bild existiert noch nicht
    
    "OK."
    "Aber was schreibe ich?"
    
    menu:
        "Ich konnte gestern nicht kommen, weil ..."
                
        "...ich bei meiner Freundin war.":
            "Ich konnte gestern nicht kommen, weil ich bei meiner Freundin war."
            "Das wird Bernd mir auf keinen Fall glauben."
            "Ein Wieherbuh und eine Freundin?"
            "Ein Bernd und eine Freundin?"
            "ICH und eine Freundin?"
            "Das ist einfach zu unrealistisch."
            
        "...meine Katze AIDS hat.":
            "Ich konnte gestern nicht kommen, weil meine Katze AIDS hat."
            "Oh wow."
            "Und mein Hund hat dazu noch die Hausaufgaben gefressen."
            "Außerdem standen meine Sterne in einem schlechten Winkel."
            "Ich konnte einfach nicht kommen."
            
        "...Globalisierung.":
            "Ich konnte gestern nicht kommen, weil Globalisierung."
            "Ich lass das einfach mal so stehen."
            
            
#GSB GSB GSB
#Bernd bekam eine zweite Mail -> Wechsel auf Anja-Route

#--------------------------------------------------------------------------#
#Dieser Abschnitt beinhaltet den Teil von Kapitel 2, bei dem sich Bernd für#
#Laura oder Yasmin entscheiden muss, und tritt auf, wenn man nicht auf die-#
#E-Mail eingeht.-----------------------------------------------------------#
#--------------------------------------------------------------------------#

label zwei_weiter_entscheid:
    
    #Die drei Werte:
    $ zwei_entschuldigt = 0

    "Das ist doch sowieso nur ein Troll gewesen."
    "Wie hätte den jemand vorher wissen sollen, dass Krautchan offline gehen würde?"
    "Damit hat ja niemand gerechnet."
    "...und warum direkt an mich wenden?"
    "Man könnte auch einfach einen Thread drüber aufmachen."
    "Schlecht getrollt, Bernd."
    scene bg keller
    with dissolve
    "Gelangweilt setze ich mich wieder auf mein Bett."
    "Gibt es denn wirklich nichts, was ich tun kann?"
    "Vielleicht sollte ich raus und ein bisschen frische Luft schnappen..."
    "Eine Runde um den Block zu gehen wird mir gut tun."
    scene bg zuhause_draussen
    with fade
    "Ich verlasse das Haus und gehe um die Ecke."
    "Hier habe ich Stalkerbernd getroffen."
    "Mein Blick wandert nach unten zu meinem Kellerfenster."
    "Man kann nichts sehen."
    "Das Gitter ist zu dicht."
    "Ich bücke mich runter und sehe durch das Gitter, aber auch so sieht man nicht viel."
    "Zufrieden stehe ich auf und gehe weiter."
    "Stalkerbernd kann mich drinnen nicht gesehen haben."
    "Er hatte ja kein Nachtsichtgerät oder sowas."
    "Ich biege um die Ecke."
    "Um irgendetwas persönliches von mir zu bekommen, müsste er schon einbrechen."
    "Moment mal...!"
    "Ich renne zurück zum Fenster und bücke mich runter."
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
    "Wohlmöglich haben sie ihn heute Nacht erwischt und er hat sie niedergeschlagen oder sonstwas mit ihnen angestellt?!"
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
    sis "Ja?"
    b "Hi, %(sisName)s. Ich bin es."
    sis "%(berndName)s?"
    b "Ja."
    b "Wo bist du?"
    sis "Im Unterricht! Wieso rufst du mich an?!"
    sis "Mein Lehrer hat mich vor die Tür geschickt, weil das Handy geklingelt hat."
    sis "Ist es so wichtig?"
    "Scheiße."
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
    "Zuhause ist sie nicht."
    "Einkaufen?"
    "Es ist 10:30 Uhr."
    "Ich bin um 10 Uhr aufgestanden, also ist sie schon mindestens eine halbe Stunde weg."
    "So lange braucht sie sonst nie."
    "In diesem Moment öffnet sich die Wohnungstür."
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
    scene black
    with fade
    "Eine halbe Stunde später klingelte das Telefon."
    "Anscheinend hatte %(sisName)s in der Schule ziemlichen Ärger bekommen, als ich sie angerufen habe."
    "Jetzt musste sie jemand abholen, und dieser jemand war ich."
    scene bg schulweg1
    with fade
    show laura angry
    with dissolve
    "Ich bin also mit %(sisName)s im Schlepptau auf dem Rückweg von der Schule nach Hause."
    "Bisher haben wir kein Wort gesprochen."
    "Anscheinend ist sie ziemlich sauer."
    "Kein Wunder."
    "Meinetwegen wurde sie für eine Woche von der Schule suspendiert."
    "Wir sind schon fast zuhause."
    scene bg zuhause_draussen
    with fade
    show laura angry
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
            show laura angry_talk
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
            sis "Oh!"
            sis "Das ist meine Freundin."
            sis "Wir wollten uns ja heute treffen."
            sis "Ich geh schon mal nach Hause vor, %(berndName)s!"
            b "Wie du meinst."
            hide laura happy
            with dissolve
            "Wahrscheinlich würde sie zuhause alles erzählen."
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
    "%(sisName)s hat natürlich schon alles erklärt."
    b "...und?"
    b "Hat sie dir alles erzählt?"
    ma "Ja."
    ma "...und ich finde es unerhört, jemandem einfach so im Unterricht anzurufen!"
    "Jetzt gehts los."
    ma "...wie kann man sowas nur machen?"
    ma "Ist doch klar, dass das Ärger gibt!"
    if(zwei_entschuldigt): #wenn bernd sich entschuldigt hat
        ma "...und sowas nennt sich Freundin."
        "Freundin?"
        b "Was meinst du...?"
        b "Freundin?"
        "Fragend sieht mich meine Mutter an."
        "Ich schau zu %(sisName)s, aber sie grinst nur und nickt mir zu."
        b "Achja!"
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
        ma "...und sowas nennt sich Bruder."
        ma "Ich bin enttäuscht, %(berndName)s!"
        ma "Du hattest ja nicht einmal einen richtigen Grund!"
        ma "Du solltest dich wirklich schämen!"
        "Das Gequatsche halte ich nicht mehr aus."
        "Ich ignoriere sie und verziehe mich in meinen Keller."
    scene black
    with wooshTrans
    scene bg keller
    with wooshTrans
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
    "Meine Schwester hat anscheinend Freunde und sowas."
    "...aber sie geht ja auch zur Schule."
    "Da findet man leicht nette Menschen."
    "Wenn ich mich an meine Schulzeit erinnere..."
    "...fällt mir auf, dass ich selbst damals keine Freunde hatte."
    b "Scheiße."
    "Vielleicht ist ja inzwischen das Essen fertig."
    "Ich gehe am besten hoch und frage wie lange es noch dauert."
    scene bg wohnung_innen
    with fade
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
    "Dafür ist es zuhause viel zu bequem."
    ma "Du kannst nicht ewig von Hartz IV leben, %(berndName)s."
    ma "Willst du denn nicht..."
    ma "...ach vergiss es."
    ma "Essen wir lieber."
    scene black
    with fade
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
    "Mein Password ist so siche-"
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
            jump yasmin_anfang
        "Nein, ich warte nur noch ein bisschen...":
            "Ich sollte wirklich nicht unüberlegt handeln."
            "Vielleicht sollte ich doch versuchen, mich ein wenig zu bewegen?"
            "Nur ein kleines Stück den Kopf drehen, damit ich den Monitor sehen kann."
            "Vielleicht durchsucht er meine Dateien, oder installiert irgendeinen Virus?"
            "Plötzlich holt er einen kleinen Kasten unter dem Mantel hervor."
            "Eine Externe Festplatte, die er per USB anschließt."
            "Ich nutze den kurzen Moment, um mich ein wenig zu drehen, so dass ich den Monitor sehen kann."
            "Er macht ein Backup meiner Daten, um dann zuhause alles in Ruhe durchzugehen."
            "Clever."
            "Wenn ich daran denke, dass er zuhause in Seelenruhe durch meine persönlichsten Informationen stöbert..."
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
            "Er hat mich bemerkt und wird mich umbringen oder sowas."
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
            jump zwei_laura