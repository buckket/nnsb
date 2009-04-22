init:
    #bilder, die noch gebraucht werden
    #  yasmin ohne kapuze, aber mit mantel
    #  yasmin schüchtern mit mantel
    #  yasmin fragezeichenmädchen mit mantel
    #  yasmin weinend mit mantel
    pass

label yasmin_polizei:
    #passiert, wenn Bernd die Polizei rufen will
    #Yasmin flieht und er sieht sie nie wieder
    #Er landet auf der Bernd-Route und schlägt sich ziemlich allein mit Lauras und Yasmins Hilfe durch
    b "Mir reicht es!"
    b "Ich rufe jetzt die Polizei!"
    show yasmin stalker_surprised
    with dissolve
    
    if yanKennen == 0:
        u"Mädchen" "Aber...!"
    else:
        yan "Aber...!"
    
    b "Kein aber!"
    b "Ich gehe jetzt hoch zum Telefon, und du kommst mit, verstanden?"
    
    show yasmin stalker_embarrased
    with dissolve
    
    if yanKennen == 0:
        u"Mädchen" "..."
    else:
        yan "..."
    
    "Ich drehe mich um und gehe in Richtung der Tür."
    "Sie folgt mir die Treppe nach oben."
    "Was soll ich der Polizei sagen?"
    "Ich werde ihnen einfach die Wahrheit erzählen."
    b "Komm schon, lauf ein bissch-"
    
    scene bg kellertreppe
    with dissolve
    
    "Ich blicke die Treppe herunter, aber sie ist nicht da."
    "Schnell renne ich zurück in den Keller."
    
    scene bg keller
    with fade
    
    "...aber hier ist sie auch nicht."
    b "Verdammt!"
    "Ich hätte sie nicht aus den Augen lassen dürfen."
    "...soll ich trotzdem die Polizei rufen?"
    "Sicher ist sicher."
    "Vielleicht kommt sie ja nochmal zurück."
    
    scene bg wohnung_innen
    with fade
    
    "Ich gehe zum Telefon und will 110 tippen, als..."
    
    show laura neutral
    with dissolve
    
    sis "Wen rufst du an, %(berndName)s?"
    "Was macht %(sisName)s so spät noch hier?"
    "Müsste die nicht schon im Bett liegen?"
    b "Niemanden."
    b "Also..."
    b "...den kennst du nicht."
    b "Geh wieder ins Bett."
    sis "Hm?"
    "Sie beugt sich über das Telefon."
    sis "Wieso steht dann da 110?"
    sis "Das ist die Nummer der Feuerwehr."
    
    show laura surprised
    with dissolve
    
    sis "Brennt es irgendwo?"
    "Oh man..."
    b "Das ist nicht die Feuerwehr, sondern die Polizei."
    b "Ich rufe die an, weil jemand bei mir eingebrochen ist."
    
    show laura happy
    with dissolve
    
    sis "Achso!"
    
    show laura surprised
    with dissolve
    
    sis "Eingebrochen!?"
    b "Ja."
    b "Ein verrücktes Mädchen ist bei mir in den Keller eingestiegen."
    "Selbst, wenn ich es sage, hört sich das nicht glaubwürdig an..."
    "...dabei habe ich es selbst erlebt."
    
    show laura happy
    with dissolve
    
    sis "Achso!"
    sis "Klar!"
    sis "Ein verrücktes Mädchen."
    sis "Wie sah die denn aus?"
    b "Naja, sie hatte einen schwarzen Mantel und schwarze Haare und..."
    b "...wieso erzähle ich dir das alles!?"
    sis "Hihi..."
    
    show laura neutral
    with dissolve
    
    sis "Könnte es sein, dass..."
    sis "...du das nur geträumt hast?"
    b "..."
    "Will sie mich für dumm verkaufen?"
    "Sowas könnte ich nie träumen."
    b "Nein, das war ganz sicher kein Traum."
    sis "Sicher?"
    sis "Es hört sich nur sehr..."
    
    show laura happy
    with dissolve
    
    sis "...lächerlich an."
    "Meine kleine Schwester macht sich über mich lustig..."
    "Aber sie hat Recht."
    "Es hört sich wirklich lächerlich an."
    
    show laura neutral
    with dissolve
    
    sis "Ist sie denn noch da?"
    b "Nein."
    b "Sie ist abgehauen."
    
    show laura happy
    with dissolve
    
    sis "Verstehe schon."
    sis "..."
    sis "Warum legst du nicht einfach den Telefonhörer zur Seite, und gehst schlafen?"
    b "..."
    "Hält sie mich irgendwie für verrückt?"
    "Naja... so ganz weit hergeholt ist das ja nicht."
    "Vielleicht sollte ich wirklich einfach schlafen gehen, und nochmal gründlich darüber nachdenken."
    b "Du hast Recht..."
    b "...ich bin mir zwar sicher, dass sie da war, aber ich schlaf lieber noch eine Nacht drüber."
    "Abgesehen davon, dass ich sowieso nicht am Telefon mit jemandem sprechen kann..."
    "Ich wüsste nicht, was ich sagen sollte."
    sis "Na dann..."
    sis "Gute Nacht, %(berndName)s."
    b "Gute Nacht."
    
    hide laura happy
    with dissolve
    
    "Ich sollte dann auch schlafen gehen..."
    
    scene black
    with fade
    
    jump b_anfang #BUTTERGOTT - b.rpy erstellen
    
    
label yasmin_anfang:
    "Stalkerbernd" "Stalkerbernd?"
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
    
    show yasmin stalker_cry #braucht noch besseres bild für wenn sie RICHTIG heult
    with dissolve
    
    yan "...es tut mir so Leid!"
    yan "*schluchz*"
    "Warum weint sie denn jetzt!?"
    "Ist das nur Show?"
    "Will sie mich auf den Arm nehmen?"
    "Nur um dann einen überraschenden Fluchtversuch zu starten?"
    "Oder ist es echt?"
    
    menu:
        
        "Ich rufe jetzt die Polizei!":
            jump yasmin_polizei
       
        "Ich habe Mitleid mit ihr.":
            "...vielleicht sollte ich sie einfach noch ein wenig hier behalten."
            "Ich muss mehr über sie herausfinden."
    
    yan "*schluchz*"
    b "Beruhig dich doch erst mal!"
    b "Ich werde schon nicht die Polizei rufen."
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
            
            scene bg kueche
            with fade
            
            "Tatsächlich."
            "Wir haben Traubensaft."
            "Genau da, wo sie gesagt hat."
            "Das ist nicht normal!"
            "Die ist ja völlig krank."
            "Ich sollte mich lieber beeilen."
            "Hastig fülle ich zwei Gläser und begebe mich so schnell es geht wieder nach unten."
            
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
    "Ich packe %(yanName)s an den Armen und werfe sie auf's Bett."
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
    
    show yasmin stalker_happy
    with dissolve
    
    "Nanu?"
    "Warum ist sie denn so fröhlich?"