label zwei_laura_anfang:
    "Immer noch starre ich ungläubig auf den Monitor."
    "...Krautchan ist wirklich offline?"
    "Immer und immer wieder drücke ich auf den Refresh-Button, aber das Ergebnis bleibt gleich."
    "404."
    "Frustriert werfe ich mich auf's Bett."
    "Krautchan ist erst seit ein paar Minuten offline, und mir ist jetzt schon langweilig."
    "...ob die Admins wieder nur trollen?"
    "Das wird es sein."
    "Wenn ich morgen früh aufwache, ist alles wieder so wie früher."
    "Mit diesem Gedanken schlafe ich ein."
    
    $ renpy.music.set_volume(0.0, .5, channel="music")
    
    scene black
    with fade
    
    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    "Am nächsten Morgen war Krautchan noch immer nicht zu erreichen."
    
    scene bg keller
    with fade
    
    "...wenn das ein Trollversuch sein soll, ist es nicht lustig."
    "Leute wie ich..."
    "...wir brauchen Krautchan einfach!"
    "Was soll ich denn jetzt den ganzen Tag machen?"
    "Mir bleibt wohl nichts übrig als abzuwarten."
    "Das wird ein mieser Tag, wenn ich jetzt schon schlecht gelaunt bin."
    "Ich werde einfach in einer Stunde wieder nachsehen."
    "Es ist jetzt kurz vor neun, also habe ich bis zehn Uhr nichts zu tun."
    b "..."
    "Naja, vielleicht gibt es schon Frühstück."
    "Ich gehe mal hoch und schaue nach."
    
    scene bg kueche
    with fade
    
    play music m_wohnung
    
    "Meine Mutter sitzt natürlich schon in der Küche und trinkt ihren Kaffee."
    ma "So früh schon wach, %(berndName)s?"
    ma "Du schläfst doch sonst immer bis eins."
    "Haha, wie lustig."
    b "Weniger dumme Kommentare, mehr Frühstück machen."
    ma "Schlecht gelaunt?"
    b "Meh."
    "\"Schlecht gelaunt?\""
    "Was soll diese dumme Frage?"
    "Sieht man das nicht?"
    ma "Wenn du so mit mir redest, kannst du dir dein Frühstück selbst machen."
    "War ja klar."
    "Missmutig nehme ich Wurst und Käse aus dem Kühlschrank und mache mir zwei Scheiben Toast."
    ma "Magst du deiner Schwester gleich einen Tee bringen?"
    b "Wieso sollte ich?"
    b "Müsste die nicht in der Schule sein?"
    "...oder ist heute schon wieder Samstag?"
    "Wenn man keinen geregelten Tagesablauf hat, vergisst man das schnell."
    ma "Ja, müsste sie."
    b "...aber dort ist sie nicht?"
    "Ich soll ihr wohl kaum Tee in die Schule bringen."
    ma "Nein, ist sie nicht."
    b "Und warum, wenn ich fragen darf?"
    ma "Sie fühlt sich nicht gut."
    ma "Ich glaube, sie ist erkältet, oder so."
    "Erkältet?"
    "So kalt ist es draußen doch gar nicht."
    b "Wenn die mal nicht nur simuliert..."
    ma "Das musst du gerade sagen."
    ma "Du hast früher immer simuliert, weil du nicht zur Schule wolltest."
    "Da hat sie auch wieder Recht."
    ma "Also bringst du ihr nun ihren Tee, oder muss ich das machen?"
    
    menu: #Entscheidet ob Anja oder Laura
        "Nein, ich mach es schon.":
            $ sisLove += 10
            b "Nein, ich mach es schon."
            ma "Gut."
            ma "Die Tasse steht da."
            jump zwei_laura_tee
       
        "Wieso sollte ich denn?":
            $ sisLove -= 10
            b "Wieso sollte ich denn?"
            ma "Na dann halt nicht."
            jump zwei_laura_keinTee

