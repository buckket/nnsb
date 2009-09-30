label eins_sisAbholen:

    stop music fadeout 0.3

    scene bg zuhause_hausflur
    with fade
    
    "Ich sollte mich mal langsam aber sicher auf den Weg machen."
    "Sonst muss ich gleich so hetzen."
    "Aber noch habe ich ja Zeit."
    
    scene bg schulweg1
    with fade
    
    play music m_schulweg fadein 0.2
    
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
    
    play music m_donerladen fadein 0.3
    
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
    $ geld -= 3.50
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
    
    play music m_schulweg fadein 0.2
    
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
    
    play music m_drama fadein 0.2
    
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
    
    play music m_schulweg fadein 0.2
    
    "Irgendwo war hier doch ein Eiswagen..."
    "Ah! Da ist er."
    
    scene bg eiswagen
    with fade
    
    show salih neutral
    with dissolve
    
    "Salih" "Guten Tag."
    "Salih" "Was darf's denn sein?"
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
    "Salih" "Das macht dann 1,50 Euro."
    $ geld -= 1.50
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
    sis "Aber wenn du mal ein Versprechen hältst, ist das etwas Besonderes."
    sis "...apropos Versprechen."
    b "Hm?"
    "Was will sie nun schon wieder?"
    sis "Würdest du mich morgen von der Schule abholen?"
    "Oh..."
    "Würde ich?"
    b "Ich weiß nicht..."
    
    show laura neutral
    with dissolve
    
    sis "Versprichst du es mir?"
    sis "Bitte?"
    
    menu:
        "OK, ich verspreche es.":
            b "In Ordnung."
            b "Ich verspreche es."
           
            show laura happy
            with dissolve
            
            sis "JUCHU!"
            sis "Ich werde auf dich warten, %(berndName)s, aber nicht lange."
            sis "Wehe dir, wenn du zu spät kommst."
            show laura neutral
            with dissolve
            sis "Dann werde ich sehr, sehr wütend."
            "Darauf kann ich verzichten."
            b "Wird nicht passieren."
            b "Du kennst mich."
            sis "Eben."
            "Was soll das heißen?"
            sis "Los, beeilen wir uns."
            
            jump eins_sisEinkaufen
            
        "Nein, ich kann nicht.":
            b "Ich weiß nicht, ob ich morgen Zeit habe."
            
    show laura pissed
    with dissolve

    sis "%(berndName)s..."
    sis "...wieso kannst du nicht ein einziges Mal wirklich nett zu mir sein?"
    b "Ich kann doch nichts dafür, dass..."
    sis "So ein Schwachsinn!"
    sis "Du willst mich doch gar nicht abholen!"
    sis "Warum sagst du es mir nicht einfach?"
    b "Was?"
    sis "Dass du mich hasst!"
    b "Aber ich hasse dich überhaupt nicht!"
    "Spinnt sie nun völlig?"
    "Wieso sollte ich sie denn hassen?"
    "Sie nervt zwar oft, aber Hass?"
    b "So ein Schwachsinn!"
    sis "Lüg mich nicht an!"
    sis "Wieso kümmerst du dich dann nie um mich?"
    sis "Andauernd sitzt du nur vor deinem Rechner."
    sis "Das ist doch nicht normal!"
    b "..."
    sis "Und dann lügst du mich immer an..."
    sis "Diese dummen Ausreden."
    sis "Wieso solltest du morgen keine Zeit haben?"
    sis "Gib einfach zu, dass du mich nicht abholen willst!"
    b "..."
    b "Das stimmt doch gar nicht..."
    sis "Du willst es also nicht zugeben..."
    sis "%(berndName)s...{w}ich hasse dich!"
    
    play music m_heul
    
    hide laura mad
    with dissolve
    
    "Sie dreht sich um und rennt los."
    b "Warte!"
    "...ich kann sie sowieso nicht einholen."
    "Sie ist schon um die Ecke."
    "Wahrscheinlich rennt sie nach Hause."
    "...und wahrscheinlich kriege ich dann gleich wieder Ärger."
    "Naja, damit muss ich mich später auseinandersetzen."
    "Zuerst muss ich noch einkaufen..."
    
    stop music fadeout 0.3
    
    scene black
    with fade
    
    $ renpy.pause(1.0)
    
    scene bg keller
    with fade
    
    play music m_bernd
    
    "Natürlich kriegte ich eine Menge Ärger, als ich wieder da war."
    "Aber morgen ist das eh wieder vergessen."
    "Das war bisher immer so."
    "Und wenn nicht morgen, dann übermorgen."
    "..."
    "...und wenn nicht?"
    "Ach was."
    "Das passiert schon nicht."
    "Laura war noch nie länger als zwei Tage sauer."
    "Wahrscheinlich hat sie es morgen früh schon vergessen."
    "Ich schau mal, was auf Krautchan los ist."
    
    scene black
    with fade
    
    $ renpy.pause(1.0)
    
    scene bg keller
    with fade
    
    #tür geht auf
    
    ma "%(berndName)s... kann ich reinkommen?"
    b "Na, wenn es sein muss..."
    #bild mutter
    b "Worum geht es denn?"
    "Als könnte ich mir das nicht denken."
    ma "Kannst du dir das nicht denken?"
    b "Nein, keine Ahnung."
    ma "Es geht um Laura!!"
    b "Oh."
    "Was sie nicht sagt..."
    "Ich spiele mal lieber den Ahnungslosen."
    b "Was ist mit Laura?"
    ma "Das weisst du doch ganz genau!"
    ma "Sie ist wirklich sauer!"
    b "Na und?"
    b "Die beruhigt sich wieder."
    ma "Das dachte ich ja auch..."
    ma "...aber dieses Mal bist du einfach zu weit gegangen."
    b "Und was soll ich jetzt dagegen machen?"
    ma "Woher soll ich das wissen?"
    ma "Lass dir was einfallen."
    ma "Das ist eine Sache, die du regeln musst."
    b "Aha."
    b "Ich warte erst mal ab. Vielleicht beruhigt sie sich ja morgen wieder."
    ma "Ob das so leicht wird..."
    b "Keine Sorge, das kriege ich hin."
    ma "..."
    ma "Wehe, wenn nicht."
    b "Jaja, nun geh schon."
    ma "..."
    "Sie verlässt das Zimmer widerwillig."
    "Endlich weiterlauern..."
    "...wie gut, dass ich Krautchan habe."
    "Mein Tag wäre sonst ziemlich einseitig." #lolwas xD
    "Oh, ein \"Gute Nacht\"-Faden."
    "...vielleicht ist das eine gute Idee."
    "Schließlich ist es schon spät."
    "...nur noch ein Mal auf /b/ gucken..."
    
    $ renpy.music.set_volume(0.0, .5, channel="music")
    
    scene black
    with fade

    $ renpy.pause(1.0)
    
    scene bg keller_blur
    with fade
    
    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    b "Ugh..."
    b "Wie spät ist es?"
    
    scene bg keller
    with dissolve
    
    "Ich werde langsam wach..."
    "Schon fast ein Uhr."
    "Wäre mal Zeit zum Aufstehen..."
    "Ich könnte auch mal wieder unter die Dusche..."
    "Schnell schalte ich den Rechner an und gehe nach oben."
    "Bis der hochgefahren ist, bin ich wieder da."
    
    scene bg wohnung_innen
    with fade
    
    ma "Ah, %(berndName)s!"
    "Auch das noch..."
    b "Äh... hi."
    ma "Wie war das mit Laura?"
    ma "Dass sie sich wieder beruhigt?"
    b "Hm?"
    ma "Als sie heute morgen zur Schule ist, war sie immer noch sauer."
    b "Aha."
    "Na und?"
    b "Sie kann aber nicht ewig sauer sein."
    ma "Ach, %(berndName)s!"
    ma "Du hast keine Ahnung von Frauen."
    b "..."
    ma "Glaub mir... {w}sie kann."
    ma "Bis du dich entschuldigst."
    b "Warum sollte ich?"
    ma "Weil ich es sage."
    b "..."
    "Das ist ein überzeugendes Argument."
    "Sie zahlt immerhin noch mein Internet."
    ma "Also?"
    b "Schon gut."
    b "Ich werde mich entschuldigen, wenn sie wieder da ist."
    ma "Sicher?"
    ma "Ich habe da eine bessere Idee..."
    
    scene black
    with fade
    
    stop music fadeout 0.2
    
    $ renpy.pause(1.0)
    
    scene bg schulweg1
    with fade
    
    "..."
    "Was für eine bescheuerte Idee."
    "Laura von der Schule abholen."
    "...als ob sie das wieder beruhigen würde."
    "Jetzt muss ich den ganzen Weg laufen."
    "VERDAMMT!"
    "Voller Wut trete ich gegen eine leere Dose, die auf dem Weg liegt, und sie fliegt scheppernd auf die Straße."
    "Da fällt es mir erst auf."
    "Es ist unheimlich still."
    "Zu still."
    "..."
    
    play music m_yasminStalk fadein 0.2

    
    "...und ich werde das Gefühl nicht los, dass mich jemand von irgendwo beobachtet."
    "..."
    "Ach was, ich bin nur paranoid wie immer."
    "...aber was wenn..."
    "Stalkerbernd?"
    "...was wenn er mich verfolgt?"
    "Es muss Stalkerbernd sein."
    "Oh, verdammt..."
        
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
            "Auch das beklemmende Gefühl ist verschwunden."
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
            
    stop music fadeout 0.3
            
    "Verdammt."
    "Nur noch 3 Minuten!"
    "Das schaffe ich ja nie!"
    "Ich sprinte die Straße runter und um die Ecke."
    
    scene bg schulweg2
    with fade
    
    "Verdammt... es ist noch viel zu weit!"
    "Das schaffe ich nie."
    "Noch fast ein ganzer Kilometer und nur eine halbe Minute Zeit."
    "Ich bin schon völlig außer Atem..."
    "Das schaffe ich nie."
    "Erschöpft bleibe ich stehen..."
    "Schon wieder versagt."
    "Ich versage jedes Mal."
    "Meine einzige Hoffnung ist, dass Laura diesen Weg nach Hause nimmt und hier vorbei kommt."
    "Also bleibt mir nichts als zu warten..."
    "..."
    "...aber es kommt niemand."
    "Nach 5 Minuten nicht."
    "Nach 10 Minuten nicht."
    "Nach 15 Minuten gehe ich nach Hause."
    "Das wird richtig Ärger geben..."
    "...ich kann froh sein, wenn ich meinen Internetzugang behalten darf."
    
    
    #------------------------------------
    #Bernd kommt wieder nach Hause
    #und sieht Stalkerbernd vor seinem Fenster
    #er verfolgt ihn, kriegt ihn aber nicht
    #Krautchan geht offline
    #und sprung auf Kapitel 2 mit Yasminroute
    
    
    scene black
    with fade
    
    "Zu Hause..."
    
    scene bg keller_aus
    with fade
    
    play music m_bernd

    "Ich habe mich extra leise in den Keller geschlichen."
    "Hoffentlich haben sie es nicht mitbekommen."
    "Jetzt habe ich wenigstens etwas Ruhe..."
    
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
            $ tentakel = True

        "Nein.":
            "NEIN!"
            "SAGE."
            $ tentakel = False


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
    "Ach so, der Ladebildschirm."
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
    "!"
    
    play music m_yasminStalk fadein 0.2
    
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
    
    play music m_bernd fadein 0.3

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
    
    #ENDE KAPITEL 1
    jump zwei_yasmin_Anfang
            
