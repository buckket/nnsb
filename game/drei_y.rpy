label drei_yasmin:    
    #anfang kapitel 3
    
    scene bg keller
    with dissolve
    
    "Zwei Stunden ist es her, dass sie gegangen ist."
    "In diesen zwei Stunden habe ich so gut wie nichts gemacht."
    "Seit zwei Stunden sitze ich hier auf meinem Bett und mache nichts."
    "Nein, das ist nicht ganz richtig."
    "Ich mache schon etwas."
    "Ich denke."
    "Ich denke sogar ziemlich viel."
    "Über das, was gestern Abend passiert ist, wie es dazu kommen konnte, was es für Folgen haben wird."
    "Ich kann %(yanName)s immer noch nicht verstehen."
    "Warum verhält sie sich so?"
    "Wo ist ihr Motiv?"
    "Sie muss ein Motiv haben, oder?"
    "Irgendwelche Beweggründe, die sie antreiben."
    "Jeder Mensch hat das."
    "Außer mir."
    "Ich habe keine Ziele. {w}Keine Motive. {w}Keinen Antrieb oder so was."
    "Deswegen bin ich ja auch ein Bernd."
    "Aber sie ist kein Bernd."
    "Welchen Grund kann sie haben?"
    "Was bringt sie dazu, erst bei mir einzubrechen und dann hier zu übernachten?"
    "Noch dazu mit mir im selben Bett."
    "Irgendetwas ist hier faul."
    "Aber ich werde der Sache auf den Grund gehen."
    "Ich werde herausfinden, warum sie so ist, wie sie ist."
    "Schließlich bin ich kein dummer Charakter aus irgendeinem Computerspiel, der nicht merkt, was um ihn herum geschieht."
    "...aber wie gehe ich vor?"
    "Wie finde ich heraus, was sie denkt?"
    "Ich muss mich in ihre Lage versetzen, aber wie macht man das?"
    "Wenn ich sie wäre... {w}was würde ich tun?"
    b "Stell es dir vor, %(berndName)s..."
    b "...du bist ein Mädchen."
    b "Du bist kein Bernd mehr."
    b "Du bist ein Mädchen... {w}eine junge Frau..."
    b "...was würdest du tun?"
    "... {w}... {w}..."
    "So sehr ich es auch versuche, ich komme zu keinem richtigen Schluss."
    "Wenn ich ein Mädchen wäre, würde ich wahrscheinlich den ganzen Tag an mir selbst rumspielen."
    "Aber ich bezweifle, dass mich das irgendwie dazu bringen könnte, sie besser zu verstehen."
    "Ich brauche mehr Informationen über sie."
    "Wenn ich verstehen will, wie sie denkt... {w}muss ich wissen, wer sie ist."
    "Aber wie soll ich mehr über sie erfahren?"
    "Dafür bräuchte ich zumindest ihren vollen Namen."
    "Das kann ich also schon mal vergessen."
    "Vielleicht sollte ich mich da anders nähern."
    "Ich muss ja nicht unbedingt herausfinden, wer sie genau ist."
    "Es reicht eventuell wenn ich herausfinde, in welcher Beziehung sie zu mir steht."
    "Wieso sollte jemand interesse an mir haben?"
    "Gehen wir mal die Möglichkeiten durch..."
    "1. Sie ist ein gewöhnlicher Dieb."
    "Gut möglich, denn sie ist bei mir eingebrochen."
    "Das spricht auf jeden Fall dafür."
    "Dagegen spricht, dass sie nicht abgehauen ist als ich sie erwischt habe."
    "Aber auch das könnte nur ein Trick sein."
    "...und er hat funktioniert."
    "Ich habe nicht die Polizei gerufen."
    "Sie ist entkommen."
    "Aber wenn sie ein Dieb wäre... {w}was würde sie bei mir klauen wollen?"
    "Ich habe nichts."
    "Sie hat auch keine Anstalten gemacht, etwas mitzunehmen, bevor ich sie überrumpelt habe."
    "..."
    "Doch, hat sie."
    "Sie hat versucht, meine Festplatte zu kopieren."
    "Warum?"
    "Was ist da drauf?"
    "Ich habe nichts außer Animevideos, Musik und ein paar Games."
    "Definitiv nichts von Wert."
    "Kommen wir zur nächsten Möglichkeit."
    "2. Sie ist doch Stalkerbernd."
    "Zwei Dinge sprechen dagegen."
    "Sie hat behauptet, kein Bernd zu sein."
    "Das könnte jeder behaupten."
    "Kein wirklich wirksames Argument."
    "Aber es gibt da noch etwas..."
    "...sie ist definitiv eine Frau."
    "Sie ist weiblich."
    "Es gibt keine weiblichen Bernds."
    "Absolut keine."
    "Sie existieren nicht."
    "Das sind irgendwelche Typen, die sich als Frauen ausgeben, um Bernd zu ärgern."
    "Wenn auch unwahrscheinlich, bleibt das trotzdem eine Möglichkeit."
    "Schließlich ist Stalkerbernd die einzige Person, von der ich irgendwie von Interesse sein könnte."
    "Die letzte Möglichkeit wäre..."
    "3. Sie ist keins von beiden."
    "Die wahrscheinlich einfachste Antwort."
    "Aber wirklich weiter bringt mich das nicht."
    "Was mir fehlt sind mehr Informationen über sie."
    "Ich kann mir schlecht ein Bild von ihr machen, wenn ich nichts über sie weiß."
    "...aber ich muss auch nicht sofort zu einem Schluss kommen, oder?"
    "Vielleicht könnte ich einfach noch ein wenig warten."
    "Sie wollte sich ja nochmal mit mir treffen."
    "Dann muss es mir gelingen, soviel wie möglich über sie herauszufinden."
    "...aber vielleicht sollte ich trotzdem schon mal in eine Richtung forschen."
    "Es kann nicht schaden."
    "Also welche Möglichkeit erscheint am wahrscheinlichsten?"
    menu:
       "Sie ist eventuell ein Dieb.":
           $ yanVerdacht = "dieb"
           "Dass sie ein Dieb ist, erscheint mir im Moment am wahrscheinlichsten."
           "Ich habe zwar keine Ahnung, was sie von mir stehlen würde, aber das werde ich herausfinden."
       "Sie ist eventuell Stalkerbernd.":
           $ yanVerdacht = "bernd"
           "Auch wenn sie ein Mädchen ist... vielleicht ist sie trotzdem ein Bernd."
           "Das würde erklären, was sie von mir will und warum sie an meinem Computer wollte."
           "Sie ist hinter meinen persönlichen Daten her, um sie auf Krautchan zu posten."
           "Aber Krautchan ist im Moment down, also habe ich fürs Erste nichts zu befürchten."
           "Trotzdem sollte ich mehr über sie herausfinden."
       "Ich kann es nicht genau sagen.":
           $ yanVerdacht = "kein"
           "Ich habe einfach zu wenig Informationen über sie."
           "Ich werde mich nochmal mit ihr treffen müssen, um wirklich zu klären, was sie von mir will."
           "Darauf sollte ich mich vorbereiten."
           
    "Aber zuerst brauche ich irgendwas zu trinken."
    "Immer noch ziemlich verwirrt, steige ich die Treppe nach oben."
    
    scene bg kueche
    with fade
    
    "In der Küche ist niemand."
    "Ich will auch im Moment niemanden sehen."
    "Das würde mich nur ablenken."
    "Nachdem ich ein Glas mit Traubensaft gefüllt habe, will ich wieder nach unten gehen aber..."
    
    show laura neutral
    with dissolve
    
    sis "Hi, %(berndName)s."
    sis "Ist deine..."
    "Sie sieht sich kurz um als würde sie sich vergewissern, dass ihr niemand zuhört und spricht dann leise weiter."
    sis "...Freundin... schon weg?"
    b "Sie ist nicht meine Freundin."
    
    show laura happy
    with dissolve
    
    sis "Alles klar..."
    
    show laura neutral
    with dissolve
    
    sis "Und was macht sie dann bei dir?"
    sis "Wieso solltest du dich denn mit einem Mädchen hier treffen, wenn sie nicht deine Freundin ist?"
    "Ich könnte es ihr erklären, aber ich habe keine Lust."
    "Was soll ich sagen?"
    sis "Na?"
    
    show laura happy
    with dissolve
    
    sis "Also hatte ich recht."
    sis "Sie ist deine Freundin."
    sis "Ist dir das peinlich?"
    sis "Wie alt ist sie überhaupt?"
    sis "Woher kennst du sie?"
    sis "Wieso ist sie so schüchtern?"
    b "Lass mich einfach in Ruhe."
    b "Nervensäge."
    
    show laura pissed
    with dissolve
    
    sis "Dann halt nicht."
    b "Richtig."
    b "Es geht dich nichts an."
    
    show laura mad
    with dissolve
    
    sis "Idiot..."
    "Zähneknirschend verlässt sie die Küche."
    
    hide laura mad
    with dissolve
    
    "%(yanName)s... meine Freundin?"
    "So ein Quatsch."
    "Ich kenne sie gar nicht."
    "Außerdem..."
    "Wieso sollte sie mich mögen?"
    "Ich bin ein Bernd."
    if yanVerdacht == "bernd":
       "Sie vielleicht auch..."
       "Trotzdem..."
    else:
       "Sie nicht."
       "Und überhaupt..."
    "Ich habe mich sowieso schon damit abgefunden, niemals eine Freundin zu finden."
    "Und ganz sicher nicht so plötzlich."
    "So was passiert nur in irgendwelchen Filmen oder Mangas."
    "Nicht im echten Leben."
    "Das wäre ja total kitschig."
    "Was sollte sie auch an mir mögen?"
    "Es gibt doch genug Typen, die nicht solche Versager sind wie ich."
    "Bei denen wäre sie besser aufgehoben."
    "Die haben einen Job, viel Geld, sind nett, gepflegt und sehen gut aus."
    "Ich bin nur ein Bernd."
    "Aber das ist ja auch völlig egal, denn sie mag mich ja überhaupt nicht."
    
    "...mal schauen, ob Krautchan schon wieder online ist."
    
    scene bg keller
    with fade
    
    "..."
    "Nein, sieht nicht so aus."
    "Verdammt."
  
    "Ich kann überhaupt nichts tun."
    "Mehrmals blicke ich mich um, aber hier ist nichts zu tun."
    "Einfach nichts."
    "Null."
    "Gar nichts."
    "Mir ist langweilig."
    "Sehr sogar."
    "Vielleicht sollte ich mal ein wenig frische Luft schnappen."
    "...obwohl..."
    "Dafür müsste ich ja in die Außenwelt."
    "Will ich das wirklich?"
    "Wohl kaum."
    "Aber was soll ich sonst machen?"
    "Es würde vielleicht reichen, das Fenster zu öffnen, aber ich habe kein richtiges Fenster."
    "Es hilft alles nichts, ich muss einen klaren Kopf kriegen."
    "Ich laufe einfach eben eine Runde um den Block."
    
    scene bg zuhause_draussen_dunkel
    with fade
    
    "Es ist schon ziemlich dunkel."
    "Aber so spät ist es doch noch gar nicht?"
    "Komisch."
    "Ich atme tief ein."
    "Die kalte Luft tut mir gut und macht mir den Kopf frei."
    "Endlich kann ich mal durchatmen."
    "Immer nur im Keller zu sitzen kann auf die Dauer ganz schön anstrengen."
    "Ich biege um die Ecke."
    "Die Straße ist leer, niemand ist hier."
    "Ich versuche an etwas anderes zu denken, aber irgendwie komme ich immer wieder auf %(yanName)s zurück."
    "Wieso werde ich aus ihrem Verhalten nicht schlau?"
    "Weil sie eine Frau ist?"
    "Verhalten sich etwa alle Frauen so merkwürdig?"
    "Was sie tut ergibt keinen Sinn..."
    "Aber warum tut sie es dann?"
    "Ich verstehe sie einfach nicht."
    "Hoffentlich sehe ich sie nicht wieder."
    "Dann könnte ich das einfach alles vergessen und wieder ein ganz normales Leben führen."
    "So wie vorher."
    "Ja, das ist das Beste."
    "Wenn Krautchan erst wieder online ist, wird alles gut."
    "...aber was mache ich, wenn sie doch wieder bei mir aufkreuzt?"
    "Sie wegschicken?"
    "Das könnte ich nicht."
    "Ich habe nicht die Kraft ihr so was zu sagen."
    "Ich konnte es schon heute morgen nicht."
    "Also was dann?"
    "Ausreden erfinden?"
    "Das kann ich ziemlich gut."
    "Ich habe mich schon immer vor allem gedrückt, indem ich mir irgendwelchen Schwachsinn ausgedacht habe."
    "Irgendwann bin ich deswegen von der Schule geflogen."
    "Aber dort hielt mich eh nichts."
    "Auch mit tollem Abschluss findet man heute kaum noch einen Job, und Freunde hatte ich da auch keine."
    "Ich hatte noch nie Freunde."
    "Immer ein paar Leute, mit denen man halbwegs reden konnte, aber auch nur über bestimmte Dinge."
    "Woran liegt das?"
    "Bin ich selbst Schuld?"
    "Hätte ich etwas ändern können?"
    "Darüber nachzudenken bringt mir jetzt auch nichts."
    "Es ist schon viel zu spät."
    "In meinem Leben ändert sich eh nichts mehr."
    "Ich werde einsam sterben."
    "Einfach irgendwann grillen gehen..."
    
    jump drei_yasmin_gewitter