label zwei_laura_tee:            
    b "Ich darf ja wohl erst meinen Toast essen, oder?"
    ma "Nein, dann wird der Tee kalt."
    "Ich stopfe mir schnell den Rest der ersten Scheibe in den Mund und lasse die zweite liegen."
    "Mit der Teetasse in der Hand, gehe ich in %(sisName)ss Zimmer."
    
    scene bg lauraszimmer
    with fade
    
    play music m_krank fadein 0.2
    
    b "Hey, %(sisName)s."
    b "Bist du wach?"
    b "Ich habe dir Tee gebracht."
    b "..."
    "Anscheinend schläft sie, denn ich bekomme keine Antwort."
    "In ihrem Bett liegt nur eine zusammengeknüllte Bettdecke."
    "Wahrscheinlich hat sie sich irgendwo darin verkrochen und schläft noch seelenruhig."
    "Ich stelle ihr den Tee neben das Bett und will gehen als..."
    
    #laura verschlafen und kränklich
    
    sis "...%(berndName)s?"
    "Sie ist wach."
    b "Habe ich dich geweckt?"
    sis "Nein, schon ok."
    "Sie lügt."
    "Natürlich habe ich sie geweckt."
    sis "Danke für den Tee."
    b "Bedank dich bei deiner Mutter."
    b "Sie hat ihn gemacht."
    sis "Aber du hast ihn mir gebracht, also muss ich mich auch bei dir bedanken."
    b "Ja ja, schon gut."
    "Sie nimmt einen Schluck vom Tee."
    "Anscheinend ist sie tatsächlich krank."
    "Sie ist ziemlich blass."
    b "Wie geht's dir?"
    sis "Schon viel besser!"
    sis "Ich glaube, ich kann schon wieder aufstehen."
    ma "Nichts da!"
    "Meine Mutter schaut mir über die Schulter."
    ma "Du bleibst heute im Bett!"
    sis "Aber...!"
    ma "Nichts \"Aber...!\"!"
    ma "Du bleibst im Bett!"
    sis "Ich bekomme doch heute Besuch!"
    sis "Da kann ich nicht im Bett liegen bleiben!"
    ma "Dann musst du das absagen."
    sis "Nein!"
    ma "Dann mache ich es halt."
    sis "NEIN!"
    sis "Ich will heute Besuch kriegen!"
    ma "Man kann nicht immer alles bekommen, was man will."
    ma "Ich rufe jetzt deine Freundin an und sage ab."
    
    b "Wie wäre es, wenn du damit noch wartest?"
    "Meine Mutter schaut verwirrt, weil ich mich sonst nie einmische."
    b "Vielleicht geht es ihr ja wirklich besser, wenn sie den Tee getrunken hat."
    sis "Ja, genau!"
    sis "%(berndName)s hat recht!"
    ma "OK, OK."
    ma "Aber wenn es dir nicht besser geht, sage ich ab!"
    ma "Und bis dahin, bleibst du im Bett liegen!"
    sis "In Ordnung!"
    ma "Und deck dich gut zu."
    sis "Ja, Mama."
    "Zufrieden verlässt meine Mutter das Zimmer."
    sis "Danke, %(berndName)s."
    b "Schon ok."
    b "Sieh nur zu, dass es dir wieder besser geht, sonst kannst du dich nicht mit deiner Freundin treffen."
    sis "OK!"
    "Ich sollte langsam zurück nach unten."
    "Krautchan ist sicher schon wieder online."
    "Aber vorher gehe ich in die Küche und hole mir meine andere Scheibe Toastbrot."
    
    play music m_wohnung fadein 0.6
    
    jump zwei_laura_medizinBekommen
   
   
label zwei_laura_keinTee:
    "Ich schnappe mir mein zweites Toastbrot und gehe wieder runter."
    
    $ renpy.music.set_volume(0.0, .5, channel="music")
    
    scene bg keller
    with fade
    
    "Krautchan ist immer noch off."
    "Langsam wird mir das zu bunt."
    "Irgendwie habe ich noch immer Hunger..."
    "...ich gehe mir lieber noch was holen."
    
    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    jump zwei_laura_medizinBekommen