label eins_sisEinkaufen:
    #Einkaufen
    scene bg supermarkt
    with fade
    
    play music m_shop fadein 0.3
    
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
    sis "Ich geb' es dir zu Hause wieder!"
    sis "Ganz bestimmt!"
    "Hm..."
    b "Na gut, nimm dir eine Packung."
    show laura happy
    with dissolve
    sis "Danke, %(berndName)s."
    
    scene black
    with fade
    
    stop music fadeout 1.0
    
    jump eins_laura_hausaufgabenHelfen

label eins_laura_hausaufgabenHelfen: #Hausaufgaben helfen
    "Eine halbe Stunde später..."
    b "Endlich wieder zu Hause."
    
    scene bg keller
    with fade
    
    play music m_bernd
    
    b "Mal schauen, ob der Faden mit meinen Daten noch auf /b/ ist..."
    "..."
    b "Nichts."
    b "Glück gehabt."
    "Es scheint als wäre wirklich weiter nichts passiert..."
    "Bernd ist wohl wirklich völlig unfähig."
    
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
            $ sisFrage = True
        "0°":
            b "Das müssten 0° sein."
            $ sisFrage = False
        "Globalisierung":
            b "Das ist ganz sicher Globalisierung."
            sis "Sicher?"
            b "Sicher."
            $ sisFrage = None
    
    show laura happy
    with dissolve
    
    sis "OK, danke %(berndName)s!"
    sis "Jetzt krieg ich sicher eine gute Note."
    b "Kein Problem."
    
    show laura neutral
    with dissolve
    
    sis "Ach so..."
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
    
    $ renpy.music.set_volume(0.0, .5, channel="music")

    scene black
    with fade
    
    $ renpy.music.set_volume(1.0, .5, channel="music")
    
    #Am nächsten Morgen
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
    b "Ja ja."
    "Hektisch ziehe ich mich an, packe alles ein und mache mich auf den Weg."
    
    scene bg zuhause_draussen
    with fade
    
    play music m_wohnung
    
    "Jetzt muss ich mich aber beeilen."
    "Der Weg ist ziemlich weit, vor allem zu Fuß, und viel Zeit habe ich nicht mehr."
    "Wenn ich zu spät bin, wird Laura sicherlich sauer sein."
    "Vor allem weil ich es ihr versprochen habe."
    "Wenn es eines gibt, was sie überhaupt nicht ausstehen kann, ist es Unpünktlichkeit."
    "Eigentlich sollte sie das ja von mir schon kennen..."
    "Naja, was solls... {w}ich sollte mich lieber auf den Weg konzentrieren, sonst finde ich die Schule nicht rechtzeitig."
    
    scene bg schulhof
    with fade
    
    "Endlich da."
    "Ich bin gut in der Zeit."
    "Bis die Stunde vorbei ist, sind es noch etwa zwei Minuten."
    "Die ersten Schüler verlassen schon das Gebäude."
    "Wahrscheinlich hat ihr Lehrer sie früher rausgelassen."
    "Wenn ich mir die so ansehe..."
    "...warum geht meine Schwester mit solchen Leuten auf eine Schule?"
    "Verdammte Unterschicht!"
    
    play sound "sounds/schulgong.wav"
    
    "Oh, es klingelt."
    
    if sisFrage is not None:
        jump eins_laura_nachhauseweg
    
    else:
        jump eins_laura_globalisierung

