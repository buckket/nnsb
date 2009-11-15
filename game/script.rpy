# Script

init python:
    import os
    from random import choice, shuffle
 
    fastFade = Fade(.2, 0, .2, color="#000")
    flash = Fade(.1, 0, .3, color="#fff")
    slowFlash = Fade(.1, 0, .5, color="#fff")
    damnSlowFlash = Fade(.2, 0, 1, color="#fff")
    slowFade = Fade(.8, 1, 0, color ="#000")
    cloudtrans = ImageDissolve("images/splash/cloud_trans.png", 1.0, 12, reverse=True)
    cloudtransSlow = ImageDissolve("images/splash/cloud_trans.png", 2.0, 12)
    noisetrans = ImageDissolve("images/splash/noise_trans.png", 1.0, 8, reverse=True)
    wooshTrans = ImageDissolve("images/splash/woosh_trans.png", 0.5, 8)
    wooshTransReverse = ImageDissolve("images/splash/woosh_trans.png", 0.5, 8, reverse=True)
    gradientTrans = ImageDissolve("images/splash/grad_trans.png", 0.5, 8)
    gradientTransReverse = ImageDissolve("images/splash/grad_trans.png", 0.5, 8, reverse=True)
    spotTrans = ImageDissolve("images/splash/spots_trans.png", 1.0, 8)
    fastMove = MoveTransition(0.2)
    slowDissolve = Dissolve(1.0)
    fastDissolve = Dissolve(0.3)
    
    #positionen
    right = Position(xpos=0.8,xanchor="right")
    left = Position(xpos=0.2,xanchor="left")
    leftoffscreen = Position(xpos=0.0,xanchor="right")
    rightoffscren = Position(xpos=1.0,xanchor="left")
    leftedge = Position(xpos=0.0,xanchor="center")
    rightedge = Position(xpos=1.0,xanchor="center")
 
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)
    config.window_icon = "laura-anja-icon 128x128.png"
    style.jp = Style(style.say_thought)
    style.jp.font = "mikachan.ttf"
    style.jp.italic = False
    
    style.jpmenu = Style(style.menu_choice)
    style.jpmenu.font = "mikachan.ttf"
    style.jpmenu.italic = False
    style.jpmenu.color = (210,210,210,255)
    
    style.slow = Style(style.say_thought)
    style.slow.slow_cps = 30    

    menuImages = ["images/title_laura.png","images/title_stalker.png","images/title_anja.png"]
    shuffle(menuImages)
    
    style.mm_root.background = anim.TransitionAnimation(
        menuImages[0], 10.0, slowDissolve,
        menuImages[1], 10.0, slowDissolve,
        menuImages[2], 10.0, slowDissolve)
    
    #config.log = "debuglog.txt"
    
    #diverse funktionen

    #string kürzen
    #kürzt einen text auf max buchstaben
    #wenn max nicht definiert oder 0 ist, auf die hälfte der länge
    def stringShorten(s,max=0):
        if(max==0):
            max = len(s)/2
        return s[0:max]
        
    def stringEnde(s,last=0):
        if(last==0):
            last = len(s)/2
        return s[len(s)-last:len(s)]
        
    if persistent.wieherbuhSprache is None:
        persistent.wieherbuhSprache = 0
    
    #Bilder laden
    #diese Funktion lädt alle Bilder aus einem gegeben Ordner
    #wenn das Bild "test.png" aus "images/backgrounds/test" geladen wird
    #entspricht das einem image backgrounds test = "images/backgrounds/test.png"
    def loadImagesFromDir(dirName):
        thePath = config.basedir + "/game/" + dirName + "/"
        thePath = thePath.replace("\\","/")
        theFiles = os.listdir(thePath) #alle files aus dirName anzeigen
        
        for file in theFiles: #jedes File durchgehen
            if file.endswith(".png") or file.endswith(".jpg"): #wenn es in .png oder .jpg endet
                theFileName = dirName[7:len(dirName)] + "/" + file[0:len(file)-4] #"images/" und die letzten vier zeichen abschneiden
                imageName = tuple(theFileName.split("/"))#von "a/b/c" nach ('a','b','c')
                renpy.image(imageName,thePath + file) #und ein bild draus machen
    
    #Diese funktion lädt ALLE Bilder
    def loadImagesFromAllDirs():  
        imagesPath = config.basedir + "/game/images/"
        filesInImages = os.listdir(imagesPath)
        
        for filePath in filesInImages:
            if os.path.isdir(imagesPath + filePath):
                loadImagesFromDir("images/" + filePath)
    
    #diese funktion zeigt eine TL-Note mit text an
    def tlnote(text):
        ui.frame(background=Solid((0,0,0,128)),xminimum=0.3,yminimum=0.1,xpos=0.5,xanchor='center',ypos=0.01)
        ui.text(text,xanchor='center',yanchor='center',ypos=0.5,xpos=0.5,drop_shadow=(1,1))
    
    #diese funktion generiert alle OS-Bilder neu, wegen background-wechsel usw.
    def refreshOS():
        #hintergrund
        bgImage = os_BG()
        renpy.image(('bg','desktop_none'),bgImage)
        
        #/a/
        uiImage_a = os_browserfenster(titel="KC Web - /a/ - Anime & Manga",url="http://www.krautchan.net/a/",site="a")
        renpy.image(('ui','a'),uiImage_a)
        
        #/b/
        uiImage_b = os_browserfenster(titel="KC Web - /b/ - Chaos",url="http://www.krautchan.net/b/",site="b")
        renpy.image(('ui','b'),uiImage_b)
        
        #email 2
        emailListe2 = [["Geh grillen","Grill-Bernd","vor 2 Minuten",0],
        ["MEIN SACK MEIN SACK MEIN SACK","Bernd Säge","vor 4 Minuten",0],
        ["Mara ist sooooo süß!","Aslan","vor 10 Minuten",0],
        ["xD","Loserbernd","vor 30 Minuten",0],
        ["^^","Loserbernd","vor 30 Minuten",0],
        ["T_T","Loserbernd","vor 30 Minuten",0],
        ["lol owned","Stalkerbernd","vor 4 Stunden",0],
        ["Originaler Inhalt","Krautbernd","vor 12 Stunden",0],
        ["Beendigung Ihrer Nazigoldmitgliedschaft","premium@krautchan.net","vor 16 Stunden",0],
        ["UND MANGA","Mangabernd","vor 22 Stunden",0],
        ["ICH LIEBE ANIME","Animebernd","vor 23 Stunden",0],
        ["Mensch, Bernd","schnuffel90@googlemail.com","gestern",0],
        ["HAHA, OH WOW","Lauer mehr","gestern",0],
        ["Neues Passwort für ein Krautwiki-Benutzerkonto","imp@schuchtel.net","gestern",0],
        ["Trolle trollen trollend Trolle trollende Trolle","Trollbernd","gestern",0],
        ["<kein Betreff>","Neubiene","gestern",0],
        ["Jetzt Penispillen bestellen!","kim@penis.de","gestern",0],
        ["Hallo Bernd!","GSB","gestern",0],
        ["lol internet","noko","gestern",0],
        ["penispenispenispenis","xenu-chan","gestern",0],
        ["HILFE","schnuffel90@googlemail.com","gestern",0],
        ["Bestellen Sie billig Viagra! Hier klicken!","BILLIG VIAGRA","gestern",0]]
        #print "max %s emails" % len(emailListe2)
        uiImage_email_2 = os_mailbox(titel="KC Mail",postfach="pyscho_kc@hotmail.de",mails="9025",ungelesen="24",mailliste=emailListe2)
        renpy.image(('ui','email_2'),uiImage_email_2)
        
        emailListe1 = [["Hallo Bernd","GSB","vor 10 Minuten",0],
        ["lol internet", "noko", "vor 11 Minuten",0],
        ["penispenispenispenis","xenu-chan","vor 14 Minuten",0],
        ["HILFE","schnuffel90@googlemail.com","vor 15 Minuten", 0],
        ["Bestellen Sie billig Viagra! Hier klicken!","BILLIG VIAGRA","vor 2 Stunden",0],
        ["~~~SEXSPIELZEUGE~~~ BILLIG","BILLIG SEXSPIELZEUG","vor 7 Tagen",0],
        ["Find freinds online! click now","FRIENDr","vor 7 Tagen",0],
        ["generic spam mail","SPAM","vor 8 Tagen",0],
        ["how do i got spam?","SPAM","vor 8 Tagen",0],
        ["i dunno lol","SPAM","vor 8 Tagen",0],
        ["Ihre Registrierung ist abgeschlossen!","premium@kautchan.net","vor 10 Tagen",0],
        ["Ihre Bestellung: Krautchan-Nazigold","premium@krautchan.net","vor 10 Tagen",0],
        ["V_iagra","BILLIG VIAGRA","vor 2 Wochen",0],
        ["RE: Kündigung","Chef","vor 2 Wochen",0],
        ["Ihre Bestellung wurde bearbeitet","amazon.de","vor 4 Wochen",0],
        ["RE: Überweisung","Bank","vor 5 Wochen",0],
        ["POPORUPIRUPIRUPIPIPIRUPI~~!","Dokuro-chan","vor 7 Wochen",0],
        ["Spenden für Afrika","ab@zoc.ke","vor 1 Jahr",0],
        ["Spenden für Afrika","be@tr.ug","vor 1 Jahr",0],
        ["Spenden für Kautchan!","fi@ck.ja","vor 1 Jahr",0],
        ["IMPOTENT? Hier klicken","admin@lachschon.de","vor 1 Jahr",0],
        ["AUGEN-OP! BILLIG IM AUSLAND!","loserbernd@krautchan.net","vorgestern",0]]
        uiImage_email_1 = os_mailbox(titel="KC Mail",postfach="pyscho_kc@hotmail.de",mails="9001",ungelesen="4",mailliste=emailListe1)
        renpy.image(('ui','email_1'),uiImage_email_1)        
        
        hilfeText_2 = "Hey, Bernd!\n\nWieso kamst du heute nicht?\nIch habe extra auf dich gewartet. Du hast noch nicht mal geantwortet.\nIch werde morgen mal bei dir vorbeikommen.\nDeine Adresse habe ich ja von Krautchan.\n\nHEIL KRAUTCHAN!\n\n   Bernd"
        uiImage_hilfe_2 = os_mailread(titel="KC Mail - Betreff: Mensch, Bernd - Absender: schnuffel90@googlemail.com",betreff="Mensch, Bernd",absender="schnuffel90@googlemail.com",empfaenger="kein Empfänger",text=hilfeText_2)
        renpy.image(('ui','hilfe_2'),uiImage_hilfe_2)
        
        hilfeText_1 = "Hey, Bernd!\n\nIch habe deine Adresse von Krautchan und ich brauche deine Hilfe!\nWenn wir nichts unternehmen, wird es KC bald nicht mehr geben.\nDu musst mir helfen!\nKomm morgen um 14 Uhr zum Alexanderplatz. Da treffen wir uns.\nAm Besten irgendwo am Rand. Ich erkenne dich schon.\nStalkerbernd war ja so nett, ein Foto zu posten.\nIch hoffe, dass ich auf deine Hilfe zählen kann.\n\nHEIL KRAUTCHAN!\n\n   Bernd"
        uiImage_hilfe_1 = os_mailread(titel="KC Mail - Betreff: HILFE - Absender: schnuffel90@googlemail.com",betreff="HILFE",absender="schnuffel90@googlemail.com",empfaenger="kein Empfänger",text=hilfeText_1)
        renpy.image(('ui','hilfe_1'),uiImage_hilfe_1)
        
        bgImage_a = LiveComposite((1024,768),(0,0),bgImage,(50,60),uiImage_a)
        renpy.image(('bg','desktop_a'),bgImage_a)
        bgImage_b = LiveComposite((1024,768),(0,0),bgImage,(50,60),uiImage_b)
        renpy.image(('bg','desktop_b'),bgImage_b)
        bgImage_email_2 = LiveComposite((1024,768),(0,0),bgImage,(300,214),uiImage_email_2)
        renpy.image(('bg','desktop_email_2'),bgImage_email_2)        
        bgImage_email_1 = LiveComposite((1024,768),(0,0),bgImage,(300,214),uiImage_email_1)
        renpy.image(('bg','desktop_email'),bgImage_email_1)
        bgImage_hilfe_2 = LiveComposite((1024,768),(0,0),bgImage,(300,214),uiImage_hilfe_2)
        renpy.image(('bg','desktop_hilfe_2'),bgImage_hilfe_2)
        bgImage_hilfe_1 = LiveComposite((1024,768),(0,0),bgImage,(50,60),uiImage_hilfe_1)
        renpy.image(('bg','desktop_hilfe'),bgImage_hilfe_1)
        
        
    config.preferences['prefs_left'].append(
        _Preference(
            "Japanisch",
            "wieherbuhSprache",
            [ ("Aus", 0, "True"),
              ("Romaji", 1, "True"),
              ("Kanji", 2, "True") ],
            base=persistent))
            
            
    defaultNamenListe = ["Name","Rot","Blau","Marc-Oliver","Kim","Kevin","Naruto","Billy","John","Horst"] #hier brauchen wir mehr

