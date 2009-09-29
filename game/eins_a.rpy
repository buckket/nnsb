label eins_treffenBerndf:
   
    scene bg zuhause_draussen
    with fade
    
    play music m_wohnung
    
    b "Wo lang jetzt...?"
    "Ich kenn mich hier ja überhaupt nicht aus."
    b "Zuerst mal zur nächsten, großen Straße."
    "Ich biege um die Ecke."
    "Eine alte Frau kommt mir entgegen."
    "Die könnte ich nach dem Weg fragen."
    "Ich gehe auf sie zu."
    "Als sie mich bemerkt, sieht sie mich an, aber ich drehe den Kopf weg und gehe an ihr vorbei."
    "Ich kann nichtmal jemanden nach dem Weg fragen."
    "Erbärmlich."
    "Ich gehe die Straße runter und blicke am Ende nach links und rechts."
    "Rechts ist eine Sackgasse, aber links scheint es auf eine größere Straße zuzugehen."
    "Also da lang."
    "Warum bin ich eigentlich nochmal losgegangen?"
    "Als würde dort ernsthaft ein Bernd auf mich warten, damit ich ihm helfe, Krautchan zu retten."
    "Das ist absurd."
    "In Gedanken versunken, laufe ich fast auf die Straße."
    "Zum Glück merke ich rechtzeitig, dass der Fußweg hier zu Ende ist."
    "Ich sehe mich um."
    b "OK."
    b "Das war leichter als gedacht."
    "In der Ferne sehe ich den Fernsehturm."
    "Wenn ich mich richtig erinnere, ist der direkt am Alexanderplatz."
    b "Also da lang..."
    
    scene black
    with fade
    
    "Einige Minuten später..."
    
    scene bg alexanderplatz_eins
    with fade
    
    b "Das ging schneller als ich dachte."
    "Jetzt muss ich warten."
    "Ich sehe auf die Uhr."
    "Genau zwei Minuten vor zwei."
    "Nirgendwo eine Spur von Bernd."
    "Aber der Platz ist groß."
    b "Am besten laufe ich ein wenig herum."
    
    scene bg alexanderplatz_zwei
    with fade
    
    "Jetzt ist es schon fünf Minuten nach zwei."
    "Wahrscheinlich hat mich Bernd doch nur verarscht und lacht sich jetzt tot."
    b "Scheiße."
    "Fünf Minuten warte ich noch, dann gehe ich."
    "Sicher sitzt er irgendwo an einer Ecke und macht grade Fotos."
    "Gab es hier nicht auch eine Live Webcam?"
    "Wahrscheinlich beobachtet mich schon ganz Krautchan."
    "Ich könnte versuchen, mich zu verstecken."
    "Zwischen den Menschen falle ich sicher nicht so auf, wie wenn ich alleine hier herumstehe."
    "..."
    "Wieso sind hier überhaupt so viele Leute?"
    "Haben die kein Zuhause?"
    "Was hier teilweise für Gestalten rumlaufen..."
    "Schrecklich."
    "Was wollen die alle h-"
    
    show anja neutral
    with flash
    
    hide anja neutral
    with dissolve
    
    b "Das war doch..."
    "Es war nur ein kurzer Augenblick, aber irgendwo in der Menge habe ich sie gesehen..."
    "Das Mädchen aus dem Supermarkt."
    "...aber warum sollte sie hier sein?"
    "Warum gerade jetzt?"
    "Ich schaue mich um, aber sie ist nirgends zu sehen."
    b "Wo ist sie hin?"
    "Da."
    "Sie ist in einer großen Menschenmenge."
    "Ein ganzes Stück weit weg, aber sie kommt in meine Richtung."
    "Oder ist sie das nicht?"
    "Ich gehe auf sie zu."
    "Was denke ich mir dabei?"
    "Will ich sie ansprechen?"
    "Das traue ich mich nicht."
    "Niemals."
    "Nur noch wenige Meter trennen uns."
    "Jetzt kann ich sie erkennen."
    "Das ist sie ganz sicher."
    
    show anja neutral
    with flash
    
    "Ich gehe an ihr vorbei und sehe sie an."
    "Nur keine Aufmerksamkeit erregen."
    "Sie dreht sich zu mir um."
    "Scheiße, jetzt hat sie mich bemerkt."
    "Ich hätte sie nicht so anstarren dürfen."
    "Schnell wende ich mich ab."
    
    u"Mädchen" "%(berndName)s?"
    
    play music m_anja fadein 0.4
    
    "Was...?"
    "Meint sie mich?"
    "Unmöglich."
    u"Mädchen" "Hey, %(berndName)s!"
    "Ich spüre eine Hand auf meiner Schulter und zucke zusammen."
    b "Was...?"
    "Woher kennt sie meinen Namen?"
    "Was soll das...?"
    u"Mädchen" "Du bist doch %(berndName)s, oder?"
    "Ich nicke verwirrt."
    u"Mädchen" "Na also."
    u"Mädchen" "Komm mit."
    u"Mädchen" "Wir gehen irgendwo hin, wo wir reden können."
    "Ich folge ihr."
    
    scene bg alexanderplatz_drei
    with fade
    
    show anja neutral
    with dissolve
    
    u"Mädchen" "Hier sind weniger Leute."
    u"Mädchen" "Das ist besser zum Reden."
    u"Mädchen" "Gut, dass du gekommen bist, %(berndName)s."
    b "Ich..."
    "Wovon redet sie?"
    
    show anja surprised
    with dissolve
    
    u"Mädchen" "Ah!"
    u"Mädchen" "Ich habe mich ja noch gar nicht vorgestellt!"
    
    show anja neutral
    with dissolve
    
    u"Mädchen" "Ich bin %(wBerndName)s."
    bw "Ich habe dir die E-Mail geschickt."
    bw "Deshalb bist du hier, oder?"
    "Was zum...?"
    "SIE ist der Bernd, der mir die Mail geschickt hat?"
    "Das ergibt keinen Sinn."
    "Verwundert sehe ich sie an."
    bw "Nicht?"
    bw "Hast du meine Mail nicht bekommen?"
    if berndName != "Bernd":
        bw "Aber du bist doch ein Bernd, oder?"
    else:
        bw "Aber du bist doch Stalkerbernds neuestes Opfer, oder?"
    "Ich nicke."
    b "J... ja."
    b "Ich bin wegen der E-Mail hier aber..."
    
    show anja surprised
    with dissolve
    
    bw "Ah!"
    bw "Jetzt versteh' ich!"
    bw "Du bist überrascht, dass ich ein Mädchen bin, richtig?"
    
    show anja doppelpunkt_drei
    with dissolve
    
    bw "Hihi."
    b "Äh... ja."
    bw "Hätte ich das geschrieben, wärst du sicher nicht gekommen, oder?"
    "Sie hat recht."
    "Ich kann immer noch nicht glauben, dass sie ein Bernd ist."
    "Ich dachte immer, es gäbe keine Frauen im Internet."
    bw "War ja klar."
    bw "Du bist ein typischer Bernd."
    "Macht sie sich über mich lustig?"
    bw "Tut mir Leid."
    bw "Ich wollte dich nicht beleidigen oder so."
    "Anscheinend kann sie meine Gedanken lesen."
    bw "Ich brauche dich schließlich noch."
    "Sie braucht mich?"
    "Wofür?"
    b "Was meinst du...?"
    bw "Na wegen Krautchan!"
    "Ach so wegen Krautchan."
    "Das erklärt..."
    "...nichts."
    bw "Wenn wir nichts unternehmen wird Krautchan untergehen!"
    "Was labert die denn da?"
    "Sind ALLE Frauen verrückt im Kopf?"
    b "Was redest du v-"
    
    show anja surprised
    with dissolve
    
    bw "OH!"
    bw "Ich muss nach Hause!"
    
    "Was zum...?"
    
    show anja neutral
    with dissolve
    
    bw "%(berndName)s."
    b "Ja?"
    bw "Wir treffen uns morgen wieder hier."
    bw "Um die gleiche Zeit."
    bw "Bis dann."
    
    hide anja neutral
    with dissolve
    
    "Sie rennt zur Straßenbahn."
    "Bevor ich merke, was passiert ist, ist sie schon weg."
    
    stop music fadeout 0.4
    
    "Was sollte das?"
    "Morgen um die gleiche Zeit?"
    "Was glaubt sie, wer sie ist?"
    "Kommandiert mich hier herum."
    "Verwirrt trete ich den Heimweg an."
    
    scene black
    with fade
    
    scene bg keller
    with fade
    
    play music m_bernd
    
    "Zu Hause angekommen lasse ich mich auf meine Matratze fallen."
    "Noch einmal lasse ich mir die Geschehnisse des heutigen Tages durch den Kopf gehen."
    "Stalkerbernd hat meinen Namen, meine E-Mail Adresse und ein Foto von mir gepostet."
    "Ein Bernd hat mir daraufhin einen Hilferuf geschickt."
    "Am vereinbarten Treffpunkt traf ich das Mädchen aus dem Supermarkt."
    "Es stellt sich heraus, dass sie der Bernd mit dem Hilferuf ist."
    "Sie will, dass ich ihr helfe, Krautchan zu retten."
    b "..."
    b "wat"
    "Das ergibt alles keinen Sinn."
    "Je mehr ich darüber nachdenke, desto mehr tut mir der Kopf weh."
    b "Nicht schon wieder..."
    b "Vielleicht sollte ich was essen..."
    
    scene bg kueche
    with fade
    
    play music m_wohnung
    
    "Ich öffne die Kühlschranktür."
    b "OH MEIN GOTT!"
    b "Das ist doch...!"
    b "Nichts."
    "Der Kühlschrank ist leer."
    "Ich höre, wie die Wohnungstür aufgemacht wird."
    ma "%(berndName)s! Wir sind wieder da!"
    ma "Bist du hier?"
    "Ich gehe in den Flur."
    
    scene bg wohnung_innen
    with fade
    
    b "Ja."
    b "Wo wart ihr?"
    ma "Ich war deine Schwester abholen."
    ma "Du wolltest ja anscheinend nicht."
    ma "Jetzt hängst du doch hier rum?"
    ma "Das muss aber ein kurzes Treffen gewesen sein."
    b "War es."
    
    show laura happy
    with dissolve
    
    sis "Hallo, %(berndName)s."
    b "Hi."
    
    hide laura happy
    with dissolve
    
    ma "Ich will, dass du %(sisName)s zum Einkaufen mitnimmst."
    ma "Der Kühlschrank ist leer."
   
    b "Ich will aber ni-{nw}"
    