label eins_laura_nachhauseweg:
    "...da kommt Laura angelaufen."
    
    show laura surprised
    with dissolve
    
    play music m_laura fadein 0.3
    
    sis "...was machst du denn hier?"
    b "Hast du es vergessen?"
    b "Ich hab dir versprochen, dass ich dich abhole."
    $ renpy.pause(1.5)
    
    show laura happy
    with dissolve
        
    sis "Wow... ich bin echt überrascht!"
    sis "Ich hätte nicht gedacht, dass du wirklich kommst."
    sis "Du bist ja sonst immer so unzuverlässig."
    b "Ich hab dich jetzt schon gestern und heute abgeholt."
    b "Ich bin nicht so unzuverlässig wie du denkst."
    sis "Du hast recht."
    sis "In letzter Zeit hast du dich gebessert."
    sis "Aber das reicht nicht."
    sis "Ich bin noch nicht überzeugt."
    b "...und was war mit den Hausaufgaben?"
    b "Damit habe ich dir doch auch geholfen!"
    
    if sisFrage == True: #richtige Antwort
        
        show laura neutral
        with dissolve
        
        sis "...das stimmt schon..."
        sis "Aber das reicht immer noch nicht!"
        sis "Du wirst mir von nun an immer bei meinen Aufgaben helfen!"
        b "..."
        "Das kann sie sich abschminken."
        "Ich hab Besseres zu tun. {w}Eigentlich nicht."
        "Aber ich mach es trotzdem nicht."
        sis "Du hast doch sowieso nie was zu tun."
        sis "Also kannst du dich doch wenigstens mal nützlich machen."
        b "Nein."
        
        show laura pissed
        with dissolve
        
        sis "Warum nicht?"
        b "Ich hab keine Lust."
        sis "Mensch, %(berndName)s."
        sis "Wieso bist du so gemein?"
        b "Ich bin nicht ..."
        
        show laura happy
        with dissolve
        
        sis "Ach, ich werde dich sowieso dazu bringen."
        b "Das glaube ich kaum."
        sis "Lass dich überraschen."
        sis "Aber jetzt gehen wir erst mal nach Hause."
        
        
    else: #falsche Antwort
        
        show laura pissed
        with dissolve
        
        sis "... die Antwort war aber falsch."
        
        show laura mad
        with dissolve
        
        sis "Ich habe mich vor der ganzen Klasse blamiert, {w}und du bist auch noch stolz drauf?!"
        sis "Das hast du doch mit Absicht gemacht!"
        b "Nein."
        b "Warum sollte ich sowas machen?"
        
        show laura pissed
        with dissolve
        
        sis "Gib es einfach zu!"
        b "Aber ich hab es nicht mit Absicht gemacht!"
                
        show laura mad_talk
        with dissolve      

        sis "Auf solche Aussagen kann ich gut verzichten."
        sis "Ist ja auch egal..."
        sis "Ich frage dich einfach nie wieder nach Hilfe."
        b "Soll mir recht sein."
        
        show laura pissed
        with dissolve
        
        sis "Du bist doof."
        sis "Wir gehen jetzt nach Hause."
        sis "Und ich will keinen doofen Kommentar von dir hören."
        b "OK, OK."
        
    scene bg schulweg2
    with fade
    
    play music m_wohnung fadein 0.2
    
    "Es ist so ruhig."
    "Sie redet doch sonst über alles Mögliche."
    "Vielleicht sollte ich das Gespräch anfan-{w}Nein."
    "Was denke ich mir eigentlich dabei?"
    "Sie nervt mich doch sonst nur wieder."
    "Mir gefällt diese Stille."
    
    scene black
    with fade
    
    "Wenig später..."
    
    scene bg schulweg1
    with fade
    
    "Sie ist immer noch ruhig."
    "Dabei sind wir schon fast zu Hause."
    b "%(sisName)s?"
    "Was mache ich hier eigentlich?"
    "Ich beschwere mich sonst immer, dass sie mich zutextet."
    "Und jetzt fange ICH das Gespräch an."
    "Irgendwas läuft hier falsch."
    
    show laura neutral
    with dissolve
    
    sis "Ja?"
    b "Bist du mir sehr böse?"
    
    show laura pissed
    with dissolve
    
    sis "Ja!"
    sis "Und jetzt sei ruhig."
    sis "Ich will da nicht drüber sprechen."
    b "Aber..."
    sis "Kein \"Aber\"!"
    b "Wie kann...{w}Wie kann ich das wieder gutmachen?"
    "Was rede ich hier überhaupt?"
    
    show laura surprised
    with dissolve
    
    sis "Hä?"
    sis "Wieso willst du das wieder gutmachen?"
    b "OK, dann nicht."
    sis "Warte."
    b "Nein."
    sis "Du kannst mir heute bei meinen Hausaufgaben helfen."
    b "Hmm...nein."
    
    show laura pissed
    with dissolve
    
    sis "Wieso nicht?"
    b "Damit ich mir wieder was anhören kann, wenn es falsch ist?"
    b "Nein, danke."
    sis "Mensch."
    sis "Du bist wirklich doof, %(berndName)s."
    
    scene bg zuhause_draussen
    with fade
    
    "Ich weiß nicht, wieso...{w}aber das Gespräch eben beruhigt mich."
        
    jump eins_laura_wiederZuhause

