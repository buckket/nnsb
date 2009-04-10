#Inhaltsverzeichnis:
#label laura_anja_mail = Wechsel von Laura-Route auf Anja-Route
#label anja_anfang = direkte Anja-Route
#label bernd_anja_besprechung = menu "Soll ich zu Anja gehen? J/N"
#label anja_weiter = statt des Wechsels auf Y geht es bei A weiter
#label anja_besprechung = Bernd geht zu Anja, Milch, Erwähnung des Tests
#label bernd_kapzwei_grillen = Bernd stirbt an Hautkrebs
#label von_anja_zu_yasmin = Wechsel von A auf Y

label laura_anja_mail:

    "Aber was schreibe ich denn rein?"
    "Ich sollte meine neuen Mails nochmal abrufen."
    
    scene bg desktop_email
    with fade
    #Bild existiert noch nicht/neues Bild bitte mit verändertem Spam
    #muss auch noch registriert werden
    #ganz oben muss nochmal eine Mail von Anja stehen (schnuffel90@googlemail.com)
    
    "Neuer Spam."
    "Löschen."
    "ALLES!"
    "Oh."
    "schnuffel90@googlemail.com."
    "Die E-Mail ist von gestern."
    "Was wohl drin steht?"
    "Ich öffne die Mail."
    #Ausbaufähig im Sinne von: GSB schon wieder? Der ist ganz schön nervig usw.
    
    scene bg desktop_hilfe
    with fade
    #Bild existiert noch nicht/neues Bild mit neuem Text bitte
    
    "gestern..."
    "heute..."
    "nicht geantwortet..."
    "bei dir vorbeikommen..."
    "Bernd"
    
    "Moment, Moment, Moment."
    "Bernd will zu mir kommen?"
    "In MEINEN Keller?"
    "Weil ich mich nicht mit ihm traf?"
    "Er scheint es wirklich ernst zu meinen."
    "Also stimmte alles?"
    "Krautchan gibt es schon nicht mehr."
    "Bernd hatte recht."
    "Ich soll ihm helfen."
    "OK."
    "Aber wie?"
    
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
    "Warum kommt immer nur ein \"KOMM SCHNELL!\", wenn ich nachfrage?"
    "Ich hasse sowas."
    b "JAJA!."
    "Ich stehe auf und ..."    
    
    play sound "sounds/metaldooropen.wav"
        
    scene bg kellertreppe
    with fade
    
    "Ich schaue die Kellertreppe nach oben."
    
    show anja neutral
    with dissolve    
    
    u"Mädchen" "Oh, hai."
    b "..."
    "Wer ist das denn?"
    u"Mädchen" "Kann ich runterkommen?"
    b "Nein."
    "Ohne ein weiteres Wort gehe ich einfach wieder in meinen Keller zurück."
    
    scene bg keller
    with fade
    
    "Ich schließe die Tür hinter mir."
    
    play sound "sounds/metaldooropen.wav"
    
    "Wie immer."
    "Was macht ein Mädchen hier?"
    "Was macht DAS Mädchen hier?"
    "Ist es wegen des Unfalls damals?"
    "Will sie mich nun deswegen anschwärzen?"
    "Habe ich irgendwas Schlimmes getan?"
    "Ich setze mich wieder in meinen Stuhl."
    
    play sound "sounds/metaldooropen.wav"
    
    show anja angry
    with dissolve
        
    u"Mädchen" "Was ist los mit dir?"
    b "..."
    "Lass mich einfach in Ruhe."
    u"Mädchen" "Du ignorierst mich einfach."
    b "..."
    "Geh einfach."
    u"Mädchen" "Dabei habe ich dir doch noch eine Mail geschrieben, dass ich vorbeikomme."
    b "..."
    u"Mädchen" "Hast du die nicht gelesen?"
    b "Moment."
    b "Eine E-Mail?"
    b "DIE E-Mail?"
    
    show anja neutral
    with dissolve
    
    u"Mädchen" "Ja."
    b "D-D-Du bist ein B-B-Bernd?"
    u"Mädchen" "Ja."
    u"Mädchen" "Willkommen in der Wirklichkeit."
    b "Ein Mädchen? Ein Bernd?"
    u"Mädchen" "Ja."
    b "Was zum?"
    u"Mädchen" "Nenn mich aber nicht immer Bernd."
    u"Mädchen" "Ich hab auch einen richtigen Namen."
    u"Mädchen" "Ich heiße %(wBerndName)s."
    b "Aha."
    bw "Ja."
    b "Ja."
    bw "Ja."
    b "Komm endlich zur Sache."
    bw "Wir müssen Krautchan retten."
    b "Und wie soll ich dir dabei helfen?"
    bw "Weiß ich noch nicht."
    b "Was ist denn eigentlich mit Krautchan passiert?"
    bw "Der Server wurde beschlagnahmt."
    b "Server beschlagnahmt."
    b "Soso."
    bw "Ja."
    bw "Von der Polizei."
    b "Polizei."
    b "Soso."
    bw "Die genauen Einzelheiten kenne ich auch nicht."
    bw "Ich weiß nur, dass der Server eines Morgens von der Polizei beschlagnahmt wurde."
    bw "Deshalb brauche ich deine Hilfe."
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
    b "Aha."
    b "Und wo wohnst du?"
    bw "Weißt du das nicht?"
    "Woher sollte ich?"
    b "Nein."
    bw "Ich wohne..."
    bw "...im Stockwerk über dir."
    
    #show blondbernd_hämisches_grinsen -> Umbennenung & Registrierung erforderlich
    #with dissolve
    #Bild existiert noch nicht
    #K1
    
    "Was zum?"
    bw "Du siehst irgendwie sprachlos aus."
    b "..."
    bw "OH MEIN GOTT!"
    bw "SCHAU DOCH NUR AUF DIE UHR!"
    bw "Ich muss jetzt auch wieder weg."
    bw "Bis morgen, %(berndName)s."
    b "..."
    
    hide anja
    with dissolve
    
    "Sie war genauso schnell weg wie sie kam."
    "Ich kann es immer noch nicht glauben."
    "Sie wohnt direkt über mir."
    "Ich überhörte vor Fassungslosigkeit sogar das Quietschen der Türe."
    "Ich sollte das irgendwie verarbeiten."
    "Ich schlafe da mal ein bis zwei Stunden drüber."
    "Hmm..."
    "Ich lasse mir alle Details nochmal durch den Kopf gehen."
    "Krautchans Server wurde beschlagnahmt."
    "Von der Polizei."
    "Grund: unbekannt."
    "Woher weiß sie eigentlich davon?"
    "Woher wusste sie, dass Krautchan off gehen würde?"
    "Woher will sie wissen, dass die Polizei dahinter steckt?"
    "Es könnte doch genauso gut Jemand gewesen sein, der sowas zum Spaß macht."
    "Ein Hacker."
    "Das macht meiner Meinung nach mehr Sinn."
    "Sie scheint mehr zu wissen, als sie mir eigentlich weiß machen will."
    "Ich sollte morgen zu ihr gehen."
    "Sie wohnt ja direkt über mir."
    "Was?"
    "Irgendwie komme ich mir immer noch dumm vor."
    "Aber sie scheint es locker zu nehmen."
    "In einer Großstadt lässt es sich nicht vermeiden, dass es mehrere Bernds gibt."
    "Besonders in Berlin nicht."
    "Das war mir vorher schon klar."
    "Vor allem, wenn sich ein Bernd schon berlinbernd nennt."
    "Aber..."
    "Bernds? In MEINEM Mehrfamilienhaus?"
    "Ich muss das verarbeiten."
    "Ich muss mich ablenken."
    "Ich sollte mir was zu essen holen."
    
    
    #Situation für abends
    #Siehe dafür ins Forum
    #BUTTERGOTT
    
    
    
    
    
    "Am nächsten Tag..."
    
    scene bg keller_aus_blur
    with fade
    
    "Langsam werde ich wach."
    "Ich schaue auf die Uhr."
    "Es ist 13:42 Uhr."
    
    scene black
    with fade
    
    "Lasst mich noch schlafen."
    "Es ist doch erst Zwanzig vor Zwei."
    
    scene bg keller_aus
    
    "WAS?!"
    "Es ist schon so spät?"
    "Ich habe wirklich lange geschlafen."
    "Ich sollte mich beeilen, wenn ich noch zu %(wBerndName)s will."
    "Andererseits sollte ich mich nicht so hetzen."
    "Der Tag hat ja schließlich noch ein paar Stunden."
    "Und sie wohnt nur ein Stockwerk weiter oben."
    
    jump anja_besprechung
    
