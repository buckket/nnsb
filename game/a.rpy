#Inhaltsverzeichnis:
#label laura_anja_mail = Wechsel von Laura-Route auf Anja-Route
#label anja_anfang = direkte Anja-Route
#label bernd_anja_besprechung = menu "Soll ich zu Anja gehen? J/N"
#label anja_besprechung = Bernd geht zu Anja, Milch, Erwähnung des Tests
#label bernd_kapzwei_grillen = Bernd stirbt an Hautkrebs

label laura_anja_mail:

    "Aber was schreibe ich denn rein?"
    "Ich sollte meine neuen Mails nochmal abrufen."
    
    scene bg desktop_email
    with fade
    #Bild existiert noch nicht/neues Bild bitte mit verändertem Spam
    #muss auch noch registriert werden
    #ganz oben muss nochmal eine Mail von Anja stehen (schnuffel90@googlemail.com)
    
    "Neuer Spam."
    "Oh."
    "Bernd schrieb mir gestern Abend noch eine Mail."
    "Mal schauen, was da drin steht."
    
    scene bg desktop_hilfe
    with fade
    #Bild existiert noch nicht/neues Bild bitte mit neuem Text
    
    "gestern..."
    "heute..."
    "nicht geantwortet..."
    "bei dir vorbeikommen..."
    "Bernd"
    
    "Moment."
    "Bernd will vorbeikommen?"
    "In MEINEN Keller?"
    
    $ berndNameUpper = berndName.upper()
    ma "%(berndNameUpper)s!"
    "..."
    ma "%(berndNameUpper)s!"
    
    scene bg keller
    with fade
    
    "Was ist denn nun schon wieder?"
    "Kann ich nicht einmal meine Ruhe haben?"
    b "WAS IST DENN?"
    ma "KOMM SCHNELL!"
    "Aussagekräftige Beschreibung ist aussagekräftig."
    b "ICH KOMME JA SCHON."
    "Ich stehe auf und gehe nach oben."    
    "Ich öffne die Tür."
    
    scene bg kellertreppe
    with fade
    
    "Ich schaue die Kellertreppe nach oben."
    
    show blond neutral_g
    with dissolve    
    #Bild existiert noch nicht
    
    "Mädchen" "Oh, hai."
    b "wat"
    "Mädchen" "Kann ich runterkommen?"
    b "..."
    "Ich gehe einfach wieder in meinen Keller zurück."
    
    scene bg keller
    with fade
    
    "Ich schließe die Tür hinter mir."
    "Wie immer."
    "Was macht das Mädchen hier?"
    "Ist es wegen des Unfalls damals?"
    "Habe ich irgendwas Schlimmes getan?"
    "Ich setze mich wieder in meinen Stuhl."
    "Die Türe geht auf."
    
    show blond mad
    with dissolve
    #Bild existiert noch nicht
    
    "Mädchen" "Was ist los mit dir?"
    b "..."
    "Mädchen" "Du ignorierst mich einfach."
    b "..."
    "Mädchen" "Dabei habe ich dir doch noch eine Mail geschrieben, dass ich vorbeikomme."
    b "wat"
    "Mädchen" "Hast du die nicht gelesen?"
    b "D-D-Du bist ein Bernd?"
    "Mädchen" "Ja."
    "Mädchen" "Willkommen in der Wirklichkeit."
    b "Ein Mädchen? Ein Bernd?"
    "Mädchen" "Ja."
    b "lolwas"
    "Mädchen" "Nenn mich aber nicht immer Bernd."
    "Mädchen" "Ich hab auch einen Namen."
    "Mädchen" "Ich heiße %(wBerndName)s."
    b "Aha."
    bw "Ja."
    "Komm endlich zur Sache."
    bw "Wir müssen Krautchan retten."
    b "Und wie soll ich dir dabei helfen?"
    bw "Weiß ich noch nicht."
    b "Auch: Was ist denn mit Krautchan passiert?"
    bw "Der Server wurde beschlagnahmt."
    "Server beschlagnahmt."
    b "So so."
    bw "Ja."
    bw "Von der Polizei."
    bw "Die genauen Einzelheiten kenne ich auch nicht."
    bw "Ich weiß nur, dass der Server eines Morgens von der Polizei beschlagnahmt wurde."
    bw "Deshalb brauch ich deine Hilfe."
    b "Und wie sollen wir da was machen?"
    bw "Weiß ich nicht."
    b "Und warum bist du dann hier?"
    bw "Weil du nicht geantwortet hast."
    b "Und woher willst du das alles wissen?"
    bw "..."
    bw "Du vertraust mir nicht?"
    "Wieso sollte ich?"
    b "Bernd, das ist lächerlich!"
    b "..."
    bw "Denk drüber nach."
    bw "Und komm morgen zu mir."
    b "Wohin?"
    bw "Zu mir."
    "Intelligente Antwort."
    b "Und wo wohnst du?"
    bw "Weißt du das nicht?"
    bw "Ich wohne im Stockwerk über dir."
    "Was zum?"
    "Bernds? In MEINER Stadt?"
    "Das lässt sich wohl in Berlin nicht vermeiden."
    bw "Ich muss dann jetzt auch wieder weg."
    bw "Bis morgen, %(berndName)s."
    b "..."
    
    hide blond mad
    with dissolve
    
    "Sie war genauso schnell weg wie sie kam."
    "Ich"
    "Hmm..."
    "Krautchans Server wurde also beschlagnahmt."
    "Von der Polizei."
    "Grund: unbekannt."
    "Woher weiß sie eigentlich davon?"
    "Sie scheint mehr zu wissen, als sie mir eigentlich weiß machen will."
    "Ich sollte morgen zu ihr gehen."
    "Aber jetzt gehe ich erstmal schlafen."
    "Ich habe in den letzten Nächten kaum geschlafen."
    
    scene black
    with fade
    
    "Am nächsten Tag..."
    
    scene bg keller_aus_blur
    with fade
    
    "Langsam werde ich wach."
    "Ich schaue auf die Uhr."
    "Es ist 13:19 Uhr."
    
    scene black
    with fade
    
    "Lasst mich noch schlafen."
    
    scene bg keller_aus
    
    "WAS?!"
    "Wir haben 13 Uhr schon durch?"
    "Ich habe wirklich lange geschlafen."
    "Ich sollte mich beeilen, wenn ich noch zu %(wBerndName)s will."
    "Andererseits sollte ich mich nicht so hetzen."
    "Der Tag hat ja schließlich noch ein paar Stunden."
    "Und sie wohnt nur ein Stockwerk weiter oben."
    
    jump anja_besprechung
    
#---------------------------------------------------------------------------------------

