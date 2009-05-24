#######################################
#Diese Datei beinhaltet die Laurastory#
#ab Kapitel zwei, und hat diverse     #
#"Eingänge", da es 9000 möglichkeiten #
#gibt, auf diese Linie zu kommen.     #
#Eingänge sind mit "ein_" markiert und#
#ihnen folgen in chronologischer      #
#Reihenfolge alle zugehörigen Labels. #
#######################################

#Inhaltsverzeichniss:
# zwei_laura - Anfang der Route
# zwei_laura_nichtMedizin - Wenn Bernd Laura nicht genug mag, kommt er nicht auf ihre Route
# zwei_laura_mail - Bernd schreibt eine Mail an Anja um sich mit ihr zu Treffen --> Raus!
# zwei_laura_irc - Bernd geht in den IRC-Channel --> Ausgang zur T- oder B-Route
# zwei_laura_anja_ausgang - Übergang zwischen zwei_laura und zwei_laura_mail am Anfang
# zwei_laura_weiter - Bernd scheißt auf Krautchan und kümmert sich lieber wieder um Laura

init:
    #lol, leerer init-Block
    pass
    
label zwei_laura:#Beginn der "echten" Laura-Story, einzige Linie, die zu Lauras Happy End führt
#Situation:
# Bernd hat sich mit Anja getroffen, ist aber nicht zum zweiten Treffen gegangen.
#Eingang:
# Automatisch wenn Bernd verspricht, Laura abzuholen.
#Ausgänge:
# Bernd kommt auf Anja zurück und landet auf ihrer Storyline.
    #UND LOS!
    "Immer noch starre ich ungläubig auf den Monitor."
    "...Krautchan ist wirklich offline?"
    "Immer und immer wieder drücke ich auf den Refresh-Button, aber das Ergebnis bleibt gleich."
    "404."
    "Frustriert werfe ich mich auf's Bett."
    "Krautchan ist erst seit ein paar Minuten offline, und mir ist jetzt schon langweilig."
    "...ob diese %(wBerndName)s Recht hatte mit ihren Verschwörungstheorien?"
    "...oder trollen die Admins wieder nur?"
    "Das wird es sein."
    "Wenn ich morgen früh aufwache, ist alles wieder so wie früher."
    "Mit diesem Gedanken schlafe ich ein."
    
    scene black
    with fade
    
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
    ma "Das musst du grade sagen."
    ma "Du hast früher immer simuliert, weil du nicht zur Schule wolltest."
    "Da hat sie auch wieder Recht."
    ma "Also bringst du ihr nun ihren Tee, oder muss ich das machen?"
    
    menu: #Entscheidet ob Anja oder Laura
        "Nein, ich mach es schon.": #Laura
            b "Nein, ich mach es schon."
            ma "Gut."
            ma "Die Tasse steht da."
        "Wieso sollte ich denn?": #Anja
            b "Wieso sollte ich denn?"
            ma "Na dann halt nicht."
            jump zwei_laura_anja_ausgang #v Das ist weiter unten! v
            
    b "Ich darf ja wohl erst meinen Toast essen, oder?"
    ma "Nein, dann wird der Tee kalt."
    "Ich stopfe mir schnell den Rest der ersten Scheibe in den Mund und lasse die zweite liegen."
    "Mit der Teetasse in der Hand, gehe ich in %(sisName)ss Zimmer."
    
    scene bg lauraszimmer
    with fade
    
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
    b "Jaja, schon gut."
    "Sie nimmt einen Schluck vom Tee."
    "Anscheinend ist sie tatsächlich krank."
    "Sie ist ziemlich blass."
    b "Wie gehts dir?"
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
    $ sisLove = 70 #test
    if sisLove < 60 or hentaiEin == False:
        jump zwei_laura_nichtMedizin
    "Ja."
    "Sie ist nur meine Schwester."
    "Es ist überhaupt nichts dabei."
    "..."
    "Ich werde es einfach tun."
    "Schließlich muss ich ihr ja nur die Brust einreiben."
    "Ist ja nicht so, als würde ich irgendwas anderes mit ihr machen."
    "Schließlich ist sie meine Schwester."
    
    scene bg lauraszimmer
    with gradientTransReverse
    
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
    #happy
    sis "Siehst du?"
    sis "Alles kein Probl-"
    
    scene bg lauraszimmer
    with vpunch
    
    #fall-sound
    
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
    "Es ist nichts schlimmes."
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
    sis "Äh... ok."
    "Sie legt sich auf den Rücken und öffnet die Knöpfe ihres Schlafanzugs."
    "..."
    #was würde ich dafür geben, hier ein bildschirmfüllendes CG von dieser situation zu haben ;_;
    #...ist das nun schon KiPo?
    
    
    
