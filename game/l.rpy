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
# Wieso ist es leer?
#  It is a mystery.

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
    ma "Du hasst früher immer simuliert, weil du nicht zur Schule wolltest."
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
            jump laura_anja_ausgang #v Das ist weiter unten! v
            
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