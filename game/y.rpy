init:
    #bilder, die noch gebraucht werden
    #  yasmin ohne kapuze, aber mit mantel
    #  yasmin schüchtern mit mantel
    #  yasmin fragezeichenmädchen mit mantel
    #  yasmin weinend mit mantel
    pass


label yasmin_anfang:
    "Stalkerbernd" "Stalkerbernd?"
    "!"
    "Es hat gesprochen."
    "Stalkerbernd" "Wer soll das sein?"
    "Diese Stimme...?"
    "Ich lasse seine Arme los, und setze mich aufs Bett."
    "Ich bin verwirrt."
    "Seine Stimmte klingt wie..."
    b "...du bist ein Mädchen?"
    #hier nimmt yasmin die kapuze runter und man sieht das gesicht
    #sie schaut schüchtern zur seite
    "Wow."
    "Ich habe mit allem gerechnet, aber damit nicht."
    b "...aber."
    b "Ich dachte doch..."
    b "Du..."
    "Mädchen" "Was?"
    "Mädchen" "Wirst du jetzt die Polizei rufen?"
    "Mädchen" "Ich bin ein Stalker, du hast ja Recht."
    "Mädchen" "Also."
    "Mädchen" "Ruf sie schon an, ich habe es verdient."
    "Ich kann ihr irgendwie nicht folgen..."
    b "Du bist kein Bernd?"
    "Mädchen" "Bernd?" #hier bitte verwirrt gucken, fragezeichenmädchen-style
    "Habe ich mich geirrt?"
    "Ist sie wirklich kein Bernd?"
    "Aber warum sollte mich sonst jemand stalken?"
    b "Verarsch mich nicht!"
    b "Warum solltest du mich sonst stalken?!"
    #wieder schüchtern
    "Mädchen" "..."
    b "..."
    "Vielleicht ist sie wirklich kein Bernd?"
    "...aber ist das nicht egal?"
    "Sie ist bei mir eingebrochen."
    "Mehrmals."
    menu:
        "Ich sollte die Polizei rufen!":
            jump yasmin_polizei
        "Ich werde sie erst befragen.":
            "Vielleicht hatte sie ja einen guten Grund."
    b "Warum bist du bei mir eingebrochen?"
    "Mädchen" "..."
    b "Warum hast du mich verfolgt?"
    "Mädchen" "..."
    b "Wer bist du?"
    "Mädchen" "..."
    b "Was willst du von mir?"
    $ yanNameKurz = stringShorten(yanName,2)
    "Mädchen" "%(yanNameKurz)s- %(yanName)s."
    b "Wa- wie bitte?"
    "%(yanName)s?"
    "Mädchen" "Ich heisse %(yanName)s."
    b "..."
    yan "..."
    "%(yanName)s also..."
    "Ich habe keine Ahnung, was ich sagen soll..."
    "...aber wenn man sie so ansieht, könnte man meinen, ihr ginge es genauso."
    yan "..."
    b "..."
    "Was soll ich nun mit ihr machen?"
    "Die Polizei rufen?"
    yan "%(berndName)s... ich..."
    "Woher kennt sie meinen Namen überhaupt?"
    b "Woher kennst du meinen Namen?"
    yan "..."
    "Jetzt schweigt sie wieder."
    "Ich sollte nicht dazwischen reden, wenn ich etwas von ihr erfahren will."
    b "Sprich ruhig weiter."
    yan "..."
    yan "Ich..."
    #weinend!
    yan "...es tut mir so Leid!"
    yan "*schluchz*"
    "Warum weint sie denn jetzt!?"
    "Ist das nur show?"
    "Verarscht sie mich, um einen überraschenden Fluchtversuch zu starten?"
    "...oder ist es echt?"
    menu:
        "Ich rufe jetzt die Polizei!":
            jump yasmin_polizei
        "Ich habe Mitleid mit ihr.":
            "...vielleicht sollte ich sie einfach noch ein wenig hier behalten."
            "Ich muss mehr über sie herausfinden."
    yan "*schluchz*"
    b "Beruhig dich doch erst mal!"
    b "Ich werde schon nicht die Polizei rufen oder so."
    b "Allerdings musst du mir schon erklären, was es mit dieser ganzen Sache auf sich hat."
    #yasmin mit tränen in den augen
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
    yan "..."
    "Zuerst frage ich sie, warum sie mich verf-... nein."
    "Das ist zu direkt."
    "Ich muss das langsamer angehen."
    b "Dein Name ist also %(yanName)s?"
    "Sie nickt."
    "Das ist doch schon mal ein Anfang."
    "...aber..."
    
    #hier folgt nun ein dialog, bei dem verschiedene fragen gestellt werden können,
    #wobei jede Frage den Spieler weiterbringen kann, aber nicht muss
    #für die erste frage erst mal zwei variablen:
    $ y_bef_11 = 0
    $ y_bef_12 = 0
    #diese symbolisieren die 2 ersten fragen, die dritte wird immer angezeigt
    
label yasmin_befragung_eins:
    menu:
        "Wie soll ich jetzt weiter Fragen?"
        
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
            b "Willst du vielleicht was trinken?"
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
            b "Na gut dann bringe ich d-"
            yan "Traubensaft."
            "Traubensaft."
            b "Ich weiß nicht, ob wir welchen hier haben."
            yan "..."
            yan "Im Kühlschrank."
            yan "Dritte Flasche von hinten."
            b "..."
            "Ich sag lieber nichts."
            b "Bin gleich wieder da."
            #scene küche
            "Tatsächlich."
            "Wir haben Traubensaft."
            "Genau da, wo sie gesagt hat."
            "Ich fülle zwei Gläser und begebe mich so schnell es geht wieder nach unten."
            #scene keller
            "Sie sitzt noch genau so da, wie ich sie verlassen habe."
            "Anscheinend hat sie wirklich nicht vor abzuhauen."
            "...oder ist das ein Trick?"
            "Ich reiche ihr ein Glas und setze mich wieder hin."
            yan "..."
            yan "Danke."
            "Also..."
            "Was nun?"