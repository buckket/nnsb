label zwei_bernd:
    #kc ist down, bernd ragiert.
    "Krautchan ist tatsächlich offline..."
    "Aber wieso?"
    "Sicher doch nur, weil mal wieder irgendwer getrollt hat."
    "Amoklauf oder so."
    "Das war bisher immer so."
    "Es ist sicherlich nichts ernstes."
    "Wieso sollte es auch?"
    "Nein."
    "Morgen ist alles wieder ok."
    "Bestimmt."
    
    if sisLove >= 40:
        #tür auf
        show laura happy
        with dissolve
    
        sis "Hey, %(berndName)s."
        b "Was willst du?"
        
        show laura pissed
        with dissolve
        
        sis "Warum bist du immer so unfreundlich?"
        
        show laura neutral
        with dissolve
        
        sis "Na, ist ja auch egal."
        sis "Ich wollte nur fragen, ob du Hunger hast."
        sis "Es gibt gleich Abendessen."
        b "Nicht wirklich."
        sis "...wirklich nicht?"
        b "Wirklich nicht."
        sis "Nicht mal ein bisschen?"
        b "Wenn du mich dann in Ruhe lässt..."
        
        show laura pissed
        with dissolve
        
        sis "Dann gehe ich eben."
        
        hide laura pissed
        with vpunch
        
        "Warum knallt sie dauernd die Tür?"
        "Ich verstehe es nicht..."
        "Egal."
        "Mal gucken, ob Krautchan schon wieder da ist."
        "..."
        "Nein."
    "Seit wann ist es wohl schon down?"
    "Heute morgen ging es noch."
    "Das muss während des Treffens mit dieser Anja passiert sein."
    "..."
    "Ob sie etwas damit zu tun hat?"
    "Angeblich ist sie ja ein Bernd..."
    "...auch wenn ich es nicht wirklich glaube."
    "Steckt sie dahinter?"
    "Immerhin redete sie dauernd davon, dass Krautchan gerettet werden müsse."
    "..."
    "Ach Unsinn!"
    "Woher sollte sie das denn wissen?"
    "Die spinnt doch nur rum."
    "Reiner Zufall."
    "Diese blöden Verschwörungstheorien sind doch eh alle nur aus der Luft gegriffen."
    "Morgen früh ist Krautchan wieder online."
    "Ganz sicher."
    
    if sisLove >= 40:
        #tür auf
        show laura happy
        with dissolve
        
        sis "Ich bringe dir dein Essen, %(berndName)s."
        "Was zum...?"
        b "Hab ich nicht gesagt, dass ich nichts möchte?"
        sis "Ist mir egal."
        
        show laura neutral
        with dissolve
        
        sis "Du sagst oft, dass du nicht willst, aber meinst genau das Gegenteil."
        "Ich gebe es nicht gern zu, aber sie hat Recht."
        "Ich habe wirklich ziemlichen Hunger."
        b "Na gut..."
        b "Dann gib halt her."
        
        show laura happy
        with dissolve
        
        "Mit einem breiten Grinsen überreicht sie mir einen Teller."
        "Nudeln mit irgendeiner roten Soße."
        "Wahrscheinlich irgendwas mit Tomate."
        "Ich schaufel mir ein paar Nudeln auf die Gabel aber..."
        b "Warum schaust du mich so an?"
        sis "Nun iss schon!"
        b "..."
        b "Ich kann nicht, wenn du mich dabei anstarrst."
        
        show laura neutral
        with dissolve
        
        sis "Schon gut, schon gut..."
        sis "Ich starre ja nicht."
        sis "Nun iss schon."
        "Irgendwas stimmt hier nicht..."
        "...ob ich das wirklich essen sollte?"
        "Nachher ist das vergiftet oder so?"
        "..."
        "Warum sollte Laura mich vergiften wollen?"
        "So ein Unsinn."
        "Ich esse es einfach."
        "Dann kriege ich schon raus, weswegen sie so scharf darauf ist."
        "Ich nehme mir die Gabel und schiebe eine Ladung Nudeln in meinen Mund."
        sis "..."
        "Hm..."
        b "Gar nicht schlecht."
        
        show laura happy
        with dissolve
        
        sis "Es schmeckt dir?"
        b "Ja, es ist sogar ziemlich gut."
        "...vielleicht liegt das auch nur daran, dass ich die letzten Wochen lang fast nur Suppe bekommen habe."
        b "Aber was ist daran so wichtig?"
        
        #laura stolz
        
        sis "Tja..."
        sis "...das habe ich gekocht!"
        "Was?"
        "Laura kann kochen?"
        sis "Überrascht?"
        b "Nicht wirklich."
        
        show laura pissed
        with dissolve
        
        sis "Was soll das denn bedeuten?"
        b "Ich dachte mir eigentlich schon, dass du gut kochen kannst."
        
        show laura surprised
        with dissolve
        
        show laura embarrassed
        with dissolve
        
        sis "W- w- was, echt?"
        sis "E-eigentlich habe ich heute zum e-ersten Mal richtig so g-gekocht..."
        "Oh, sieh an, das ist ihr peinlich."
        "Naja, Hauptsache ist, dass das Essen schmeckt."
        sis "I-ich geh dann wieder nach oben..."
        b "Okay."
        
        show laura happy
        with dissolve
        
        sis "Bis später, %(berndName)s!"
        b "Ja, bis später."
        
        hide laura happy
        with dissolve
        
    "...und was mache ich jetzt?"
    "Irgendwie kann ich nicht den ganzen Tag herumsitzen und warten, bis Krautchan wiederkommt."
    "...wenn es überhaupt jemals zurückkommt."
    "Ich sollte..."
    menu:
        "...einfach abwarten. Das wird schon wieder.":
            "Das wird sich schon von selbst wieder richten."
            "Hat es bisher ja immer."
            
            jump zwei_bernd_ende
            
            
        "...etwas unternehmen! Wer, wenn nicht ich?":
            jump zwei_bernd_kc_retten