label zwei_laura_medizinBekommen:
    
    scene bg kueche
    with gradientTrans
    
    #mutter
    ma "Oh, %(berndName)s!"
    ma "Du, ich muss ganz schnell weg, es ist dringend."
    ma "Schau ab und zu nach %(sisName)s und gib ihr was hiervon."
    "Sie drückt mir eine Pappschachtel in die Hand und verschwindet."
    "Wieso hat sie es denn so eilig?"
    "Und was meint sie mit \"gib %(sisName)s etwas hiervon\"?"
    "Ich sehe mir die Packung genauer an."
    "Es ist irgendeine Medizin gegen Husten."
    "Ist das ein Saft oder so?"
    "Ich nehme die Packungsbeilage aus dem Karton und überfliege sie schnell."
    "Da steht es."
    "Anwendung: Die Salbe bei Erwachsenen und Kindern ab 6 Jahren auf Brust, Hals und Rücken auftragen und 3-5 Minuten sorgfältig leicht massierend verreiben."
    "..."
    "Was zum...!?"
    "Ich soll %(sisName)s..."
    "...einreiben?"
    "Das bringe ich nie fertig!"
    "Ich hab noch nie ein Mädchen angefasst."
    "Jedenfalls nicht so..."
    "Was soll ich jetzt machen?"
    "Soll ich es einfach tun...?"
    "Wäre vielleicht gar nicht so schlecht...?"
    "Höhöhö hö..."
    "Schwachsinn!"
    "Soll ich einfach runtergehen, und sagen, dass ich es vergessen habe?"
    "Das wäre die beste Idee."
    "Andererseits ist %(sisName)s wirklich krank."
    "Sie ist immerhin meine Schwester."
    #entscheidung abhängig von sisLove aaaaaaw :3
    #entscheidung außerdem abhängig davon, ob H-szenen aktiv sind
    #$ sisLove = 70 #test
  
    #if sisLove < 60 or hentaiEin == False:
    jump zwei_laura_nichtMedizin
    "Ja."
    "Sie ist nur meine Schwester."
    "Es ist überhaupt nichts dabei."
    "..."
    "Ich werde es einfach tun."
    "Schließlich muss ich ihr ja nur die Brust einreiben."
    "Ist ja nicht so, als würde ich irgendwas anderes mit ihr machen."
    "Schließlich ist sie meine Schwester."