label drei_yasmin_gewitter:

    scene bg zuhause_draussen_dunkel
    with flash
    
    play sound "sounds/donner.wav"
    
    "Ein Blitz holt mich aus meinen Gedanken."
    "..."
    "Ein Gewitter?"

    play music "sounds/regen.wav" fadein 2.0
    
    "Na toll."
    "Es fängt an zu regnen und ich habe keine Schirm oder so was."
    "Wo bin ich überhaupt?"
    "Ich bin so sehr in Gedanken versunken gewesen, dass ich einfach weiter gelaufen bin, ohne auf den Weg zu achten."
    "Hier kenne ich mich nicht aus."
    "Der Regen wird stärker."
    #"Ich bin schon ganz feucht."
    "Ich bin schon ganz nass." # :3
    "Wo komme ich her?"
    "Ich habe mich verlaufen."
    
    scene bg zuhause_draussen_dunkel
    with flash
    
    play sound "sounds/donner.wav"
    
    "Da vorne ist eine Bushaltestelle."
    "Dort stelle ich mich unter, bis der Regen aufhört."
    "Da ist bestimmt auch ein Stadtplan."
    "Vielleicht finde ich dann den Weg zurück."
    
    scene bg bushaltestelle
    with dissolve
    
    "Hier ist es erst mal trocken."
    "Auch wenn ich sowieso schon klitschnass bin."
    "Ein Stadtplan hängt hier auch, aber irgendwer hat ihn vollgekritzelt."
    "Man kann nichts erkennen."
    "Scheiß Unterschichtkinder."
    "Haben die sonst nichts zu tun?"
    "Warum machen sie anderen das Leben schwer?"
    
    scene bg bushaltestelle
    with flash
    
    play sound "sounds/donner.wav"
    
    "Es bleibt mir wohl nichts anderes übrig, als hier zu warten bis es vorbei ist."
    "..."
    "Der Regen nimmt kein Ende."
    "Inzwischen ist es wirklich stockdunkel."
    "Als wäre es Nacht."
    "...oder ist es schon Nacht?"
    "Bin ich so lange gelaufen?"
    "Ich habe keine Uhr dabei, aber es erscheint mir unwahrscheinlich."
    "Das liegt wohl nur am Gewitter."
    "Ich werde hier wohl noch eine Weile warten müssen."
    "Hoffentlich nicht zu lange."
    "Notfalls muss ich einfach durch den Regen zurück."
    "...aber ob ich im Dunkeln den Weg finde..."
    
    scene bg bushaltestelle
    show yasmin stalker_schwarz_k
    with flash
    
    play sound "sounds/donner.wav"
    
    hide yasmin stalker_schwarz_k
    with fastDissolve
    
    "...!"
    "Ich habe es nur kurz gesehen, aber auf der anderen Straßensteite steht jemand."
    "Irgendwer steht dort und schaut in meine Richtung."
    "Ganz sicher."
    "Wer?"
    "Wer ist das?"
    "Nur irgendein Fußgänger?"
    "Nein."
    "Wer würde bei diesem Regen freiwillig draußen herumlaufen und sich den Tod holen?"
    "Das ist verdächtig."
    "Steht er noch dort?"
    "Oder ist er vielleicht einfach weitergegangen?"
    "Oder kommt er wohlmöglich schon auf mich zu?"
    "Sicher will er mich ausrauben oder..."
    
    scene bg bushaltestelle
    with flash
    
    play sound "sounds/donner.wav"
    
    "...weg."
    "Er ist weg."
    "...oder war er gar nicht da?"
    "Bilde ich mir schon Dinge ein?"
    "Nein."
    "Er war da."
    "Ganz sicher."
    "Es war am Ende doch nur ein Fußgänger."
    "Irgendjemand, der vom Regen überrascht wurde und nun auf dem Weg nach Hause ist."
    "Hoffentlich bleibt das meine einzige Begegnung für heute..."
    "Schritte."
    "Ich höre Schritte."
    "Von wo?"
    "Irgendwo auf der Straße läuft jemand."
    "Sie werden lauter."
    "Jemand läuft in meine Richtung."
    "Will er nur vorbei?"
    "Oder will er zu mir?"
    "Was soll ich tun?"
    "Ich warte einfach."
    "Es wird schon nichts passieren."
    "...hoffe ich."
    "Die Schritte sind jetzt ganz nah."
    "Eine Person tritt in den Schein der Haltestellenbeleuchtung."
    
    show yasmin stalker_neutral
    with dissolve
    
    "Aber... {w}das ist ja...{w} %(yanName)s."
    
    jump drei_yasmin_regen
    