#---------------------------------------------------------------------------------------

label anja_anfang:

    scene bg desktop_none
    with fade
    
    "Bitte wie?"
    "Liegt wohl an meiner Verbindung."
    "F5."
    "404."
    "Diese Verbindung hier regt mich auf."
    "F5."
    "404."
    "Das geht so nicht."
    "F5."
    "404."
    "Jetzt reicht es mir."
    "Google..."
    "...geht."
    "Krautchan..."
    "...geht nicht."
    "Wieso nicht?"
    "Ich kann es nicht glauben."
    "Sie hatte verdammt nochmal Recht."
    "Was soll ich jetzt bloß machen?"
    "Zurück zum Vierka-"
    "Nein."
    "Das ist der Krebs."

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
    b "Du weißt, dass ich kein Interesse an einer Freundin habe, oder?"
    ma "Ich weiß, %(berndName)s."
    ma "Das sagst du immer."
    ma "Aber ich kann dir nicht glauben, dass du keinerlei Interesse hast."
    b "Es ist aber so."
    ma "Du sitzt den ganzen Tag im Zimmer und schaust deine Männekes."
    b "Anime, Mutter, Anime."
    ma "Aber sie wäre wirklich nichts für dich?"
    ma "Wie hieß sie noch gleich?"
    ma "%(wBerndName)s oder so?"
    b "Nein."
    b "Außerdem..."
    b "Was willst du eigentlich?"
    b "Du hast sie noch nicht einmal gesehen."
    ma "Also eher nicht."
    b "Ach, lass mich doch in Ruhe."
    b "Ich geh schlafen."
    b "Gute Nacht."
    "Genervt gehe ich eilig zurück in meinen Keller."

    scene bg keller_aus
    with fade

    "Was soll ich jetzt nur tun?"
    "Ob sie wohl Recht hatte?"
    "Ob Krautchan wirklich übernommen worden ist?"
    "Dass Tsaryu nach Japan ausgewandert ist, ist gut möglich."
    "Aber Shaky?"
    "Ist er wirklich nach Mexiko geflohen?"
    "Ach Quatsch."
    "Schüttli hat doch kein Geld für sowas."
    "Andererseits habe ich auch lange nichts mehr von ihm gehört."
    "Allerdings war er auch eher ein Mitläufer."
    "dergeneral kümmerte sich ja um das Meiste."
    "Apropos dergeneral."
    "Der soll untergetaucht sein?"
    "Haha, der doch nicht."
    "Ich finde, dergeneral ist ein cooler Typ. Re ist EXPERTENPROGRAMMIERER und ist vor nichts Angst."
    "Aber er verhält sich in letzter Zeit komisch."
    "Wie ein kleines Kind."
    "Ja, das trifft es genau."
    "Er verhält sich in letzter Zeit wie ein kleines Kind."
    "Vielleicht ist wirklich was dran."
    "Aber wieso sollte Krautchan übernommen worden sein?"
    "Das macht immer noch keinen Sinn."
    "Hmmm..."
    "Was könnte wohl der Grund sein?"
    "Vielleicht weiß %(wBerndName)s mehr als sie mir bisher weiß gemacht hat."
    "Ich sollte morgen mal zu ihr gehen."
    "%(wBerndName)s wird mir ihre Adresse ja bestimmt nicht umsonst gegeben haben."
    "Sie wartet bestimmt darauf, dass ich bei ihr \"spontan\" vorbeikomme."
    "Warum sonst brach sie die beiden Treffen nach kurzer Zeit ab?"
    "Sie ist doch auch nur ein Bernd."
    "Das heißt sie kann im wirklichen Leben auch nicht allzu beschäftigt sein."
    "Sie will, dass ich bei ihr vorbeikomme."
    "Sie wartet auf mich."
    "Ach Quatsch."
    "Warum sollte sie?"
    "Hmmm..."
    "Was wohl sein wird, wenn ich sie morgen besuche?"
    "Sie wird mir bestimmt auch was zu trinken anbieten."
    "Chance auf einen indirekten Kuss?"
    "Eher gering."
    "Dann müssten wir ja schon aus dem selben Glas trinken."
    "Oder aus der selben Flasche mit dem Mund trinken."
    "Und das wird wahrscheinlich nicht geschehen."
    "Hmm..."
    "Wie ihr Zimmer wohl aussehen mag?"
    "Es ist bestimmt ein typisches Mädchenzimmer."
    "Aber wie sieht ein typisches Mädchenzimmer aus?"
    "Ich war ja noch nie bei einem Mädchen im Zimmer."
    "Gute Frage."
    "Wie sieht ein typisches Mädchenzimmer aus?"
    "Helle Tapeten?"
    "Wahrscheinlich."
    "Die Tapeten werden wahrscheinlich eine helle Farbe haben."
    "Das Zimmer wird auf jeden Fall nicht so duster wie mein Keller sein."
    "Und sie wird bestimmt auch irgendwo Kuscheltiere rumstehen haben."
    "Sie hat bestimmt eine Plüschfigur von Hello, Kitty."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Wie süß!"
    if persistent.wieherbuhSprache is 1:
        "Kawaii desu, ne?"
    if persistent.wieherbuhSprache is 2:
        "{=jp}かわいいですね。{/=jp}"
    #-----------------------------------------------
    "Hat nicht jedes Mädchen heutzutage eine Figur von Hello, Kitty?"
    "Und die Figur wird nach %(wBerndName)s riechen."
    "Das Zimmer wird nach ihr riechen."    
    "Und ich werde auf ihrem Bett sitzen."
    "Es wird schön weich sein."
    "Nicht so hart und unnachgiebig wie meins."
    "Hmm..."
    "Ich kann nicht, %(wBerndName)s..."
    "Wenn du so weitermachst..."
    "Ich kann jetzt nicht mehr..."
    "Hmmmmm...."
    "%(wBerndName)s..."
    "Schnell."
    "Ein Taschentuch."
    "AH-HAH!"
    "Hach..."
    "%(wBerndName)s..."

    scene black
    with fade

    "Am darauffolgenden Tag..."
    
    scene bg keller_blur
    with fade

    "*Gähn*"
    "Ich bin noch so müde."
    "Ich würde am liebsten noch ein bisschen weiterschlafen."
    "Aber ich wollte heute ja %(wBerndName)s besuchen."
    "Ich gähne nochmal und strecke mich dabei."
    "Ich reibe mir durch die Augen"

    scene bg keller
    with fade

    "Ich bin so müde."
    "Ich hätte doch nicht so lang wach bleiben sollen."
    "Ich gähne. Aber daran lässt sich auch nichts mehr ändern."
    "Ich erhebe meinen Körper."
    "Mit hängenden Armen wandere ich ins Badezimmer als plötzlich..."

    play sound "sounds/hit_1.wav"
    #Sound noch nicht vorhanden
    #an diese Szene angepasster Soundeffekt fehlt

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

    show laura scared
    with dissolve
    #Bild fehlt noch
    #K1

    b "Was ist los, %(sisName)s?"
    $ berndNameUpper = berndName.upper()
    sis "%(berndNameUpper)s!, HILFE!"
    sis "DA."
    b "Was ist da?"
    sis "EINE...EINE...EINE...EINE SPINNE!"
    b "Ich laufe langsam zu meiner Schwester hin."
    b "Nun stell dich mal wegen einer Spinne nicht so an."
    "Ich greife nach meinem Schuh."
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

    scene bg wohnung_innen
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

    #show laura closed_eyes #AE unnötig? evtl. sis scared?
    #with dissolve
    #Bild existiert nicht
    #Vielleicht die Hände vor die Augen halten
    #K1
  
    "FLATSCH!"
    sis "Ist sie nun weg?"
    b "Ja."
    b "Du kannst die Augen wieder öffnen."
    
    show laura sad
    with dissolve
    
    sis "IIIIIIIIHHHHHHHHHHHHHHHHHHHHH!"
    b "Was?"
    sis "Sie klebt ja an der Wand."
    b "Ja."
    sis "MACH SIE WEG!"
    b "Jetzt warte doch einmal."
    "Ich zücke ein Taschentuch, nehme die Spinne damit auf und schmeiße das Taschentuch in den Mülleimer."
    sis "NEIN!"
    b "Was?"
    sis "MACH SIE KOMPLETT WEG!"
    "Ich nehme das Taschentuch und gehe ins Bad."
    
    scene bg badezimmer
    with fade
    
    "Ich schmeiße das Taschentuch in die Toilette."
    
    play sound "sounds/toilet.wav"
    
    "Ich gehe wieder zurück zu Laura."
    
    scene bg lauraszimmer
    with fade
    
    show laura sad
    with dissolve
    
    b "So."
    b "Jetzt ist sie weg."
    sis "Wirklich?"
    b "Ja."
    sis "Und du lügst mich auch nicht an?"
    b "Nein."
    
    show laura crying
    with dissolve
    
    "Nicht das schon wieder."
    sis "Ich hatte solche Angst."
    b "Ich weiß, %(sisName)s."
    "Wieso bekommt sie solche Angstzustände, wenn sie eine Spinne sieht?"
    "Das hatte sie schon als kleines Kind."
    b "Jetzt ist ja wieder alles in Ordnung."
    "Wäre sie ein Charakter aus einem Galge, würde ihre Angst vor Spinnen ihren Schmachtfaktor steigern."
    "Aber im realen Leben?"
    "Im realen Leben ist sowas lächerlich."
    "Und nervig."
    "Es passt auch gar nicht zu ihr."
    b "Geht's jetzt wieder?"
    
    show laura sad_smile
    with dissolve
    
    sis "Ich glaube schon."
    sis "Danke, %(berndName)s."
    "Ich gehe wieder in meinen Keller."
    
    scene bg keller_aus
    with dissolve
    
    "Ich sollte mich beeilen."
    "Die Spinne hat zu viel Zeit gekostet."
    "Die Spinne..."
    "Spinne..."
    "Kum0!"
    "Krautchan!"
    "Oh, Moment."
    
    scene bg badezimmer
    with dissolve
    
    "Ich ziehe mich aus und stelle mich auf die Waage."
    "Verdammt."
    "Schon wieder zugenommen."
    "Und alles nur FETT."
    "Ob %(wBerndName)s wohl auch Leute mit meinem Aussehen mag?"
    "Eher nicht."
    "Wahrscheinlich steht sie mehr auf Muskeln."
    "Sie ist halt auch nur ein Mädchen."
    "Ich sollte wirklich mal etwas für meine Figur tun."
    "Ich werde von Tag zu Tag dicker."
    "Ich sollte Sport machen."
    "Ja."
    "Nein."
    "Kein Sport."
    "Sport ist Mord."
    "Ich sollte keine Chips mehr essen."
    "Ja."
    "Nein."
    "Was soll ich sonst essen, während ich Anime schaue?"
    "Ich könnte weniger essen."
    "Das könnte ich hinbekommen."
    "Bestimmt."
    "Wahrscheinlich."
    "Eventuell."
    "Nicht."
    "Ich sollte die Türe abschließen."
    "Sonst passiert das Gleiche wie letztens."
    
    play sound "sounds/doorlock.wav"
    
    "So."
    "Jetzt kann %(sisName)s hier nicht einfach reinplatzen."
    "Ich steige unter die Dusche und drehe das Wasser auf."
    "Ach, %(wBerndName)s."
    "Nein."
    "Ich kann nicht schon wieder auf %(wBerndName)s fappieren."
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
            "Ich schaue ihr tief in die Augen."
            "Dann bewege ich meinen Kopf immer näher an ihren."
            "Ich flüstere ihr \"Ich liebe dich\" ins Ohr."
            "Sie zieht ihren Kopf zurück."
            "Sie wird rot."
            "Nach ein paar Sekunden kommt sie wieder näher."
            "Sie geht mit ihrem Mund zu meinem Ohr..."
            
            play sound "sounds/knock.wav"
            
            "Mein Herz fängt an zu klopfen."
            "Sie haucht mir etwas ins Ohr..."
            $ berndNameUpper = berndName.upper()
            sis "%(berndNameUpper)s, ICH MUSS AUF KLO!"
            "Was?"
            "Verdammt."
            
            play sound "sounds/knock2.wav"
            
            sis "JETZT MACH ENDLICH DIE TÜR AUF!"
            "%(sisName)s hämmert gegen die Türe."
            "Und ich war so kurz davor."
            
            play sound "sounds/knock2.wav"
            
            sis "MACH DIE TÜR AUF!"
            sis "ICH WILL MIR NICHT IN DIE HOSEN MACHEN!"
            "Ich lege mir schnell ein Handtuch um und mache die Tür auf."
            
            play sound "sounds/doorlock.wav"
        
            show laura mad_talk
            with dissolve
        
            sis "Du wartest draußen."
            b "Draußen?"
            b "Aber da hole ich mir den Tod."
            sis "Mir egal."
            sis "Ich hab' Vorrang."
            
            scene bg zuhause_drinnen 
            with fade
            
            play sound "sounds/door_1.wav"
            
            "Na toll."
            "Das habe ich nun anscheinend davon, dass ich ihr vorhin half."
            "Naja, eigentlich war ich sowieso schon fertig."
            "Ich wollte nur noch fertig fappieren."
            "Muss mich nur noch abtrocknen."
            "Und anziehen."
            "Und fertig fappieren."
            "Dazu habe ich nun auch keine Lust mehr."
            "Ich sollte wieder in meinen Keller gehen."
            
            scene bg keller_aus
            with dissolve
        
            "Ich trockne mich ab und ziehe mich dann an."
                    
        "Nein, sie ist zu rein.":
            "Ich muss mich davon ablenken."
            "Ich darf nicht auf sie fappieren."
            "Ich darf nicht."
            "Sie ist einfach zu rein."
            "Ihre blonden Haare..."
            "Ich stelle das Wasser der Dusche kälter ein."
            "Ihre Brille..."
            "Ihr Gesicht..."
            "Ich stelle das Wasser noch kälter."
                        
            scene bg keller_aus
            with dissolve
            #-----------------------------------------------
            "Einmal kalt duschen und man möchte nicht mehr."
            if persistent.wieherbuhSprache is 0:
                "Genau nach Plan."
            if persistent.wieherbuhSprache is 1:
                "Genau nach keikaku."
            if persistent.wieherbuhSprache is 2:
                "{=jp}Genau nach 計画。{/=jp}"
            #-----------------------------------------------
            #Bild
            #Hier würde ich gerne oben im Bild einen Kommentar einbauen "Bemerkung: keikaku heißt Plan."
            #Wie machte ich das?

    "Damit wäre ich eigentlich fertig."
    
    scene bg wohnung_innen
    with fade

    "Ich gehe nochmal alles durch."
    "Sicher ist sicher."
    "Es ist immerhin das erste Mal, dass ich bei einem Mädchen bin."
    "Und dann noch bei so einem süßen."
    "Also..."
    "Habe ich gefrühstückt?."
    "Ja."
    "Habe ich geduscht?"
    "Ja."
    "Habe ich mich mit Deo eingesprüht?"
    "Ja."
    "Habe ich Zähne geputzt?"
    "Ja."
    "Sehen die Schuhe annehmbar aus?"
    "Ja."
    "Ich bin bereit."
    "Ich bin in Form."
    "Ich bin bereit."
    "Ja, ganz enorm."
    "Ich bin bereit."
    "Jederzeit."
    
    scene bg treppenhaus
    with fade
            
    "Nun folgt also der schwierige Teil."
    "Ich laufe die Treppenstufen nach oben."
    
    scene bg tuere
    with fade
    #Bild existiert noch nicht
    
    "Ich stehe nun vor ihrer Türe."
    "Ich will anklopfen, doch meine Hand stoppt ein paar Zentimeter vor der Türe."
    "Moment mal."
    "Was soll ich denn sagen, wenn jemand aufmacht?" 
    "Unsicherheit macht sich bei mir breit."
    "Ich war noch nie in so einer Situation."
    "Werde ich mich bei anderen Leuten wohl fühlen?"
    "Ich war noch nie in so einer Situation."
    "Werde ich mich wirklich in einem Mädchenzimmer wohl fühlen?"
    "Ich war noch nie in so einer Situation."
    "Voller Angst nehme ich meine Hand wieder runter."
    "Das Gefühl der Unsicherheit in mir wird immer stärker."
    "Was ist nur los mit dir, %(berndName)s?"
    "Seit wann gibst du so schnell auf?"
    "OK, eigentlich gebe ich immer schnell auf."
    "Aber jetzt bist du schon so weit gekommen."
    "Warum traust du dich nicht mehr weiter?"
    "Ich hole einmal tief Luft und nehme meinen ganzen Mut zusammen."
    
    play sound "sounds/knock.wav"
    
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
    
    play sound "sounds/knock.wav"
    
    "Ich höre immer noch jemanden reden, aber niemand macht auf." 
    "Ich drehe mich um und laufe los."
        
    play sound "sounds/anja_dooropen.wav"
    
    "Die Tür geht auf."
    "Plötzlich kehrt die Angst zurück."
    "Ich will wegrennen, doch mein Körper hört nicht mehr auf mich."
    "Wie angewurzelt stehe ich vor der Türe."
    "Verdammt."
    "Was mache ich denn jetzt?"
    
    show yasmin surprise at left
    with dissolve
    #Bild existiert noch nicht

    "Wer ist DAS denn?"
    "Und warum starrt sie mich so an?"
    "Kann sie nicht woanders hinschauen?"
    "Sie soll mich nicht anschauen."
    "Ich mag das nicht."
    "Irgendwie..."

    show anja neutral at right
    with dissolve

    bw "Hallo, %(berndName)s."
    b "..."

    show yasmin neutral at left
    with dissolve
    #Bild existiert noch nicht

    "Mädchen" "Wer ist das, %(wBerndName)s?"
    bw "Das ist nur %(berndName)s."
    "Was soll hier \"nur\" heißen?"
    bw "Er ist nur ein Nachbarsjunge."
    "Nachbarsjunge?"
    "Was soll das denn heißen?"
    "Ich dachte, ich wäre ihr sympathisch."
    "Sie braucht mich also nur für Krautchan."
    "Hätte ich mir ja gleich denken können."
    "Sie will mich nur ausnutzen."
    "Typisch Frau."

    show yasmin embarassed at left
    with dissolve
    #Bild existiert noch nicht

    "Mädchen" "Oh, hi."
    b "..."
    "Ich will sprechen."
    "Aber ich kann nicht."
    b "..."
    "Mädchen" "Du musst wohl einer von der schüchternen Sorte sein."
    bw "Oh ja, %(berndName)s ist sehr schüchtern."
    "Ich bin immer noch nicht in der Lage zu sprechen."
    "Mädchen" "Na dann, ich muss jetzt los."
    "Mädchen" "Tschau, %(wBerndName)s."
    bw "Tschüss, %(yanName)s."
    yan "Tschau, %(berndName)s."
    b "..."

    scene bg treppenhaus
    with fade
    
    show yasmin from_behind
    with dissolve
    #Bild existiert noch nicht

    "Ich sehe nur noch, wie das Mädchen die Treppen runtergeht."
    
    bw "%(berndName)s."
    "Ich drehe mich wieder um."

    scene bg tuere
    with fade
    #Bild fehlt noch

    show anja neutral
    with dissolve

    b "..."
    bw "H-A-L-L-O?"
    b "..."
    bw "Na ja, komm' erstmal rein."
    "Ich drehe mich zur Treppe hin."

    scene bg treppenhaus
    with fade
    
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

    show laura neutral
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
    with dissolve

    "Ich will mich auf andere Gedanken bringen."
    "Wie immer öffne ich als erstes meinen Browser und öffne Krautchan."
    "404..."
    "Achja..."
    "Was mach ich denn jetzt?"
    "Zum Glück gehe ich auf mehr Seiten als nur Krautchan wie zum Beispiel ..."
    "zum Beispiel..."
    "Öhm..."
    "Öhm..."
    "Verdammt."
    "Ohne Krautchan hat mein Leben einfach keinen Sinn."
    "Ich schau einen Anime."
    "Aber welchen?"
    "Ich öffne meine Animepartition."
    "Saint October?"
    "Nicht schon wieder."
    "Gundam?"
    "Langweilig."
    "Akagi?"
    "Nein."
    "Was ist nur aus mir geworden?."
    "Selbst auf Akagi habe ich keine Lust."    
    "Ich werfe mich auf's Bett."
    "Ich kann mich einfach nicht auf andere Gedanken bringen."
    "Ich muss immer wieder an vorhin denken."
    "Ob es vorhin richtig war, einfach so zu gehen?"
    "Ja."
    "Sie ist ja Schuld."
    "Mädchen sind immer Schuld."
    "IMMER!"
    "Nie kann man es ihnen recht machen."
    "Ich kenne es nicht anders."     
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "GO TO HELL, BITCHES!"
    if persistent.wieherbuhSprache is 1:
        "KIEUSERO, ONNA-DOMO!"
    if persistent.wieherbuhSprache is 2:
        "{=jp}消えうせろ、 女共！{/=jp}"
    #-----------------------------------------------
    "Aber sie ist eine Bernadette."
    "Und ich ein Bernd."
    "Das hat anscheinend nichts zu sagen, wenn man sich im realen Leben kennt."
    "Irgendwie traurig."
    "Liegt wohl doch an mir und nicht am Berndsein."
    "Mehr wie: Liegt wohl doch daran, dass sie ein Mädchen ist."
    "Ich hatte ja noch nie was mit Mädchen am Hut."
    "Da bleibe ich lieber bei mai waifus."
    "Hach, Lynette..."
    #Bild "traumkueche.jpg", aber mit kleiner, weißer Umrandung, um anzuzeigen, dass es nur ein Traum ist
    
    scene bg traumkueche
    with fade
    
    show lynette_essen
    with dissolve
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Lynette" "...Meister."
    if persistent.wieherbuhSprache is 1:
        "Lynette" "...Goshujin-sama."
    if persistent.wieherbuhSprache is 2:
        "Lynette" "{=jp}。。。御主人様。{/=jp}"
    #-----------------------------------------------
    b "Hmm?"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Lynette" "Guten Morgen, Meister."
    if persistent.wieherbuhSprache is 1:
        "Lynette" "Ohayou gozaimasu, Goshujin-sama."
    if persistent.wieherbuhSprache is 2:
        "Lynette" "{=jp}お早うございます、　御主人様。{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        b "Morgen."
    if persistent.wieherbuhSprache is 1:
        b "Ohayou."
    if persistent.wieherbuhSprache is 2:
        b "{=jp}お早う。{/=jp}"
    #-----------------------------------------------
    "Lynette" "Ich habe dir Frühstück gemacht."
    b "Aber Lynette."
    b "Wir sind doch noch gar nicht umgezogen."
    b "Und es ist erst 7 Uhr."
    "Lynette" "Aber ich..."
    "Lynette" "...ich..."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Lynette" "...ich koche doch so gerne für dich, Meister."
    if persistent.wieherbuhSprache is 1:
        "Lynette" "...ich koche doch so gerne für dich, Goshujin-sama."
    if persistent.wieherbuhSprache is 2:
        "Lynette" "...ich koche doch so gerne für dich, {=jp}御主人様。{/=jp}"
    #-----------------------------------------------
    b "Ach, Lynette."
    b "Was soll ich nur mit dir machen."
    b "Da bleibt mir wohl nichts Anderes übrig."
    b "Ich werde es wohl erst essen müssen."
    b "Nachher wäre es kalt."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Lynette" "Bitteschön."
    if persistent.wieherbuhSprache is 1:
        "Lynette" "Douzo."
    if persistent.wieherbuhSprache is 2:
        "Lynette" "{=jp}どうぞ。{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        b "Dankeschön."
    if persistent.wieherbuhSprache is 1:
        b "Arigatou."
    if persistent.wieherbuhSprache is 2:
        b "{=jp}ありがとう。{/=jp}"
    #-----------------------------------------------
    "Ich nehme das Tablett und setze mich damit an den Tisch."
    #Bild von Lynette ohne Tablett
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        b "Guten Appetit!"
    if persistent.wieherbuhSprache is 1:
        b "Itadakimasu!"
    if persistent.wieherbuhSprache is 2:
        b "{=jp}いただきます！{/=jp}"
    #-----------------------------------------------    
    if persistent.wieherbuhSprache is 0:
        "Lynette" "Meister?"
    if persistent.wieherbuhSprache is 1:
        "Lynette" "Goshujin-sama?"
    if persistent.wieherbuhSprache is 2:
        "Lynette" "{=jp}御主人様？{/=jp}"
    #-----------------------------------------------
    b "Ja?"
    "Lynette" "Ich muss gleich noch einkaufen gehen, aber ich habe kein Geld."
    b "Kein Problem."
    "Ich greife in meine Anzugsjacke und hole mein Portemonnaie heraus."
    b "Hier."
    "Ich gebe ihr zwei 200-Euroscheine."
    "Lynette" "Aber..."
    "Lynette" "Das ist so viel Geld."
    "Lynette" "Ist das denn wirklich in Ordnung?"
    #-----------------------------------------------    
    if persistent.wieherbuhSprache is 0:
        b "Natürlich ist es das."
    if persistent.wieherbuhSprache is 1:
        b "Atarimae sa."
    if persistent.wieherbuhSprache is 2:
        b "{=jp}当たり前さ。{/=jp}"
    #-----------------------------------------------
    #EXPERTENWIEHERBUH GEFRAGT: "Atarimae sa" oder "mochiron"?
    
    
    b "Da gab es doch diese Halskette, die du unbedingt haben wolltest."
    b "Wie teuer war die noch gleich?"
    b "300 Euro?"
    "Ich hole noch einen weiteren 200-Euroschein aus dem Portemonnaie."
    b "Hier."
    "Lynette" "Woher weißt du davon?"
    b "Ich wäre nicht mit dir zusammen, wenn ich sowas nicht wüsste."
    #Bild mit blush von Lynette für maximalen Gewinn
    #-----------------------------------------------    
    if persistent.wieherbuhSprache is 0:
        "Lynette" "Das ist...."
    if persistent.wieherbuhSprache is 1:
        "Lynette" "Sonna..."
    if persistent.wieherbuhSprache is 2:
        "Lynette" "{=jp}そんな。。。{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Stimme" "Meister!"
    if persistent.wieherbuhSprache is 1:
        "Stimme" "Goshujin-sama!"
    if persistent.wieherbuhSprache is 2:
        "Stimme" "{=jp}御主人様！{/=jp}"
    #-----------------------------------------------
    "Diese Stimme..."
    "Das ist..."
    
    #Lynette nach rechts
    show erika_normal at left
    with dissolve
    
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Erika" "Meister!"
    if persistent.wieherbuhSprache is 1:
        "Erika" "Goshujin-sama!"
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}御主人様！{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Erika" "Morgen!"
    if persistent.wieherbuhSprache is 1:
        "Erika" "Ohayou!"
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}お早う！{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        b "Morgen!"
    if persistent.wieherbuhSprache is 1:
        b "Ohayou!"
    if persistent.wieherbuhSprache is 2:
        b "{=jp}お早う！{/=jp}"
    #-----------------------------------------------
    "Erika" "Wie befohlen bin ich nun geduscht."
    b "Fein."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Erika" "Mann."
    if persistent.wieherbuhSprache is 1:
        "Erika" "Mou."
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}もう。{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Erika" "Gemein."
    if persistent.wieherbuhSprache is 1:
        "Erika" "Iyashii."
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}卑しい。{/=jp}"
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        b "Was?"
    if persistent.wieherbuhSprache is 1:
        b "Nani?"
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}何？{/=jp}"
    #-----------------------------------------------
    "Lynette" "Für dich habe ich doch auch Frühstück gemacht, Erika."
    "Erika" "Ihr esst aber schon."
    "Erika" "Ihr habt ohne mich angefangen."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        b "Sorry, Erika-chan."
    if persistent.wieherbuhSprache is 1:
        b "Gomen, Erika-chan."
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}ごめん、 ダーリング{/=jp}"
    #-----------------------------------------------
    #Sorry benutzt, weil es lockerer rüberkommt als ein "Entschuldigung"
 
    "Erika" "Dafür musst du aber gleich was mit mir unternehmen."
    b "OK."
    "Erika" "Versprochen?"
    b "Ja."
    b "Worauf hast du denn Lust?"
    "Erika" "Also eigentlich bin ich noch müde."
    "Erika" "Ich würde mich am liebsten noch eine Runde hinlegen."
    b "Ich soll also mit dir schlafen?"
    "Erika" "Ja."
    b "Sicher?"
    "Erika" "Ja."
    #Blushbild von Lynette für maximalen Gewinn
    #Bild existiert noch nicht
    #ansonsten muss ich das irgendwie per Dialog darstellen
    
    "Erika" "Was ist denn los, Lynette?"
    "Lynette" "Das ist einfach..."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Lynette" "Meister!"
    if persistent.wieherbuhSprache is 1:
        "Lynette" "Goshujin-sama!"
    if persistent.wieherbuhSprache is 2:
        "Lynette" "{=jp}御主人様！{/=jp}"
    #-----------------------------------------------
    "Lynette" "Sagt doch auch mal was!"
    b "Was denn?"
    "Lynette" "Na, Ihr weißt schon."
    b "Sie versteht es nicht, Lynette-chan."
    "Erika" "Was versteh' ich nicht?"
    b "Nichts..."
    #Bild von Erika mit --( - Gesichtsausdruck, sofern es überhaupt solch ein Bild gibt
    #Bild existiert noch nicht
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Erika" "Mann."
    if persistent.wieherbuhSprache is 1:
        "Erika" "Mou."
    if persistent.wieherbuhSprache is 2:
        "Erika" "{=jp}もう。{/=jp}"
    #-----------------------------------------------
    "Erika" "Immer verheimlicht ihr mir irgendwas."
    "Lynette" "Aber Erika..."
    "Erika" "Kein Aber, Lynette."
    "Ich gehe zu Erika und streichle ihr über das blonde Haar."
    b "Nimm solche Sachen doch nicht so ernst, Erika-chan."
    "Erika" "Aber..."
    "Erika" "aber..."
    "Sie senkt ihren Blick Richtung Boden und verstummt."
    b "Was ist denn?"
    "Erika" "Ich..."
    "Erika" "{size=4}Ich liebe dich.{/size}"
    b "Ich kann dich nicht verstehen, wenn du nuschelst."
    "Erika" "{size=6}Ich liebe dich.{/size}"
    b "Ach, Erika."
    b "Jetzt schau mich doch mal an, wenn du mir was sagen willst."
    "Sie hebt ihren Kopf und schaut mir in die Augen."
    "Erika" "Ich will nicht, dass du mir Sachen verheimlichst."
    "Erika" "Ich habe auch keine Geheimnisse vor dir!"
    "Erika" "Ich..."
    "Sie neigt ihren kurz nach rechts unten."
    "Dann hebt sie ihn wieder und schaut mir wieder tief in die Augen."
    "Erika" "Ich..."
    "Erika" "li..."
    
    #BUTTERGOTT

    scene black
    with fade
    
    $ renpy.pause(1)