#$ eins_streit = 1 => Bernd läuft Laura hinterher und dankt ihr nachher
#$ eins_streit = 2 => Bernd läuft Laura hinterher und dankt ihr nachher NICHT
#$ eins_streit = 3 => Bernd wartet bis Laura sich beruhigt hat und bringt ihr Kaugummis mit
#$ eins_streit = 4 => Bernd wartet bis Laura sich beruhigt hat und bringt ihr KEINE Kaugummis mit
#unterschiedliche Variablen habe ich nicht hinbekommen, da u. U. dem System eine Variable nicht bekannt ist und dann abstürzt
#und ich wollte nicht immer eins_hinterherlaufen_danken = 0 und in der nächsten Zeile dann
#eins_hinterherlaufen_nicht_danken = 1 etc. schreiben


    show laura happy
    with dissolve
    
    sis "OK!"
    sis "Komm, %(berndName)s!"
    "Sie nimmt meinen Arm und versucht mich nach draußen zu ziehen."
    b "Na gut, ich komm ja schon..."
    
    scene bg zuhause_draussen
    with fade
    
    if supermarkt == "":
        $ supermarkt = "Aldi"
    
    "Wir gehen in Richtung %(supermarkt)s."
    
    show laura neutral
    with dissolve
    
    sis "Sag mal, %(berndName)s..."
    b "Ja?"
    sis "Wieso hast du mich heute nicht von der Schule abgeholt?"
    "Oh Mann."
    "Wie erklär' ich ihr das?"
    b "Ich... äh..."
    sis "Du hattest wieder keine Lust, oder?"
    b "Nein."
    
    show laura pissed
    with dissolve
    
    sis "Ich wusste es."
    b "Äh...ich mein, DOCH!"
    "Verdammt."
    b "Doch, ich hatte Lust."
    sis "Du bist hoffnungslos, %(berndName)s."
    
    show laura mad_talk
    with dissolve
    
    sis "Wenn du wenigstens jetzt ehrlich zu mir wärst..."
    sis "...aber du versuchst dich lieber herauszureden."    
    b "Aber..."
    sis "Kein Aber."
    sis "Du warst schon immer so."
    sis "Wenn du einen Fehler gemacht hast, hast du Anderen die Schuld gegeben."
    "Ist das wirklich noch..."
    sis "Nie warst du Schuld."
    "...meine..."
    sis "Immer hast du dich vor der Schuld gedrückt."
    "...%(sisName)s?"
    "Sie ist doch sonst nicht so."
    "Sie hat wohl ihre Tage."
    "Ich lass die mal reden."
    sis "Und jetzt denkst du dir gerade, dass ich heute nur einen schlechten Tag hatte."
    "Woher...?"
    sis "Ich kenn dich, %(berndName)s."
    sis "Gib doch einfach zu, dass du mich nicht abholen wolltest."
    sis "Gib doch einfach zu, dass ich dir egal bin."
    sis "Gib doch einfach zu, dass du mich hasst."
    b "..."
    sis "Antworte verdammt nochmal!"
    "Aber was?"
    "Was soll ich ihr antworten?"
    
    menu:
        " "
        
        "Ja, ich gebe es zu.":
            $ sisLove -= 20
            $ maLove -= 10
            b "OK, OK."
            "Wenn es das ist, was sie hören will."
            b "Ich gebe es ja zu."
            b "Ich gebe zu, dass ich dich nicht abholen wollte."
            b "Ich gebe auch zu, dass du mir ziemlich egal bist."
            b "Und..."
            
            play music m_heul
            
            b "...ich gebe auch zu, dass ich dich hasse."
        
            show laura crying
            with dissolve
            
            sis "Ich wusste es."
            sis "Ich hab es von Anfang an gewusst."
            sis "Du hast mich nie gemocht."
            sis "Immer wenn ich dich fragte, ob du mit mir spielst..."
            sis "Nie hattest du Zeit für mich."
            
            #show laura vonhinten
            #with dissolve
            #Bild existiert noch nicht
            #Ginga Ale
            
            "Sie dreht sich um und..."            
            sis "Ich hasse dich auch!"
            
            play sound "sounds/laura_rennt.wav"
            #Sound existiert noch nicht
            
            "...rennt weg."
            "Verdammt."
            "Was mach ich denn jetzt?"
            "Ich weiß es nicht."
            "Soll ich ihr hinterherlaufen?"
            "Soll ich abwarten bis sie sich beruhigt?"
            "Sie wird spätestens heute Abend wieder zu Hause sein."
            
            stop music fadeout 0.4
            
            menu:
                "Ich..."
                
                "...laufe ihr hinterher.":
                    "Ich laufe ihr besser hinterher."
                    "Und ich sollte mich lieber beeilen."
                    
                    scene bg alexanderplatz_eins
                    with fade
                    
                    "Mann, bin ich fertig."
                    "Sie ist zwar nicht so untrainiert wie ich es bin."
                    "Aber sie ist kleiner und jünger."
                    "Sie muss auch schon fertig sein."
                    
                    scene bg alexanderplatz_zwei
                    with fade
                
                    "Moment mal."
                    "Hier war ich doch schon mal."
                    "Es ist doch alles %(wBerndName)s Schuld."
                    "Hätte sie mich nicht gezwungen hierhin zu kommen, hätte ich %(sisName)s abholen können."
                    "Und hätte ich %(sisName)s abgeholt, hätte ich jetzt keinen Streit mit ihr."
                    "Diese verdammten Mädchen."
                    "Sie sind Schuld."
                    "Immer."
                    "Argh."
                    "Ich hab keine Zeit mich über Mädchen aufzuregen."
                    "Ich muss %(sisName)s finden."
                    
                    scene bg alexanderplatz_drei
                    with fade
                    
                    "Irgendwo hier muss sie doch sein."
                    "Ich hab sie hierhin rennen sehen."
                    "Ah!"
                    "Da hinten."
                    "Ich sehe sie."
                    "Ich hole noch einmal tief Luft{w} und renne dann los."
                    b "{size=60}%(sisName)s!!{/size}"
                    "Ich bin schon fast bei ihr."
                    
                    show laura surprised_drop
                    with dissolve
                    
                    "Sie will sich umdrehen, aber ich bin schneller und packe sie am Arm."
                    
                    show laura mad_talk
                    with dissolve
                    
                    sis "Lass mich los!"
                    "Sie fuchtelt wie wild mit ihren Armen rum."
                    b "Nein."
                    sis "Doch."
                    b "Nein."
                    sis "Doch."
                    b "Jetzt hör mir doch mal zu."
                    sis "Lass mich endlich los."
                    b "Ich lasse dich nicht los."
                    sis "Wieso nicht?"
                    b "Weil du mir zuhören sollst."
                    sis "Aber ich will nicht."
                    b "Du hast keine Wahl."
                    sis "Lass mich los oder ich schreie."
                    b "Das wäre wirklich ein Problem."
                    b "Aber es ist mir egal."
                    b "Erinnerst du dich?"
                    b "Mir ist es egal, was man über mich denkt."
                    
                    show laura crying
                    with dissolve
                    
                    sis "Du hasst mich!"
                    b "Blödsinn."
                    sis "Du hast es selbst gesagt!"
                    b "Ja."
                    sis "Na also."
                    b "Ich sagte es, um dich zu ärgern."
                    sis "Du bist ein schlechter Lügner."
                    b "Ich lüge nicht."
                    b "Ich hab doch schon immer so reagiert."
                    sis "Du hast mich immer schon gehasst."
                    "Wieso kann sie nicht einfach Ruhe geben?"
                    "3D-Mädchen sind so anstrengend."
                    b "Ich hasse dich nicht, %(sisName)s."
                    b "Das habe ich noch nie getan."
                    b "Du gehst mir zwar oft auf die Nerven..."
                    sis "Ich wusste es!"
                    b "Jetzt lass mich doch mal ausreden."
                    b "Du gehst mir zwar oft auf die Nerven, {w}aber deswegen hasse ich dich noch lange nicht." 
                    sis "Du lügst!"
                    b "NEIN!"
                    b "Jetzt versteh es doch endlich mal."
                    b "Ich hasse weder dich, noch unsere Mutter."
                    
                    show laura sad
                    with dissolve
                    
                    sis "Wirklich?"
                    b "Ja."
                    b "Wirklich."
                    sis "Wirklich wirklich?"
                    b "Wirklich wirklich."
                    sis "Warum sagst du dann so gemeine Sachen?"
                    b "Ich weiß es nicht."
                    b "Aber ich meine sowas nicht ernst."
                    
                    show laura sad_smile
                    with dissolve                    
                    
                    b "Und jetzt lass uns einkaufen gehen."
                    sis "Ich mag nicht mehr."
                    "Ich fühle mich gerade so dumm."
                    "Immerhin wollte sie unbedingt einkaufen gehen und hat mich mitgeschleppt."
                    b "Aber wir haben es versprochen."
                    sis "Ich will jetzt aber nach Hause."
                    "Mann."
                    "Erst führt sie sich auf und jetzt noch das."
                    b "OK."
                    b "Dann gehen wir halt nach Hause."
                    sis "Musst du nicht noch was einkaufen?"
                    b "Nein."
                    b "Ich gehe nur einkaufen, wenn du mitkommst."
                    sis "Aber ich will nicht."
                    b "Dann gehe ich auch nicht."
                    
                    show laura happy
                    with dissolve
                    
                    sis "Hihi."
                    #Ich hätte hier gerne ein CG davon, wie Laura Bernds Arm umklammert
                    #Ginga Ale
                    "Sie greift an meinen rechten Arm und umklammert ihn."
                    "Jeder, der das sieht, denkt, dass wir ein Paar seien."
                    b "Was ist so lustig?"
                    sis "Du verhältst dich gerade wie ein kleines Kind."
                    b "Und du bist anscheinend nicht mehr traurig."
                    sis "Doch, bin ich."
                    b "Wieso lachst du dann?"
                    
                    show laura pissed
                    with dissolve
                    
                    sis "Darf ich nicht lachen?"
                    b "Doch schon, aber..."
                    sis "Aber...?"
                    b "Ich weiß auch nicht."
                    
                    show laura happy
                    with dissolve
                    
                    "Irgendwie beruhigt es mich, dass sie nun wieder lacht."
                    
                    scene bg zuhause_draussen
                    with fade
                    
                    show laura happy
                    with dissolve
                    
                    sis "Sag mal, %(berndName)s..."
                    b "Ja?"
                    sis "Holst du mich morgen von der Schule ab?"
                    b "Ich kann nicht."
                    
                    show laura pissed
                    with dissolve
                    
                    sis "Wieso nicht?"
                    b "Ich hab einen Termin."
                    sis "Ist der wichtiger als seine kleine Schwester von der Schule abholen?"
                    b "Ja, irgendwie schon."
                    sis "Was ist das dann für ein Termin?"
                    b "Nun ja..."
                    sis "Ja?"
                    b "Ich treffe ein Mädchen."
                    
                    show laura surprised
                    with dissolve
                    
                    sis "Ohhhhh."
                    b "Ja, du kannst dich jetzt ruhig über mich lustig machen."
                    
                    #show laura suspicious
                    #with dissolve
                    #Bild existiert noch nicht
                    #Ginga Ale
                    
                    sis "Du hast eine Freundin." 
                    "Was?"
                    "Wie kommt sie jetzt darauf?"
                    b "Nein."
                    b "Wie kommst du drauf?"
                    
                    show laura happy
                    with dissolve
                    
                    sis "Du magst sie."
                    b "Nein."
                    b "Sie ist mir egal."
                    
                    #show laura suspicious
                    #with dissolve
                    #Bild existiert noch nicht
                    #Ginga Ale
                    
                    show laura neutral
                    with dissolve
                    
                    sis "Warum triffst du dich dann mit ihr?"
                    sis "Warum ist sie dann wichtiger als seine kleine Schwester von der Schule abzuholen?"                    
                    b "..."
                    "Sie hat mich."
                    "Aber eigentlich habe ich mir darüber noch keine Gedanken gemacht."                    
                    
                    show laura happy
                    with dissolve
                    
                    sis "Ich hätte nie gedacht, dass du vor mir eine Beziehung anfängst."
                    sis "Du warst nie der Typ für sowas."
                    b "Ich habe keine Beziehung mit ihr."
                    sis "Du bist so schlecht im Lügen."
                    b "Aber ich..."
                    sis "Wir sind schon fast wieder zu Hause, %(berndName)s."
                    "Was soll dieser plötzliche Themenwechsel?"
                    sis "Was wirst du Mutter sagen?"
                    b "Was soll ich ihr schon sagen?"
                    sis "Na ja, wir haben nichts eingekauft."
                    "Oh."
                    "Das habe ich ganz vergessen."
                    "Was sage ich ihr?"
                    b "Ich hab keine Ahnung."
                    b "Ich lass es auf mich zukommen."
                    
                    scene bg wohnung_innen
                    with fade
                    
                    "Anscheinend ist meine Mutter gerade nicht da."
                    
                    show mutter
                    with dissolve
                    #Bild existiert noch nicht
                    #Ginga Ale
                    
                    ma "Hallo, ihr beiden."
                    "Oder auch doch."
                    ma "Wo habt ihr die Einkäufe?"
                    ma "Habt ihr die schon weggeräumt."
                    b "Nein."
                    ma "Dann macht das bitte."
                    b "Ähm...also eigentlich..."
                    ma "Ja?"
                    b "Also eigentlich waren wir..."
                    
                    show mutter at left
                    with move
                    #Bild existiert noch nicht
                    #Ginga Ale                    
                
                    show laura neutral at right
                    with dissolve
                
                    sis "Wir waren nicht einkaufen."
                    
                    show mutter boese at left
                    with dissolve
                
                    ma "Wieso nicht?"
                    
                    sis "Wir haben uns verlaufen."
                    "Was?"
                    sis "Als wir wieder wussten, wo wir waren, wollte ich nur noch nach Hause."
                    "Wieso hilft sie mir?"
                    sis "Und alleine wollte ich nicht."
                    "Nach dem, was vorgefallen ist, sollte sie doch sauer sein."
                    sis "Darum musste %(berndName)s mitkommen."
                    
                    "Ich höre, wie unsere Mutter tief durchatmet."
                    "Jetzt wird mir wieder die Schuld gegeben, dass wir nicht einkaufen waren."
                    
                    show mutter smile at left
                    with dissolve
                    
                    ma "Dann werde ich wohl gleich noch einkaufen müssen."
                    "Ich hab's geah- {w}Warte, was?"
                    ma "Ich hab übrigens Bananenshake gemacht."
                    ma "Der steht in der Küche."
                    ma "Ihr könnt euch was nehmen, wenn ihr wollt."
                    sis "Danke."
                    b "OK."
                    
                    scene bg kueche
                    with fade
                    
                    show laura neutral
                    with dissolve
                    
                    sis "Der Bananenshake ist wirklich lecker."
                    b "Ich..."
                    sis "Ja?"
                    b "Äh...nichts."
                    
                    $ renpy.pause(3)
                    
                    "Ich sollte ihr danken."
                    "Aber..."
                    
                    menu:
                        "Soll ich meiner Schwester danken?"
                        
                        "Ja.":
                            b "%(sisName)s..."
                            sis "Ja?"
                            b "Wegen gerade..."
                            sis "Ja?"
                            b "Dan-"
                            sis "Bitte?"
                            b "Danke..."
                            $ sisLove += 5
                            
                            show laura happy
                            with dissolve
                            
                            sis "Gern geschehen."
                            b "Wieso lachst du jetzt?"
                            sis "Na ja..."
                            sis "Du dankst mir so gut wie nie."
                            sis "Darum macht mich das irgendwie glücklich."                            
                            $ eins_streit = 1
                            
                        
                        "Nein.":
                            $ eins_streit = 2
                    
                
                "...warte bis sie sich beruhigt hat.":
                    $ sisLove -=5
                    "Ich sollte erst einmal einkaufen gehen."
                    "Um %(sisName)s kann ich mich später noch kümmern."
                    "Die läuft mir schon nicht weg."
                    "Oh, Moment."
                    "Na ja, was soll's?"
                    "Heute Abend ist sie wieder zu Hause und ich kann mit ihr darüber reden."
                    "Oder es auch sein lassen."
                    "Da ist ja auch schon der %(supermarkt)s."
        
                    scene bg supermarkt
                    with fade
    
                    play music m_shop
                    
                    "Was sollte nun noch einmal eingekauft werden?"
                    "Ich weiß es nicht."
                    "Wenn %(sisName)s hier wäre, könnte sie nun unsere Mutter anrufen."
                    "Nie ist sie da, wenn man sie braucht."
                    "Ich sollte erstmal das nehmen, was man immer braucht."
                    "Butter und Rügenwalder."
                    "Ach, ich nehme einfach auch etwas Brot mit."
                    "Ohne Brot sind Butter und Rügenwalder weitgehend wertlos."
                    "Ach ja, und Milch."
                    "Mit Milch kann man nichts falsch machen."
                    "Nachdem ich alles gefunden habe, gehe ich zur Kasse."
                    "Vor mir ist eine ältere Frau, die langsam einen Artikel nach dem anderen auf's Band legt."
                    "Die Kassiererin ist sichtlich genervt."
                    "Warum kaufen alte Leute immer so viel ein und müssen immer auf den Cent genau bezahlen?"
                    "Vielleicht sollte ich auch etwas für Laura kaufen..."
                    "Sie wird wohl nichts dagegen haben, wenn ihr großer Bruder ihr eine Packung Kaugummi mitbringt."
                    "Andererseits..."
                    
                    menu:
                        "Soll ich meiner Schwester eine Packung Kaugummi mitbringen?"
                        
                        "Ja.":
                            $ sisLove += 5
                            $ kaugummi = 1
                            "Ja."
                            "Ich sollte sie damit heute Abend aufmuntern."
                            "Falls sie es aus Wut nicht will, kann ich es selbst nehmen."
                            "Aber welche Sorte?"
                            "Ich kenne ihren Geschmack nicht."
                            "Ich schätze sie aber als eine Person ein, die Erdbeergeschmack mag."
                            "Ich lege noch eine Packung Erdbeer-Kaugummis auf's Band."
                            $ eins_streit = 3
                    
                    
                        "Nein.":
                            $ kaugummi = 0
                            "Nein."
                            "Ich sollte es sein lassen."
                            "Warum sollte ich derjenige sein, der nachgibt?"
                            "Ich bin nicht schwach."
                            "Ich muss nicht nachgeben."        
                            "Nein."
                            "Ich darf nicht nachgeben."
                            "Sie soll sich entschuldigen."
                            $ eins_streit = 4


        "Aber das stimmt doch gar nicht!":
            b "Du irrst dich."
            b "Ich könnte dich doch niemals hassen!"
            b "Immerhin bist du doch meine kleine Schwester."
            sis "Es ist so offensichtlich, dass du dich gerade nur herausreden willst."
            b "Aber..."
            b "Dann verrat mir doch mal, wie man seine eigene Schwester hassen kann."
            sis "Das ist einfach."
            sis "Man muss nur immer in seinem Zimmer sitzen,{w} Comics schauen{w} und vor der Realität fliehen."
            sis "Dann wird man automatisch so wie du."
            sis "Und dann hasst man auch andere Menschen."
            sis "Selbst seine eigene Familie."
            b "So ein Unsinn."
            b "Ich sitze zwar immer in meinem Zimmer und schaue Anime."
            b "Aber deswegen hasse ich noch lange nicht andere Menschen."
            b "Vor allem nicht dich und unsere Mutter."
            b "Auch wenn es manchmal so rüberkommt."
            b "Also komm."
            b "Lass uns einkaufen gehen."
            sis "Nein."
            sis "Ich will nicht mehr."
            sis "Mir ist die Lust vergangen."
            sis "Ich geh nach Hause."
            b "Bist du dir da sicher?"
            sis "Ja."
            b "Aber ich bin mir sicher, dass %(supermarkt)s nun auch...{w}ähm...{w}ähm...{w}Gummibärchen hat!"

            show laura surprised
            with dissolve

            sis "Vielleicht sollte ich doch mitgehen."
            
            show laura embarrassed
            with dissolve
            
            sis "Immerhin hab ich es unserer Mutter versprochen."
            
            show laura mad
            with dissolve
            
            sis "Aber ich mach das nicht gerne!"
            
            b "Ich hab's ja verstanden."
            "Typisch %(sisName)s."
            "Sie ist ja soooo berechenbar."
            b "Wir sollten uns mit dem Einkaufen beeilen."
            sis "OK."
  
            scene bg supermarkt
            with fade
    
            play music m_shop
    
            sis "%(berndName)s?"
            b "Ja?"
    
            #show laura fragezeichen
            #with dissolve
            #Bild existiert noch nicht
            #Ginga Ale
    
            sis "Was sollen wir nochmal einkaufen?"
    
            b "Keine Ahnung!"
            b "Ich dachte, du wüsstest das."
            
            #show laura mad
            #with dissolve
            
            sis "Großartig..."
            sis "Dich kann man auch für Nichts gebrauchen."
            b "Naja..."
            b "Kaufen wir halt Butter und Rügenwalder."   
            sis "Sicher, dass wir nicht mehr brauchen?"
            b "Nein, aber was sollen wir machen?"
            sis "Ich könnte Mama anrufen."
            sis "Ich hab' mein Handy dabei."
            b "Na dann, ruf sie an."   
            sis "OK."
            "Sie zieht ein rosafarbenes Handy aus der Tasche."
            "Die tippt aber schnell."
            "Fast so schnell wie ich an der Computertastatur."
            "Aber wieso hat sie in ihrem Alter schon ein Handy?"
            "Ist das normal heutzutage?"
           
            show laura neutral
            with dissolve
            
            sis "Hallo Mama, ich bin's."
            sis "Wir wissen nicht, was wir einkaufen sollen."
            sis "..."
            sis "OK."
            sis "Sonst noch was?"
            sis "..."
            sis "Alles klar!"  
            sis "Bis gleich!"
            "Sie legt auf."
            
            show laura mad
            with dissolve
            
            sis "Sie sagt, dass wir auch noch Milch und Brot brauchen."
            "Also Milch, Butter, Brot und Rügenwalder."
            b "OK."
            b "Dann besorgen wir das schnell und gehen dann nach Hause."
            sis "Ja."
          
            hide laura mad
            with dissolve
            
            "Nachdem wir alles gefunden haben, gehen wir zur Kasse."
            "Vor uns ist eine ältere Frau, die langsam einen Artikel nach dem anderen auf's Band legt."
            "Die Kassiererin ist sichtlich genervt."
            "Warum kaufen alte Leute immer so viel ein und müssen immer auf den Cent genau bezahlen?"
            
            b "%(sisName)s?"
            
            show laura mad
            with dissolve
            
            sis "Was denn?"
            b "Willst du Kaugummis?"
            sis "Nein."
            b "Wirklich nicht?"
            sis "Nein!"
            b "Sicher?"
            sis "Ja."
            b "Nun stell dich nicht so an."
            
            show laura mad_talk
            with dissolve
            
            sis "Ich will aber keine."
            b "Ich schenk sie dir auch."
            
            show laura surprised
            with dissolve
            
            sis "Warum?"
            b "Darum."
            b "Und jetzt nimm sie gefälligst."
    
            show laura happy
            with dissolve
            
            "Sie nimmt sich eine Packung Erdbeer-Kaugummis und legt sie auf's Band."
            
            $ eins_streit = 5
            

    scene black
    with fade
    
    if eins_streit in (1,2):   
        "Ich gehe in meinen Keller."
    
    else:
        "Eine halbe Stunde später..."
        b "Endlich wieder zu Hause."
    
    stop music fadeout 1.0
    
    scene bg keller
    with fade
    
    play music m_bernd
    
    b "Mal schauen, ob der Faden mit meinen Daten noch auf /b/ ist..."
   
    scene bg keller_kc
    with dissolve
   
    "..."
    b "Nichts."
    b "Glück gehabt."
    "Es scheint, als wäre wirklich nichts weiter passiert..."
    "Bernd ist wohl wirklich völlig unfähig."
    
    if eins_streit in (1,2):
        jump eins_streit_mit_aussprache
        
    elif eins_streit == 5:
        jump eins_streit_nicht
    
    else:
        jump eins_streit_ohne_aussprache    
    
    