#---------------------------------------------------------------
#Stepmania Stepmania Stepmania

    scene bg lauraszimmer
    with gradientTransReverse
    
    play music m_krank fadein 0.2
    
    b "Bist du wach, %(sisName)s?"
    #kranke laura
    sis "Mhm..."
    sis "Was ist denn, %(berndName)s?"
    "Sie sieht wirklich sehr krank aus."
    "Ich muss da jetzt durch."
    b "Geht es dir schon wieder besser?"
    sis "Hm..."
    sis "Ja, ein Bisschen."
    sis "Der Tee hat geholfen."
    b "Ah, das ist gut."
    "...dann muss ich vielleicht gar nicht..."
    sis "Ich glaube, ich kann schon wieder aufstehen."
    b "Ich denke nicht, dass du..."
    "Zu spät."
    "Sie ist schon aus dem Bett geklettert."
    
    show laura happy
    with dissolve
    #Bild mit Pyjama?
    
    sis "Siehst du?"
    sis "Alles kein Probl-"
    
    scene bg lauraszimmer
    with vpunch
    
    play sound "sounds/hit_1.wav"
    
    b "%(sisName)s!"
    "Schnell bücke ich mich zu ihr runter."
    b "Alles ok?"
    sis "Mhm..."
    sis "Mein Kopf."
    b "Hast du dich gestoßen?"
    b "Tut es weh?"
    sis "Nein..."
    sis "Es dreht sich alles."
    b "Leg dich lieber wieder ins Bett."
    b "Komm ich helfe dir."
    "Ich nehme sie hoch und lege sie auf ihr Bett."
    "Sie ist ganz leicht, selbst für jemanden wie mich, der kaum Muskeln hat."
    "Was ist nur in mich gefahren?"
    "Ich bin in letzter Zeit so nett zu ihr..."
    "Aber irgendwie kann ich nicht anders."
    "Sie hat außer mir und Mama niemanden."
    "Daher muss ich sie beschützen."
    b "Ma-"
    b "Mama hat mir... Salbe gegeben... gegen Erkältung, und ich..."
    b "Also... darf ich..."
    b "...soll ich dich..."
    "Scheiße."
    "Klar denken!"
    b "...soll ich dich einreiben?"
    "..."
    sis "Werde ich dann wieder gesund?"
    b "Ja."
    b "Ganz sicher."
    sis "Bis heute Nachmittag?"
    "Was soll ich dazu sagen?"
    "Das ist wohl eher unwahrscheinlich."
    "Aber..."
    b "Naja... ich kann es nicht sagen."
    b "Ich bin kein Arzt oder so."
    b "Aber es kann nicht schaden, oder?"
    sis "Hm..."
    sis "Dann ist es ok."
    "Oh man, was mache ich hier eigentlich?"
    "Ich bin kurz davor einem kleinen Mädchen die Brust zu streicheln."
    "Wahrscheinlich würde mich jeder andere Bernd darum beneiden, aber ich fühle mich alles andere als beneidenswert in meiner Situation."
    "Ich kann kaum die Dose aus der Packung nehmen, so sehr zittere ich."
    "Beruhig dich, %(berndName)s."
    "Sie ist deine Schwester."
    "Es ist nichts Schlimmes."
    "Ich gebe ihr nur Medizin, damit sie wieder gesund wird."
    "Ich bin einfach nur ihr netter, großer Bruder."
    "Nichts weiter."
    "..."
    
    "OK, jetzt geht es mir besser."
    "Wenigstens zittere ich nicht mehr so sehr."
    "Ich schraube den Deckel ab und gebe etwas von der Salbe auf meinen Finger."
    "..."
    b "Du..."
    b "Du musst schon deinen Schlafanzug aufmachen und dich hinlegen..."
    b "...sonst kann ich dich nicht einreiben."
    
    show laura surprised
    with dissolve
    
    sis "Äh..."
    sis "OK."
    "Sie legt sich auf den Rücken und öffnet langsam die Knöpfe ihres Schlafanzugs."
    "Der erste Knopf."    
    "Ich muss schlucken."
    "Ich hab doch noch nie ein nacktes Mädchen in der Realität gesehen."
    "Auf einem Bild, ja."
    "In einem Video, ja."
    "Auch in einem Hentai."
    "Aber in der Realität?"
    "Sie öffnet den zweiten Knopf."
    "Reiß dich zusammen, %(berndName)s."
    "Sie ist nur deine Schwester."
    sis "Geht's dir nicht gut, Bernd?"
    b "D-{w}Doch."
    b "Alles in Ordnung."
    sis "Ich kann das auch alleine machen, wenn du willst."
    b "N-Nein, das ist es nicht."
    sis "Wenn du meinst..."
    "Der dritte Knopf."
    "Nun sind alle Knöpfe offen."
    "In wenigen Sekunden liegt ein Mädchen vor mir. {w}In einem Bett. {w}Nackt."
    "Es ist zwar nur meine Schwester...{w}aber trotzdem ein Mädchen!"
    "Das ist das erste Mal, dass ich meine Schwester so sehe."
    sis "Sei ganz zärtlich, ok?"
    b "O-OK."
    "Ist das hier ein Eroge?"
    "Quatsch."
    "Aber ich fühle mich gerade wie ein Protagonist in einem Eroge."    
    
    scene cg laura_nackt
    with dissolve
    #auf CG wartend erst einmal:
    
    scene bg lauraszimmer
    with fade
    
    #show laura krank
    #with dissolve
    
    "Ich fahre mit vier Fingern meiner rechten Hand durch die Dose Vaporub."
    "Langsam führe ich meine Hand zu %(sisName)ss Brust."
    "Mir wird jetzt schon ganz anders."
    "Ich lege meine Hand sanft auf ihre Brust."
    "Sie zuckt etwas zusammen."
    
    #show laura krank geschlossene Augen nach oben gezogenene Schultern
    #with dissolve
    #bester Bildname jemals
    
    "Vor Schreck ziehe ich meine Hand zurück."
    
    #show laura krank
    #with dissolve
    
    sis "Nein...{w}du darfst weitermachen..."
    sis "Ich hab mich nur erschreckt, weil es so kalt ist, %(berndName)s."
    b "{size=6}O-O-O-OK.{/size}"
    sis "Hm? {w}Hast du was gesagt?"
    "Ich schüttel mit dem Kopf."
    "Ich trau mich noch nicht mal mehr richtig zu sprechen."
    "Ich lege meine rechte Hand wieder auf ihre Brust."
    "Sie zuckt wieder leicht zusammen."
    "Ich bewege meine Hand nach rechts."
    "%(sisName)ss Brust ist so warm."    
    "Dann lasse ich meine Hand nach links gleiten."
    "Und meine Hand ist kalt."
    "Das ist sicher unangenehm für sie."
    "Bald wird es ihr wieder besser gehen."
    "Es passt einfach nicht zu ihr im Bett zu liegen und nichts zu tun."
    "Es macht mich glücklich zu wissen, dass es %(sisName)s besse{nw}"
    sis "AUA!"
    sis "Du tust mir weh."

    #show laura nackt_pissed
    #with dissolve

    sis "Ich hab doch gesagt, dass du nicht so drücken sollst."
    b "Ent-Entschuldigung."
    "Das ist so falsch..."
    "Ich nehme noch ein bisschen Vaporub, um es dann auf ihrer Brust zu verteilen."
    
    $ renpy.pause(1.5)
    
    sis "Ha~."
    "Ich bin an ihre rechte Brustwarze gekommen."
    b "Ah...{w}T-t-tut mir l-lei-leid."
    sis "Was tut dir leid?"
    b "Äh...{w}ni-nichts."
    sis "Du bist komisch. {w}Anders als sonst. {w}Geht es dir wirklich gut?"
    b "J-ja, na-natürlich."
    "Ich bin gerade bestimmt knallrot."
    "Aber es ist nicht meine Schuld..."
    "...{w}hart...{w}es war hart."
    "Wenn ich nur daran denke..."
    "Lange halte ich das nicht mehr aus."
    "Wann sind die 5 Minuten endlich vorbei?"
    "Ich mache das doch jetzt schon eine Ewigkeit."
    
    $ renpy.pause (1.0)
    
    b "F-fer-fertig."
    b "D-du kannst dich wie-wieder anzie-hen."
    sis "OK."
    "Sie knöpft ihren Schlafanzug wieder zu."
    sis "%(berndName)s?"
    b "J-ja?"
    sis "Du hattest kalte Hände."
    sis "Bist du krank?"
    sis "Habe ich dich vielleicht angesteckt?"
    b "Nein!"
    sis "Geht es dir wirklich gut?"
    b "J-ja!"
    sis "OK."
        
    #show laura krank happy
    #with dissolve
    
    sis "Danke, %(berndName)s!"
    b "..."
    "Ich packe die Dose wieder in die Verpackung, stehe auf und gehe aus dem Zimmer."
    "Ich öffne die Türe und gehe in den Flur."
    
    scene bg wohnung_innen
    with fade
    
    sis "%(berndName)s?"
    "Was ist denn jetzt noch?"    
    
    scene bg lauraszimmer
    with fade
    
    b "Ja?"
    sis "Gute Nacht, %(berndName)s."
    b "Gute Nacht."
    "Ich schließe die Türe."
    
    scene bg wohnung_innen
    with fade
    
    #Bernd geht erstmal kalt duschen
    #das darfst du aber wieder schreiben, Step
    
    "Meine Knie geben zitternd nach und ich sinke vor der Tür zusammen."
    "Ich kann eigentlich nicht glauben, dass das wirklich passiert ist."
    "..."
    #diese szene brauchen wir doch eigentlich gar nicht, wieso schreibe ich hier grade?
    
