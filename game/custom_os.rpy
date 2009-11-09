init python:

    #alle diese funktionen geben displayables zurück, die durch die parameter generiert werden
    #beispiel zur benutzung:
    #image mailfenster = os_mailread("Mail", "Hallo", "Bernd", "Bernd", "Hallo, Bernd!\nDu versagst.")
    #show mailfenster

    #diese funktion gibt ein displayable zurück mit dem aktuellen desktopbg
    def os_BG():
        return im.Image(bgfilename) #bgfilename vorher definieren
        
    def os_mailread(titel="",betreff="",absender="",empfaenger="",text=""):
        background = im.Image("images/ui/os/mailfenster.png") #bild laden
        text_titel = Text(titel,size=8,color="#000") #titeltext erzeugen
        text_infoFeld = Text("Betreff: "+betreff+"\nvon: "+absender+"\nan: "+empfaenger,size=9,color="#000") #infotext erzeugen
        text_mailText = Text(text,size=10,color="#000") #mailinhalt erzeugen
        
        resultDisp = LiveComposite((520,394), #größe des mailbgs
                                   (0  ,0  ),background, #bg anzeigen
                                   (17 ,4  ),text_titel, #titeltext
                                   (23, 24 ),text_infoFeld, #infotext
                                   (23, 67 ),text_mailText) #mailinhalt
        
        return resultDisp