label eins_streit_mit_aussprache:
    
    play sound "sounds/door_1.wav"
    
    show laura neutral
    with dissolve
    
    sis "%(berndName)s?"
    "Nicht die schon wieder."
    "Jetzt kommt noch was zu der Sache von vorhin."
    b "Ja? {w}Was ist?"
    
    show laura happy
    with dissolve
    
    sis "Deine Freundin..."
    "Ist sie jetzt gekommen, um sich doch über mich lustig zu machen?"
    b "Sie ist nicht meine Freundin."
    sis "Doch, doch."
    b "Nein."
    sis "Also deine Freundin..."
    "Hört sie mir überhaupt zu?"
    sis "Wie sieht sie denn aus?"
    b "Was?"
    "Wieso interessiert sie das?"
    sis "Erzähl doch mal."
    sis "Welche Haarfarbe hat sie?"
    sis "Trägt sie eine Brille?"
    sis "Was für Hobbys hat sie?"
    b "Sie ist blond, trägt eine Brille und..."
    b "Moment mal."
    b "Wieso interessiert dich das überhaupt?"
    
    show laura surprised_drop
    with dissolve
    #Rolleyes wären hier besser
    #Ginga Ale
    
    sis "Ähm...also...ähm..."
    b "Hmm?"
    
    show laura pissed
    with dissolve
    
    sis "Darf deine kleine Schwester das denn nicht wissen?"
    b "Doch, aber..."
    sis "Aber?"
    b "Aber das hat dich sonst nie interessiert."
    sis "Doch. {w}Hat es. {w}Aber du hast immer nur deine Anime geschaut."
    b "Anime, %(sisName)s, Anime."
    
    show laura neutral
    with dissolve
    
    sis "Ja, ich weiß."
    sis "Das habe ich doch auch gesagt."
    "Warte, was?"
    "Hat sie es soeben wirklich gesagt?"
    "Irgendwie macht mich das glücklich."
    sis "Weißt du denn, was ich den ganzen Tag über so mache?"
    "Wenn sie mich so fragt..."
    b "Nein."
    
    show laura pissed
    with dissolve
    
    sis "Mensch, %(berndName)s."
    b "Was denn?"
    sis "Wieso interessierst es dich nicht, wie es mir geht oder was ich mache?"
    b "Weil du meine Schwester bist?"
    sis "Du bist doof."
    b "Seit wann interessieren sich Geschwister für sowas?"
    sis "Idiot."
    "Sie geht aus dem Zimmer und knallt die Türe zu."
    
    hide laura pissed
    with dissolve
    
    "Was war das denn jetzt gerade für eine Aktion?"
    "Na ja, was soll's."
    "Ich lauer noch ein wenig auf Krautchan und gehe dann schlafen."
    
    jump eins_streit_tag_darauf
    
    