#Stepmania Stepmania Stepmania
#---------------------------------------------------------------

    
label zwei_laura_nichtMedizin:
    "Unmöglich!"
    "Ich kann das einfach nicht..."
    "Ich sollte es einfach vergessen."
    "Am besten gehe ich wieder nach Unten."
    
    scene bg keller_aus
    with fade
    
    play music m_bernd
    
    "...ob ich es hätte machen sollen?"
    "Nein."
    "Das hätte ich sowieso nicht durchgezogen."
    "Ich sollte lieber mal nach Krautchan schauen."
    
    scene bg keller
    with dissolve
    
    play sound "sounds/boot.wav"
    
    "..."
    "Immer noch offline."
    "Was habe ich auch anderes erwartet."
    "Kann ich denn gar nichts tun?"
    "Ohne Krautchan ist das Leben langweilig."
    "Ich glaube, ich gehe erst mal duschen."
    
    scene bg wohnung_innen
    with fade
    
    play music m_wohnung
    
    "Vielleicht sollte ich doch mal bei Laura reinschauen..."
    "..."
    "...nein, lieber nicht."
    "Ich gehe jetzt erst mal duschen."
    
    scene bg badezimmer
    with fade
    
    play sound "sounds/dusche.wav"
    
    "Das tut gut."
    "Endlich habe ich mal einen Moment, um ruhig über alles nachzudenken."
    
    play sound "sounds/knock2.wav"
    
    $berndNameCaps = berndName.upper()
    ma "KOMM AUS DER DUSCHE RAUS, %(berndNameCaps)s!"
    "Oh, verflucht!"
    ma "ICH BIN WIEDER DA UND BRAUCH DICH MAL EBEN!"
    "Ich stelle das Wasser ab und steige aus der Dusche."
    b "Ich komme gleich!"
    "Schnell trockne ich mich ab und ziehe mich an."
    "Die kann was erleben."
    "Mich einfach so aus der Dusche zu holen..."
    "Ich öffne die Tür."
    ma "%(berndName)s!"
    ma "Hast du Laura ihre Medizin gegeben?"
    "Ich wusste es."
    b "Äh... nein."
    b "Habe ich vergessen."
    ma "Interessiert dich deine Schwester denn gar nicht?"
    b "Nicht wirklich."
    ma "War ja klar."
    ma "Dann gebe ich ihr die Medizin und du gehst zur Apotheke und besorgst das hier."
    "Sie drückt mir ein Rezept in die Hand."
    ma "Das habe ich grade vom Arzt geholt."
    ma "Laura braucht das."
    ma "Und jetzt geh."
    b "Darf ich wenigstens vorher..."
    ma "Nein!"
    ma "Du gehst."
    ma "Jetzt."
    "Naja, ich habe eh nichts anderes zu tun."
    "Vielleicht kann ich ja dabei einen klaren Gedanken fassen..."
    
    jump zwei_laura_medizinHolen
    
    