init:
    #Wichtige Storyflags:
    #anjaTreffen - Mit Anja getroffen? (1.1)
    #lauraRoute - Laura Abgeholt? (1.1)
    #stalker - mit oder ohne stalker (1.1)
    #anjaAccept - Anja angenommen? (1.1)

    #styles
    #style.say_window.background = "#f00"

    $ bgfilename = "images/ui/os/bg.png"
    
    $ loadImagesFromAllDirs()
    
    $ refreshOS()
    
    # hintergründe
    #global
    image black = Solid((0,0,0,255))
    image white = Solid((255,255,255,255))
    
    $ fastFade = Fade(.2, 0, .2, color="#000")
    $ flash = Fade(.1, 0, .3, color="#fff")
    $ slowFlash = Fade(.1, 0, .5, color="#fff")
    $ damnSlowFlash = Fade(.2, 0, 1, color="#fff")
    $ slowFade = Fade(.8, 1, 0, color ="#000")
    $ cloudtrans = ImageDissolve("images/splash/cloud_trans.png", 1.0, 12, reverse=True)
    $ cloudtransSlow = ImageDissolve("images/splash/cloud_trans.png", 2.0, 12)
    $ noisetrans = ImageDissolve("images/splash/noise_trans.png", 1.0, 8, reverse=True)
    $ wooshTrans = ImageDissolve("images/splash/woosh_trans.png", 0.5, 8)
    $ wooshTransReverse = ImageDissolve("images/splash/woosh_trans.png", 0.5, 8, reverse=True)
    $ gradientTrans = ImageDissolve("images/splash/grad_trans.png", 0.5, 8)
    $ gradientTransReverse = ImageDissolve("images/splash/grad_trans.png", 0.5, 8, reverse=True)
    $ spotTrans = ImageDissolve("images/splash/spots_trans.png", 1.0, 8)
    $ fastMove = MoveTransition(0.2)
    $ slowDissolve = Dissolve(1.0)
    $ fastDissolve = Dissolve(0.3)
    
    #positionen
    $ right = Position(xpos=0.8,xanchor="right")
    $ left = Position(xpos=0.2,xanchor="left")
    $ leftoffscreen = Position(xpos=0.0,xanchor="right")
    $ rightoffscren = Position(xpos=1.0,xanchor="left")
    $ leftedge = Position(xpos=0.0,xanchor="center")
    $ rightedge = Position(xpos=1.0,xanchor="center")
    $ xyCenter = Position(xalign=0.5,yalign=0.5)


    # charaktere
    $ b = DynamicCharacter("berndName", color="#dddddd")
    $ ma = DynamicCharacter("maName", color="#c8ffc8")
    $ sis = DynamicCharacter("sisName", color="#ff5555")
    $ bw = DynamicCharacter("wBerndName", color="#00dd00")
    $ yan = DynamicCharacter("yanName", color="#ff00ff")
    $ e = Character("Eich")
    $ nvlc = Character(None, kind=nvl)
        
    #Musik
    $ m_bernd = "music/bernd_theme.ogg" #Draußen, Keller
    $ m_wohnung = "music/bernd_wohnung.ogg" #Wohnung, Treppenhaus
    $ m_laura = "music/laura_theme.ogg" #Schwester
    $ m_shop = "music/shop.ogg" #Supermarkt
    $ m_anja = "music/anja_theme.ogg" #Anja und ihr Zimmer
    $ m_anjaWohnung = "music/anja_wohnung.ogg" #Anjas Wohnung, außer ihrem Zimmer
    $ m_psycho = "music/psycho.ogg" #Psychosachen
    $ m_traurig = "music/ronery.ogg" #traurige Stellen
    $ m_drama = "music/sad.ogg" #ebenfalls traurige Stellen
    $ m_date = "music/date.ogg" #Dates usw.
    $ m_schulweg = "music/schulweg.ogg" #Schulweg usw.
    $ m_donerladen = "music/donerladen.ogg"
    $ m_spannung = "music/exciting.ogg" #Spannung usw.
    $ m_rennen = "music/run_fast.ogg" #Action
    $ m_yasminStalk = "music/yasmin_stalkerbernd_theme.ogg" #Stalkerbernd-Theme
    $ m_yasmin = "music/yasmin_theme.ogg" #Yasmin
    $ m_yasminWohnung = "music/yasmin_wohnung.ogg" # Yasmins Wohnung (sie wohnt alleine...)
    $ m_traum = "music/traum.ogg" #für Bernds Animeträume und seinen vielen Waifus
    $ m_battle = "music/battle.ogg" #u. a. bisher für die Spinnenszene, weil ich noch keine bessere BGM fand,
    $ m_treffen = "music/Treffen, das niemals stattfinden sollte.ogg" #siehe Folge 1 von Sayonara Zetsubou Sensei, genau so etwas...
    $ m_cafe = "music/cafe.ogg" #falls Bernd mal mit einem Mädchen in ein Café geht
    $ m_kanashimi = "music/insert_kanashimi.ogg" #Insert-Song für Abstechszenen
    $ m_heul = "music/;_;.ogg" #;_;
    $ m_lauraende = "music/lauraende.ogg"
    $ m_rabe = "music/rabe.ogg"
    $ m_schule = "music/schule.ogg" #in der Schule
    $ m_krank = "music/krank.ogg" #kranke Laura
    $ m_liebe = "music/liebe.ogg" #LIEBE <3
    $ m_eich  = "music/pokemon_eich.mp3"
    
    #WICHTIG: Handy-Klingeltöne bitte nicht registrieren, die sind zwar in dem Ordner drin, werden aber mit dem Sound-Befehl abgerufen
    
    #namen
    $ berndName = "Bernd"
    $ sisName = "Laura"
    $ maName = "Dorothea"
    $ wBerndName = "Anja"
    $ yanName = "Yasmin"
    
    #beziehungen
    $ maLove = 20
    $ sisLove = 40
    $ friendLove = 0
    $ yanLove = 0
    
    #flags
    $ anjaRoute = 0
    $ anjaOffer = 0
    $ lauraRoute = 0
    $ yanKennen = 0 #bestimmt, ob Bernd Yasmins Namen kennt
    $ stalker_eins = 0
    
    #andere stats
    $ geld = 0
    $ supermarkt = ""
    $ mitbringen = "nichts"
    
    $ show_editor_button = False
    $ hentaiEin = False
    
    #fragebogen
    $ f_anime = 0
    $ f_figuren = 0
    $ f_lauern = 0
    