label anja_anfang:

    scene bg keller
    with fade

    "wat"
    "F5 F5 F5 F5 F5 F5 F5 F5 F5 F5"
    "RAAAAAAAAAAAAGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEE"
    "Sie hatte verdammt nochmal Recht."
    "Ich kann es nicht glauben."
    "Was soll ich jetzt bloß machen?"
    "4chan?"
    "Nein."
    "4chan ist der Krebs."

    $ berndNameUpper = berndName.upper()
    ma "%(berndNameUpper)s!"
    "Oh Gott, nicht die schon wieder."
    ma "KOMMST DU MAL EBEN?"
    b "JA."

    scene bg kueche
    with fade

    ma "Wie war denn das Treffen?"
    b "Wie soll es schon gewesen sein?"
    b "Und wieso interessiert dich das?"
    ma "Na ja, du bist nun 25."
    b "Und weiter?"
    ma "Und du hattest noch keine Freundin."
    b "Ach, nicht das schon wieder."
    ma "Aber es ist nur normal für eine Mutter sich Sorgen zu machen."
    b "Du weißt, dass ich kein Interesse an einer Freundin habe."
    ma "Ich weiß."
    ma "Du sitzt den ganzen Tag im Zimmer und schaust deine Männekes."
    ma "Und sie wäre wirklich nichts für dich?"
    ma "Wie hieß sie noch gleich?"
    ma "%(wBerndName)s oder so?"
    b "Was willst du eigentlich?"
    b "Du hast sie noch nicht einmal gesehen."
    ma "Also eher nicht."
    b "Ach, lass mich doch in Ruhe."
    "Genervt gehe ich zurück in meinen Keller."

    scene bg keller
    with fade

    "Was soll ich jetzt nur tun?"
    "Ob sie wohl Recht hatte?"
    "Ob Krautchan wirklich übernommen worden ist?"
    "Dass Tsaryu nach Japan ausgewandert ist..."
    "Gut möglich."
    "Aber Shaky?"
    "Ist er wirklich nach Mexiko geflohen?"
    "Ach Quatsch."
    "Der doch nicht."
    "Andererseits habe ich auch lange nichts mehr von ihm gehört."
    "Und dergeneral?"
    "Untergetaucht?"
    "Haha, der doch nicht."
    "Ich finde, dergeneral ist ein cooler Typ. Re ist EXPERTENPROGRAMMIERER und ist vor nichts Angst."
    "Allerdings verhält er sich in letzter Zeit komisch."
    "Wie..."
    "Wie..."
    "...ein kleines Kind."
    "Ja, das trifft es genau."
    "Er verhält sich in letzter Zeit wie ein kleines Kind."
    "Vielleicht ist wirklich was dran."
    "Aber wieso sollte Krautchan übernommen worden sein?"
    "Das macht immer noch keinen Sinn."
    "Wegen Pest?"
    "Als ob."
    "Hmmm..."
    "Was könnte wohl der Grund sein?"
    "Hmmm..."
    "Vielleicht weiß %(wBerndName)s mehr als sie mir bisher weiß gemacht hat."
    "Ich glaub, ich geh morgen mal zu ihr."
    "%(wBerndName)s wird mir ihre Adresse ja bestimmt nicht umsonst gegeben haben."
    "Ob sie wohl auf mich wartet?"
    "Ach Quatsch."
    "Warum sollte sie?"
    "Hmmm..."
    "Ich frage mich, wie ihr Zimmer wohl aussehen mag."
    "Es ist bestimmt ein typisches Mädchenzimmer."
    "Aber wie sieht ein typisches Mädchenzimmer aus?"
    "Ich war ja noch nie bei einem Mädchen im Zimmer."
    "Gute Frage."
    "Wie sieht ein typisches Mädchenzimmer aus?"
    "Helle Tapeten?"
    "Ja."
    "Die Tapeten werden wahrscheinlich eine helle Farbe haben."
    "Und sie wird bestimmt auch irgendwo Kuscheltiere rumstehen haben."
    "Kawaii desu, ne?"
    "Das Bett wird so schön weich sein."
    "Und es wird nach Parfum riechen."
    "Hmm..."
    "Hmmmmmm..."
    "Hmmmmmmmmmmmm..."
    "Ein plötzliches Gefühl riss mich aus dem Schwärmen."
    "Ich kam."
    #Mir ist hier auf Anhieb nix Besseres eingefallen.
    #Vielleicht fragt sich Bernd, ob da auch Dildos rumstehen, wie er es von Kamerahuren kennt.
    #Statt „Ich kam.“ vielleicht auch „Ich kam unkontrolliert.“
    "Hach..."
    "%(wBerndName)s..."

    scene black
    with fade

    scene bg keller_blur
    with fade

    "Ich gähne."
    #Sieht dumm aus, aber wie soll man das sonst darstellen?
    "Ich bin noch so müde."
    "Ich würde am liebsten noch ein bisschen weiterschlafen."
    "Aber ich wollte heute ja %(wBerndName)s besuchen."
    "Ich gähne nochmal und strecke mich dabei."
    #Wie stellt man ein Recken und Strecken dar?
    "Ich reibe mir durch die Augen"

    scene bg keller
    with fade

    "Ich bin so fertig mit der Welt."
    "Ich hätte doch nicht so lang wach bleiben sollen."
    "Ich gähne. Aber daran lässt sich auch nichts mehr ändern."
    "Ich erhebe meinen Körper."
    "Mit hängenden Armen wandere ich ins Badezimmer als plötzlich..."

    play sound "sounds/hit_1.wav"
    #Sound noch nicht vorhanden

    "Uhhhh, das hört sich nicht gut an."
    "Aber was war das?"
    "Nicht wissend, aus welcher Richtung das Geräusch kam, schaue ich aus Reflex nach rechts."
    "Doch da ist nichts."
    "Ich schaue nach links."
    "Wieder nichts."
    "Stimme" "HIIIIILLLLLLLFFFFFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!"
    "..."
    "Das klang nach %(sisName)s."
    "Ich sprinte in ihr Zimmer."

    scene bg lauraszimmer
    with fade
    

    "Ich sehe Laura auf einem Stuhl stehen."

    show sis scared
    with dissolve
    #Bild fehlt noch

    b "Was ist los, %(sisName)s?"
    $ berndNameUpper = berndName.upper()
    sis "%(berndNameUpper)s!, HILFE!"
    sis "DA."
    b "Was ist da?"
    sis "EINE...EINE...EINE...EINE SPINNE!"
    b "Ich laufe langsam zu meiner Schwester hin."
    b "Nun stell dich mal wegen einer Spinne nicht so an."
    b "Ich greife nach meinem Schuh."
    b "Hö?"
    b "Wo ist mein Schuh?"
    "Ich laufe immer noch barfuß durch die Gegend."
    b "Hast du hier etwas, womit ich sie platt machen kann?"
    sis "NEIN."
    sis "MACH' SIE PLATT."
    sis "SCHNELL."
    "Einfacher gesagt als getan."
    b "Ich geh eben einen Schuh holen."
    b "Ich bin gleich wieder da."
    sis "Was?"
    sis "Du...Du willst mich alleine lassen?"
    sis "MIT DEM RIESENVIECH DA?"
    b "Ich bin jeden Moment wieder zurück."
    b "Halte bitte noch so lang aus."

    scene bg hausflur
    with fade

    "Ich renne aus dem Zimmer raus auf der Suche nach einem Schuh."
    b "Irgendwo muss hier doch ein Schuh sein."
    b "Da ist ja einer."
    "Ich spurte wieder zurück zu meiner Schwester."

    scene bg lauraszimmer
    with fade
    
    b "Bin schon wieder zurück."
    sis "SCHNELL. Sie krabbelt davon."
    b "Nicht bewegen, %(sisName)s."
    b "Warte nur."
    b "Mir entkommst du nicht."
    "Ich hole weit aus."
    sis "Das kann ich mir nicht mit ansehen."

    show sis closed_eyes
    with dissolve
    #Bild existiert nicht
    #Vielleicht die Hände vor die Augen halten
  
    "FLATSCH!"
    sis "Ist sie nun weg?"
    b "Ja."
    b "Du kannst die Augen wieder öffnen."
    #Hier könnte ich den Grad des Angstzustandes indirekt nennen.
    #Da ich aber nicht weiß, wie das Bild aussieht, lasse ich es ab hier offen.
    #Szene zu Ende schreiben
    
    scene bg keller_aus
    with dissolve
    
    "Ich sollte mich beeilen."
    "Die Spinne hat zu viel Zeit gekostet."
    "Die Spinne..."
    "Spinne..."
    "Kum0!"
    "Oh, Moment."
    
    scene bg badezimmer
    with dissolve
    
    "Ich ziehe mich aus und stelle mich auf die Waage."
    "Verdammt."
    "Schon wieder zugenommen."
    "Und alles nur FETT."
    "Ob %(wberndName)s wohl auch Leute mit meinem Aussehen mag?"
    "Eher nicht."
    "Wahrscheinlich steht sie mehr auf Muskeln."
    "Sie ist halt auch nur ein Mädchen."
    "Ich sollte wirklich mal etwas für meine Figur tun."
    "Ich werde von Tag zu Tag dicker."
    "Ich sollte Sport machen."
    "Sport?"
    "Nein."
    "Lieber nicht."
    "Ich sollte weniger Chips essen."
    "Das könnte ich hinbekommen."
    "So."
    "Noch eben die Türe abschließen."
    "Damit nicht wieder das Gleiche wie letztens passiert."
    "Ach, %(wberndName)s."
    "Nein."
    "Ich kann nicht schon wieder auf %(wberndName)s fappieren."
    "Nicht schon wieder."
    "Ich darf einfach nicht."
    "Obwohl..."
    menu:
        " "
        
        "Ich fappiere auf sie.":
            "Ich schließe meine Augen."
            "Ich stelle mir vor, wie ich meine Arme um sie lege."
            "Ich drücke sie ganz nah an mich dran."
            "Die Welt um uns herum verschwindet."
            "Es gibt nur noch uns beide."
            "Ich flüstere ihr \"Ich liebe dich\" ins Ohr."
            "Sie haucht mir leise ins Ohr zurück."
            $ berndNameUpper = berndName.upper()
            sis "%(berndNameUpper)s, ICH MUSS AUF KLO!"
            "Was?"
            "Verdammt."
            sis "JETZT MACH ENDLICH DIE TÜR AUF!"
            "%(sisName)s hämmert gegen die Türe."
            "Und ich war so kurz davor."
            sis "MACH DIE TÜR AUF!"
            sis "ICH WILL MIR NICHT IN DIE HOSEN MACHEN!"
            "Ich lege mir schnell ein Handtuch um und mache die Tür auf."
        
            show sis angry_talk
            with dissolve
        
            sis "Du wartest draußen."
            b "Draußen?"
            b "Aber hier hole ich mir den Tod."
            sis "Mir egal."
            sis "Ich hab Vorrang."
        
            scene bg keller_aus
            with dissolve
        
            "Eigentlich war ich sowieso schon fertig."
            "Muss mich nur noch abtrocknen."
            "Und anziehen."
            "Und fertig fappieren."
            "Hmm..."
            "Jetzt habe ich auch keine Lust mehr."
            "Ich trockne mich ab und ziehe mich dann an."
            
        
        "Nein, sie ist zu rein.":
            "Ich stelle das Wasser der Dusche kälter ein."
            "Ich muss mich davon ablenken."
        
            scene black
            with dissolve
        
            scene bg keller_aus
            with dissolve
        
            "Einmal kalt duschen und man möchte nicht mehr."
            "Genau nach keikaku."

    "So."
    "Damit wäre ich eigentlich fertig."
    
    scene bg zuhause_drinnen
    with fade

    "Ich gehe nochmal alles durch."
    "Sicher ist sicher."
    "Es ist immerhin das erste Mal, dass ich bei einem Mädchen bin."
    "Und dann noch bei so einem süßen."
    "Also..."
    "Gefrühstückt und geduscht habe ich."
    "Mit Deo habe ich mich auch eingesprüht."
    "Schuhe auch nochmal extra geputzt."
    "So, ich bin bereit."
    "Ich sollte mich nun auch wirklich auf den Weg machen."
    
    scene black
    with fade
    
    scene bg zuhause_drinnen
    with fade
    
    "So, angezogen bin ich nun auch."
    "OK."
    "Nun folgt also der schwierige Teil."

    scene bg treppenhaus
    with fade
    #Bild existiert noch nicht

    scene bg tuere
    with fade
    #Bild existiert noch nicht
    
    "Ich stehe nun vor ihrer Türe."
    "Ich will anklopfen, doch meine Hand stoppt ein paar Zentimeter vor der Türe."
    "Was soll ich denn sagen, wenn jemand aufmacht?" 
    "Plötzlich fühlte ich Unsicherheit."
    "Werde ich mich wirklich in einem Mädchenzimmer wohl fühlen?"
    "Was?"
    "Ich war noch nie in so einer Situation."
    "Ich umklammerte mich selbst."
    "Das Gefühl der Unsicherheit in mir wurde immer stärker."
    "Was ist nur los, %(berndName)s?"
    "Jetzt bist du schon so weit gekommen."
    "Warum traust du dich nicht mehr weiter?"
    "Ich nehme meinen ganzen Mut zusammen."
    "Ich klopfe."
    "Ich warte."
    "Nichts passiert."
    "Ich höre aber jemanden reden."
    "Nun lacht jemand."
    "Vielleicht wurde mein Klopfen einfach überhört."
    "Moment."
    "Vielleicht ist dieser jemand %(wBerndName)s."
    "Und sie lacht über mich."
    "Sie hat ihre Freundinnen eingeladen."
    "Und sie warten nur darauf, dass ich komme."
    "Um mich dann auszulachen."
    "Das war doch bisher immer so."
    "Warum sollte sich auch ein Mädchen mit mir abgeben?"
    "Ich bin so dumm, dass ich darauf reingefallen bin."
    "Andererseits..."
    "Woher kannte sie sonst Krautchan?"
    "So bekannt ist das nun auch wieder nicht."
    "Sie muss ein Krautchannutzer sein."
    "Sonst wüsste sie doch nichts davon."
    "Ich darf jetzt nicht davonlaufen."
    "Ich darf einfach nicht."
    "Ich klopfe nochmals."
    "Ich höre immer noch jemanden reden, aber niemand macht auf." 
    "Ich drehe mich um."
    "Ich laufe los."
    "Plötzlich höre ich das Knatschen einer Türe."
    "Die Tür, vor der ich mich so fürchtete zu berühren, geht auf."
    "Plötzlich kehrt die Unsicherheit zurück."
    "Ich will wegrennen, doch..."
    "Mein Körper hört nicht mehr auf mich."
    "Wie angewurzelt stehe ich vor der Türe."
    "Scheiße."
    "Was mache ich jetzt?"
    
    show yandere surprise at left
    with dissolve
    #Bild existiert noch nicht

    "Wer ist das denn?"
    "Und warum starrt sie mich so an?"
    "Kann sie nicht woanders hinschauen?"
    "Sie nervt."
    "Aber irgendwie..."
    "ist sie auch süß."

    show blond neutral_g at right
    with dissolve

    bw "Hallo, %(berndName)s."
    b "Hi."

    show yandere neutral at left
    with dissolve
    #Bild existiert noch nicht

    yan "Wer ist das, %(wBerndName)s?"
    bw "Das ist nur %(berndName)s."
    "Was soll hier \"nur\" heißen?"
    bw "Er ist nur ein Nachbarsjunge."
    "Nachbarsjunge?"
    "Will die mich verarschen?"
    "Ich dachte, ich wäre ihr sympathisch."
    "Sie braucht mich also nur für Krautchan."
    "Hätte ich mir ja gleich denken können."

    show yandere embarassed at left
    with dissolve
    #Bild existiert noch nicht

    yan "Oh, hi."
    b "..."
    "Ich will sprechen."
    "Aber ich kann nicht."
    b "..."
    yan "Du musst wohl einer von der schüchternen Sorte sein."
    bw "Oh ja, %(berndName)s ist sehr schüchtern."
    "Ich bin immer noch nicht in der Lage zu sprechen."
    yan "Na dann, ich muss jetzt los."
    yan "Tschau, %(wBerndName)s."
    bw "Tschüss, %(yanName)s."
    yan "Tschau, %(berndName)s."
    b "Tsch-Tschüss."

    scene bg treppenhaus
    with fade
    #Bild existiert noch nicht

    show yandere from_behind
    with dissolve
    #Bild existiert noch nicht

    "Ich sehe nur noch, wie das Mädchen die Treppen runtergeht."
    
    bw "%(berndName)s."
    "Ich drehe mich wieder um."

    scene bg tuere
    with fade
    #Bild fehlt noch

    show berndw glasses neutral
    with dissolve

    b "..."
    bw "H-A-L-L-O?"
    b "..."
    bw "Na ja, komm' erstmal rein."
    "Ich drehe mich zur Treppe hin."

    scene bg treppenhaus
    with fade
    #Bild fehlt noch

    bw "Was ist los?"
    "Ich gehe einfach."
    bw "%(berndName)s?"
    "Einfach nur weiterlaufen."
    bw "HALLO? Was ist los mit dir?"
    "Einfach nur weiterlaufen."
    "Ich bin die Treppe schon zur Hälfte runtergelaufen."
    bw "Dann halt nicht."
    "Ich bleibe kurz stehen."
    "Dann laufe ich einfach weiter."
    "Ich stehe nun vor der Wohnungstüre."
    "War das wirklich richtig?"
    "Ja."
    "Ich habe nichts falsch gemacht."
    "Nein."
    "Ich habe es richtig gemacht."
    "Ja."
    "Ich habe nichts falsch gemacht."
    "Sie hat mich doch schlecht gemacht."
    "Ja."
    "Es ist ihre Schuld."
    "Ja."
    "Nicht meine."
    "Nein."
    "Ich öffne die Türe."

    scene bg wohnung_innen
    with fade

    "Ich ziehe meine Schuhe aus."
    "Dann gehe ich direkt in meinen Keller."

    show sis neutral
    with dissolve

    $ berndNameKurz = stringShorten(berndName,2)
    sis "%(berndNameKurz)s-"
    "Ich laufe einfach an ihr vorbei."
    "Ich will jetzt meine Ruhe."
    sis "%(berndName)s?"

    scene bg keller_aus
    with fade
 
    "Ich werfe erstmal meinen Computer an."

    scene bg keller
    with fade

    "Ich will mich auf andere Gedanken bringen."
    "Wie immer öffne ich als erstes meinen Browser und öffne Krautchan."
    "404..."
    "Achja..."
    "Was mach ich denn jetzt?"
    "Zum Glück gehe ich auf mehr Seiten als nur Krautchan wie zum Beispiel ..."
    "zum Beispiel..."
    "Öhm..."
    "Ohne Krautchan hat mein Leben einfach keinen Sinn."
    #Hier könnte man ein Bild von KC bringen, wie es nicht erreichbar ist. KÖNNTE.

    "Ich schau einen Anime."
    "Aber welchen?"
    "Ich öffne meine Animepartition."
    "Nein."
    "Nein."
    "Der nicht."
    "Nicht dieser."
    "Der schon wieder? Lieber nicht."
    #Hier könnte man ein Bild von einer Animepartition bringen. KÖNNTE.

    "Hmm..."
    "Ach, ich kann mich einfach nicht auf andere Gedanken bringen."
    "Ich muss immer wieder an vorhin denken."
    "Ich geh schlafen."
    "Ich werfe mich aufs Bett."
    "Ob es vorhin richtig war, einfach so zu gehen?"
    "Ja."
    "Sie ist ja Schuld."
    "Dass ein Mädchen mich abweist."
    "Wie immer."
    "Ich kenne es nicht anders."
    "Aber das selbst eine Bernadette einen Bernd abweist."
    "Irgendwie traurig."
    "Liegt wohl doch an mir und nicht am Berndsein."
    #den oberen Abschnitt nochmal durchgehen wegen PC-Bildern

    scene bg black
    with fade

    "Stimme" "He, %(berndName)s."

    scene bg keller_blur
    with fade
 
    "Stimme" "Aufstehen."
    b "Ja ja."
    "Ich reibe mir einmal durch die Augen."

    scene bg keller
    with fade

    show sis neutral
    with dissolve
    "Es ist %(sisName)s."
    sis "Das Abendessen ist fertig."
    b "Ist ja gut."
    sis "Ich geh schon mal vor."
    "Ich setze mich aufrecht hin."
    "Ich lasse mir die Sache mit %(wberndName)s nochmal durch den Kopf gehen."
    "Ich wollte sie besuchen."
    "Sie kommt mit ihrer Freundin raus."
    "Die Freundin..."
   
    menu:
        " "
       
        "...ist irgendwie süß.":
            jump von_anja_zu_yasmin
       
       
        "ist irgendwie süß. NICHT!":
            $ yanlove -=5
            #Anspruchsvoller Bernd ist anspruchsvoll und ihr Aussehen gefällt ihm nicht. Nettigkeit? HUARGH
    
    "Ich sollte erstmal das Essen holen gehen."
   
    scene bg kueche
    with fade
   
    ma "Oh, %(berndName)s."
    ma "Wie war es bei %(wberndName)s?"
    b "Nicht das schon wieder."
    b "Sie ist nicht das, was du dir wünschst."
    ma "Also lief es nicht so gut?"
    b "*seufz*"
    "Also gut."
    
    menu:
        " "
        
        "Ich erzähle es ihr.":
            $ malove +=5
            b "Also gut."
            b "Ich erzähle es dir."
            b "Ich wollte zu ihr."
            b "Aber sie war nicht da."
            ma "Sie war nicht da?"
            b "Nein."
            ma "Na, dann."
            ma "Gehst du morgen dann wieder zu ihr?"
            b "Ich weiß noch nicht."
            b "Wahrscheinlich nicht."
            ma "Wieso nicht?"
            b "..."
            ma "Läuft es schlecht?"
            b "Ja."
            ma "Dabei habe ich mich so darauf gefreut sie mal kennenzulernen."
            "Sie hat ja keine Ahnung."
            b "..."
            "Ohne ein weiteres Wort zu sagen gehe ich wieder zurück in meinen Keller."
        
        
        "Lass mich in Ruhe.":
            $ malove -=5
            b "Kannst du mich nicht einmal damit in Ruhe lassen?"
            ma "Jetzt sei doch nicht so, %(berndName)s."
            "Ich nehme mir mein Essen und gehe wieder zurück in meinen Keller."
    
    scene bg keller
    with fade
    
    "So, endlich habe ich wieder meine Ruhe."
    "Was nun?"
    "Mal schauen..."
    "Spiele?"
    "Nicht beim Abendessen."
    "Internet?"
    "Ach, nee."
    "Ohne KC ist das Internet so fad."
    "Ich schau einen Anime."
    "Hmm..."
    "Mal schauen, ob eine neue Folge Strike with Cheese rausgekommen ist."
    "Oh, schon die elfte Folge."
    "Bald ist der Anime vorbei."
    
    scene bg black
    with fade
    
    $ berndNameUpper = berndName.upper()
    ma "%(berndNameUpper)s!"
    "..."
    ma "%(berndNameUpper)s!"
    
    scene bg keller
    with fade
    
    "Was ist denn nun schon wieder?"
    "Kann ich noch nicht einmal in Ruhe meine Kampflolis schauen?"
    b "WAS IST DENN?"
    ma "KOMM SCHNELL!"
    "Aussagekräftige Beschreibung ist aussagekräftig."
    b "ICH KOMME JA SCHON."
    "Ich stehe auf und gehe nach oben."
    #Gefällt mir so nicht.
    #Eventuell vorher schreiben, dass Bernd Animu glotzt und was da gerade so passiert. Dann schreit die Mutter und er
     #drückt Pause.
    
    "Ich öffne die Tür."
    
    scene bg kellertreppe
    with fade
    
    "Ich schaue die Kellertreppe nach oben."
    
    show blond neutral_g
    with dissolve    
    #Bild existiert noch nicht
    
    bw "Oh, hai."
    b "wat"
    bw "Kann ich runterkommen?"
    b "..."
    "Ich gehe einfach wieder in meinen Keller zurück."
    
    scene bg keller
    with fade
    
    "Ich schließe die Tür hinter mir."
    "Wie immer."
    "Ich setze mich wieder in meinen Stuhl."
    "Die Türe geht auf."
    
    show blond mad
    with dissolve
    #Bild existiert noch nicht
    
    bw "Was ist los mit dir?"
    b "..."
    bw "Du ignorierst mich einfach."
    b "..."
    "Du nervst."
    bw "Was habe ich dir getan?"
    b "..."
    "Sei ruhig."
    bw "Was ist jetzt?"
    b "..."
    "Geh weg."
    bw "Weswegen kamst du heute zu mir?"
    b "..."
    "Geh einfach."
    bw "Sprechenden Leuten kann man helfen, %(berndName)s."
    b "..."
    "Geh sterben."
    
    show blond really mad
    with dissolve
    #Bild existiert noch nicht
    
    bw "Ach, %(berndName)s."
    bw "Wenn du wenigstens mal was sagen würdest."
    bw "So schüchtern kannst selbst du nicht sein."
    b "..."
    bw "Ist es wegen %(yanName)s?"
    b "Wer?"
    bw "AHA!"
    bw "Du hast etwas gesagt."
    "Verdammt."
    
    show blond mad
    with dissolve
    #Bild existiert noch nicht
    
    bw "Jetzt will ich nur noch wissen, warum du mich ignorierst."
    b "Denk mal nach."
    bw "Ich hab schon nachgedacht."
    bw "Ich weiß es nicht, sonst wäre ich jetzt nicht hier."
    bw "Traust du mir nicht, weil ich vorher wusste, dass KC off gehen würde?"
    b "Das ist es nicht."
    bw "Hab ich dich irgendwie verletzt?"
    bw "Hab ich irgendwas Falsches gesagt?"
    b "..."
    bw "Ich habe also was Falsches gesagt."
    bw "Aber was?"
    bw "Hat es vielleicht doch etwas mit %(yanName)s zu tun?"
    b "..."
    bw "Also doch."
    bw "Was machte ich falsch?"
    bw "Sag es mir."
    b "Du..."
    b "Du..."
    bw "Was?"
    b "Du sagtest, das..."
    bw "Ich sagte was?"
    bw "OH, WARTE."
    bw "Ich sagte, du seist nur ein Nachbarsjunge."
    bw "Und du kommst damit nicht klar, habichrecht?"
    b "..."
    bw "Ich hab Recht."
    bw "Ach, %(berndName)s."
    
    show blond doppelpunkt_drei
    with dissolve
    
    bw "Was soll ich nur mit dir machen?"
    bw "Aber irgendwie süß von dir."
    bw "Dass du dich deswegen anstellst."
    
    show blond neutral_g
    with dissolve
    
    bw "Na ja, auf jeden Fall tut es mir Leid."
    bw "Ich hab das nicht böse gemeint."
    b "..."
    bw "Wie ich sehe, willst du gerade Animu schauen und essen."
    bw "Sollen wir uns dann morgen bei mir treffen?"
    bw "Du kannst ja irgendwann morgen vorbeikommen."
    b "...oder auch nicht."
    bw "Oder so."
    bw "Ich werde auf jeden Fall morgen den ganzen Tag zu Hause sein."
    b "Mir egal."
    b "Ich werde nicht kommen."  
    bw "Bis morgen, %(berndName)s."
    "Hört sie mir überhaupt zu?"
    bw "Tschüss."
    b "..."
    "Sie dreht sich um und geht aus dem Keller raus."
    "Sie macht die Tür hinter sich zu."
    "Etwas, das meine Mutter nie macht, wenn sie aus dem Keller rausgeht."
    "Ich höre sie noch die Kellertreppe hochstapfen."
    
    "Ich wende mich wieder dem Bildschirm zu."
    "Endlich."
    "Endlich kann ich Animu schauen."
    
    scene bg black
    with fade
    
    scene bg keller
    with fade
    #Wie stellte ich das besser dar?
    
    "Hmm..."
    "Erstmal schauen, ob schon ein Faden darüber auf Krautcha-"
    "OH, WARTE."
    "Hmm..."
    "Vielleicht auf Vier-"
    "NEIN!"
    "Was mache ich denn nun?"
    "So langweilig."
    "Ich geh schlafen."
    
    scene bg black
    with fade
    
    "Am nächsten Tag."
    
    scene bg keller_blur
    with fade
    
    "Hmm..."
    "Hmmmm....."
    "Aigis."
    "Deine Hände..."
    "Ahhhh~"
    "Bitte..."
    "Nimm ihn in den Mund!"
    $ renpy.pause(0.5)
    "Mit Sack!"
    $ renpy.pause(0.5)
    "Der muss stinken!"
    $ renpy.pause(0.5)
    "Aigis."
    "Das ist so schön."
    "Deine Lippen..."
    "so weich."
    "Ahhhh~"
    "Ahhhhhhhh~"
    "Oh, Aigis."
    "Ich liebe dich."
 
    scene bg keller_aus
    with fade
    
    "Hach, das war so gut."
    "Wenn ich das doch nur wirklich erleben dürfte."
    "Ich bin so ronery."
    "Ich kenne keine Mädche-"
    "Oh, warte."
    "Vergiss das."
    "Andererseits..."
    "Soll ich %(wberndName)s wirklich glauben?"
    "Soll ich wirklich zu ihr gehen?"
    "Sie könnte auch ein guter Troll sein."
    "Krautchan geht bestimmt auch wieder."
    "Ich stehe auf und setze mich an meinen PC."
    "Dann schalte ich den Computer an."
    
    "Dann kann ich jetzt erstmal auf Badezimmer gehen."
    
    scene bg black
    with fade
    
    $ renpy.pause(2)
    
    "Ich gehe wieder zurück in meinen Keller."
    
    scene bg keller
    with fade
    
    "Oh."
    "Schon hochgefahren?"
    "Das ging aber erstaunlich schnell."
    "Normalerweise braucht der doch seine halbe Stunde zum Hochfahren."
    "Ich hätte jetzt *wirklich* Lust auf einen neuen PC."
    "Na ja, egal."
    "Für Internet und Anime reicht der noch."
    "Ich öffne meinen Internetbrowser."
    "Wie immer drücke ich automatisch Strg + L und tippe dann \"kr\" ein."
    "Dann drücke ich mit der Pfeiltaste einen runter und drücke Enter."
    "Es lädt nor-"
    "404."
    "Verdammt."
    "Ich hätte nie gedacht, dass ich das jemals sagen werde."
    "Aber damit ist das Internet für mich gestorben."
    "Hmm..."
    "Was mache ich denn jetzt?"
    "Mein PC ist zu schlecht für Spiele."
    "Und nur Anime und Manga ist langweilig."
    "Ich sollte..."
    
    menu:
        " "
        
        "doch zu %(wberndName)s gehen.":
            jump bernd_anja_besprechung
        

        "mir einen Job suchen.":
            jump bernd_kapzwei_grillen