label zwei_laura_nichtMedizin:
    "Unmöglich!"
    "Ich kann das einfach nicht..."
    "Ich sollte es einfach vergessen."
    "Am besten gehe ich wieder nach Unten."
    
    scene bg keller
    with fade
    
    "Mal sehen, was auf Krautchan so los ist."
    "..."
    "Nichts."
    "Immer noch offline."
    "Ich muss rausfinden, was es damit auf sich hat."
    "Wo fängt man an?"
    "..."
    "Ich habe keine Ahnung."
    "Vielleicht... sollte ich erst eine Liste machen."
    "Eine Liste mit Anhaltspunkten und Hinweisen."
    "Dann habe ich wenigstens was zu tun."
    "Was wäre denn der erste Punkt..."
    "Ich könnte ja mal auf anderen Imageboards nach Hinweisen suchen."
    "Vielleicht ist Bernd dorthin ausgewandert..."
    "Nein."
    "Andere Imageboards sind der Krebs."
    "Das sollte meine letzte Option sein."
    "Wer würde denn etwas über Krautchan wissen?"
    "Bernd."
    "Wer noch?"
    "Die Admins."
    "..."
    "Dann war da noch dieses Mädchen..."
    show anja neutral
    with flash
    hide anja neutral
    with dissolve
    "%(wBerndName)s..."
    "Vielleicht sollte ich ihr eine E-Mail schreiben."
    "Was fehlt noch...?"
    "Eventuell ist wieder irgendwas vorgefallen?"
    "Wieder eine Amok-Ankündigung?"
    "Mal sehen, was die größeren Nachrichtenseiten dazu sagen..."
    "..."
    "Nichts."
    "Kein Amoklauf."
    "Keine Suchergebniss für \”Krautchan\"."
    "Das war es also nicht."
    "Wo könnte ich noch suchen...?"
    "Wo ist Bernd, wenn er nicht auf Krautchan ist?"
    "Im Keller."
    "Wo sonst?"
    "Im Internet."
    "Es muss doch andere Seiten geben, die eine große Zahl von Bernds häufig besuchen."
    "...aber mir fallen keine ein."
    "Im IRC."
    "...sollte man auf jeden Fall nicht ausschließen."
    "Hm..."
    "Was habe ich bisher alles?"
    "Eine verdächtige E-Mail, einen IRC-Channel und überhaupt keine Lust mehr."
    "Das bringt mich nicht weiter."
    "Was soll ich nur tun?"
    #hoho Entscheidungen über Entscheidungen!
    menu:
        "Ich sollte %(wBerndName)s eine Mail schreiben.":
            jump zwei_laura_mail
        "Ich sollte im IRC-Channel suchen.":
            jump zwei_laura_irc
        "Ich sollte einfach was anderes machen.":
            jump zwei_laura_weiter
            
label zwei_laura_mail: #Bernd schreibt eine E-Mail an Anja
#Er entschuldigt sich dafür, dass er nicht gekommen ist.
#Sie verabreden sich erneut. -> Übergang Anja Route
#Eventuell noch eine Möglichkeit zu Laura zurückzukommen.
    pass
    
label zwei_laura_irc: #Bernd geht in den IRC-Kanal und trifft dort auf die Mods.
#Das dortige Gespräch führt dazu, dass Bernd sich entweder mit dem General trifft (T-Route) oder auf eigene Faust loszieht um KC zu retten (B-Route)
    pass
    
label zwei_laura_anja_ausgang: #Übergang zwischen zwei_laura und zwei_laura_mail
#Tritt auf, wenn Bernd den Tee nicht bringt. Keine Möglichkeit auf Laura zurückzukommen.
    "Ich schnapp mit mein Toastbrot und gehe wieder in den Keller."
    
    scene bg keller
    with fade
    
    "Krautchan ist immer noch offline."
    "Es muss doch irgendwie Möglich sein, herauszufinden, wieso."
    "Wer könnte mir da helfen...?"
    show anja neutral
    with flash
    hide anja neutral
    with dissolve
    pass
   
label zwei_laura_weiter: #Bernd entscheidet sich, anscheinend, gegen Krautchan
#Er geht lieber hoch und will Laura einreiben, aber sie macht es selbst.
#Wer zu spät kommt, verpasst eben das Beste.
#Laura wird gesund und ihre Freundin, der General, kommt vorbei.
#Bernd bleibt so auf der Laura-Story und rettet nebenbei durch General-chans Hilfe KC.
#TOL
    pass