#-------- hier erstmal ein Trennstrich, um die beiden Szenen voneinander unterscheiden zu können

    "Stimme" "He, %(berndName)s."

    scene bg keller_blur
    with fade
    #Bild existiert noch nicht (DOCH!?)
    
    "Stimme" "Aufstehen."
    b "Jaja."
    "Ich reibe mir einmal durch die Augen."

    scene bg keller
    with wooshTrans

    show laura neutral
    with dissolve
    
    sis "Das Abendessen ist fertig."
    b "Ist ja gut, ist ja gut."
    sis "Ich geh schon mal vor."
    
    hide laura
    with dissolve
    
    "Ich setze mich aufrecht auf mein Bett."
    "Die Sache mit %(wBerndName)s geht mir nochmal durch den Kopf."
    "Ich gehe zu ihr."
    "Niemand machte auf."
    "Just in dem Moment, als ich gehen will, kommt sie mit ihrer Freundin raus."
    "Was für ein Zufall."
    "Die Freundin..."
    "Wie hieß sie noch gleich?"
    "Ich glaube, es war %(yanName)s."
    "Sie..:"
   
    menu:
        " "
       
        "...ist irgendwie süß.":
            jump von_anja_zu_yasmin
       
       
        "ist irgendwie süß. NICHT!":
            $ yanLove -=5
            "Schwarze Haare?"
            "Nicht mein Ding."
            "Schwarze Haare sind etwas für Emos."
            "Brünett ist schön."
            "Blond ist auch fein."
            "Aber schwarz ist nicht schön."
            "Nein."
            "Wirklich nicht."
            "Dazu dann noch ihre Augen."
            "Ihre Tränensäcke."
            "Sowas sieht nicht sehr schön aus."
            "Sie sieht aus wie ein Verbrecher."
            "Sie sieht aus wie ein Stalker."
            "Da läuft es mir eiskalt den Rücken runter."
            jump anja_weiter
            
