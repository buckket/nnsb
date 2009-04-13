init:
    #bilder, die noch gebraucht werden
    #  yasmin ohne kapuze, aber mit mantel
    #  yasmin schüchtern mit mantel
    #  yasmin fragezeichenmädchen mit mantel
    #  yasmin weinend mit mantel
    pass

label yasmin_polizei:
    "lol bullenschweine"


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
    hide yasmin stalker
    with dissolve
    show yasmin stalker_neutral
    with dissolve
    "Wow."
    "Ich habe mit allem gerechnet, aber damit nicht."
    b "...aber."
    b "Ich dachte doch..."
    b "Du..."
    u"Mädchen" "Was?"
    u"Mädchen" "Wirst du jetzt die Polizei rufen?"
    u"Mädchen" "Ich bin ein Stalker, du hast ja Recht."
    u"Mädchen" "Also."
    u"Mädchen" "Ruf sie schon an, ich habe es verdient."
    "Ich kann ihr irgendwie nicht folgen..."
    b "Du bist kein Bernd?"
    u"Mädchen" "Bernd?" #hier bitte verwirrt gucken, fragezeichenmädchen-style
    "Habe ich mich geirrt?"
    "Ist sie wirklich kein Bernd?"
    "Aber warum sollte mich sonst jemand stalken?"
    b "Verarsch mich nicht!"
    b "Warum solltest du mich sonst stalken?!"
    #wieder schüchtern
    u"Mädchen" "..."
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
    u"Mädchen" "Ich heisse %(yanName)s."
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
    
    show yasmin stalker_cry
    with dissolve
    
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
    
    show yasmin stalker_cry
    with dissolve
    
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
            scene bg kueche
            with fade
            "Tatsächlich."
            "Wir haben Traubensaft."
            "Genau da, wo sie gesagt hat."
            "Ich fülle zwei Gläser und begebe mich so schnell es geht wieder nach unten."
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
            b "Warum bist du nicht weggelaufen."
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
             b "Ich gehe auf."
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
    
    b "{b}Verdammt!{/b}"
    
    show yasmin stalker_surprised
    with dissolve
    
    b "Was willst du nur von mir!?"
    "Ich springe auf und drücke sie gegen die Wand."
    b "ANTWORTE!"
    yan "..."
    
    "Stimme" "%(berndName)s?"
    "Das ist Laura!"
    "Verdammt, was mache ich jetzt?"
    "Ich hätte nicht so schreien sollen."
    sis "Alles ok da unten?"
    "Scheiße!"
    b "J- Ja!"
    b "Alles ok!"
    b "Nicht reinkommen!"
    "Ich muss dieses verrückte Mädchen loswerden!"
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
    "%(yanName)s steht immer noch wie angewurzelt da."
    b "Los!"
    b "Irgendwo!"
    sis "Mit wem sprichst du?"
    b "Mit niemandem!"
    "Ich packe %(yanName)s an den Armen und werfe sie aufs Bett."
    b "Los, unter die Decke!"
    
    show yasmin stalker_embarrased
    with dissolve
    
    yan "...!"
    b "Los!"
    sis "Ich komme jetzt rein, %(berndName)s!"
    
    hide yasmin stalker_embarrased
    with dissolve
    
    show laura neutral
    with dissolve
    
    sis "Was machst du denn hier?"
    b "N- nichts!"
    "Ich stelle mich vorsichtshalber vor das Bett."
    sis "Ist wirklich alles ok?"
    b "Ja!"
    b "Alles ok!"
    "Hoffentlich merkt sie nichts."
    sis "Du bist komisch."
    b "Tja."
    "Mehr bringe ich nicht hervor."
    b "D- Du kannst jetzt gehen."
    sis "OK."
    b "..."
    sis "..."
    b "Worauf wartest du?"
    sis "...ganz sicher, dass alles ok ist?"
    b "Ja."
    sis "Mit wem hast du dann eben gesprochen?"
    b "Ich..."
    b "Das war online!"
    "Perfekte Ausrede ist perfekt!"
    sis "Achso!"
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
    #yasmin blush happy
    "Nanu?"
    "Warum ist sie denn so fröhlich?"