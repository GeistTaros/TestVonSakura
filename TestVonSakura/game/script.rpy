python:
    import storetest2.rpy
    import pygame as pg
define name1="?"
define bday="??" 
define bmonth="??"
define byear="????"   
# Maincharacter
define test11 = Character(
    "[name1]",
    what_size=28,
    what_outlines=[( 1, "#160215", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')
 
 
# Hier beginnt das Spiel.
label start:
    default index = 0
    python:
        for i in IDNitem:
            i.Erhalten = False
        sa_park = False
        Namenscounter = 5
        birthdate = "[birthdate]"
        Sakura_hunting_you=False
        Portmonaie_credits=100
        
label namenschreiben:
    if Namenscounter == 0 :
        return
    elif Namenscounter <= 4:
        warning "Du hast noch [Namenscounter] Versuche den Namen zu ändern, sonst wird das Spiel abgebrochen"
    $ Happyending = 0
    label nleng:
    python:
        name1 = renpy.input("Wie lautet dein Name?",length=20)
        name1 = name1.strip() or "Test11"
    if  name1 == "T23" or name1 == "t23":
        jump Marcoo
menu Namensgebung: 
    sys "Du heist wirklich [name1]???"
    "Ja ich heiße wirklich [name1]":
        jump Geburtstagschreibung
    "Nein ich heiße anders":
        jump namenschreiben
label Geburtstagschreibung:
    sys "Nun kommen wir zum Geburtstag."
    python:

        #old test
        byear = renpy.input("Gib nun das Jahr ein ",allow="1234567890",length=4) or 0
        bmonth = renpy.input("Gib nun den Monat ein",allow="1234567890",length=2) or 0
        bday = renpy.input("Nun den Tag",allow="1234567890",length=2) or 0
        #dateformation = dzahl/mzahl/yzahl 
    if  (int(bmonth)<=12) and (int(bday)<=31):
        jump akt0
    else:
        jump geburtfalsch
label geburtfalsch:
    warning "Dein Geburtstag ist kein Zifferformat oder ist falsch"  
    jump Geburtstagschreibung
        

       
label Marcoo:
    $ bday = 00
    $ bmonth = 00
    $ byear = 0000
    $ G000.Erhalten=True
    $ int(Portmonaie_credits) + 99999999
label akt0:
#    show screen Artzkastener  
    narrator "Dies hier ist nur ein Test... "
    if G001.Erhalten:
        "Test Gescheitert"
    else:
        "Test bestanden"
    $ G007.Erhalten=True
    $ G001.Erhalten=True
    $ G002.Erhalten=True
    $ G003.Erhalten=True
    $ G004.Erhalten=True
    $ B001.Erhalten=True
    # $ G0.Erhalten=True
    if G001.Erhalten:
        "Test [G001.Gname] Erfolgreich"
    if G002.Erhalten:
        "Test [G002.Gname] Erfolgreich"
    if G003.Erhalten:
        "Test [G003.Gname] Erfolgreich"
    if G004.Erhalten:
        "Test [G004.Gname] Erfolgreich"
    else:
        "Test gescheitert"
    #"[dateformation]"
    with Pause (3)
    scene background_park
    show sakura at links 
    with dissolve
    sa "Hi, ich bin Sakura"
    sa "Freut mich"
menu Sakura_Frage1:
    sa "Findest du mich hübsch?"
    "Ja":
        jump saja1
    "Nein":
        jump sanein1
label saja1:
    sa "Dankeschön mein süßer"
    hide sakura with dissolve
    jump akt00
    
label sanein1:
    $ Sakura_hunting_you=True
    sa1 "Du bist tot"
    $ G005.Erhalten = True
    sa1 "TOT!!!!!!!"
menu Teleporter:
    "Teleportiere dich weg" if G007.Erhalten:
        jump teleportaway
    "Von einen Mädel umgebracht zu werden, war schon immer mein Traum":
        jump tot
    "Test" if G000.Erhalten:
        jump test00001
label tot:
    python:
        about_ach2.locked=False 
        Happyending -=99999999999 
    $ renpy.notify([about_ach2.name])  
    hide sakura with vpunch
    scene black
    sa2 "Warum {cps=5}fandest du mich hässlich??????{/cps}"
    with Pause(3)
    
    "You died with [Happyending] points"
    return
label teleportaway:
    $ about_ach1.locked=False
    hide sakura
    $ G007.Erhalten=False
label akt00:
    hide sakura
    show marta normal at mitte
    ak "..."
    test11 "test bestanden"
    ma "test"
    ak "hello test"
    ma happy "ich bin glücklich"
    narrator "Entscheide dich nun"

menu testmenu1:
    "Deine Entscheidung. Wählst du die blaue Pille oder die Rote"
    "Blaue Pille":
        jump Blaue_Pille
        
    "Rote Pille":
        jump Rote_Pille
        
    

label Blaue_Pille:
    $ about_ach4.locked=False
    $ Happyending += 1
    $ blue_flag = True 
    show sakura at links
    with dissolve
    show akane at rechts
    with move

    ak " Herzlichen Glückwunsch du hast [Happyending] P"
    if Sakura_hunting_you:
        sa "Ich bring dich gleich um"
    else:
        sa "hello my friend"

    test11 "Hi, ich bin [name1], du bist [ak]"

    jump Akt1

label Rote_Pille:
    $ Happyending -= 1
    $ blue_flag = False
    hide marta
    with Pause(1)
    
    show sakura at rechts
    with dissolve

    sa "Herzlichen glückwunsch du hast [Happyending] P"
    jump Akt1

label Akt1:

    hide sakura 
    with dissolve
    hide marta
    with dissolve
    hide akane
    with dissolve
    if blue_flag:

        "Du hast du Blaue Pille genommen"
    else:
        
        "Du hast die Rote Pille genommen"
    jump Akt2

label Akt2:
    scene bg_night
    "Wir sind nun am Ende angekommen"

menu testmenu2:
    "Wie gefiel es dir?"
    "Gut":
        jump Akt2_gut
        
    "Nicht gut":
        jump Akt2_schlecht

label Akt2_gut:
    $ Happyending +=1
    jump Akt2P2

label Akt2_schlecht:
    $ Happyending -=1

    jump Akt2P2

label Akt2P2:
    if Sakura_hunting_you:
        jump BadEnding   
    elif Happyending >= 2:
        jump Goodending  
    elif Happyending == 0 :
        jump Nending
    elif Happyending <= 0 :
        jump BadEnding
    else:
        jump BadEnding

            
label Goodending:
    $ about_ach3.locked=False
    $ sa_park = True 
    hide Marta
    hide Akane
    scene background_park
    show sakura at mitte
    Park_narrator "Du triffst dich mit Sakura im Park"
    sa "Schönes Wetter, findest du nicht [name1]"
    name1 "Mit dir sicherlich"
    Park_narrator "Du hast das gute Ende erhalten mit [Happyending] P"

    jump AktEnde
label Nending:
    show marta normal
    "Du hast das normale Ende erhalten mit [Happyending] P"
    hide marta 
    jump AktEnde
label BadEnding:
    show akane at rechts
    if Sakura_hunting_you:
        "Du hast das schlechte Ende erhalten weil du Sakura beleidigt hast"
    else:
        "Du hast das schlechte Ende erhalten [Happyending] P"
    hide akane
    jump AktEnde
            
label AktEnde:
    if sa_park:
        jump sakurahappy
    else:
        jump normal
label normal:
    ak "Tschüss"
    sa "Tsüsch"
    ma "Bye"
    return
label sakurahappy:
    sa "wiedersehen"
    return
    