label drei_yasmin_regen:    
    show yasmin stalker_happy
    with dissolve
    yan "Hey, %(berndName)s."
    b "Äh... Hey."
    show yasmin stalker_neutral
    with dissolve
    yan "Was machst du hier draußen?"
    yan "Noch dazu bei diesem Wetter?"
    yan "Hätte nicht gedacht, dass du jemand bist, der oft draußen herumläuft."
    yan "Vor allem nicht bei Regen..."
    "Wer würde auch bei Regen freiwillig rausgehen?"
    b "Tja, das hat sich so ergeben."
    b "Irgendwie war ich unterwegs und dann zog dieses Gewitter auf..."
    b "Nun sitze ich hier und..."
    "Ich kann ihr schlecht sagen, dass ich den Rückweg nicht finde."
    "Das ist ja peinlich."
    b "...und ich warte, bis es zu regnen aufhört."
    show yasmin stalker_happy
    with dissolve
    yan "Ach so."
    yan "Na dann..."
    yan "Würde es dich stören, wenn ich neben dir sitze?"
    "Ja."
    b "Nein."
    "Verdammt."
    "Ich würde lieber allein sein, aber das kann ich ihr nicht sagen."
    "Sie nimmt direkt neben mir Platz."
    "Viel zu nah."
    "Ich rutsche ein Stück zur Seite."
    "Eine Weile lang schweigen wir."
    "Sollte ich irgendwie ein Gespräch anfangen?"
    "Oder einfach sitzen bleiben?"
    "Was würde ich denn sagen?"
    show yasmin stalker_embarrased
    with dissolve
    yan "%(berndName)s..."
    yan "Wie lange willst du hier noch sitzen?"
    b "Bis der Regen aufhört."
    yan "...das kann aber dauern."
    yan "Willst du so lange hier bleiben?"
    b "Ja."
    yan "...ok."
    show yasmin stalker_happy
    with dissolve
    yan "Dann werde ich auch warten."
    "Na super."
    "Ich werde also die nächsten Minuten, Stunden oder Tage neben ihr sitzen und schweigen."
    "Was macht sie überhaupt hier?"
    "Wieso läuft sie im Regen herum?"
    b "Was treibt dich eigentlich her?"
    b "Wieso bist du hier?"
    yan "Hm... {w}ich war auf dem Weg... {w}zu dir!"
    b "Wieso zu mir?"
    yan "Ich wollte mal wieder vorbeischauen..."
    b "...aber du bist vor ein paar Stunden erst gegangen..."
    b "...und du meintest, dass du wirklich gehen musst..."
    show yasmin stalker_embarrased
    with dissolve
    yan "Das ist..."
    yan "...also ich musste auch weg."
    yan "Aber ich hab alles erledigt..."
    yan "...und ich hatte nichts zu tun, also wollte ich vorbeischauen."
    "Als ob."
    b "Soso."
    "Jetzt schweigen wir wieder."
    "Was sie sagt ergibt keinen Sinn."
    
    scene bg bushaltestelle
    show yasmin stalker_schwarz
    with flash
    show yasmin stalker_surprised
    with dissolve
    
    play sound "sounds/donner.wav"
    
    yan "Ah!"
    "Sie zuckt zusammen und ich kann mir ein Lächeln nicht verkneifen."
    "Wieso hat sie in ihrem Alter noch Angst vor Gewitter?"
    
    show yasmin stalker_embarrased
    with dissolve
    
    yan "...albern, oder?"
    b "Hm?"
    "Sie hat wohl gemerkt, dass ich mich über sie lustig gemacht habe."
    yan "...ach nichts."
    "Wieder Stille."
    yan "Wollen wir nicht zu dir gehen, %(berndName)s?"
    b "...aber es regnet noch."
    
    show yasmin stalker_shy
    with dissolve
    
    yan "Bist du so empfindlich?"
    b "Nein... ich..."
    "Ich kann ihr schlecht sagen, dass ich den Weg nicht finde."
    "Oder...?"
    
    menu:
        "Ich sollte es ihr sagen.":
            "Richtig, ich sollte ihr einfach sagen, was Sache ist."
            "Sie wird mich ja wohl nicht auslachen."
            "Und wenn... {w}das interessiert mich überhaupt nicht."
            "Ich bin es ja gewohnt, dass man sich über mich lustig macht."
            "Also dann..."
            b "Ich..."
            b "Ich finde nicht mehr nach Hause."
            b "Das ist alles."
            
            show yasmin stalker_surprised
            with dissolve
            
            yan "Was?"
            yan "Du..."
            
            show yasmin stalker_smile
            with dissolve
            
            yan "Wenn das alles ist..."
            yan "Ich kenne den Weg doch."
            yan "Warum hast du nichts gesagt?"
            b "..."
            yan "Es muss dir nicht peinlich sein."
            yan "Nur weil du dich hier nicht auskennst?"
            yan "Ist doch nicht schlimm... oder?"
            "Sie hat Recht."
            b "Nein..."
            b "Du hast Recht."
            yan "Also dann... wollen wir?"
            b "OK..."
            
        "Ich sollte mich weiter rausreden.":
            "Nein, ich kann es ihr auf keinen Fall sagen."
            "Viel zu peinlich."
            "Aber was erzähle ich ihr dann?"
            b "Ich..."
            "Verdammt, %(berndName)s, überleg dir was!"
            b "Ich will nicht nach Hause."
            
            show yasmin stalker_surprised
            with dissolve
            
            yan "Wieso das?"
            b "Ich..."
            "Oh man, was jetzt?"
            b "Ich will nicht darüber sprechen."
            "Ich höre mich an wie irgendein Emo oder so was..."
            
            show yasmin stalker_shy
            with dissolve
            
            yan "Das..."
            yan "Das verstehe ich."
            yan "Aber du kannst nicht die ganze Nacht hier sitzen bleiben."
            yan "Lass uns gehen, ok?"
            yan "Bitte?"
            b "..."
            yan "..."
            "Ach, was soll's."
            b "OK... gehen wir."
            
            show yasmin stalker_happy
            with dissolve
            
            yan "Gut."
            
    "Sie tritt hinaus in den Regen."
    
    show yasmin stalker_happy
    with dissolve
    
    yan "Beeil dich, sonst werden wir ganz nass."
    b "Du hast wenigstens eine Kapuze."
    b "Warum setzt du sie nicht auf?"
    
    show yasmin stalker_smile
    with dissolve
    
    yan "Mir macht Regen nichts."
    yan "Ist im Endeffekt ja nur Wasser."
    "Wo sie Recht hat, hat sie Recht."
    "Ich stehe auf und mache zwei Schritte vorwärts."
    "Innerhalb von wenigen Sekunden bin ich nass von Kopf bis Fuß."
    b "..."
    
    show yasmin stalker_happy
    with dissolve
    
    yan "Willst du meinen Mantel haben?"
    b "Nein."
    "Ganz bestimmt nicht."
    
    show yasmin stalker_shy
    with dissolve
    
    yan "...dann nicht."
    
    show yasmin stalker_neutral
    with dissolve
    
    yan "Los, beeil dich ein bisschen."
    
    hide yasmin stalker_neutral
    with dissolve
    
    "Sie rennt voraus und ich folge ihr."
    
    scene black
    with fade

