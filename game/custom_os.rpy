init python:

    #alle diese funktionen geben displayables zurück, die durch die parameter generiert werden
    #beispiel zur benutzung:
    #image mailfenster = os_mailread("Mail", "Hallo", "Bernd", "Bernd", "Hallo, Bernd!\nDu versagst.")
    #show mailfenster

    #diese funktion gibt ein displayable zurück mit dem aktuellen desktopbg
    def os_BG():
        return im.Image(bgfilename) #bgfilename vorher definieren
        
    def os_mailread(titel="KC Mail",betreff="kein Betreff",absender="kein Absender",empfaenger="kein Empfänger",text="Leere E-Mail"):
        background = im.Image("images/ui/os/mailfenster.png") #bild laden
        text_titel = Text(titel,size=8,color="#000") #titeltext erzeugen
        text_infoFeld = Text("Betreff: "+betreff+"\nvon: "+absender+"\nan: "+empfaenger,size=9,color="#000") #infotext erzeugen
        text_mailText = Text(text,size=10,color="#000") #mailinhalt erzeugen
        
        
        
        resultList = [(520,394),(0,0),background,(17,4),text_titel,(23,24),text_infoFeld,(23,67),text_mailText]
        
        resultDisp = apply(LiveComposite,resultList)
        
        return resultDisp

    def os_mailbox(titel="KC Mail",postfach="unbekannt",mails="0",ungelesen="0",mailliste=list()):
        #mailliste ist eine liste aus listen mit je vier dingensen
        #[betreff,von,uhrzeit,gelesen]
        background = im.Image("images/ui/os/mailfenster.png") #bild laden
        text_titel = Text(titel,size=8,color="#000") #titeltext erzeugen
        text_infoFeld = Text("Postfach von: "+postfach+"\nE-Mails: "+mails+"\ndavon ungelesen: "+ungelesen,size=9,color="#000") #infotext erzeugen
        #text_mailText = Text(text,size=10,color="#000") #mailinhalt erzeugen
        
        resultList = [(520,394),(0,0),background,(17,4),text_titel,(23,24),text_infoFeld]
        
        mailDispList = [(484,305)]
        
        print len(mailliste)
        
        for i in range(len(mailliste)):
            for j in range(len(mailliste[i])):
                if j == 0:
                    xval = 0
                elif j == 1:
                    xval = 250
                else:
                    xval = 400
                mailDispList += [(xval,i*14),Text(mailliste[i][j],size=9,color="#000")]
        
        mailDisp = apply(LiveComposite,mailDispList)
        
        resultList += [(23,65),mailDisp]
        
        resultDisp = apply(LiveComposite,resultList)
        
        return resultDisp
        
    def os_browserfenster(titel="KC Web - Krautchan.net",url="http://www.krautchan.net/",site=None):
        background = im.Image("images/ui/os/browserfenster.png") #bild laden
        text_titel = Text(titel,size=8,color="#000")
        text_url = Text(url,size=8,color="#000")
        if site is None:
            site_image = Solid((0,0,0,0))
        else:
            site_image = im.Image("images/ui/os/browser_"+site+".png")

        resultList = [(925,664),(0,0),background,(17,4),text_titel,(171,27),text_url,(22,68),site_image]
         
        resultDisp = apply(LiveComposite,resultList)
         
        return resultDisp