#nun noch ein Event mit Bernd und Laura und dann kommt general-chan zu Besuch! ^_^


label zwei_laura_medizinHolen:
    
    scene bg keller
    with fade
    
    "Ich hole mein Portemonnaie, {w}schaue rein {w}und stelle fest, dass ich kein Geld mehr habe."
    "Toll, jetzt muss ich erst noch nach Geld fragen."
    "Ich gehe in Lauras Zimmer."
    
    scene bg lauraszimmer
    with fade
    
    b "Mama?"

    #show mutter sauer #at left
    #with dissolve    

    ma "Was? {w}Du bist immer noch nicht weg?"
    b "Nein."

    #show laura krank at right
    #with dissolve
    
    #sis "%(berndName)s?"
    #sis "Bist du es?"
    #b "Ja."
    #"Ihr scheint es wirklich schlecht zu gehen."
    #ma "Sieh nur, was du angerichtet hast."
    #ma "Jetzt ist sie wieder wach."
    ma "Wieso bist du noch nicht weg?"
    b "Ich hab kein Geld."
    ma "Mensch, %(berndName)s."
    "Meine Mutter rennt an mir vorbei in die Küche."
    "Ich folge ihr."
    
    scene bg kueche
    with fade
    
    #show mutter sauer
    #with dissolve
    
    ma "Hier hast du 25 Euro."
    $ geld += 25
    ma "Und jetzt geh endlich."
    b "OK, OK. {w}Ich geh ja schon."
    "Meine Mutter spurtet zurück in %(sisName)ss Zimmer."
    "Nachdem ich die 25 Euro in mein Portemonnaie gesteckt habe, ziehe ich meine Jacke und meine Schuhe an."
    
    scene black
    with fade
    
    scene bg zuhause_draussen
    with fade
    
    "Wo ist jetzt eine Apotheke?"
    "Ich glaub, ich hab letztens eine gesehen."
    "Aber wo?"
    "Hmm...{w}so oft war ich ja nicht draußen..."
    "Das war als ich...{w}als ich %(sisName)s abholte."
    "Ich muss einfach nur ihren Schulweg gehen."
    
    scene bg schulweg1
    with fade
    
    "Wenn ich so darüber nachdenke...{w}ich ging in Berlin bisher nur für %(sisName)s aus der Wohnung."
    "Unglaublich. {w}Was man nicht alles für seine kleine Schwester tut."
    
    scene bg apotheke_aussen
    with fade
    
    play music m_wohnung
    
    "Ah, da ist die Apotheke ja."
    "Zur Sicherheit greife ich noch einmal nach dem Rezept."
    "Es ist da."
    "Und nochmal nach meinem Portemonnaie."
    "Es ist da."
    "Wenn jetzt irgendwas gefehlt hätte, wäre es sowieso zu spät gewesen."
    
    scene bg apotheke
    with fade
    
    "Ein Glück."
    "Kaum jemand ist hier."
    "Eine Schlange hätte mir gerade noch gefehlt."
    "Ich gehe an einen Schalter."
    
    show salih neutral
    with dissolve
    
    "Hmm...den kenn ich doch!"
    "Aber woher nur?"
    
    b "Äh...{w}Hallo."
    "Salih" "Guten Tag."
    "Salih" "Wie kann ich Ihnen weiterhelfen?"
    b "Ich..{w}ähm...{w}hier."    
    "Salih" "Oh, ein Rezept?" 
    "Salih" "Einen Moment bitte."
    "Woher kenn ich den jetzt bloß?"
    ".{w}.{w}.{w}hmm{w}.{w}.{w}."
    "Keine Ahnung."
    "Salih" "Das wäre dann ein Mal Mucosolvan und ein Mal Sinupret."
    "Salih" "Das macht zusammen 17,58 Euro."
    "Warum sind Medikamente eigentlich so teuer?"
    "Sollen die nicht der allgemeinen Bevölkerung helfen?"
    "Ich greife nach dem 20-Euro-Schein, den meine Mutter mir gab."
    "Salih" "Vielen Dank."
    "Salih" "Hier ist Ihr Rückgeld."
    $ geld -= 17.58
    #Bernd hat nun noch 7,42 Euro übrig
    "Ich packe das Geld in meine Geldbörse und greife nach der Tüte, in der die Medikamente sind."
    "Salih" "Vielen Dank und gute Besserung!"
    b "Ja ja."
    "Ich verlasse die Apotheke."

    stop music fadeout 0.4

    scene bg apotheke_aussen
    with fade
    
    "Ich geh lieber direkt nach Hause."
    
    scene bg schulweg1
    with fade
    
    
    play music m_lauraende

    "Aus der Ferne höre ich einen Straßenmusiker..."
    
    jump ende