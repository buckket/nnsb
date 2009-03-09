init:
    #bilder, die noch gebraucht werden
    #  yasmin ohne kapuze, aber mit mantel
    #  yasmin schüchtern mit mantel
    #  yasmin fragezeichenmädchen mit mantel
    #  yasmin weinend mit mantel
    pass


label yasmin_anfang:
    "Stalkerbernd" "Stalkerbernd?"
    "!"
    "Es hat gesprochen."
    "Stalkerbernd" "Wer soll das sein?"
    "Diese Stimme...?"
    "Ich lasse seine Arme los, und setze mich aufs Bett."
    "Ich bin verwirrt."
    "Seine Stimmte klingt wie..."
    b "...du bist ein Mädchen?"
    #hier nimmt yasmin die kapuze runter und man sieht das gesicht
    #sie schaut schüchtern zur seite
    "Wow."
    "Ich habe mit allem gerechnet, aber damit nicht."
    b "...aber."
    b "Ich dachte doch..."
    b "Du..."
    "Mädchen" "Was?"
    "Mädchen" "Wirst du jetzt die Polizei rufen?"
    "Mädchen" "Ich bin ein Stalker, du hast ja Recht."
    "Mädchen" "Also."
    "Mädchen" "Ruf sie schon an, ich habe es verdient."
    "Ich kann ihr irgendwie nicht folgen..."
    b "Du bist kein Bernd?"
    "Mädchen" "Bernd?" #hier bitte verwirrt gucken, fragezeichenmädchen-style
    "Habe ich mich geirrt?"
    "Ist sie wirklich kein Bernd?"
    "Aber warum sollte mich sonst jemand stalken?"
    b "Verarsch mich nicht!"
    b "Warum solltest du mich sonst stalken?!"
    #wieder schüchtern
    "Mädchen" "..."
    b "..."
    "Vielleicht ist sie wirklich kein Bernd?"
    "...aber ist das nicht egal?"
    "Sie ist bei mir eingebrochen."
    "Mehrmals."
    menu:
        "Ich sollte die Polizei rufen!":
            jump yasmin_polizei
        "Ich werde sie erst befragen.":
            "Vielleicht hatte sie ja einen guten Grund."
    b "Warum bist du bei mir eingebrochen?"
    "Mädchen" "..."
    b "Warum hast du mich verfolgt?"
    "Mädchen" "..."
    b "Wer bist du?"
    "Mädchen" "..."
    b "Was willst du von mir?"
    $ yanNameKurz = stringShorten(yanName,2)
    "Mädchen" "%(yanNameKurz)s- %(yanName)s."
    b "Wa- wie bitte?"
    "%(yanName)s?"
    "Mädchen" "Ich heisse %(yanName)s."
    b "..."
    yan "..."
    "%(yanName)s also..."
    "Ich habe keine Ahnung, was ich sagen soll..."
    "...aber wenn man sie so ansieht, könnte man meinen, ihr ginge es genauso."
    yan "..."
    b "..."
    "Was soll ich nun mit ihr machen?"
    "Die Polizei rufen?"
    yan "%(berndName)s... ich..."
    "Woher kennt sie meinen Namen überhaupt?"
    b "Woher kennst du meinen Namen?"
    yan "..."
    "Jetzt schweigt sie wieder."
    "Ich sollte nicht dazwischen reden, wenn ich etwas von ihr erfahren will."
    b "Sprich ruhig weiter."
    yan "..."
    yan "Ich..."
    #weinend!
    yan "...es tut mir so Leid!"
    yan "*schluchz*"
    "Warum weint sie denn jetzt!?"
    "Ist das nur show?"
    "Verarscht sie mich, um einen überraschenden Fluchtversuch zu starten?"
    "...oder ist es echt?"
    menu:
        "Ich rufe jetzt die Polizei!":
            jump yasmin_polizei
        "Ich habe Mitleid mit ihr.":
            "...vielleicht sollte ich sie einfach noch ein wenig hier behalten."
            "Ich muss mehr über sie herausfinden."
    yan "*schluchz*"