label anja_weiter:
    
    "Ich sollte erstmal das Essen holen gehen."
   
    scene bg kueche
    with fade
   
    ma "Oh, %(berndName)s."
    ma "Wie war es bei %(wBerndName)s?"
    b "Nicht das schon wieder."
    b "Sie ist nicht das, was du dir wünschst."
    ma "Also lief es nicht so gut?"
    b "*seufz*"
    "Also gut."
    
    menu:
        " "
        
        "Ich erzähle es ihr.":
            $ maLove +=5
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
            
            scene bg keller
            with fade
        
        
        "Lass mich in Ruhe.":
            $ malove -=5
            b "Kannst du mich nicht einmal damit in Ruhe lassen?"
            ma "Jetzt sei doch nicht so, %(berndName)s."
            "Ich nehme mir mein Essen und gehe wortlos wieder zurück in meinen Keller."
            
            scene bg keller
            with fade
            
            "So, endlich habe ich wieder meine Ruhe."
    
    "Ich setze mich vor meinen Rechner."
    
    scene bg desktop_none
    with fade
    
    "Was nun?"
    "Mal schauen..."
    "Spiele?"
    "Nicht beim Abendessen."
    "Internet?"
    "Nein."
    "Ohne KC ist das Internet so fad."
    "Ich hab's."
    "Ich schau einen Anime."
    "Hmm..."
    "Mal schauen, ob schon die neue Folge Strike with Cheese fertig heruntergeladen ist."
    "Sehr gut."
    "Oh, schon die elfte Folge."
    "Bald ist der Anime vorbei."
    "Schade irgendwie."
    "Lynette ist so moe."
    "Sie ist mai waifu."
    
    scene black
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
    "Sehr aussagekräftig."
    "Aber das ruft sie immer."
    b "ICH KOMME JA SCHON!"
    "Ich stehe auf und gehe nach oben."
    
    play sound "sounds/metaldooropen.wav"
        
    scene bg kellertreppe
    with fade
    
    "Ich schaue die Kellertreppe nach oben."
    
    show anja neutral
    with dissolve
    
    bw "Oh, hai."
    b "wat"
    bw "Kann ich runterkommen?"
    b "..."
    "Ich gehe einfach wieder in meinen Keller zurück."
    
    scene bg keller
    with fade
    
    play sound "sounds/metaldooropen.wav"
    
    "Ich schließe die Tür hinter mir."
    "Wie immer."
    "Ich setze mich wieder vor meinen Rechner."
    
    play sound "sounds/metaldooropen.wav"
    
    show anja angry
    with dissolve
    
    bw "Was ist los mit dir?"
    b "..."
    "Lass mich in Ruhe."
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
    
    show anja mad
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
    
    show anja neutral
    with dissolve
        
    bw "Jetzt will ich nur noch wissen, warum du mich ignorierst."
    b "..."
    bw "Ich hab schon nachgedacht."
    bw "Ich weiß es nicht, sonst wäre ich jetzt nicht hier."
    bw "Traust du mir nicht, weil ich vorher wusste, dass KC off gehen würde?"
    b "Das ist es nicht."
    bw "Was ist es dann?"
    b "..."
    bw "Hab ich irgendwas Falsches gesagt?"
    b "..."
    bw "Das ist wohl das Wahrscheinlichste."
    bw "Aber was?"
    bw "Hat es vielleicht doch etwas mit %(yanName)s zu tun?"
    b "..."
    bw "Was machte ich falsch?"
    bw "Sag es mir."
    b "Du..."
    b "Du..."
    bw "Was?"
    b "Du sagtest, dass..."
    bw "Ich sagte was?"
    bw "OH, WARTE."
    bw "Ich sagte, du seist ein Nachbarsjunge."
    bw "Ist es das?"
    b "..."
    
    show anja doppelpunkt_drei
    with dissolve
    #Bild existiert noch nicht
    
    bw "Ach, %(berndName)s."
    bw "Was soll ich nur mit dir machen?"
    bw "Aber irgendwie süß von dir."
    bw "Dass du dich deswegen anstellst."
    
    show anja neutral
    with dissolve
    
    bw "Auf jeden Fall tut es mir Leid."
    bw "Ich habe das nicht böse gemeint."
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
    
    play sound "sounds/metaldooropen.wav"
    
    "Sie macht die Tür hinter sich zu."
    "Etwas, das meine Mutter nie macht, wenn sie aus dem Keller rausgeht."    
    "Ich wende mich wieder dem Bildschirm zu."
    
    scene bg desktop_none
    with fade
    
    "Endlich."
    "Endlich habe ich meine Ruhe."
    "Endlich kann ich Animu schauen."
    
    scene black
    with fade
    
    $ renpy.pause(1)
    
    scene bg desktop_none
    with fade
    
    "So moe."
    "Mal schauen, ob schon ein Faden darüber auf Krautcha-"
    "Verdammt."
    "Vielleicht auf Vier-"
    "NEIN!"
    "Was mache ich denn nun?"
    "Ich schaue nicht genug Animeserien."
    "Jetzt habe ich nichts mehr zum Schauen."
    "So langweilig."
    "Ich geh schlafen."
    
    scene black
    with fade
    
    "Am nächsten Tag."
    
    scene bg keller_aus_blur
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
    with dissolve
    
    "Hach, das war so gut."
    "Wenn ich das doch nur wirklich erleben dürfte."
    "Ich bin so ronery."
    "Ich kenne keine Mädche-"
    "Moment."
    "Andererseits..."
    "Sollte ich %(wBerndName)s wirklich glauben?"
    "Sollte ich wirklich zu ihr gehen?"
    "Sie könnte auch ein guter Troll sein."
    "Ein verdammt Guter."
    "Krautchan geht bestimmt auch wieder."
    "Ich stehe auf und setze mich an meinen PC."
    "Dann schalte ich den Computer an."
    
    "Dann kann ich jetzt erstmal auf Badezimmer gehen."
    
    scene black
    with fade
    
    $ renpy.pause(1.5)
    
    "Ich gehe wieder zurück in meinen Keller."
    
    scene bg keller
    with fade
    
    "Oh."
    "Schon hochgefahren?"
    "Das ging aber schnell."
    "Normalerweise braucht der doch seine halbe Stunde zum Hochfahren."
    "Ich hätte jetzt *wirklich* Lust auf einen neuen PC."
    "Was soll's."
    
    scene bg desktop_none
    with fade
    
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
        
        "doch zu %(wBerndName)s gehen.":
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
    "Selbst ein Bernd hat Stolz!"
    "Ich kann doch nicht..."
    "Allerdings ist ein Leben ohne KC kein Leben."
    "Und ich habe sonst sowieso nichts tun."
    "Weder heute, noch in der Zukunft."
    "Was mache ich denn jetzt?"
    "Ich weiß."
    "Ich nutze ihre Hilfe aus."
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
            "...wenn ich könnte!"
            "Aber eine Anya ist auch fein."
            "Ich hab nichts mehr zum Schauen."
            "Ich brauche unbedingt neue Animeserien."
        
                
        "Ich hab gerade eh nichts Besseres zu tun.":
            $ friendLove += 10
    
    "Ich schaue auf die Uhr."
    "Es ist schon 14:06 Uhr."
    "Dann mache ich mich mal langsam auf den Weg."
    "Geduscht habe ich ja gestern."
    
    scene black
    with fade
    
    scene bg tuere
    with fade
    #Bild existiert noch nicht
    
    "Irgendwie habe ich kein gutes Gefühl."
    "Ich sollte einfach wieder gehen."
    "Moment."
    "Dann kommt sie nachher einfach wieder in meinen Keller."
    "Bei meinem Glück kommt sie genau dann rein, während ich fappiere."
    "Ich sollte einfach klopfen."
    "Ich bin ein Bernd."
    "Sie ist ein Bernd."
    "Wir wollen Krautchan retten."
    "Mehr gibt es da nicht."
    
    play sound "sounds/knock.wav"
    
    $ renpy.pause(0.5)
    
    "Stimme" "Ich komme gleich."
    "..."
    
    $ renpy.pause(2.0)
   
    play sound "sounds/knock.wav"
    
    $ renpy.pause(0.5)
    
    "Stimme" "JAAAA, ich komme gleich."
    "..."
    $ renpy.pause(0.5)
    
    play sound "sounds/knock.wav"
    
    $ renpy.pause(0.5)
    
    "Dieses Mal gibt es gar keine Reaktion."
    
    play sound "sounds/knock2.wav"
    
    $ renpy.pause(0.5)
      
    "Stimme" "JAAAAHAAAAA!"
    "Stimme" "Ich komme doch."
    "..."
    "Ich höre jemanden rennen."
    "Jemand drückt die Türklinke runter."
    
    play sound "sounds/anja_dooropen.wav"
    
    show anja neutral
    with dissolve
    
    bw "Oh, hai."
    b "Jaja."
    b "Also."
    b "Du sagtest, ich solle vorbeikommen."
    bw "Ja."
    bw "Komm doch rein."
    "Ich trete ein."
    
    scene bg anjas_wohnung
    with fade
    #Bild existiert noch nicht
    
    show anja neutral
    with dissolve
    
    "Nett."
    "Nichts Außergewöhnliches."
    bw "Komm mit in mein Zimmer."
    b "..."
    "Ich folge ihr kommentarlos."
    "Wozu sollte ich auch dafür etwas sagen?"
    
    scene bg anjas_zimmer
    with fade
    
    show anja neutral
    with dissolve
    
    "Das ist also ihr Zimmer."
    bw "Setz dich."
    bw "Ich hole eben was zu trinken."
    
    hide anja
    with dissolve
    
    "Ich setze mich auf das Bett."
    "Es ist weich."
    "Wie ich es mir dachte."
    "Ganz anders als meins."
    "Bei mir macht es keinen Unterschied, ob man auf dem Fußboden liegt oder im Bett."
    "Ich lasse meinen Blick durch das Zimmer schweifen."
    "PLÖTZLICH: Pokémon."
    "Mehrere Plüschfigur davon."
    "Pikachu."
    "Das Standardpokémon schlechthin."
    "Evoli."
    "Wie süß."
    "Glurak."
    b "JA MAN GLUARK!"
    "Habe ich das gerade laut gesagt?"
    "Verdammt."
    "%(wBerndName)s steht mit zwei Gläsern wieder im Zimmer."
    
    show anja neutral
    with dissolve
    
    "Hat sie das gerade gehört?"
    bw "Du wirst aber schnell wieder ruhig."
    "Hat sie."
    bw "Ich hab dir ein Glas Milch mitgebracht."
    "Milch? In MEINEM Glas?"
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
    
    show anja smiling
    with dissolve
    
    $ renpy.pause(1.0)
    "Stille."
    $ renpy.pause(1.0)
    "Stille."
    "Wie in einem Anime, in dem gerade ein schlechter Witz gemacht wurde."
    "Nur, dass es diesmal in der Wirklichkeit so ist."
    
    show anja angry
    with dissolve
    
    b "Sch-"
    bw "Ich werde dich erstmal testen."
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
    
    show anja smiling
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
    
    #---------------------------------------------------
    bw "Deine Milch."
    b "Was ist damit?"
    bw "Du hast sie noch nicht getrunken."
    "Erst jetzt bemerke ich, dass sie ihr Glas schon ausgetrunken hat."
    "Sie trank ihr Glas während des Gesprächs aus."
    "Ich schaue auf das weiße Getränk."
    "Dann nehme ich einen großen Schluck von der Milch."
    "Es ist köstliche Milch."
    "Wirklich erfrischend."
    "Deliziös."
    bw "Die Milch ist übrigens nicht FETTreduziert."
    "Ich setze das Glas kurz ab."
    b "FETT."
    b "Lecker."
    "Ich trinke weiter."
    "Das Glas ist leer."
    b "MEER MILCH!"
    bw "Du scheinst Milch zu lieben."
    b "Milch ist die Butter der Getränke."
    b "Beweise mich falsch."
    bw "Komm mit in die Küche."
    b "..."
    bw "Ich bin gerade sowieso alleine hier."
    b "..."
    "Ich laufe ihr hinterher."
    
    scene bg anja_kueche
    with fade
    
    show anja smiling
    with dissolve
    #Bild existiert noch nicht
    
    bw "Hier."
    bw "Genieße deine Milch."
    "Sie schenkt mir neue Milch ein."
    "Ich nehme das Glas wieder in meine Hand und trinke einfach."
    "Normalerweise trinke ich nichts auf ex."
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
    #------------------------------------------------
    
    play sound "sounds/telefon.wav"
    
    "Plötzlich geht das Telefon."    
    "Ich werde aus meinen Träumen gerissen."
    "%(wBerndName)s läuft zum Telefon und schaut auf das Display."
    
    play sound "sounds/telefon.wav"
    
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
    #Bild existiert noch nicht
    
    "Sie zieht sich an."
    bw "So, %(berndName)s."
    bw "Ich geh jetzt einkaufen."
    bw "Du solltest nach Hause gehen."
    b "OK."
    "Ich trete aus der Wohnung aus."
    
    scene bg treppenhaus
    with fade
    
    play sound "sounds/doorlock.wav"
    
    bw "Bis morgen, %(berndName)s."
    b "..."
    "Sie rennt die Treppe runter."
    "Ich sollte auch nach Hause gehen."
    "Hier rumstehen bringt mir nichts."
    
    scene black
    with fade
    
    scene bg keller_aus
    with fade
    
    "Ich schau erstmal einen Animu."
    "Die ersten paar Folgen von Akagi sind fertig."
    #-----------------------------------------------
    if persistent.wieherbuhSprache is 0:
        "Genau nach Plan."
    if persistent.wieherbuhSprache is 1:
        "Keikaku doori!"
    if persistent.wieherbuhSprache is 2:
        "{=jp}計画通り。{/=jp}"
    #-----------------------------------------------
    "AKAGI!"
    "QUALITÄTSNASEN!"
    
    #jump kapitel_3
    #erst mal rauslassen, sonst gibts nen fehler.
    #auch: drei_anja oder anja_drei aber nicht kapitel_3