label bernd_anja_besprechung:

    "Ja."
    "Ich sollte zu ihr gehen."
    "Aber soll ich wirklich nachgeben?"
    "Bei einem Mädchen?"
    "Bei einem Bernd?"
    "Ich?"
    "Niemals!"
    "Ich nicht!"
    "Nein!"
    "So tief bin ich nun auch noch nicht gesunken."
    "Ich habe doch auch meinen Stolz."
    "Ich kann doch nicht..."
    "Allerdings ist ein Leben ohne KC kein Leben."
    "Ich hab ja sonst nichts zu tun."
    "Ich sollte zumindest ihre Hilfe ausnutzen." 
    "Ja."
    "Ich werde sie ausnutzen."
    "Aber nicht jetzt."
    jump anja_besprechung
    
label anja_besprechung:
    "Erst..."
    
    menu:
        
        "Erst schaue ich Animu.":
            scene bg desktop_none
            with fade
        
            "Mal sehen."
            "Oh."
            "Kot Gayass ist fertig."
            "Den werde ich nun schauen."
        
            scene black
            with fade
        
            scene bg desktop_none
            with fade
        
            "Hmm..."
            "Ich würde C.C...."
            "wenn ich könnte!"
            "Aber eine Anya ist auch fein."
            "Ich hab nichts mehr zum Schauen."
        
                
        "Ich hab gerade eh nichts Besseres zu tun.":
            $ wBerndLove += 5
    
    "Ich geh mal auf Krautchan."
    "404."
    "Ach ja."
    "Ich vergaß."
    "Ich wollte mich deswegen ja mit %(wBerndName)s treffen."
    "Geduscht habe ich ja gestern."
    "Dann mache ich mich mal auf den Weg."
    
    scene black
    with fade
    
    scene bg tuere
    with fade
    #Bild existiert noch nicht
    
    "Irgendwie habe ich kein gutes Gefühl."
    "Ich sollte einfach wieder gehen."
    "Moment."
    "Dann kommt sie nachher einfach wieder in meinen Keller."
    "Ich sollte einfach klingeln."
    "Ich bin ein Bernd."
    "Sie ist ein Bernd."
    "Wir wollen Krautchan retten."
    "Mehr gibt es da nicht."
    "Ich klopfe an die Türe."
    "Stimme" "Ich komme gleich."
    "..."
    $ renpy.pause(1.5)
    "..."
    $ renpy.pause(1.5)
    "..."
    $ renpy.pause(1.5)
    "..."
    "Ich klopfe nochmals."
    "Stimme" "JAAAAA, ich komme gleich."
    "..."
    $ renpy.pause(0.5)
    "Ich klopfe nochmal."
    "Ich klopfe immer fester gegen die Türe."
    "Ich klopfe ununterbrochen gegen die Türe."
    "Stimme" "JAAAAHAAAAA!"
    "Stimme" "Ich komme doch."
    "..."
    "Ich höre jemanden rennen."
    "Jemand drückt die Türklinke runter."
    "Die Tür öffnet sich."
    
    show blond neutral_g
    with dissolve
    
    bw "Oh, hai."
    b "Ja ja."
    b "Also."
    b "Du sagtest, ich soll vorbeikommen."
    bw "Ja."
    bw "Komm doch rein."
    "Ich trete ein."
    
    scene bg anjas_wohnung
    with fade
    #Bild existiert noch nicht
    
    show blond neutral_g
    with dissolve
    
    "Nett."
    "Nichts Außergewöhnliches."
    bw "Komm mit in mein Zimmer."
    b "..."
    "Ich folge ihr kommentarlos."
    "Wozu sollte ich auch dafür etwas sagen?"
    
    scene bg anjas_zimmer
    with fade
    #Bild existiert noch nicht
    
    show blond neutral_g
    with dissolve
    
    "Das ist also ihr Zimmer."
    bw "Setz dich."
    bw "Ich hole eben was zu trinken."
    
    hide blond neutral_g
    with dissolve
    
    "Ich setze mich auf das Bett."
    "Es ist weich."
    "Ganz anders als meins."
    "Bei mir macht es keinen Unterschied, ob man auf dem Fußboden liegt oder im Bett."
    "Ich lasse meinen Blick durch das Zimmer schweifen."
    "PLÖTZLICH: Glurak."
    "Eine Plüschfigur davon."
    b "JA MAN GLUARK!"
    bw "FICK JA!"
    
    show blond neutral_g
    with dissolve
    
    b "..."
    "Sie steht mit zwei Gläsern wieder im Zimmer."
    bw "Du wirst aber schnell wieder ruhig."
    bw "Ich hab dir ein Glas Milch mitgebracht."
    b "Milch? In MEINEM Glas?"
    b "Zum Trinken?"
    bw "Ja."
    bw "Natürlich zum Trinken."
    b "Wieso würdest du das tun?"
    bw "Einfach so."
    b "..."
    "Ich nehme das Glas entgegen."
    bw "Du bist also doch gekommen."
    b "Ja."
    bw "Ja."
    b "Wegen Krautchan."
    bw "Ja."
    b "Was ist nun?"
    bw "Wir müssen Krautchan retten."
    "Wir?"
    b "Ja."
    b "Ich weiß."
    b "Was willst du tun?"
    bw "Ich werde Krautchan retten."
    "Sie?"
    b "Ja."
    b "Wie?"
    bw "weissnichlol."
    
    show blond happy_g
    with dissolve
    
    $ renpy.pause(1.0)
    "Stille."
    $ renpy.pause(1.0)
    "Stille."
    "Wie in einem Anime, in dem gerade ein schlechter Witz gemacht wurde."
    "Nur, dass es diesmal in der Wirklichkeit so ist."
    
    show blond serious_g
    with dissolve
    
    b "Sch-"
    bw "Ich werde dich erstmal testen."
    "Testen?"
    b "Testen?"
    bw "Ja."
    "Was zum?"
    b "Wieso?"
    bw "Weil du dich gestern komisch verhalten hast."
    b "Wie verhielt ich mich denn?"
    bw "Komisch."
    "Geniale Antwort ist genial."
    "NICHT."
    $ renpy.pause(0.5)
    bw "Dabei dachte ich, dass jeder Bernd auch an die schlimmsten Sachen gewöhnt wäre."
    bw "Deswegen werde ich dich testen."
    b "Aha."
    b "Und wie?"
    bw "Weiß ich noch nicht."
    b "Und was soll ich dann hier?"
    
    show blond happy_g
    with dissolve
    
    bw "Ich wollte mich mal ein bisschen mit dir unterhalten."
    bw "Wir kennen uns doch kaum."
    b "Aha."
    b "Und worüber?"
    bw "Unzulässige Information."
    b "Ist das eine Anspielung?"
    bw "Unzulässige Information."
    b "Was wird passieren, wenn ich beim Test versage?"
    bw "Unzulässige Information."
    b "%(wBerndName)s?"
    bw "Ja?"
    b "Können wir das alles erstmal vergessen?"
    bw "Klar."
    b "Darf ich dir vielleicht eine einzige Frage stellen?"
    bw "Und was willst du wissen?"
    b "Ich möchte einfach gern wissen, wie alt du bist."
    bw "Unzulässige Information."
    b "Yuki ist sowieso überlegen."
    bw "Yuki ist eine modifizierte Rei."
    b "Eine Rei ist auch fein."
    bw "Ja."
    b "Ja."
    $ renpy.pause(1.0)
    "Oh wow. Ein QUALITÄTSGESPRÄCH!"
    bw "Deine Milch."
    b "Was ist damit?"
    bw "Du hast sie noch nicht getrunken."
    "Ich setze das Glas Milch vor mein Gesicht."
    "Ich schaue auf das weiße Getränk."
    "Dann nehme ich einen großen Schluck von der Milch."
    "Es ist köstliche Milch."
    "Wirklich erfrischend."
    "Deliziös."
    bw "Die Milch ist übrigens nicht FETTreduziert."
    "Ich setze das Glas kurz ab."
    b "FICK JA."
    b "FETT."
    b "Lecker."
    "Ich trinke weiter."
    "Das Glas ist leer."
    b "MEER!"
    b "MEER MILCH!"
    bw "Du scheinst Milch zu lieben."
    b "Milch ist die Butter der Getränke."
    b "Beweise mich falsch."
    bw "Komm mit in die Küche."
    bw "Du brauchst keine Angst zu haben."
    bw "Ich bin gerade sowieso alleine hier."
    b "OK."
    "Ich laufe ihr hinterher."
    
    scene bg anjas_kueche
    with fade
    
    show blond happy_g
    with dissolve
    
    bw "Hier."
    bw "Genieße deine Milch."
    "Ich bekomme noch ein Glas randvoll gefüllt mit Milch in die Hand gedrückt."
    "Ich stelle es erstmal auf den Tisch ab."
    "Dann trinke ich einen Schluck ab, damit nichts beim Hochheben verschüttet."
    "Doch ich trinke einfach weiter."
    "Ich kann nicht mehr aufhören."
    "Dieses Gefühl."
    "Es fühlt sich so gut an."
    "So erfrischend."
    "Ich liebe dieses Gefühl."
    "Ich liebe Milch."
    "Ich liebe das Leben."
    "Ich vergesse alles um mich herum."
    "Mir ist gerade alles egal."
    
    play sound "sound/telefon.wav"
    #da muss ein besserer Sound rein
    
    "Plötzlich geht das Telefon."    
    "Ich werde aus meinen Träumen gerissen."
    "%(wBerndName)s läuft zum Telefon und schaut auf das Display."
    bw "Oh, es ist nur meine Mutter."
    "Dann nimmt sie den Hörer ab."
    bw "Ja, Mama?"
    bw "Milch?"
    bw "Nein, wir haben keine mehr."
    bw "Ich trank sie vorhin aus."
    "Ich trank ihnen die Milch weg."
    bw "OK."
    bw "Sonst noch etwas?"
    bw "OK."
    bw "Bis nachher."
    "Sie legt den Hörer wieder auf."
    bw "Sorry, %(berndName)s."
    bw "Ich muss jetzt einkaufen gehen."
    bw "Lass uns morgen nochmal reden."
    "Ich könnte ihr ja anbieten, dass ich ihr hel-"
    "OH WARTE"
    "Wieso bin ich eigentlich so gut drauf?"
    b "OK."
    bw "Ich komm dann morgen zu dir."
    "Wieso zu mir?"
    b "OK."
    "Und wieso stimme ich einfach so zu?"
    bw "Ich werde mir bis morgen auch was für den Test einfallen."
    "Wir gehen in den Flur."
    
    scene bg anjas_wohnung
    with fade
    
    "Sie zieht sich an."
    bw "So, %(berndName)s."
    bw "Ich geh jetzt einkaufen."
    bw "Du solltest nach Hause gehen."
    b "OK."
    "Ich trete aus der Wohnung aus."
    
    scene bg treppenhaus
    with fade
    
    "Sie schließt die Wohnung ab."
    bw "Bis morgen, %(berndName)s."
    b "..."
    "Sie rennt die Treppe runter."
    "Ich sollte auch nach Hause gehen."
    "Hier rumstehen bringt mir nichts."
    
    scene black
    with fade
    
    scene bg keller_aus
    with fade
    
    "Ich schau erstmal einen Anime."
    "AKAGI!"
    "FICK JA!"
    "QUALITÄTSNASEN!"
    
    jump kapitel_3