label eins_streit_ohne_aussprache:

    show mutter boese
    with dissolve
    #Bild existiert noch nicht
    #Ginga Ale
    
    $ berndNameCaps = berndName.upper()
    ma "{size=24}%(berndNameCaps)s!{/size}"
    
    "Urghs."
    "Ich zucke aufgrund der lauten Stimme zusammen."
    
    ma "%(berndName)s!"
    "Was ist denn nun schon wieder?"
    b "Was ist?"
    ma "Du gehst jetzt auf der Stelle zu deiner Schwester und entschuldigst dich!"
    "Die kleine Petze."
    b "Nein, wieso sollte ich?"
    ma "Das fragst du noch?"
    ma "Du bist wirklich dumm, %(berndName)s."
    ma "Deine Schwester kam weinend nach Hause, {w}hat sich in ihr Zimmer eingeschlossen{w} und weint immer noch."
    ma "Man hört sie immer noch schluchzen."
    b "Und wo ist das Problem?"
    "Kann man nicht einmal seine Ruhe haben?"
    b "Sie ist nun mal eine kleine Heulsuse."

    $ berndNameCaps = berndName.upper()
    ma "%(berndNameCaps)s!"
    ma "Du gehst dich jetzt auf der Stelle entschuldigen."

                
    menu:
        "Soll ich auf meine Mutter hören?"
        
        "Ich sollte mich vielleicht wirklich entschuldigen gehen.":
            $ sisLove += 5
            b "Ist ja gut."
            b "Ich geh mich ja schon entschuldigen."
            ma "Und wehe, sie weint danach immer noch."
            b "Was ist dann?"
            ma "Dann setzt es was."
            ma "Und zwar richtig, das kann ich dir versprechen."
            "Oh, Mann. {w}Sie scheint wohl *wirklich* sauer zu sein."
        
        
        "Nie im Leben.":
            $ sisLove -= 5
            $ maLove -= 5
            b "Lass mich überlegen."
            
            $ renpy.pause(2)
            
            b "Nö."
            ma "Das meinst du nicht wirklich."
            
            menu:
                " "
                
                "Doch.":
                    b "Doch."
                    b "Ich meine das ernst."
                    ma "{size=20}DU GEHST DICH JETZT ENTSCHULDIGEN.{/size}"
                    ma "{size=20}SOFORT!!{/size}"
                    ma "{size=20}ODER ES SETZT WAS!{/size}"
                    b "Und was wäre das?"
                    
                    show mutter hochnaesig
                    with dissolve
                    #Bild exisitiert noch nicht
                    #Ginga Ale
                    
                    ma "Du bist schon 25."
                    ma "Du bist damit alt genug, um auszuziehen und auf eigenen Beinen zu stehen."
                    "Verdammt."
                    "Das ist mein Schwachpunkt."
                    "Egal, wie alt ich auch sein mag."
                    "Ich bin von ihr abhängig."
                    b "OK, OK."
                    b "Ich geh ja schon."
                
                "Nein.":
                    b "Nein."
                    b "Verstehst du keinen Spaß?"
                    ma "In solchen Sachen nicht, %(berndName)s."
                    ma "Du hast sowieso einen komischen Humor."               
                    
    scene bg wohnung_innen
    with fade
        
    sis "*schluchz*"
    "Oh, Mann."
    "Man hört sie wirklich in der kompletten Wohnung."
    "Kann sie nicht wenigstens einmal ihre Ruhe geben?"
    "Vielleicht sollte ich einfach warten, bis sie sich beruhigt hat."
    "Ich drehe mich um, doch in dem Moment..."
    
    show mutter boese
    with flash
    
    "Verdammt."
    sis "*schluchz*"
    
    play sound "sounds/knock.wav"
    
    sis "*schluchz*"
    sis "J-ja?"
        
    b "Ähm...{w}%(sisName)s?"    
    sis "Was ist?"
    b "Kannst du die Tür aufmachen?"
    sis "NEIN."
    sis "ICH WILL NICHT. *schluchz*"
    b "Nun komm schon."
    sis "NEIN! DU HASST MICH!"
    b "Das stimmt doch gar nicht."
    sis "DU HAST ES DOCH SELBST GESAGT!"    
    b "Ich hab das nicht so gemeint."
    sis "WIE DENN DANN? *schluchz*"
    sis "WIE KANN MAN EIN {w}*schluchz* {w}\"ICH HASSE DICH!\" ANDERS MEINEN?"
    b "Komm schon, mach die Tür auf, dann können wir darüber reden."
    sis "NEIN!"
    b "Nun stell dich nicht so an."
    sis "ICH MACHE DIE {w}*schluchz* {w}TÜR NICHT AUF!"
    sis "ERST MUSST DU DICH {w}*schluchz* {w}ENTSCHULDIGEN!"
    b "OK, dann..."
    "Wieder drehe ich mich um {w}und wieder sehe ich..."
    
    show mutter boese
    with flash
    
    "Mist."
    b "{size=6}T-tut mi-mir...{/size}"
    b "{size=6}Tut mir...{/size}"
    "Es hat keinen Sinn."
    "Ich kann das nicht."
    
    #scene cg laura_tuer
    #with fade
    #Bild existiert noch nicht
    #Ginga Ale

    #In diesem CG sieht man eine leicht geöffnete Tür und eine mit einem Auge herauslugende Laura
    #ähnlich wie http://img3.imageshack.us/img3/3193/konbanwa.jpg
    #nur, dass Laura hier weinen muss oder aber rote Augen hat (ihr wisst, wie ich das meine)
        
    "!"
    "Sie hat die Tür geöffnet."
    sis "Hm?"
    b "{size=8}E-e-es tut...{/size}"
    sis "Was sagst du da?"
    sis "Ich kann dich nicht verstehen."
    b "{size=10}T-tut mir l-...{/size}"
    sis "Du bist komisch."
    sis "Wenn du nicht lauter sprichst, mache ich die Türe wieder zu."
    b "Warte!"
    "Doch sie scheint es nicht zu hören."
    #irgendwie gefallen mir die obigen paar Zeilen nicht
    "Langsam schließt sie die Türe wieder."
          
    $ maLove -= 5
    "Die Türe ist wieder zu."
    b "Ent...schuldi...gung."
    "Ich drehe mich um und will gehen."
             
    show mutter boese
    with dissolve
    #Bild existiert noch nicht
    #Ginga Ale
             
    ma "Das war noch nicht alles!"
    ma "Du entschuldigst dich jetzt sofort anständig bei ihr!"
    b "Ich hab mich entschuldigt."
    ma "Nein."
    b "Ach, lass' mich in Ruhe."
    $ berndNameCaps = berndName.upper()
    ma "%(berndNameCaps)s!"
    "Frustriert gehe ich wieder in meinen Keller zurück."

    scene bg keller
    with fade
    
    "Ich werfe mich auf mein Bett."
    
    play music m_traurig

    "Verdammt."
    if kaugummi == 1:
        "Ich hole die Kaugummipackung, die ich für %(sisName)s kaufte, aus der Hosentasche."
    else:
        pass
    "Wieso?"
    "Wieso kann ich mich nicht entschuldigen?"
    "Wieso kann ich mich noch nicht mal bei meiner eigenen Schwester entschuldigen?"
    "Wieso muss ich Mädchen immer so schlecht behandeln?"
    "Dabei will ich doch nur mal in den Arm genommen werden und ein \"Ist schon in Ordnung, %(berndName)s.\" hören."
    "Aber das wird nie geschehen."
    "Denn ich bin ein Versager."
    "Ich versage hart mit Menschen."
    "Ich versage hart mit Mädchen."
    "Ich versage hart beim Normalsein."
    "Ich habe keine Freunde."
    "Ich gehe nicht auf Partys."
    "Ich mache nichts Anderes außer im Keller zu sitzen und zu lauern."
    "Ich werde niemals Freunde haben."
    "Ich werde niemals eine Freundin haben."
    "Weinend schlafe ich ein..."    
    
    stop music
    
    jump eins_streit_tag_darauf
    
