# Script

init python:
    import os
    
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)
    style.jp = Style(style.say_thought)
    style.jp.font = "mikachan.ttf"
    style.jp.italic = False
    
    config.log = "debuglog.txt"
    
    
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
        persistent.wieherbuhSprache = 2
    
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
            
    config.preferences['prefs_left'].append(
        _Preference(
            "Japanisch",
            "wieherbuhSprache",
            [ ("Aus", 0, "True"),
              ("Romaji", 1, "True"),
              ("Kanji", 2, "True") ],
            base=persistent))

init:
    #Wichtige Storyflags:
    #anjaTreffen - Mit Anja getroffen? (1.1)
    #lauraRoute - Laura Abgeholt? (1.1)
    #stalker - mit oder ohne stalker (1.1)
    #anjaAccept - Anja angenommen? (1.1)

    #styles
    #style.say_window.background = "#f00"
    
    $ loadImagesFromAllDirs()
    
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

    # charaktere
    $ b = DynamicCharacter("berndName", color="#dddddd")
    $ ma = DynamicCharacter("maName", color="#c8ffc8")
    $ sis = DynamicCharacter("sisName", color="#ff5555")
    $ bw = DynamicCharacter("wBerndName", color="#00dd00")
    $ yan = DynamicCharacter("yanName", color="#ff00ff")
        
    #Musik
    $ m_bernd = "music/bernd_theme.ogg" #Draußen, Keller
    $ m_wohnung = "music/bernd_wohnung.mp3" #Wohnung, Treppenhaus
    $ m_laura = "music/laura_theme.ogg" #Schwester
    $ m_shop = "music/shop.mp3" #Supermarkt
    $ m_anja = "music/anja_theme.mp3" #Anja und ihr Zimmer
    $ m_anjaWohnung = "music/anja_wohnung.mp3" #Anjas Wohnung, außer ihrem Zimmer
    $ m_pyscho = "music/psycho.mp3" #Psychosachen
    $ m_traurig = "music/sad_ronery.mp3" #traurige stellen
    $ m_date = "music/date.mp3" #Dates usw.
    $ m_spannung = "music/exciting.mp3" #Spannung usw.
    $ m_rennen = "music/run_fast.mp3" #wegrennen, hinterherrennen, usw.
    $ m_yasminStalk = "music/yasmin_stalkerbernd.mp3" #Stalkerbernd-Theme
    $ m_yasmin = "music/yasmin_theme.mp3" #Yasmin
    #Irgendwie fehlt aber noch das passende Lied für die Laura-Spinnen-Szene
    
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
    
    #andere stats
    $ geld = 0
    $ supermarkt = ""
    $ mitbringen = "nichts"
    
    $ show_editor_button = True

# Neues Spiel startet hier
label start:
    #jump namenFrage
            

label skipTo: #namen des labels eingeben -> springen
    
    menu:
        "Normal beginnen oder springen?"
        
        "Springen":
            $ skipToLabel = renpy.input("Name des labels?") or "namenFrage"
            if renpy.has_label(skipToLabel):
                $ renpy.jump(skipToLabel)
            else:
                "Label nicht gefunden."
                jump skipTo
        "Normal beginnen":
            jump namenFrage

label namenFrage:
    menu:
        "Möchtest du die Charaktere der Geschichte selbst benennen?"
        
        "Ja.":
            
            jump namenGeben
            
        "Nein.":
        
            jump prolog

label namenGeben:
    $ berndName = renpy.input("Wie ist dein Name?") or "Bernd"
    #bild von mutter
    $ maName = renpy.input("Wie heisst deine Mutter?") or "Dorothea"
    show laura neutral
    with dissolve
    $ sisName = renpy.input("...und deine Schwester?") or "Laura"
    hide laura neutral
    with dissolve
    show anja neutral
    with dissolve
    $ wBerndName = renpy.input("Zuletzt noch dieses Mädchen hier.") or "Anja"
    hide anja neutral
    with dissolve
    show yasmin neutral
    with dissolve
    $ yanName = renpy.input("Oh, ich habe dieses Mädchen hier noch vergessen.") or "Yasmin"
    hide yasmin neutral
    with dissolve
    
    "OK, das war schon alles."
    "Viel Spaß, %(berndName)s!"
    
    jump prolog


label ende: 
    scene owari
    $ renpy.pause(2.0)
    scene ende
    with slowDissolve
    $ renpy.pause()