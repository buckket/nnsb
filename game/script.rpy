# Script

init python:
    import os
    import random
    
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)
    style.jp = Style(style.say_thought)
    style.jp.font = "mikachan.ttf"
    style.jp.italic = False
    
    style.slow = Style(style.say_thought)
    style.slow.slow_cps = 30
    
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
            
            
    namenListe = ["Bernd","Name","Rot","Blau","Marc-Oliver","Kim","Kevin"] #hier brauchen wir mehr


#-----------------------------------------------------------------------    
    #Musikraum:    
    def set_playing_(track):
        store.playing = track
        return True

    set_playing = renpy.curry(set_playing_)

    # Call this with a button name and a track to define a music
    # button.
    def music_button(name, track):
    
        if store.playing == track:
            role = "selected_"
        else:
            role = ""
    
 #       if not renpy.seen_audio(track):
  #          name = "???"
   #         clicked = set_playing(track)
    #    else:
     #       clicked = set_playing(track)

        clicked = set_playing(track)

        ui.textbutton(
            name,
            clicked=clicked,
            role=role,
            size_group="music")

label music_room:

    scene black

    python:
        _game_menu_screen = None

        # The default track of music.
        playing = None

label music_room_loop:

    # Play the playing music, if it changed.
    python:
        renpy.music.play(playing, if_changed=True, fadeout=1)

        # Display the various music buttons.
        ui.vbox(xalign=0.5, ypos=100)
        music_button("Titelbildschirm", "music/main_menu_theme.mp3")
        music_button("Arrein, arrein...", "music/ronery.mp3")
        music_button("Anjas Thema", "music/anja_theme.mp3")     
        music_button("eines Mädchens Wohnung", "music/anja_wohnung.mp3")
        music_button("Ich wähle dich, Schuh!", "music/battle.mp3")
        music_button("Jamba", "music/bernd_handy.mp3")
        music_button("Thema eines Helden", "music/bernd_theme.mp3")      
        music_button("Pause muss auch mal sein", "music/bernd_wohnung.mp3")
        music_button("<3", "music/date.mp3")   
        music_button("Salih-Time", "music/donerladen.ogg")
        music_button("Wie kam ich auf Namen für die Musikstücke?", "music/exciting.mp3")
        music_button("Das ist sowieso das einzige Lied, das gehört werden wird", "music/laura_theme.ogg")
        music_button("Ich sterbe fast vor Anspannung...fast", "music/psycho.mp3")
        music_button("Er kommt!", "music/rugenwalder.ogg")
        music_button("Renn schneller", "music/run_fast.mp3")
        music_button(";_;", "music/sad.mp3")
        music_button("Wie kam ich zur Schule?", "music/schulweg.mp3")
        music_button("Kaufe das Hyrule-Schild, stelle fest, dass man es kurz danach umsonst bekommt", "music/shop.mp3")
        music_button("Träume sind sooo toll", "music/traum.mp3")
        music_button("Hier fiel mir überhaupt kein Name ein", "music/Treffen, das niemals stattfinden sollte.mp3")
        music_button("Stalk, stalk...", "music/yasmin_stalkerbernd_theme.mp3")
        music_button("[drei Punkte in diesem Feld]", "music/yasmin_theme.mp3")
        music_button("...Wohnung", "music/yasmin_wohnung.mp3")
        ui.close()

        # This is how we return to the main menu.
        ui.textbutton(
            "Return",
            clicked=ui.returns(False),
            xalign=1.5,
            ypos=0,
            size_group="music")

    if ui.interact():
        jump music_room_loop
    else:
        return

    
#---------------------------------
    




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
    $ fastDissolve = Dissolve(0.3)
    
    #positionen
    $ right = Position(xpos=0.8,xanchor="right")
    $ left = Position(xpos=0.2,xanchor="left")
    $ leftoffscreen = Position(xpos=0.0,xanchor="right")
    $ rightoffscren = Position(xpos=1.0,xanchor="left")
    $ leftedge = Position(xpos=0.0,xanchor="center")
    $ rightedge = Position(xpos=1.0,xanchor="center")


    # charaktere
    $ b = DynamicCharacter("berndName", color="#dddddd")
    $ ma = DynamicCharacter("maName", color="#c8ffc8")
    $ sis = DynamicCharacter("sisName", color="#ff5555")
    $ bw = DynamicCharacter("wBerndName", color="#00dd00")
    $ yan = DynamicCharacter("yanName", color="#ff00ff")
        
    #Musik
    $ m_bernd = "music/bernd_theme.ogg" #Draußen, Keller
    $ m_wohnung = "music/bernd_wohnung.mp3" #Wohnung, Treppenhaus
    $ m_handyb = "music/bernd_handy.mp3" #Bernds Klingelton
    $ m_laura = "music/laura_theme.ogg" #Schwester
    $ m_shop = "music/shop.mp3" #Supermarkt
    $ m_anja = "music/anja_theme.mp3" #Anja und ihr Zimmer
    $ m_anjaWohnung = "music/anja_wohnung.mp3" #Anjas Wohnung, außer ihrem Zimmer
    $ m_pyscho = "music/psycho.mp3" #Psychosachen
    $ m_traurig = "music/ronery.mp3" #traurige Stellen
    $ m_drama = "music/sad.mp3" #ebenfalls traurige Stellen
    $ m_date = "music/date.mp3" #Dates usw.
    $ m_schulweg = "music/schulweg.mp3" #Schulweg usw.
    $ m_donerladen = "music/donerladen.ogg"
    $ m_spannung = "music/exciting.mp3" #Spannung usw.
    $ m_rennen = "music/run_fast.mp3" #Action
    $ m_yasminStalk = "music/yasmin_stalkerbernd.mp3" #Stalkerbernd-Theme
    $ m_yasmin = "music/yasmin_theme.mp3" #Yasmin
    $ m_yasminWohnung = "music/yasmin_wohnung.mp3" # Yasmins Wohnung (sie wohnt alleine...)
    $ m_traum = "music/traum.mp3" #für Bernds Animeträume und seinen vielen Waifus
    $ m_battle = "music/battle.mp3" #u. a. bisher für die Spinnenszene, weil ich noch keine bessere BGM fand,
    $ m_treffen = "music/Treffen, das niemals stattfinden sollte.mp3" #siehe Folge 1 von Sayonara Zetsubou Sensei, genau so etwas...
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
    $ yanKennen = 0 #bestimmt, ob Bernd Yasmins Namen kennt
    
    #andere stats
    $ geld = 0
    $ supermarkt = ""
    $ mitbringen = "nichts"
    
    $ show_editor_button = True
    $ hentaiEin = False
    
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

    $ nameEins = random.choice(namenListe)
    $ nameZwei = random.choice(namenListe)

    menu:
        "Wie ist dein Name?"
        
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
    "Viel Spaß, %(berndName)s!"
    
    jump prolog


label ende: 
    scene splash owari
    $ renpy.pause(2.0)
    scene splash ende
    with slowDissolve
    $ renpy.pause()