label eins_streit_nicht:
    
    play sound "sounds/door_1.wav"
    
    show laura neutral
    with dissolve
    
    sis "%(berndName)s?"
    "Was will die denn jetzt schon wieder?."
    b "Ja?" 
    sis "Hier. {w}Das Geld."
    b "Welches Geld?"
    sis "Das Geld für die Kaugummis? {w}Nimm es{nw}"
    b "Behalt' es. Ich sagte, ich schenke dir die Kaugummis."
    
    show sis pissed
    with dissolve
    
    sis "Aber...{nw}"
    b "Kein \"Aber\". Ich sagte, du sollst es behalten."
    
    show sis mad
    with dissolve
    
    sis "Du bist wirklich unmöglich."
    
    "Sie geht wieder aus dem Keller und knallt die Türe zu."
    
    hide laura pissed
    with dissolve
    
    "Was war das denn jetzt gerade für eine Aktion?"
    "Na ja, was soll's."
    "Ich lauer noch ein wenig auf Krautchan und gehe dann schlafen."
    
    jump eins_streit_tag_darauf
    
label eins_streit_tag_darauf:
    
    scene black
    with fade
    
    "Am nächsten Morgen..."
    
    ma "%(berndName)s?"
    ma "Willst du nicht langsam mal aufstehen?"
    b "Wie spät ist es denn?"
    ma "Schon 13 Uhr."
    
    scene bg keller_aus
    with flash
    
    show mutter neutral
    with dissolve
    
    b "WAS!?"
    b "Schon so spät?"
    ma "Wird Zeit, dass du deine Schwester abholst."
    ma "Oder muss ich das wieder machen?"
    "Wieso soll ich das immer machen?"
    "Kann sie nicht einsehen, dass ich andere Dinge zu tun habe."
    b "Nein, ich habe wieder eine Verabredung."
    ma "Mit wem?"
    b "Mit %(wBerndName)s."
    ma "Wer ist %(wBerndName)s?"
    ma "Deine imaginäre Freundin?"
    ma "Mach dich nicht lächerlich."    
    ma "Was soll ich nur mit dir machen...?"
    "Sie verlässt das Zimmer."
    
    "Ich mache mich fertig, um mich mit %(wBerndName)s zu treffen."
    
    stop music fadeout 1.0
    
    scene bg zuhause_draussen
    with fade
    
    "Dieses Mal sollte der Weg leichter zu finden sein."
    "Tatsächlich, ich weiß noch genau, wo es lang geht."
    
    scene bg alexanderplatz_drei
    with fade
    
    "Als ich ankomme wartet %(wBerndName)s bereits auf mich."
    show anja neutral
    with dissolve
    
    play music m_anja
    
    bw "Hey, %(berndName)s."
    b "H- Hi."
    bw "..."
    b "..."
    "Spannendes Gespräch."
    bw "...und?"
    b "Was?"
    bw "Na... wie gehts dir so?"
    b "Hm..."
    b "Ja."
    bw "Du bist ja nicht sehr gesprächig..."
    "Komm endlich zur Sache."
    b "..."
    b "Du wolltest mir erklären, warum du meine Hilfe brauchst."
    bw "Ja."
    bw "Also..."
    bw "Um es auf den Punkt zu bringen:"
    bw "Wir müssen Krautchan retten."
    "Krautchan retten."
    "Soso."
    b "Aha."
    b "Warte... was?"
    bw "Krautchan ist nicht mehr das, was es mal war."
    b "Du meinst die Neuschwuchteln."
    b "Die stören doch kaum noch."
    bw "Nein."
    bw "Wie erkläre ich das am besten..."
    bw "Krautchan wurde übernommen."
    b "lolwas?"
    "Wer würde denn Krautchan übernehmen?"
    "4chan?"
    "Oder ein anderes Imageboard?"
    bw "Der Server wurde beschlagnahmt."
    bw "Krautchan..."
    bw "...ist bereits tot."
    b "Was zum...?"
    "Server beschlagnahmt."
    "Von der Polizei?"
    "Warum das denn?"
    "Kinderpornografie?"
    "Wohl kaum..."
    bw "Die genauen Einzelheiten kenne ich auch nicht."
    bw "Ich weiß nur, dass der Server eines Morgens von der Polizei beschlagnahmt wurde."
    bw "Wir sind die Einzigen, die Krautchan retten können, %(berndName)s."
    bw "Deshalb brauch ich deine Hilfe."
    bw "Du bist der Einzige, dem ich vertrauen kann."
    b "..."
    "Was soll das?"
    "Sie trollt mich doch nur."
    "Ich wusste es von Anfang an."
    "Aber wie kann ich mir sicher sein?"
    "..."
    "Aha!"
    b "Aber Krautchan ist doch noch online?"
    b "0/10"
    b "Offensichtlicher Troll ist offensichtlich."
    "Der habe ich's gezeigt."
    "So leicht lasse ich mich nicht trollen."
    bw "Es scheint, als wäre Krautchan noch online, ja."
    bw "Aber die Realität sieht anders aus."
    b "Was soll das heissen?"
    "Willkommen in der Matrix oder was wird das hier?"
    bw "Die Seite wird von der Polizei benutzt um Bernds zu überwachen."
    bw "Es ist eine Falle!"
    "Oho!"
    "Totale Überwachung!"
    "So was glaubt doch kein Mensch."
    b "Wieso sollte ich dir das glauben?"
    b "Die Admins hätten doch schon längst-"
    bw "Die Admins?"
    bw "Tsaryu ist nach Japan ausgewandert."
    bw "Shaky wird von der Polizei verfolgt und ist nach Mexiko geflohen."
    bw "dergeneral ist untergetaucht."
    bw "Krautchan ist definitiv tot."
    "Da ist was dran..."
    "In letzter Zeit gab es auf KC wenig sichtbare Aktivität von Seiten der Mods."
    b "...und woher willst du das alles wissen?"
    bw "..."
    bw "Du vertraust mir nicht?"
    "Wieso sollte ich?"
    b "Bernd, das ist lächerlich!"
    b "Das klingt doch alles völlig absurd."
    bw "Hm..."
    bw "Ich habe mir wohl den falschen Bernd ausgesucht."
    bw "Ich kann also nicht auf deine Hilfe zählen?"
    b "Nicht, wenn du mir nicht erklärst, was das alles zu bedeuten hat."
    bw "Wenn ich es wüsste, würde ich es dir erklären."
    bw "Es liegt an uns, das herauszufinden."
    "Klingt wie der Plot eines schlechten Action-Adventures."
    bw "Wir müssen den Verantwortlichen finden und Krautchan retten!"
    b "Das ergibt doch alles keinen Sinn..."
    bw "Entweder du glaubst mir oder du glaubst mir nicht."
    bw "Was nun?"
    "So, %(berndName)s."
    "Jetzt musst du dich entscheiden."
    
    menu:
        "Ich..."
        
        "...glaube ihr.":
            $ friendLove += 10
            jump eins_accept_fBernd
        "...glaube ihr. NICHT.":
            $ friendLove -= 5
            jump eins_refuse_fBernd
            
