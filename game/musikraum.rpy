init python:

    style.musicButton = Style(style.button)
    style.musicButton.background=Solid((0,0,0,0))
    style.musicButton.hover_background=Solid((223,223,233,255))
    style.musicButton.xfill=True
    
    style.musicButtonPlaying = Style(style.musicButton)
    style.musicButtonPlaying.background=Solid((223,223,223,255))
    
    style.musicButtonText = Style(style.default)
    style.musicButtonText.size = 9
    style.musicButtonText.color = (0,0,0,255)
    
    style.playingName = Style(style.default)
    style.playingName.size = 15
    style.playingName.color = (0,0,0,255)
        
    class mtrack:
        def __init__(self,title,file):
            self.title = title
            self.filepath = file
        
    class mtracklist:
        def __init__(self):
            self.tracks = []
            self.playing = 0
            
        def addTrack(self,title,file):
            self.tracks.append(mtrack(title,file))
            
        def getTrack(self,id):
            return self.tracks[id]
            
        def getSize(self):
            return len(self.tracks)-1
        
        def printList(self):
            for id in range(0,len(self.tracks)):
                track = self.getTrack(id)
                if id == self.playing:
                    bStyle = "musicButtonPlaying"
                else:
                    bStyle = "musicButton"
                ui.textbutton(track.title,clicked=set_playing(id),style=bStyle,text_style="musicButtonText")
                ui.sizer(maxheight=1)
                ui.image(Solid((0,0,0,255)),xfill=True,yfill=False)
            
    tracks = mtracklist()
    
    tracks.addTrack("GO, GO, TITELBILDSCHIRM! MIGHTY MORPHIN TITELBILDSCHIRM!", "music/main_menu_theme.ogg")
    tracks.addTrack("So arreine...", "music/ronery.ogg")
    tracks.addTrack("Anjas Thema", "music/anja_theme.ogg")     
    tracks.addTrack("eines Mädchens Wohnung", "music/anja_wohnung.ogg")
    tracks.addTrack("Ich wähle dich, Schuh!", "music/battle.ogg")
    tracks.addTrack("Jamba", "music/bernd_handy.ogg")
    tracks.addTrack("Im Keller...", "music/bernd_theme.ogg")      
    tracks.addTrack("Pause muss auch mal sein", "music/bernd_wohnung.ogg")
    tracks.addTrack("<3", "music/date.ogg")   
    tracks.addTrack("Salih-Time", "music/donerladen.ogg")
    tracks.addTrack("Ich sterbe fast vor Anspannung...fast", "music/exciting.ogg")
    tracks.addTrack("Das ist sowieso das einzige Lied, das gehört werden wird...", "music/laura_theme.ogg")
    tracks.addTrack("Nein, nicht das Messer, NICHT DAS MESSER!!", "music/psycho.ogg")
    tracks.addTrack("Er kommt!", "music/rugenwalder.ogg")
    tracks.addTrack("Renn schneller", "music/run_fast.ogg")
    tracks.addTrack("Warum ist dieses Lied eigentlich noch dabei?", "music/sad.ogg")
    tracks.addTrack("Wie kam ich zur Schule?", "music/schulweg.ogg")
    tracks.addTrack("Schon wieder Jamba", "music/anja_handy.ogg")
    tracks.addTrack("Kaufe das Hyrule-Schild, stelle fest, dass man es kurz danach umsonst bekommt", "music/shop.ogg")
    tracks.addTrack("Träume sind sooo toll", "music/traum.ogg")
    tracks.addTrack("Ein \"Mann\", der alles negativ sieht...ein \"Mädchen\", das alles positiv sieht...", "music/Treffen, das niemals stattfinden sollte.ogg")
    tracks.addTrack("Stalk, stalk [drei Punkte am Ende der Zeile]", "music/yasmin_stalkerbernd_theme.ogg")
    tracks.addTrack("[drei Punkte in diesem Feld]", "music/yasmin_theme.ogg")
    tracks.addTrack("[drei Punkte am Anfang der Zeile] Wohnung", "music/yasmin_wohnung.ogg") 
    tracks.addTrack(";_;", "music/;_;.ogg")
    
    def set_playing_(track):
        if track < 0:
            track = 0
        if track > tracks.getSize():
            track = tracks.getSize()
        store.playing = track
        tracks.playing = track
        return True
 
    set_playing = renpy.curry(set_playing_)


label music_room:

    scene ui musikspieler

    python:
        _game_menu_screen = None

        playing = 0
        musicOn = 1

label music_room_loop:

    python:
        
        if musicOn == 1:
            renpy.music.play(tracks.getTrack(playing).filepath, if_changed=True, fadeout=1)
        else:
            renpy.music.stop()

        p = "images/ui/musik_"
        
        ui.hbox(xpos=78,ypos=86)
        ui.imagebutton(p+"hinten.png", p+"hinten_h.png", clicked=set_playing(playing-1), right_margin=7)
        ui.imagebutton(p+"stop.png", p+"stop_h.png", clicked=ui.returns(False), right_margin=7)
        if musicOn == 1:
            ui.imagebutton(p+"pause.png", p+"pause_h.png", clicked=ui.returns("play"), right_margin=7)
        else:
            ui.imagebutton(p+"start.png", p+"start_h.png", clicked=ui.returns("play"), right_margin=7)
        ui.imagebutton(p+"vorne.png", p+"vorne_h.png", clicked=set_playing(playing+1), right_margin=25)
        
        
        tit = ui.viewport(ypos=4,ymaximum=20,clipping=True,xmaximum=740)
        ui.text(tracks.getTrack(playing).title,style="playingName")
        
        ui.close()
        
        vp = ui.viewport(child_size=(870,576),xpos=72,ypos=125,xmaximum=870,ymaximum=576)
        ui.vbox(ypos=10)
        tracks.printList()
        ui.close()
        ui.bar(adjustment=vp.yadjustment, style="vscrollbar",ymaximum=576,xpos=945,ypos=125)
        
        result = ui.interact()

    if result:
        if result == "play":
            $ musicOn = -musicOn
            
        jump music_room_loop
    else:
        return
    