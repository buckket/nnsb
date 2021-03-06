#Inhaltsverzeichnis:
#label yasmin_polizei = Bernd will Polizei anrufen, Yasmin flieht, Laura hält ihn davon ab, Übergang zur Bernd-Route
#label yasmin_anfang = Yasmin-Route, sie schauen gemeinsam Lucky Star
#label yasmin_befragung_eins = Bernd fragt Yasmin aus 
#label yasmin_befragung_zwei = Bernd fragt Yasmin aus 
#label yasmin_befragung_drei = Bernd fragt Yasmin aus, sie schauen am Ende Lucky Star
#label yasmin_zwei_derMorgenDanach = Was nach der Lucky Star-Nacht passiert, Frühstück etc.

init:
    #bilder, die noch gebraucht werden
    #  yasmin ohne kapuze, aber mit mantel
    #  yasmin schüchtern mit mantel
    #  yasmin fragezeichenmädchen mit mantel
    #  yasmin weinend mit mantel
    $ yanVerdacht = "" #dieb/bernd/kein
    pass

label yasmin_polizei:
    #passiert, wenn Bernd die Polizei rufen will
    #Yasmin flieht und er sieht sie nie wieder
    #Er landet auf der Laura-Route und manchmal hilft ihm Yasmin ein bisschen aus dem Hintergrund
    
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
    
    sis "Ach so!"
    
    show laura surprised
    with dissolve
    
    sis "Eingebrochen!?"
    b "Ja."
    b "Ein verrücktes Mädchen ist bei mir in den Keller eingestiegen."
    "Selbst, wenn ich es sage, hört sich das nicht glaubwürdig an..."
    "...dabei habe ich es selbst erlebt."
    
    show laura happy
    with dissolve
    
    sis "Ach so!"
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
    "So was könnte ich nie träumen."
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
    
    scene black
    with fade
    
    $ renpy.pause(1.0)
    
    jump yasmin_zwei_derMorgenDanach
    
label yasmin_zwei_derMorgenDanach:
    
    scene bg keller
    with fade
    
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
   
    yan "Guten Morgen, %(berndName)s."
    b "Oh, guten Morgen, %(yanName)s."
    "..."
    b "W-w-w-w-as machst du hier?!"
    "%(yanName)s sitzt neben mir im Bett."
    "Wieso sitzt sie da?"
    
    show yasmin embarrased
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
    show yasmin embarrased
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
    #hier muss dann die musik stoppen
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
    
    scene bg keller
    show yasmin neutral
    with vpunch
    
    show laura neutral at Position(xpos=0.0,xanchor="right")
    with None
    
    show yasmin surprised at right
    show laura happy at left
    with move
    
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
    show yasmin embarrased at rightedge
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
    
    show yasmin embarrased at center
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
    
    #ende kapitel 2
    jump yasmin_drei_von_yasmin
    
