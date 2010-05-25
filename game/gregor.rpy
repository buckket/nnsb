#Bernd macht einen Waldspaziergang, unten stehendes Event kann man nach Belieben einbauen.
#Da Bernd schon im Wald ist, fällt das scene bg wald unten weg.
#Es stehen mit Stand vom 15.04.10 trotzdem 4 Waldweg-Bilder zur Auswahl, von denen man sich eines aussuchen kann, man muss nur den Filter drüberlegen und ggf. Größe des Bildes anpassen.

label gregor:
    
    "Von weitem höre ich eine Stimme."
    
    play music m_gregor fadein 0.3
    
    "Stimme" "Platz da! Jetzt komm ich! Macht den Weg zum Tor frei!"
    "?"
    "Stimme" "Haha."
    "Sie kommt näher."
    "Stimme" "Yeah. Haha."
      
    play sound "sounds/fussballschuss.wav"
    #Sound existiert noch nicht
    #GSB
    
    "Stimme" "FLANKE!"
    "Stimme" "Oh."
    
    play sound "sounds/batz.wav"
    #Sound existiert noch nicht
    #GSB
    
    "Aus Reflex zucke ich zusammen."
    "Als ich meine Augen wieder öffne, sehe ich einen kleinen, schwarzhaarigen Knirps in einem blauen Fußballtrikot vor mir stehen."
    
    $ renpy.pause(1)
    
    "Stimme" "Ha."
    "Stimme" "Verzeih. {w}Ist dir was passiert?"
    "Ja, mir lief ein kleiner Knirps über den Weg, der fremde Leute mit Fußbällen abschießt."
    "Stimme" "Mein Name ist Gregor, ich bin neu hier."
    "Aha... {w}und wieso sollte mich das nun interessieren?"
    "Gregor" "Gibst du mir den Ball wieder, ich muss zur Schule."
    
    menu:
        "Ball wiedergeben?"
        
        "Ja.":
            "Ich nicke."
            b "Hier."
            "Gregor" "Danke. Na... {w}dann mach's gut."
            "Er rennt mit dem Ball am Fuß wieder weiter."
        
        "Nein.":
            b "Nein."
            "Gregor" "Ach, komm schon."
            b "Mach doch, was du willst."
            "Ich laufe weiter und lasse den Knirps hinter mir."
            
        "Ball wegschießen.":
            b "Aber klar doch."
            "Ich werde ihn mit aller Kraft wegschießen."
            "Ich hebe mein rechtes Bein nach hinten, um mit voller Kraft zu schießen."
            b "HIER hast du-{nw}"
            "Doch..."
            
            scene bg wald
            with vpunch
            
            "...ich treffe den Ball nicht."
            "Ich bin ausgerutscht."
            $ idiotenpunkt += 1
            
            "Gregor" "Bist du ok?"
            b "Ja ja."
            "Mürrisch laufe ich einfach an ihm vorbei und lasse den Knirps hinter mir."