label eins_accept_fBernd:
    $ anjaAccept = 1
    $ anjaRoute = 1

    b "Das klingt zwar alles sehr merkwürdig aber..."
    b "Ich glaube dir."
    "Tue ich das?"
    bw "Gut."
    bw "Wir haben keine Zeit zu verlieren."
    bw "Wie gehen wir vor?"
    "Das fragt sie mich?"
    b "Woher soll ich das wissen?"
    b "Es war doch deine Idee."
    bw "Also gut dann..."
    bw "Versuch' so viele Informationen wie möglich zu finden."
    bw "Bleib' am besten zu Hause und benutze das INTERNET."
    "Das kann ich wenigstens."
    bw "Ich werde mich ein wenig umhören..."
    bw "Soziale Interaktion liegt mir wohl besser als dir."
    "Das merkt sie aber früh."
    b "In Ordnung."
    b "Ich werde sehen, was ich tun kann."
    bw "OK."
    bw "Dann sehen wir uns demnächst."
    bw "Ich werde dir eine E-Mail schreiben, wenn ich was herausfinde."
    b "Einverstanden."
    bw "Bis dann."
    b "OK..."
    "Sie bricht zur Straßenbahnhaltestelle auf."
    hide anja neutral
    with dissolve
    b "Am besten gehe ich nach Hause."
   
    stop music fadeout 0.4
   
    scene black
    with fade
    
    "Später am Abend..."
    
    scene bg keller
    with fade
    
    play music m_bernd
     
    "Ich setze mich vor meinen Rechner."
    b "Informationen sammeln..."
    b "Wo fange ich da an?"
    "Krautchan."
    "Wo sonst?"
    "www.krautchan.net"
    "..."
    "..."
    b "Warum dauert das so lange?"
    "Ah..."
    "Endlich lä-"
    "404"
    "File not found."
    b "Krautchan ist..."
    b "...tatsächlich offline."
    
    scene black
    with fade
    
    stop music fadeout 0.4
    
    jump zwei_anja
    