label drei_yasmin_rauswurf:
    
    #nun wir bernd rausgeworfen und zieht bei yasmin ein
    #kawaii desu ne? ^_^
    
    scene bg zuhause_draussen_dunkel
    with fade
    
    "Völlig durchnässt stehen wir endlich vor der Haustür."
    "Ich habe mir grade sicher eine Erkältung geholt."
    "Verzweifelt versuche ich, die Tür zu öffnen, aber der Schlüssel rutscht immer wieder ab."
    "Dieses verdammte..."
    show yasmin stalker_neutral
    with dissolve
    yan "Sag mal %(berndName)s..."
    b "Was denn?"
    yan "...standen diese Kisten hier vorher auch schon?"
    "Tatsächlich stehen vor der Haustür ein paar Pappkartons, teilweise durchnässt vom Regen."
    yan "Wer stellt denn Pappkartons raus in den Regen? {w}Wem die wohl gehören?"
    "Ich weiß es."
    b "Das... {w}sind meine."
    show yasmin stalker_surprised
    with dissolve
    yan "Was?"
    "Wieso steht mein ganzer Besitz vor der Haustür im Regen?"
    yan "Wer hat die denn hier hingestellt?"
    b "Keine Ahnung."
    show yasmin stalker_neutral
    with dissolve
    yan "Schau mal hier..."
    "Auf einem Karton liegt ein zusammengefalteter Zettel."
    yan "Der ist an dich, %(berndName)s."
    "Ich befürchte schlimmes, während ich den Zettel auseinanderfalte."
    
    #show bg zettel
    #with fade
    #evtl. halt den Zettel einblenden
    
    nvlc "Lieber %(berndName)s,\n"
    nvlc "du wirst dich sicher wundern, warum dein ganzer Besitz hier vor der Haustür steht, daher will ich es dir erklären."
    nvlc "Ich habe jetzt schon lange darüber nachgedacht, und dieser Schritt fällt mir nicht leicht, aber es muss wohl sein."
    nvlc "Von nun an wirst du nicht mehr bei uns wohnen."
    nvlc "Es tut mir wirklich sehr Leid, dir das antun zu müssen, aber wenn du nicht lernst, auf eigenen Füßen zu stehen, wie soll dann jemals etwas aus dir werden?"
    nvlc "Es ist wirklich nur zu deinem Besten, also bitte sei mir nicht böse.\n"
    nvlc "In Liebe"
    nvlc "  %(maName)s"
    
    nvl clear
    
    "..."
    yan "Und? {w}Was steht drin?"
    b "..."
    yan "Sag schon!"
    b "Sie haben mich rausgeworfen."
    show yasmin stalker_surprised
    with dissolve
    yan "Was?! {w}Ernsthaft!?"
    b "Ja."
    yan "Aber..."
    "Ich setze mich auf einen der Kartons und versuche zu begreifen, in welcher Situation ich mich überhaupt befinde."
    show yasmin stalker_neutral
    with dissolve
    yan "%(berndName)s."
    "Ich bin obdachlos."
    "Kein Strom, kein Internet."
    "Und es regnet."
    yan "%(berndName)s."
    "Und ich werde draußen schlafen müssen."
    "Und mir einen Job suchen müssen."
    "Und eine eigene Wohnung."
    "Keine Zeit mehr zum Lauern."
    yan "%(berndName)s?"
    b "Was denn?"
    yan "Ich hab da eine Idee..."
    yan "...wartest du hier auf mich?"
    b "Wo willt du hin?"
    yan "Ich hol kurz etwas."
    "Als ob ich irgendwo hingehen würde."
    "Wo denn auch?"
    "Ich kann nirgendwo hin."
    b "Ist gut."
    show yasmin stalker_happy
    with dissolve
    yan "Ich beeil mich!"
    hide yasmin stalker_happy
    with dissolve
    "Sie rennt davon und ich bin wieder allein."
    
    # jetzt redet bernd eine weile mit sich selbst
    # und malt sich die schlimmsten horrorvorstellungen aus.
    # dann kommt yasmin mit ihrem auto und holt ihn ab,
    # damit er bei ihr wohnen kann. er hat keine andere wahl, als anzunehmen