label eins_laura_globalisierung:
    "Die Menge der Kinder nimmt zu, aber Laura ist nicht zu sehen."
    "Wo bleibt sie denn?"
    "Sie ist doch sonst immer und überall die Erste..."
    "Ein Kind nach dem Anderen verlässt die Schule."
    "...wenn ich bedenke, dass Laura jeden Tag mit denen zur Schule gehen muss, tut sie mir irgendwie leid."
    "Typische Unterschicht."
    "Sie prollen mit ihren Billighandies und den Klingeltönen die sie sich vom Geld, das ihre Eltern nicht haben, runterladen."
    "...aber wo bleibt Laura?"
    "Vielleicht hat sie Klassendienst oder sowas?"
    "Ich warte noch zwei Minuten, dann gehe ich rein."
    "Die meisten Schüler sind schon gegangen."
    "Nur ein paar kommen ab und zu noch aus dem Gebäude, aber auch die werden immer weniger, bis schließlich niemand mehr zu sehen ist."
    "Laura ist nicht hier."
    "Sie ist nicht an mir vorbeigekommen, also ist sie noch drinnen."
    "...es reicht."
    "Ich gehe rein."
    
    scene bg schule_innen_1
    with fade
    
    play music m_schule fadein 0.2
    
    "Hm..."
    "Ich war hier noch nie drin."
    "Wo ist ihr Klassenraum?"
    "Ich weiß nicht mal, in welche Klasse sie geht."
    "Vielleicht sollte ich einfach hier warten..."
    "...nein."
    "Ich suche sie."
    "Egal wo."
    "Ich gehe einfach in irgendeinen Korridor."
    
    scene bg schule_innen_2
    with fade
    
    "Obwohl es unwahrscheinlich scheint, habe ich sie tatsächlich auf Anhieb gefunden."
    "Sie steht da vorne und redet mit jemandem."
    "Wer ist das?"
    "Ihr Lehrer?"
    "Ich gehe hin."
    
    show laura crying #at left
    with dissolve
    
    #lehrer wütend
    #with dissolve
    
    "Lehrer" "Dir ist klar, dass ich das nicht akzeptieren kann?"
    sis "...aber..."
    sis "Er war sich ganz sicher!"
    sis "Woher sollte ich wissen, dass es falsch ist."
    "Lehrer" "Mir ist völlig egal, wie sicher sich dein Bruder war."
    "Lehrer" "Sinus von \"Globalisierung\" ist nicht 1."
    "Oha..."
    "Scheint als hätte ich Mist gebaut."
    "Lehrer" "Wer sind Sie denn?"
    "Oh, er hat mich bemerkt..."
    
    show laura surprised #at left
    with dissolve
    
    sis "%(berndName)s!"
    sis "Was machst du denn hier?"
    "Na super..."
    "Lehrer" "Wer sind Sie?"
    "Lehrer" "Ich habe Sie noch nie hier gesehen."
    "Lehrer" "Gehen Sie auf diese Schule?"
    b "Nein."
    b "Ich bin Lauras Bruder."
    "Lehrer" "Oh."
    b "Ich bin hier um sie abzuholen."
    
    show laura happy #at left
    with dissolve
    
    "Lehrer" "Wie passend."
    "Lehrer" "Wir haben grade über Sie gesprochen."
    
    show laura sad #at left
    with dissolve
    
    b "Das habe ich mitbekommen."
    "Lehrer" "Dann wissen Sie, worum es geht?"
    "Wenn der hier einen auf Oberlehrer machen will, dann kann er das vergessen."
    "Dem werde ich es zeigen."
    "Geschwollen daherreden kann ja wohl jeder."
    b "Nein, klären Sie mich auf."
    "Lehrer" "Laura behauptet, dass Sie ihr gestern bei den Hausaufgaben geholfen hätten. {w}Stimmt das?"
    "Ich schaue sie an."
    b "Ja, das stimmt."
    b "Gibt es damit ein Problem?"
    b "Das wird wohl nicht verboten sein, oder?"
    "Lehrer" "Natürlich nicht."
    "Lehrer" "Es geht nur darum, dass die Antwort nicht ganz richtig war."
    b "Nicht ganz richtig?"
    b "Inwiefern?"
    "Lehrer" "Nun... {w}vielleicht habe ich mich nicht klar ausgedrückt."
    "Lehrer" "Die Antwort war so katastrophal falsch, dass ich nicht glauben kann, dass sie ernst gemeint ist."
    b "...und weiter?"
    "Lehrer" "Ich denke icht, dass \"Globalisierung\" eine akzeptable Antwort ist, und habe Grund zur Annahme, dass Sie versucht haben, Ihre Schwester reinzulegen."
    "Lehrer" "Das verurteile ich."
    
    show laura surprised #at left
    with dissolve
    
    sis "Aber..."
    b "Lass mich das regeln."
    "Mit dem alten werde ich allein fertig."
    b "Sie unterstellen mir also, dass ich so mit meiner Schwester umgehe?"
    "Lehrer" "In der Tat."
    b "Nun... ich kann ihnen versichern, dass das nicht meine Absicht war, und dass ich nach bestem Wissen und Gewissen geantwortet habe."
    "Lehrer" "Sie sind also der Meinung, dass der Sinus von \"Globalisierung\" 1 ist?"
    b "Absolut. {w}Haben Sie damit ein Problem?"
    "Lehrer" "Allerdings."
    b "...und können Sie mir erklären wieso?"
    "Lehrer" "Der Sinus ist eine Funktion, die sich auf den Winkel eines rechtwinkligen Dreiecks bezieht."
    "Lehrer" "Ich denke nicht, dass Globalisierung ein Winkel in einem  rechtwinkligen Dreieck ist."
    b "...und genau hier liegen Sie falsch."
    "Lehrer" "Was...!?"
    b "Jetzt sagen Sie bloß nicht, dass ihnen das Dreifaltigkeitsmodell der globalen Weltwirtschaftsbeziehungen nicht bekannt ist..."
    "Lehrer" "Tut mir Leid, aber ich unterrichte Wirtschaftslehre nicht."
    "Perfekt."
    "Ich habe seinen Schwachpunkt entdeckt."
    "Lehrer mögen zu ihrem Spezialgebiet eine Menge wissen, aber sobald man sie auf etwas anderes anspricht, haben sie keine Ahnung."
    "Nicht, dass ich Ahnung von Wirtschaft hätte, aber das muss er ja nicht wissen."
    b "Nun... lassen Sie mich erklären."
    "Lehrer" "Ich sehe nicht, wie uns das in dieser Situation weiterbringen könnte."
    b "Lassen Sie mich bitte ausreden?"
    "Lehrer" "Natürlich..."
    b "Das Dreifaltigkeitsmodell der globalen Weltwirtschaftsbeziehungen wurde 2004 von einem Expertenausschuss hier in Deutschland entwickelt und perfektioniert."
    "Ich zeichne mit dem Finger ein Dreieck in die Luft."
    b "Die unteren beiden Ecken sind die Wirtschaft und der Welthandel."
    b "Können Sie mir folgen?"
    "Lehrer" "Durchaus."
    b "Gut."
    b "Die obere Ecke... das ist die Globalisierung."
    "Lehrer" "Paradox."
    b "Inwiefern?"
    "Lehrer" "Die Globalisierung ist ein Resultat, keine Ursache."
    b "Das mag vor ein paar Jahren so gewesen sein."
    b "Heutzutage ist sie so stark ausgeprägt und im Weltwirtschaftssystem verankert, dass sie zu den Ursachen für bestimmte Phänomene gezählt wird."
    "Lehrer" "Davon habe ich noch nie gehört."
    b "Glauben Sie mir."
    b "Ich kenne mich besser mit Wirtschaft aus, als sie denken würden."
    "Lehrer" "Ich sehe trotzdem nicht, wie uns das jetzt weiterhilft..."
    b "Schauen Sie genau hin."
    b "Stellen Sie sich das Dreieck vor, und dann überlegen Sie wo die Globalisierung dort steht."
    "Lehrer" "Hm..."
    "Lehrer" "!!!"
    "Lehrer" "Unmöglich!"
    b "Nein!"
    b "Es ist genau so, wie Sie denken!"
    b "Der Winkel an der oberen Ecke entspricht genau 90°!"
    "Lehrer" "D- das kann nicht sein!"
    "Lehrer" "Dann würde das bedeuten..."
    b "...beide Antworten sind richtig."
    "Lehrer" "...unmöglich..."
    "Lehrer" "Mehrere mögliche Lösungsansätze..."
    "Lehrer" "...für eine Aufgabe."
    "Lehrer" "Davon habe ich noch nie gehört..."
    "Lehrer" "Ich werde dem auf jeden Fall nachgehen!"
    "Lehrer" "Wenn Sie mich nun entschuldigen würden?"
    "Er dreht sich um und geht in einen Klassenraum."
    
    #hide lehrer
    #with dissolve
    
    show laura happy
    with move
    
    sis "..."
    sis "Wow."
    "Dem hab ich es gezeigt."
    sis "Wie hast du das gemacht, %(berndName)s?"
    "Tja... wie habe ich das gemacht?"
    b "Gut, würde ich behaupten."
    sis "..."
    sis "Wow."
    "Dem hab ich es gezeigt."
    sis "Wie hast du das gemacht, %(berndName)s?"
    "Tja... wie habe ich das gemacht?"
    b "Gut, würde ich behaupten."    
    sis "Danke!"
    sis "Du hast mir echt geholfen."
    sis "...dass du mich überhaupt abholen kommst ist ja schon etwas Besonderes... {w}aber dann sowas." 
    b "Aber ich hab es dir doch versprochen."
    sis "Du versprichst mir öfters etwas und hältst es dann nicht ein."
    b "Das ist..."
    "Moment. {w}Das stimmt."
    sis "Dafür bin ich umso glücklicher, wenn du es einhältst."
    "Sie greift meinen rechten Arm und klammert sich um ihn."
    sis "Ich hab dich lieb, %(berndName)s."
    
    jump eins_laura_wiederZuhause
    pass

label eins_laura_wiederZuhause:

    stop music fadeout 0.4

    scene black
    with fade
    
    "Endlich wieder zu Hause..."
    
    scene bg keller
    with fade
    
    play music m_bernd    
    
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
    
    jump zwei_laura_anfang