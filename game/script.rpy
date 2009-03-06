# Netto no Shishou: Bernd
# Script

init python:
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

init:

    #Wichtige Storyflags:
    #anjaTreffen - Mit Anja getroffen? (1.1)
    #lauraRoute - Laura Abgeholt? (1.1)
    #stalker - mit oder ohne stalker (1.1)
    #anjaAccept - Anja angenommen? (1.1)

    #styles
    #style.say_window.background = "#f00"
    
    # hintergründe
    #global
    image black = Solid((0,0,0,255))
    image white = Solid((255,255,255,255))
    image owari = "images/owari.png"
    image ende = "images/ende.png"
    $ fastFade = Fade(.2, 0, .2, color="#000")
    $ flash = Fade(.1, 0, .3, color="#fff")
    $ slowFlash = Fade(.1, 0, .5, color="#fff")
    $ damnSlowFlash = Fade(.2, 0, 1, color="#fff")
    $ slowFade = Fade(.8, 1, 0, color ="#000")
    $ cloudtrans = ImageDissolve("images/bg/cloud_trans.png", 1.0, 12, reverse=True)
    $ cloudtransSlow = ImageDissolve("images/bg/cloud_trans.png", 2.0, 12)
    $ noisetrans = ImageDissolve("images/bg/noise_trans.png", 1.0, 8, reverse=True)
    $ wooshTrans = ImageDissolve("images/bg/woosh_trans.png", 0.5, 8)
    $ wooshTransReverse = ImageDissolve("images/bg/woosh_trans.png", 0.5, 8, reverse=True)
    $ gradientTrans = ImageDissolve("images/bg/grad_trans.png", 0.5, 8)
    $ gradientTransReverse = ImageDissolve("images/bg/grad_trans.png", 0.5, 8, reverse=True)
    $ spotTrans = ImageDissolve("images/bg/spots_trans.png", 1.0, 8)
    $ fastMove = MoveTransition(0.2)
    $ slowDissolve = Dissolve(1.0)
    #prolog
    image splash prolog = "images/bg/splash_prolog.png"
    image bg zuhause_draussen = "images/bg/strasse.jpg"
    image bg zuhause_hausflur = "images/bg/hausflur.jpg"
    image bg zuhause_drinnen = "images/bg/wohnung_innen.jpg"
    image bg badezimmer = "images/bg/badezimmer.jpg"
    image bg keller = "images/bg/berndszimmer_os.jpg"
    image bg keller_kc = "images/bg/berndszimmer.jpg"
    image bg keller_blur = "images/bg/berndszimmer_blur.jpg"
    image bg supermarkt_innen = "images/bg/supermarkt.jpg"
    image bg aldi = "images/bg/aldi.jpg"
    image bg lidl = "images/bg/lidl.jpg"
    image bg kueche = "images/bg/kueche.jpg"
    image bg kellertreppe = "images/bg/kellertreppe.jpg"
    image bg kellertreppe_blur = "images/bg/kellertreppe_blur.jpg"
    
    #kapitel 1
    image splash eins_open = "images/bg/splash_eins.png"
    image bg keller_aus = "images/bg/berndszimmer_aus.jpg"
    image bg keller_bluescreen = "images/bg/berndszimmer_blau.jpg"
    image bg alexanderplatz_eins = "images/bg/alexanderplatz_1.jpg"
    image bg alexanderplatz_zwei = "images/bg/alexanderplatz_2.jpg"
    image bg alexanderplatz_drei = "images/bg/alexanderplatz_3.jpg"
    image bg gasse1 = "images/bg/gasse1.png"
    image bg gasse2 = "images/bg/gasse2.png"
    image bg schulweg1 = "images/bg/schulweg1.jpg"
    image bg schulweg2 = "images/bg/schulweg2.jpg"
    image bg schulwegPano = "images/bg/schulweg_pano.jpg"
    image bg schulhof = "images/bg/schulhof.jpg"
    image bg eiswagen = "images/bg/eiswagen.jpg"
    image bg donerladen = "images/bg/donerladen.jpg"
    image bg desktop_none = "images/bg/desktop_none.png"
    image bg desktop_email = "images/bg/desktop_mail.jpg"
    image bg desktop_hilfe = "images/bg/desktop_hilfe.jpg"
    image bg desktop_a = "images/bg/desktop_a.jpg"
    image bg desktop_b = "images/bg/desktop_b.jpg"
    
    #kapitel 2
    image gameover_vierkanal = "images/bg/gameover_vierkanal.jpg"
    image bg lieferwagen = "images/bg/lieferwagen.jpg"
    image bg lauraszimmer = "images/bg/lauras_zimmer.jpg"
    
    #charakter bilder
    #prolog
    image sis neutral = "images/char/schwester_neutral.png"
    image sis happy = "images/char/schwester_happy.png"
    image sis surprised = "images/char/schwester_surprised.png"
    image sis embarrassed = "images/char/schwester_emb.png"
    image sis emb_surprised = "images/char/schwester_surprised_drop.png"
    image sis crying = "images/char/schwester_crying.png"
    image sis sad = "images/char/schwester_sad.png"
    image sis sadsmile = "images/char/schwester_sad_smile.png"
    image sis angry = "images/char/schwester_mad.png"
    image sis angry_talk = "images/char/schwester_mad_talk.png"
    image sis pissed = "images/char/schwester_pissed.png"
    
    image blond neutral_g = "images/char/blondBernd_glasses.png"
    image blond surprised = "images/char/blondBernd_surprised.png"
    image blond surprised_g = "images/char/blondBernd_surprised_glasses.png"
    image blond weird = "images/char/blondBernd_weird.png"
    image blond neutral = "images/char/blondBernd.png"
    image blond shy = "images/char/blondBernd_shy_glasses.png"
    
    image yasmin stalker = "images/char/stalker_bernd.png"

    image salih = "images/char/salih.png"

    # charaktere
    $ b = DynamicCharacter("berndName", color="#dddddd")
    $ ma = DynamicCharacter("maName", color="#c8ffc8")
    $ sis = DynamicCharacter("sisName", color="#ff5555")
    $ bw = DynamicCharacter("wBerndName", color="#00dd00")
    
    #musik
    #draussen, keller = 1.ogg
    #wohnung = 2.mp3
    #schwester = schwester.ogg
    #supermarkt = 3.mp3
    
    #sounds
    #tür = door_1.wav
    #schlag = hit_1.wav
    
    #namen
    $ berndName = "Bernd"
    $ sisName = "Laura"
    $ maName = "Dorothea"
    $ wBerndName = "Anja"
    
    #beziehungen
    $ maLove = 20
    $ sisLove = 40
    $ friendLove = 0
    
    #flags
    $ anjaRoute = 0
    $ anjaOffer = 0
    $ lauraRoute = 0
    
    #andere stats
    $ geld = 0
    $ supermarkt = ""
    $ mitbringen = "nichts"
    
    $ show_editor_button = False

# Neues Spiel startet hier
label start:
    #menu:
    #    "Springe zu Kapitel..."
    #    
    #    "Prolog":
    #        jump namenFrage
    #        
    #    "Eins":
    #        jump eins
            


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
    show sis neutral
    with dissolve
    $ sisName = renpy.input("...und deine Schwester?") or "Laura"
    hide sis neutral
    with dissolve
    show blond neutral_g
    with dissolve
    $ wBerndName = renpy.input("Zuletzt noch dieses Mädchen hier.") or "Anja"
    hide blond neutral_g
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