label yasmin_drei_von_yasmin: #übergang von y route
    
    #anfang kapitel 3
    
    scene bg keller
    with dissolve
    
    "Zwei Stunden ist es her, dass sie gegangen ist."
    "In diesen zwei Stunden habe ich so gut wie nichts gemacht."
    "Seit zwei Stunden sitze ich hier auf meinem Bett und mache nichts."
    "Nein, das ist nicht ganz richtig."
    "Ich mache schon etwas."
    "Ich denke."
    "Ich denke sogar ziemlich viel."
    "Über das, was gestern Abend passiert ist, wie es dazu kommen konnte, was es für Folgen haben wird."
    "Ich kann %(yanName)s immer noch nicht verstehen."
    "Warum verhält sie sich so?"
    "Wo ist ihr Motiv?"
    "Sie muss ein Motiv haben, oder?"
    "Irgendwelche Beweggründe, die sie antreiben."
    "Jeder Mensch hat das."
    "Außer mir."
    "Ich habe keine Ziele. {w}Keine Motive. {w}Keinen Antrieb oder so was."
    "Deswegen bin ich ja auch ein Bernd."
    "Aber sie ist kein Bernd."
    "Welchen Grund kann sie haben?"
    "Was bringt sie dazu, erst bei mir einzubrechen und dann hier zu übernachten?"
    "Noch dazu mit mir im selben Bett."
    "Irgendetwas ist hier faul."
    "Aber ich werde der Sache auf den Grund gehen."
    "Ich werde herausfinden, warum sie so ist, wie sie ist."
    "Schließlich bin ich kein dummer Charakter aus irgendeinem Computerspiel, der nicht merkt, was um ihn herum geschieht."
    "...aber wie gehe ich vor?"
    "Wie finde ich heraus, was sie denkt?"
    "Ich muss mich in ihre Lage versetzen, aber wie macht man das?"
    "Wenn ich sie wäre... {w}was würde ich tun?"
    b "Stell es dir vor, %(berndName)s..."
    b "...du bist ein Mädchen."
    b "Du bist kein Bernd mehr."
    b "Du bist ein Mädchen... {w}eine junge Frau..."
    b "...was würdest du tun?"
    "... {w}... {w}..."
    "So sehr ich es auch versuche, ich komme zu keinem richtigen Schluss."
    "Wenn ich ein Mädchen wäre, würde ich wahrscheinlich den ganzen Tag an mir selbst rumspielen."
    "Aber ich bezweifle, dass mich das irgendwie dazu bringen könnte, sie besser zu verstehen."
    "Ich brauche mehr Informationen über sie."
    "Wenn ich verstehen will, wie sie denkt... {w}muss ich wissen, wer sie ist."
    "Aber wie soll ich mehr über sie erfahren?"
    "Dafür bräuchte ich zumindest ihren vollen Namen."
    "Das kann ich also schon mal vergessen."
    "Vielleicht sollte ich mich da anders nähern."
    "Ich muss ja nicht unbedingt herausfinden, wer sie genau ist."
    "Es reicht eventuell wenn ich herausfinde, in welcher Beziehung sie zu mir steht."
    "Wieso sollte jemand interesse an mir haben?"
    "Gehen wir mal die Möglichkeiten durch..."
    "1. Sie ist ein gewöhnlicher Dieb."
    "Gut möglich, denn sie ist bei mir eingebrochen."
    "Das spricht auf jeden Fall dafür."
    "Dagegen spricht, dass sie nicht abgehauen ist als ich sie erwischt habe."
    "Aber auch das könnte nur ein Trick sein."
    "...und er hat funktioniert."
    "Ich habe nicht die Polizei gerufen."
    "Sie ist entkommen."
    "Aber wenn sie ein Dieb wäre... {w}was würde sie bei mir klauen wollen?"
    "Ich habe nichts."
    "Sie hat auch keine Anstalten gemacht, etwas mitzunehmen, bevor ich sie überrumpelt habe."
    "..."
    "Doch, hat sie."
    "Sie hat versucht, meine Festplatte zu kopieren."
    "Warum?"
    "Was ist da drauf?"
    "Ich habe nichts außer Animevideos, Musik und ein paar Games."
    "Definitiv nichts von Wert."
    "Kommen wir zur nächsten Möglichkeit."
    "2. Sie ist doch Stalkerbernd."
    "Zwei Dinge sprechen dagegen."
    "Sie hat behauptet, kein Bernd zu sein."
    "Das könnte jeder behaupten."
    "Kein wirklich wirksames Argument."
    "Aber es gibt da noch etwas..."
    "...sie ist definitiv eine Frau."
    "Sie ist weiblich."
    "Es gibt keine weiblichen Bernds."
    "Absolut keine."
    "Sie existieren nicht."
    "Das sind irgendwelche Typen, die sich als Frauen ausgeben, um Bernd zu ärgern."
    "Wenn auch unwahrscheinlich, bleibt das trotzdem eine Möglichkeit."
    "Schließlich ist Stalkerbernd die einzige Person, von der ich irgendwie von Interesse sein könnte."
    "Die letzte Möglichkeit wäre..."
    "3. Sie ist keins von beiden."
    "Die wahrscheinlich einfachste Antwort."
    "Aber wirklich weiter bringt mich das nicht."
    "Was mir fehlt sind mehr Informationen über sie."
    "Ich kann mir schlecht ein Bild von ihr machen, wenn ich nichts über sie weiß."
    "...aber ich muss auch nicht sofort zu einem Schluss kommen, oder?"
    "Vielleicht könnte ich einfach noch ein wenig warten."
    "Sie wollte sich ja nochmal mit mir treffen."
    "Dann muss es mir gelingen, soviel wie möglich über sie herauszufinden."
    "...aber vielleicht sollte ich trotzdem schon mal in eine Richtung forschen."
    "Es kann nicht schaden."
    "Also welche Möglichkeit erscheint am wahrscheinlichsten?"
    menu:
       "Sie ist eventuell ein Dieb.":
           $ yanVerdacht = "dieb"
           "Dass sie ein Dieb ist, erscheint mir im Moment am wahrscheinlichsten."
           "Ich habe zwar keine Ahnung, was sie von mir stehlen würde, aber das werde ich herausfinden."
       "Sie ist eventuell Stalkerbernd.":
           $ yanVerdacht = "bernd"
           "Auch wenn sie ein Mädchen ist... vielleicht ist sie trotzdem ein Bernd."
           "Das würde erklären, was sie von mir will und warum sie an meinem Computer wollte."
           "Sie ist hinter meinen persönlichen Daten her, um sie auf Krautchan zu posten."
           "Aber Krautchan ist im Moment down, also habe ich fürs Erste nichts zu befürchten."
           "Trotzdem sollte ich mehr über sie herausfinden."
       "Ich kann es nicht genau sagen.":
           $ yanVerdacht = "kein"
           "Ich habe einfach zu wenig Informationen über sie."
           "Ich werde mich nochmal mit ihr treffen müssen, um wirklich zu klären, was sie von mir will."
           "Darauf sollte ich mich vorbereiten."
           
    "Aber zuerst brauche ich irgendwas zu trinken."
    "Immer noch ziemlich verwirrt, steige ich die Treppe nach oben."
    
    scene bg kueche
    with fade
    
    "In der Küche ist niemand."
    "Ich will auch im Moment niemanden sehen."
    "Das würde mich nur ablenken."
    "Nachdem ich ein Glas mit Traubensaft gefüllt habe, will ich wieder nach unten gehen aber..."
    
    show laura neutral
    with dissolve
    
    sis "Hi, %(berndName)s."
    sis "Ist deine..."
    "Sie sieht sich kurz um als würde sie sich vergewissern, dass ihr niemand zuhört und spricht dann leise weiter."
    sis "...Freundin... schon weg?"
    b "Sie ist nicht meine Freundin."
    
    show laura happy
    with dissolve
    
    sis "Alles klar..."
    
    show laura neutral
    with dissolve
    
    sis "Und was macht sie dann bei dir?"
    sis "Wieso solltest du dich denn mit einem Mädchen hier treffen, wenn sie nicht deine Freundin ist?"
    "Ich könnte es ihr erklären, aber ich habe keine Lust."
    "Was soll ich sagen?"
    sis "Na?"
    
    show laura happy
    with dissolve
    
    sis "Also hatte ich recht."
    sis "Sie ist deine Freundin."
    sis "Ist dir das peinlich?"
    sis "Wie alt ist sie überhaupt?"
    sis "Woher kennst du sie?"
    sis "Wieso ist sie so schüchtern?"
    b "Lass mich einfach in Ruhe."
    b "Nervensäge."
    
    show laura pissed
    with dissolve
    
    sis "Dann halt nicht."
    b "Richtig."
    b "Es geht dich nichts an."
    
    show laura mad
    with dissolve
    
    sis "Idiot..."
    "Zähneknirschend verlässt sie die Küche."
    
    hide laura mad
    with dissolve
    
    "%(yanName)s... meine Freundin?"
    "So ein Quatsch."
    "Ich kenne sie gar nicht."
    "Außerdem..."
    "Wieso sollte sie mich mögen?"
    "Ich bin ein Bernd."
    if yanVerdacht == "bernd":
       "Sie vielleicht auch..."
       "Trotzdem..."
    else:
       "Sie nicht."
       "Und überhaupt..."
    "Ich habe mich sowieso schon damit abgefunden, niemals eine Freundin zu finden."
    "Und ganz sicher nicht so plötzlich."
    "So was passiert nur in irgendwelchen Filmen oder Mangas."
    "Nicht im echten Leben."
    "Das wäre ja total kitschig."
    "Was sollte sie auch an mir mögen?"
    "Es gibt doch genug Typen, die nicht solche Versager sind wie ich."
    "Bei denen wäre sie besser aufgehoben."
    "Die haben einen Job, viel Geld, sind nett, gepflegt und sehen gut aus."
    "Ich bin nur ein Bernd."
    "Aber das ist ja auch völlig egal, denn sie mag mich ja überhaupt nicht."
    
    "...mal schauen, ob Krautchan schon wieder online ist."
    
    scene bg keller
    with fade
    
    "..."
    "Nein, sieht nicht so aus."
    "Verdammt."
  
    "Ich kann überhaupt nichts tun."
    "Mehrmals blicke ich mich um, aber hier ist nichts zu tun."
    "Einfach nichts."
    "Null."
    "Gar nichts."
    "Mir ist langweilig."
    "Sehr sogar."
    "Vielleicht sollte ich mal ein wenig frische Luft schnappen."
    "...obwohl..."
    "Dafür müsste ich ja in die Außenwelt."
    "Will ich das wirklich?"
    "Wohl kaum."
    "Aber was soll ich sonst machen?"
    "Es würde vielleicht reichen, das Fenster zu öffnen, aber ich habe kein richtiges Fenster."
    "Es hilft alles nichts, ich muss einen klaren Kopf kriegen."
    "Ich laufe einfach eben eine Runde um den Block."
    
    scene bg zuhause_draussen_dunkel
    with fade
    
    "Es ist schon ziemlich dunkel."
    "Aber so spät ist es doch noch gar nicht?"
    "Komisch."
    "Ich atme tief ein."
    "Die kalte Luft tut mir gut und macht mir den Kopf frei."
    "Endlich kann ich mal durchatmen."
    "Immer nur im Keller zu sitzen kann auf die Dauer ganz schön anstrengen."
    "Ich biege um die Ecke."
    "Die Straße ist leer, niemand ist hier."
    "Ich versuche an etwas anderes zu denken, aber irgendwie komme ich immer wieder auf %(yanName)s zurück."
    "Wieso werde ich aus ihrem Verhalten nicht schlau?"
    "Weil sie eine Frau ist?"
    "Verhalten sich etwa alle Frauen so merkwürdig?"
    "Was sie tut ergibt keinen Sinn..."
    "Aber warum tut sie es dann?"
    "Ich verstehe sie einfach nicht."
    "Hoffentlich sehe ich sie nicht wieder."
    "Dann könnte ich das einfach alles vergessen und wieder ein ganz normales Leben führen."
    "So wie vorher."
    "Ja, das ist das Beste."
    "Wenn Krautchan erst wieder online ist, wird alles gut."
    "...aber was mache ich, wenn sie doch wieder bei mir aufkreuzt?"
    "Sie wegschicken?"
    "Das könnte ich nicht."
    "Ich habe nicht die Kraft ihr so was zu sagen."
    "Ich konnte es schon heute morgen nicht."
    "Also was dann?"
    "Ausreden erfinden?"
    "Das kann ich ziemlich gut."
    "Ich habe mich schon immer vor allem gedrückt, indem ich mir irgendwelchen Schwachsinn ausgedacht habe."
    "Irgendwann bin ich deswegen von der Schule geflogen."
    "Aber dort hielt mich eh nichts."
    "Auch mit tollem Abschluss findet man heute kaum noch einen Job, und Freunde hatte ich da auch keine."
    "Ich hatte noch nie Freunde."
    "Immer ein paar Leute, mit denen man halbwegs reden konnte, aber auch nur über bestimmte Dinge."
    "Woran liegt das?"
    "Bin ich selbst Schuld?"
    "Hätte ich etwas ändern können?"
    "Darüber nachzudenken bringt mir jetzt auch nichts."
    "Es ist schon viel zu spät."
    "In meinem Leben ändert sich eh nichts mehr."
    "Ich werde einsam sterben."
    "Einfach irgendwann grillen gehen..."
    $ vonYasmin = True
    
    jump drei_yasmin_gewitter