label bernd_kapzwei_grillen:

    "Hahaha oh wow."
    "Arbeit? In meinem Leben?"
    "Ich vergesse das lieber mal direkt wieder."
    "Aber ich könnte echt mal was in meinem Leben verändern."
    
    scene black
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
   
    show laura sad_smile at left
    with dissolve
    
    show doc at right
    with dissolve
    #Bild existiert noch nicht
    
    ma "Wie geht es ihm, Herr Doktor?"
    "Arzt" "Wir können leider nicht mehr allzu viel für ihn tun."

    show laura sad at left
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
 
    show laura crying at left
    with dissolve
    
    ma "Ist schon gut..."
    "Ich heb meine linke Hand leicht."
    b "Komm her."
    b "%(sisName)s."
    
    show laura sad at left
    with dissolve
    
    sis "Ja?"
    b "Hör auf."
    b "Hör auf zu weinen."
    sis "Aber..."
    sis "aber..."
    sis "%(berndName)s."
    
    show laura crying at left
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
       
    show laura crying
    with dissolve
            
    if sisLove >= 60:
        
        "Ich richte mich einigermaßen auf, sodass ich nun auf dem Bett sitze."
        b "%(sisName)s."
        sis "Ich will nicht, dass du stirbst."
        sis "Immerhin bist du..."
        sis "Ich bin ..."
        b "Ich weiß, was du sagen willst."
        
        show laura sad
        with dissolve
        
        b "Ich weiß auch, dass ich es dir nie gesagt habe."
        b "Aber ich liebe dich."
        
        show laura sad_smile
        with dissolve
        
        sis "Ach, %(berndName)s."
        sis "Ich hab dich auch lieb."
        b "Also, versprich mir, dass du stark bist und nicht mehr weinst."
        b "Einverstanden?"
        sis "Einverstanden."
        b "Auch, wenn ich sterben sollte."
        b "Ich möchte nicht, dass du wegen mir weinst."
        sis "OK."
    
    if sisLove < 60:
        
        b "Also hör auf zu weinen."
        b "Das kann ich nicht mit ansehen."
        b "Das ist ja erbärmlich."
        b "Und du sagst, dass du ein großes Mädchen wärst?"
        b "Dann hör auf zu weinen."
        sis "Aber..."
        b "Kein \"Aber\"."
        sis "OK."
        sis "Ich versuch's."
                
    jump ende
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
    "Ihre schwarzen Haare."
    "Ich steh' auf schwarze Haare."
    "Sie hat zwar Tränensäcke, aber sie ist natürlich."
    "Ich liebe natürliche Frauen."
    "Schminke ist der Krebs, der die Frauen zerfrisst."
    #hier müsste man nun einen gemeinsamen Übergang finden
    #solange erst einmal:
    
    jump ende