label eins_refuse_fBernd:
    $ anjaAccept = 0
    $ anjaRoute = 0
    b "Ich kann das irgendwie nicht glauben."
    b "Das ist doch völliger Unsinn."
    bw "Aber %(berndName)s!"
    bw "An wen soll ich mich sonst wenden?"
    bw "Bitte!"
    bw "Hilf mir!"
    menu:
        "..."
        "OK.":
            $ friendLove += 10
            jump eins_accept_fBernd
        "Nein.":
            $ friendLove -= 10
            b "Tut mir Leid, aber ich denke, ich gehe besser."
            
    "Ohne ein weiteres Wort zu sagen, drehe ich mich um und gehe."
    hide anja neutral
    with dissolve
    
    bw "%(berndName)s!!"
    bw "Du kannst mich doch nicht im Stich lassen!"
    
    "Doch."
    "Das kann ich."
    "Verarschen kann ich mich nämlich selbst."
    
    stop music fadeout 0.4
    
    scene black
    with fade
    
    "Wieder zu Hause..."
    
    jump eins_krautchanOffBernd
    
label eins_krautchanOffBernd:
    "Ich setze mich vor meinen Rechner."
    "www.krautchan.net"
    "..."
    "..."
    b "Warum dauert das so lange?"
    "Ah..."
    "Endlich lä-"
    "404"
    "File not found."
    b "Krautchan ist..."
    b "...offline."
    
    jump zwei_bernd #Kapitel 2 - Bernd