label drei_yasmin_gewitter:

    scene bg zuhause_draussen_dunkel
    with flash
    
    play sound "sounds/donner.wav"
    
    "Ein Blitz holt mich aus meinen Gedanken."
    "..."
    "Ein Gewitter?"

    play music "sounds/regen.wav" fadein 2.0
    
    "Na toll."
    "Es fängt an zu regnen und ich habe keine Schirm oder so was."
    "Wo bin ich überhaupt?"
    "Ich bin so sehr in Gedanken versunken gewesen, dass ich einfach weiter gelaufen bin, ohne auf den Weg zu achten."
    "Hier kenne ich mich nicht aus."
    "Der Regen wird stärker."
    #"Ich bin schon ganz feucht."
    "Ich bin schon ganz nass." # :3
    "Wo komme ich her?"
    "Ich habe mich verlaufen."
    
    scene bg zuhause_draussen_dunkel
    with flash
    
    play sound "sounds/donner.wav"
    
    "Da vorne ist eine Bushaltestelle."
    "Dort stelle ich mich unter, bis der Regen aufhört."
    "Da ist bestimmt auch ein Stadtplan."
    "Vielleicht finde ich dann den Weg zurück."
    
    scene bg bushaltestelle
    with dissolve
    
    "Hier ist es erst mal trocken."
    "Auch wenn ich sowieso schon klitschnass bin."
    "Ein Stadtplan hängt hier auch, aber irgendwer hat ihn vollgekritzelt."
    "Man kann nichts erkennen."
    "Scheiß Unterschichtkinder."
    "Haben die sonst nichts zu tun?"
    "Warum machen sie anderen das Leben schwer?"
    
    scene bg bushaltestelle
    with flash
    
    play sound "sounds/donner.wav"
    
    "Es bleibt mir wohl nichts anderes übrig, als hier zu warten bis es vorbei ist."
    "..."
    "Der Regen nimmt kein Ende."
    "Inzwischen ist es wirklich stockdunkel."
    "Als wäre es Nacht."
    "...oder ist es schon Nacht?"
    "Bin ich so lange gelaufen?"
    "Ich habe keine Uhr dabei, aber es erscheint mir unwahrscheinlich."
    "Das liegt wohl nur am Gewitter."
    "Ich werde hier wohl noch eine Weile warten müssen."
    "Hoffentlich nicht zu lange."
    "Notfalls muss ich einfach durch den Regen zurück."
    "...aber ob ich im Dunkeln den Weg finde..."
    
    scene bg bushaltestelle
    show yasmin stalker_schwarz_k
    with flash
    
    play sound "sounds/donner.wav"
    
    hide yasmin stalker_schwarz_k
    with fastDissolve
    
    "...!"
    "Ich habe es nur kurz gesehen, aber auf der anderen Straßensteite steht jemand."
    "Irgendwer steht dort und schaut in meine Richtung."
    "Ganz sicher."
    "Wer?"
    "Wer ist das?"
    "Nur irgendein Fußgänger?"
    "Nein."
    "Wer würde bei diesem Regen freiwillig draußen herumlaufen und sich den Tod holen?"
    "Das ist verdächtig."
    "Steht er noch dort?"
    "Oder ist er vielleicht einfach weitergegangen?"
    "Oder kommt er wohlmöglich schon auf mich zu?"
    "Sicher will er mich ausrauben oder..."
    
    scene bg bushaltestelle
    with flash
    
    play sound "sounds/donner.wav"
    
    "...weg."
    "Er ist weg."
    "...oder war er gar nicht da?"
    "Bilde ich mir schon Dinge ein?"
    "Nein."
    "Er war da."
    "Ganz sicher."
    "Es war am Ende doch nur ein Fußgänger."
    "Irgendjemand, der vom Regen überrascht wurde und nun auf dem Weg nach Hause ist."
    "Hoffentlich bleibt das meine einzige Begegnung für heute..."
    "Schritte."
    "Ich höre Schritte."
    "Von wo?"
    "Irgendwo auf der Straße läuft jemand."
    "Sie werden lauter."
    "Jemand läuft in meine Richtung."
    "Will er nur vorbei?"
    "Oder will er zu mir?"
    "Was soll ich tun?"
    "Ich warte einfach."
    "Es wird schon nichts passieren."
    "...hoffe ich."
    "Die Schritte sind jetzt ganz nah."
    "Eine Person tritt in den Schein der Haltestellenbeleuchtung."
    
    show yasmin stalker_neutral
    with dissolve
    
    "Aber... {w}das ist ja...{w} %(yanName)s."
    
    #hier wird die story aufgespalten in zwei teile abhängig davon, ob Bernd
    #von yasmins oder von anjas route zu diesem treffen kommt. beide storys
    #vereinigen sich, sobald yasmin auf krautchan aufmerksam wird
    
    if vonYasmin == True: #wird nur gesetzt, wenn bernd über yasmin_drei_von_yasmin kommt
        jump drei_yasmin_regen_vonYasmin
    else: #sonst muss er über anja gekommen sein
        jump drei_yasmin_regen_vonAnja
    
    