# Neues Spiel startet hier
label start:
    stop music
    jump namenGeben
            

label skipTo: #namen des labels eingeben -> springen
    
    menu:
        "Normal beginnen oder springen?"
        
        "Springen":
            $ skipToLabel = renpy.input("Name des labels?") or "namenFrage"
            if renpy.has_label(skipToLabel):
                $ renpy.music.stop()
                $ renpy.jump(skipToLabel)
            else:
                "Label nicht gefunden."
                jump skipTo
        "Normal beginnen":
            #jump namenFrage
            
            jump namenGeben #temporär

label namenFrage:
    menu:
        "Möchtest du die Charaktere der Geschichte selbst benennen?"
        
        "Ja.":
            
            jump namenGeben
            
        "Nein.":
        
            jump prolog

label namenGeben:

    #$ mouse_visible = False

    #image browserfenster = os_browserfenster(site="a")
    #image bg_image = os_BG()
    #scene bg_image
    #show ui hilfe_1 at xyCenter
    #scene bg desktop_a
    #with fade
    #scene bg desktop_b
    #with fade
    #scene bg desktop_email
    #with fade
    #scene bg desktop_email
    #with fade
    #"Cool, E-Mails!"
    #"Sogar mit Cursor."
    #show ui cursor at Position(xpos=400,ypos=60,yanchor=0.0)
    #with move
    
    #"Wusch!"
    #show ui cursor at Position(xpos=340,ypos=5,yanchor=0.0)
    #show browserfenster at Position(yalign=0.0,xalign=0.0)
    #with move
    
    #"Wow, ich kann sogar Fenster bewegen!"
    #"Naja, mal die Mails abrufen."
    #image mailfenster = os_mailbox(mailliste=[["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"]])
    #show mailfenster at Position(xpos=500,ypos=300,xanchor=0.0,yanchor=0.0)
    #with None
    
    #"Was ist das denn?"
    #hide ui cursor
    #with None
    #show ui cursor at Position(xpos=340,ypos=5,yanchor=0.0)
    #with None
    #show ui cursor at Position(xpos=600,ypos=305,xanchor=0.0,yanchor=0.0)
    #with move
    
    #"Was ist denn hier passiert?"
    #show ui cursor at Position(xpos=600,ypos=600,xanchor=0.0,yanchor=0.0)
    #with move
    
    #"Komisch."
    "HALT"
    "POKEMONZEIT"
    
    #$ mouse_visible = True
    
    scene black

    show eich normal at Position(ypos=0.5,yanchor=0.5)
    with fade
    
    play music m_eich
    
    "Mann" "Hallo, willkommen in der Welt der Pokémon!"
    "Mann" "Mein Name ist Eich und man nennt mich den Pokémonprofessor."
    e "Wie lautet dein Name?"
    $ namenListe = defaultNamenListe

    $ nameEins = choice(namenListe)
    $ namenListe.remove(nameEins)
    $ nameZwei = choice(namenListe)

    menu:
        #"Wie ist dein Name?"
        
        "Bernd":
            $ berndName = "Bernd"
        "%(nameEins)s":
            $ berndName = nameEins
        "%(nameZwei)s":
            $ berndName = nameZwei
        "Anderer...":
            $ berndName = renpy.input("Wie ist dein Name?") or "Bernd"
            
    #$ berndName = renpy.input("Wie ist dein Name?") or "Bernd"
    #bild von mutter
    #$ maName = renpy.input("Wie heisst deine Mutter?") or "Dorothea"
    #show laura neutral
    #with dissolve
    #$ sisName = renpy.input("...und deine Schwester?") or "Laura"
    #hide laura neutral
    #with dissolve
    #show anja neutral
    #with dissolve
    #$ wBerndName = renpy.input("Zuletzt noch dieses Mädchen hier.") or "Anja"
    #hide anja neutral
    #with dissolve
    #show yasmin neutral
    #with dissolve
    #$ yanName = renpy.input("Oh, ich habe dieses Mädchen hier noch vergessen.") or "Yasmin"
    #hide yasmin neutral
    #with dissolve
    
    #"OK, das war schon alles."
    
    e "Richtig, %(berndName)s. Es lag mir auf der Zunge."
    e "Nun, %(berndName)s, ich würde gern einiges über dich wissen, bevor dein Abenteuer beginnt."
    e "Bist du bereit, mir ein paar Fragen zu beantworten?"
    e "Wenn nicht, hast du Pech gehabt, denn du musst."
    e "Kommen wir also zu Frage 1."
    menu:
        e "Schaust du Anime, und wenn ja, wieviele hast du bisher vollständig gesehen?"
        "Keine.":
            $ f_anime = 0
        "Unter 10.":
            $ f_anime = 1
        "10-20":
            $ f_anime = 2
        "20-50":
            $ f_anime = 3
        "Über 50":
            $ f_anime = 4
    e "Hm... interessant."
    e "Kommen wir zu Frage 2."
    if f_anime > 0:
        menu:
            e "Besitzt du Animefiguren, und wenn ja, wieviele?"
            "Keine.":
                $ f_figuren = 0
            "Eine.":
                $ f_figuren = 1
            "2-5.":
                $ f_figuren = 2
            "6-10":
                $ f_figuren = 3
            "11-20":
                $ f_figuren = 4
            "Mehr als 20.":
                $ f_figuren = 5
        e "In Ordnung."
        e "Nächste Frage."
    menu:
        e "Wie lange lauerst du pro Tag auf Krautchan?"
        "< 1 Stunde":
            $ f_lauern = 0
        "1-2 Stunden":
            $ f_lauern = 1
        "2-4 Stunden":
            $ f_lauern = 2
        "4-8 Stunden":
            $ f_lauern = 3
        "8-16 Stunden":
            $ f_lauern = 4
        "24 Stunden":
            $ f_lauern = 5
    
    e "Gut, weiter im Text..."
    menu:
        e "Bist du noch Jungfrau?"
        "Ja.":
            pass
        "Oui.":
            pass
        "Si.":
            pass
        "{=jpmenu}はい。{/=jpmenu}":
            pass
        "{=jpmenu}是.{/=jpmenu}":
            pass    
    e "Ja, das dachte ich mir schon."
    e "Also weiter."
    e "Keine Angst, es dauert nicht mehr lange."
    e "Eigentlich möchte ich nur noch eins von dir wissen."
    e "%(berndName)s."
    e "Ich habe hier drei Pokémon, und du darfst dir eines von ihnen aussuchen."
    e "Nun, welches soll es sein?"
    python:
        ui.vbox(xfill=True,yfill=True,xalign=0.5)
        ui.hbox(xalign=0.5,yalign=0.5)
        ui.imagebutton("images/eich/bisa.png", "images/eich/bisa_g.png", xpadding=10, clicked=ui.returns("Bisasam"))
        ui.imagebutton("images/eich/glumanda.png", "images/eich/glumanda_g.png", xpadding=10, clicked=ui.returns("Glumanda"))
        ui.imagebutton("images/eich/schiggy.png", "images/eich/schiggy_g.png", xpadding=10, clicked=ui.returns("Schiggy"))
        ui.close()
        ui.close()
        f_poke = ui.interact()
    e "%(f_poke)s, eine gute Wahl!"
    e "Nun, %(berndName)s..."
    e "...dein Abenteuer in der Welt der Pokémon erwartet dich!"
    $ berndNameCaps = berndName.upper()
    scene black
    with fade
    $ renpy.pause(2.0)
    jump prolog

label ende: 
    scene splash owari
    $ renpy.pause(2.0)
    scene splash ende
    with slowDissolve
    $ renpy.pause()