label zwei_bernd_kc_retten:    
    "Diese Ungewissheit macht mich fertig!"
    "Ich muss es wissen."
    "Irgenwas muss ich doch tun können."
    
label zwei_bernd_ende:
    scene bg keller
    with fade
    #test
    "Plötzlich höre ich etwas..."
    "...ein Klopfen?"
    "Irgendwas ist dort am Fenster..."
    "Ich stelle mich auf Zehenspitzen auf mein Bett und sehe nach draußen, aber ich kann nichts erkennen."
    "Was ist das?"
    "Ob ich das Gitter einfach rausnehmen kann?"
    "Ich greife nach dem Gitter und ziehe mit meinem ganzen Gewicht."
    
    #show bg rabe
    #with dissolve
    
    #hide bg rabe
    #with flash
    
    #$ renpy.pause(0.5)
    
    #scene black
    #with fade
    
    #$ renpy.pause(2.0)
    
    #scene bg keller
    #with fade
    
    nvl clear
    
    nvlc "Riss das Blech vom Fenster runter, und herein stolziert' - oh Wunder!"
    nvlc "Ein gewalt'ger, hochbejahrter Rabe schwirrend zu mir her;"
    nvlc "Flog, mit mächt'gen Flügelstreichen, ohne Gruß und Dankeszeichen,"
    nvlc "Stolz und stattlich sonder Gleichen, durch den Keller hin und her -"
    nvlc "Setzte sich auf meinen Bildschirm, rutschte etwas hin und her"
    nvlc "Setzte sich und sonst Nichts mehr."
    
    nvl clear
    
    nvlc "Und trotz meiner Trauer brauchte er dahin mich, daß ich lachte,"
    nvlc "So gesetzt und gravitätisch herrscht' auf meinem Bildschirm er."
    nvlc "\"Ob auch alt und nah dem Grabe,\" sprach ich, \"bist kein feiger Knabe,"
    nvlc "Grimmer, glattgeschor'ner Rabe, der Du kamst vom Schattenheer -"
    nvlc "Sprich, welch' stolzen Namen führst Du in der Nacht pluton'schem Heer?\""
    nvlc "Sprach der Rabe: \"Lauer Meer.\""
    
    nvl clear
    
    nvlc "Ganz erstaunt war ich, zu hören dies Geschöpf, es weiß von Memen,"
    nvlc "Schien auch wenig Sinn zu liegen in dem Wort bedeutungsleer;"
    nvlc "Denn wohl Keiner könnte sagen, dass ihm je in seinen Tagen"
    nvlc "Sonder Zier und sonder Zügen so ein Tier erschienen wär',"
    nvlc "Dass auf seinem Bildschirmrande so ein Tier erschienen wär'"
    nvlc "Das ihm sagte: \"Lauer meer.\""
    
    nvl clear
    
    nvlc "Dieses Wort nun sprach der Rabe dumpf und hohl, wie aus dem Grabe,"
    nvlc "Als ob seine ganze Seele in dem einen Worte wär'."
    nvlc "Weiter Nichts ward dann gesprochen, nur mein Herz noch hört' ich pochen,"
    nvlc "Bis das Schweigen ich gebrochen: \"Lauern würde ich gerne sehr -"
    nvlc "Morgen wird KC zurück sein, denn man trollt nur grade sehr.\""
    nvlc "Sprach der Rabe: \"Lauer meer.\""
    
    nvl clear
    
    nvlc "Plötzlich durch die Lüfte schwebend, seine Stimme bald erhebend,"
    nvlc "Segelt durch mein Kellerfenster, noch ein zweiter Vogel her,"
    nvlc "Dieser Vogel, ein knallgrüner, mit zerrüttetem Gefieder"
    nvlc "Vor dem Regen reingeflohen, tropfend voller kalter Nässe,"
    nvlc "Setze sich neben den Raben, zitterte vor kalter Nässe,"
    nvlc "Und laut rief er: \"Halt die Fresse!\""
    
    nvl clear
    
    