label drei_yasmin_regen_vonYasmin:
    show yasmin stalker_happy
    with dissolve
    yan "Hey, %(berndName)s."
    b "Äh... Hey."
    show yasmin stalker_neutral
    with dissolve
    yan "Was machst du hier draußen?"
    yan "Noch dazu bei diesem Wetter?"
    yan "Hätte nicht gedacht, dass du jemand bist, der oft draußen herumläuft."
    yan "Vor allem nicht bei Regen..."
    "Wer würde auch bei Regen freiwillig rausgehen?"
    b "Tja, das hat sich so ergeben."
    b "Irgendwie war ich unterwegs und dann zog dieses Gewitter auf..."
    b "Nun sitze ich hier und..."
    "Ich kann ihr schlecht sagen, dass ich den Rückweg nicht finde."
    "Das ist ja peinlich."
    b "...und ich warte, bis es zu regnen aufhört."
    show yasmin stalker_happy
    with dissolve
    yan "Ach so."
    yan "Na dann..."
    yan "Würde es dich stören, wenn ich neben dir sitze?"
    "Ja."
    b "Nein."
    "Verdammt."
    "Ich würde lieber allein sein, aber das kann ich ihr nicht sagen."
    "Sie nimmt direkt neben mir Platz."
    "Viel zu nah."
    "Ich rutsche ein Stück zur Seite."
    "Eine Weile lang schweigen wir."
    "Sollte ich irgendwie ein Gespräch anfangen?"
    "Oder einfach sitzen bleiben?"
    "Was würde ich denn sagen?"
    show yasmin stalker_embarrased
    with dissolve
    yan "%(berndName)s..."
    yan "Wie lange willst du hier noch sitzen?"
    b "Bis der Regen aufhört."
    yan "...das kann aber dauern."
    yan "Willst du so lange hier bleiben?"
    b "Ja."
    yan "...ok."
    show yasmin stalker_happy
    with dissolve
    yan "Dann werde ich auch warten."
    "Na super."
    "Ich werde also die nächsten Minuten, Stunden oder Tage neben ihr sitzen und schweigen."
    "Was macht sie überhaupt hier?"
    "Wieso läuft sie im Regen herum?"
    b "Was treibt dich eigentlich her?"
    b "Wieso bist du hier?"
    yan "Hm... {w}ich war auf dem Weg... {w}zu dir!"
    b "Wieso zu mir?"
    yan "Ich wollte mal wieder vorbeischauen..."
    b "...aber du bist vor ein paar Stunden erst gegangen..."
    b "...und du meintest, dass du wirklich gehen musst..."
    show yasmin stalker_embarrased
    with dissolve
    yan "Das ist..."
    yan "...also ich musste auch weg."
    yan "Aber ich hab alles erledigt..."
    yan "...und ich hatte nichts zu tun, also wollte ich vorbeischauen."
    "Als ob."
    b "Soso."
    "Jetzt schweigen wir wieder."
    "Was sie sagt ergibt keinen Sinn."
    
    scene bg bushaltestelle
    show yasmin stalker_schwarz
    with flash
    show yasmin stalker_surprised
    with dissolve
    
    play sound "sounds/donner.wav"
    
    yan "Ah!"
    "Sie zuckt zusammen und ich kann mir ein Lächeln nicht verkneifen."
    "Wieso hat sie in ihrem Alter noch Angst vor Gewitter?"
    
    show yasmin stalker_embarrased
    with dissolve
    
    yan "...albern, oder?"
    b "Hm?"
    "Sie hat wohl gemerkt, dass ich mich über sie lustig gemacht habe."
    yan "...ach nichts."
    "Wieder Stille."
    yan "Wollen wir nicht zu dir gehen, %(berndName)s?"
    b "...aber es regnet noch."
    
    show yasmin stalker_shy
    with dissolve
    
    yan "Bist du so empfindlich?"
    b "Nein... ich..."
    "Ich kann ihr schlecht sagen, dass ich den Weg nicht finde."
    "Oder...?"
    
    menu:
        "Ich sollte es ihr sagen.":
            "Richtig, ich sollte ihr einfach sagen, was Sache ist."
            "Sie wird mich ja wohl nicht auslachen."
            "Und wenn... {w}das interessiert mich überhaupt nicht."
            "Ich bin es ja gewohnt, dass man sich über mich lustig macht."
            "Also dann..."
            b "Ich..."
            b "Ich finde nicht mehr nach Hause."
            b "Das ist alles."
            
            show yasmin stalker_surprised
            with dissolve
            
            yan "Was?"
            yan "Du..."
            
            show yasmin stalker_smile
            with dissolve
            
            yan "Wenn das alles ist..."
            yan "Ich kenne den Weg doch."
            yan "Warum hast du nichts gesagt?"
            b "..."
            yan "Es muss dir nicht peinlich sein."
            yan "Nur weil du dich hier nicht auskennst?"
            yan "Ist doch nicht schlimm... oder?"
            "Sie hat Recht."
            b "Nein..."
            b "Du hast Recht."
            yan "Also dann... wollen wir?"
            b "OK..."
            
        "Ich sollte mich weiter rausreden.":
            "Nein, ich kann es ihr auf keinen Fall sagen."
            "Viel zu peinlich."
            "Aber was erzähle ich ihr dann?"
            b "Ich..."
            "Verdammt, %(berndName)s, überleg dir was!"
            b "Ich will nicht nach Hause."
            
            show yasmin stalker_surprised
            with dissolve
            
            yan "Wieso das?"
            b "Ich..."
            "Oh man, was jetzt?"
            b "Ich will nicht darüber sprechen."
            "Ich höre mich an wie irgendein Emo oder so was..."
            
            show yasmin stalker_shy
            with dissolve
            
            yan "Das..."
            yan "Das verstehe ich."
            yan "Aber du kannst nicht die ganze Nacht hier sitzen bleiben."
            yan "Lass uns gehen, ok?"
            yan "Bitte?"
            b "..."
            yan "..."
            "Ach, was soll's."
            b "OK... gehen wir."
            
            show yasmin stalker_happy
            with dissolve
            
            yan "Gut."
            
    "Sie tritt hinaus in den Regen."
    
    show yasmin stalker_happy
    with dissolve
    
    yan "Beeil dich, sonst werden wir ganz nass."
    b "Du hast wenigstens eine Kapuze."
    b "Warum setzt du sie nicht auf?"
    
    show yasmin stalker_smile
    with dissolve
    
    yan "Mir macht Regen nichts."
    yan "Ist im Endeffekt ja nur Wasser."
    "Wo sie Recht hat, hat sie Recht."
    "Ich stehe auf und mache zwei Schritte vorwärts."
    "Innerhalb von wenigen Sekunden bin ich nass von Kopf bis Fuß."
    b "..."
    
    show yasmin stalker_happy
    with dissolve
    
    yan "Willst du meinen Mantel haben?"
    b "Nein."
    "Ganz bestimmt nicht."
    
    show yasmin stalker_shy
    with dissolve
    
    yan "...dann nicht."
    
    show yasmin stalker_neutral
    with dissolve
    
    yan "Los, beeil dich ein bisschen."
    
    hide yasmin stalker_neutral
    with dissolve
    
    "Sie rennt voraus und ich folge ihr."
    
    scene black
    with fade
            
    
label drei_yasmin_regen_vonAnja:
    pass