label bernd_kapzwei_grillen:

    "Hahaha oh wow."
    "Arbeit? In meinem Leben?"
    "Ich vergesse das lieber mal direkt wieder."
    "Aber ich könnte echt mal was in meinem Leben verändern."
    
    scene bg black
    with fade
    
    "Einige Monate später."
    
    "Stimme" "Oh, seine Augen."
    "Stimme" "Er bewegt seine Augen."
    
    "Diese Stimme."
    $ sisNameKurz = stringShorten(sisName,3)
    "%(sisNameKurz)s..."
    $ sisNameEnde = stringEnde(sisName,2)
    "...%(sisName)s..."
    sis "Da."
    sis "Er kommt zu sich."
    
    scene bg krankenzimmer_blur
    with fade
    
    "Wo..."
    "Wo bin ich?"    
   
    show sis sadsmile at left
    with dissolve
    
    show doc at right
    with dissolve
    #Bild existiert noch nicht
    
    ma "Wie geht es ihm, Herr Doktor?"
    "Arzt" "Wir können leider nicht mehr allzu viel für ihn tun."
    #Step sagte, ich solle ihm glaube, dass "Arzt" reicht
        
    show sis sad at left
    with dissolve
    
    ma "Was heißt das?"
    "Arzt" "Der Krebs ist schon zu weit fortgeschritten."
    "Arzt" "Wir können es nur noch verlangsamen."
    ma "Wie konnte es nur soweit kommen?"
    "Arzt" "Er hat empfindliche Haut."
    "Arzt" "Und hat sich zu lange der Sonne ausgesetzt."
    sis "Heißt das, dass %(berndName)s sterben wird?"
    ma "..."
    "Arzt" "Es tut mir Leid."
    sis "Ich will nicht, dass er stirbt."       
 
    show sis crying at left
    with dissolve
    
    ma "Ist schon gut..."
    "Ich heb meine linke Hand leicht."
    b "Komm her."
    b "%(sisName)s."
    
    show sis sad at left
    with dissolve
    
    sis "Ja?"
    b "Hör auf."
    b "Hör auf zu weinen."
    sis "Aber..."
    sis "aber..."
    sis "%(berndName)s."
    
    show sis crying at left
    with dissolve
    
    b "Das ist ja nicht auszuhalten."
    b "Hör endlich auf zu weinen."
    sis "Wie soll ich denn aufhören?"
    sis "Du wirst sterben."
    b "Aber du hast doch immer noch Mama."
    
    sis "Aber Mama reicht mir nicht."
    sis "Ich..."
    "Ich gebe meiner Mutter und dem Arzt eine Handbewegung, dass sie rausgehen sollen."
     
    hide doc
    with dissolve
       
    show sis crying
    with dissolve
            
    if sislove >= 75: 
        #muss eventuell angepasst werden
        
        "Ich richte mich einigermaßen auf, sodass ich nun auf dem Bett sitze."
        b "%(sisName)s."
        sis "Ich will nicht, dass du stirbst."
        sis "Immerhin bist du..."
        sis "Ich bin ..."
        b "Ich weiß, was du sagen willst."
        
        show sis sad
        with dissolve
        
        b "Ich weiß auch, dass ich es dir nie gesagt habe."
        b "Aber ich liebe dich."
        
        show sis sadsmile
        with dissolve
        
        sis "Ach, %(berndName)s."
        sis "Ich hab dich auch lieb."
        b "Also, versprich mir, dass du stark bist und nicht mehr weinst."
        b "Einverstanden?"
        sis "Einverstanden."
        b "Auch, wenn ich sterben sollte."
        b "Ich möchte nicht, dass du wegen mir weinst."
        sis "OK."
    
    if sislove < 75:
        #muss eventuell angepasst werden
        
        b "Also hör auf zu weinen."
        b "Das kann ich nicht mit ansehen."
        b "Erbärmlich."
        b "Und du sagst, dass du ein großes Mädchen wärst?"
        b "Dann hör auf zu weinen."
        sis "Aber..."
        b "Kein aber, %(sisName)s."
        sis "OK."
        sis "Ich versuch's."
                
    scene owari
    with fade
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
label von_anja_zu_yasmin:

    $ yanLove += 5
    "Aber ich werde sie wahrscheinlich nie wieder sehen."
    #auf das Aussehen eingehen
    "blablubb"
