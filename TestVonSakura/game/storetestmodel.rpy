init python:

# index = IDN
    IDNitem = []
    IDNbook = []
    IDNwho = []

        
    class Gegenstand(object):
        def __init__(Gegst, Gname="Noname",Erhalten=False, tx="Keine Info vorhanden",cr=1,buy=True,anzahl=int(0)):
            super(Gegenstand, Gegst,).__init__()
            Gegst.Gname = Gname
            Gegst.Erhalten = Erhalten
            Gegst.tx = tx
            Gegst.cr = int(cr)
            Gegst.buy = buy
            Gegst.anzahl = int(anzahl)
            IDNitem.append(Gegst)
        def __str__(Gegst):
            return Gegst.Gname + Gegst.tx 
#Gegenstände

define G000 = Gegenstand("Test", False,)
define G001 = Gegenstand("Regenschirm",False, "Ein Schirm, der vor Regen und Sonne schützt",19,True)
define G002 = Gegenstand("Messer",False, "Frauen mit Messer sind meistens Gefährlich" )
define G003 = Gegenstand("Wunderkerzen",False, "Leuchtet schön in der Nacht")
define G004 = Gegenstand("Getränkedose",False, "`Verleiht Fittiche` steht auf der Dose")
define G005 = Gegenstand("Schreibstift",False, "Um eine Nachricht zu hinterlassen")
define G006 = Gegenstand("Leeres Papier",False, "Ideal zum Beschriften")
define G007 = Gegenstand("Floh´s Teleporter", True, "Neuste Erfindung Von Floh",0,False)
# define G0 = Gegenstand()

init python:
    class Tasche(Gegenstand):
        def __init__(self, Gname="Noname",Erhalten=False, tx="Keine Info vorhanden"):
            super(Tasche, self,).__init__(Gegenstand,)
            self.Gname = Gname
            self.Erhalten = Erhalten
            self.tx = tx
        def __str__(self):
            return self.Gname + self.Erhalten + self.tx
  
define P000 = Tasche("Handtasche",False,"Wie viel in so eine Tasche passen kann. Fazinierend" )        


define P001 = Tasche("Portmonaie",False,"Ein Portmonee voller Geld und Karten" )

define P002 = Tasche("Verband",False,"Für eine Schnelle Verartztung" )

init python:
    class Buch:
        def __init__(self, Bname,Erhalten=False, tx="Keine Info vorhanden"):
            super(Buch, self).__init__()
            self.Bname = Bname
            self.Erhalten = Erhalten
            self.tx = tx
            IDNbook.append(self)
        def __str__(self):
            return self.Bname  + self.Erhalten +  self.tx

define B000 = Buch("Testbuch",True,"""
                                            Test zeile 1
                                            Test zeile 2
                                            Test zeile 3
                                            Test zeile 4
                                            Test zeile 5
                                            Test zeile 6
                                            Test zeile 7
                                            Test zeile 8""")

define B001 = Buch("Handbuch",False, "Ein Handbuch zum lesen")
define B002 = Buch("Brief",False, "Ein Brief. Von Wem könnte er nur Stammen?" )
define B003 = Buch("Beschriebenes Papier",False, "Nicht entzifferbare Buchstaben stehen auf den Papier")



style Item_Text:
    idle_color"#c0c0c0c0"
    hover_color"#ff0000ff"

#Menüs

#menü offen
screen openmenu():
    tag tag_screen
    frame:
        xalign 0 ypos 0
        vbox:
            text "Spielername: [name1]"
            text "Geburtstag: [bday].[bmonth].[byear]"
            text "Punktestand [Happyending]"
            textbutton "Gegenstände":
                action ShowMenu("player1_items")
            textbutton "Exit":
                action Return(True) 
#menü geschlossen
screen player1_items():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            textbutton "Portmonaie":
                action ShowMenu("MoneyBag")
            textbutton "Biblothek":
                action ShowMenu("Menu_book")
            textbutton "Handtasche":
                action ShowMenu("Menu_item")
            textbutton "Zurück":
                action Return()

#Taschen menü
screen MoneyBag():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[Portmonaie_credits] Credits"
            textbutton "Shop":
                action ShowMenu("player1_Shop")
            textbutton "Zurück":
                action ShowMenu("player1_items")
#Gegenstände

screen Menu_item():
    tag tag_screen
    frame:
        viewport:
            xalign 0.0 
            ypos 0
            ysize 200
            xsize 400
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vbox:
                text "Index"
                for i in IDNitem:
                    $ list_position = IDNitem.index(i)
                    
                    if i.anzahl > 0:
                        textbutton "{color=#ac2cbb}[i.Gname]{/color}":
                            action SetVariable("index",list_position),ShowMenu("Menu_item_more")
                            
                textbutton "Zurück":
                    action ShowMenu("player1_items")


screen Menu_item_more():
    
    tag tag_screen
    $ info_name = IDNitem[index].Gname
    $ info_tx = IDNitem[index].tx
    $ info_cr = IDNitem[index].cr
    $ info_count = IDNitem[index].anzahl
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "Preis:[info_cr] Cr"
            text "Name: [info_name]"
            text "Anzahl: [info_count]"
            textbutton "Bezeichnung":
                action ShowMenu("Item_detailed")
            textbutton "Zurück":
                action ShowMenu("Menu_item")


screen Item_detailed():
    tag tag_screen
    $ info_tx = IDNitem[index].tx
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[info_tx] "
            textbutton "Zurück":
                action ShowMenu("Menu_item_more")
            

#Ende Gegenstand
#
#Bücher Menüs

screen Menu_book():
    tag tag_screen
    frame:
        viewport:
            xalign 0.0 
            ypos 0
            ysize 200
            xsize 400
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vbox:
                vbox:
                    for i in IDNbook:
                        $ list_position = IDNbook.index(i)
                        
                        if i.Erhalten == True:
                            textbutton "[i.Bname]":
                                action SetVariable("index",list_position),ShowMenu("Menu_book_more"), 
                    textbutton "Zurück":
                        action ShowMenu("openmenu")

screen Menu_book_more():
    tag tag_screen
    $ info_name = IDNbook[index].Bname
    
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "Name: [info_name]"
            textbutton "Mehr":
                action  ShowMenu("Novel")
            textbutton "Zurück":
                action ShowMenu("Menu_book")
screen Novel():
    tag tag_screen
    $ info_tx = IDNbook[index].tx
    frame:
        xfill True
        background  "gui/nvl.png"
        viewport:
            xpos 0.0 
            ypos 0
            ysize 4500
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vbox:       
                vbox:
                    xpos 360 ypos 0.0 xsize 1200 ysize 1500 
                    text "[info_tx]" 
                    textbutton "Zurück":
                        action ShowMenu("Menu_book_more")                

screen player1_Shop:
    tag tag_screen
    frame:
        viewport:
            xalign 0.0 
            ypos 0
            ysize 200
            xsize 400
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vbox:
                text "Index"
                for i in IDNitem:
                    $ list_position = IDNitem.index(i)
                    if i.buy == True:
                            textbutton "[i.Gname]":
                                action SetVariable("index",list_position),ShowMenu("buying"), 
                textbutton "Zurück":
                    action ShowMenu("openmenu")

screen buying:
    $ item_cost = IDNitem[index].cr
    $ item_name = IDNitem[index].Gname
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "Name: [item_name]"
            text "Kosten: [item_cost]"
            textbutton "Kaufen":
                action Call("Kaufenscreen")
            textbutton "Zurück":
                action Return(i)
    
label Kaufenscreen:
    scene shoppingroom
    python:
        anzahl1 = renpy.input("Wie viel möchten sie kaufen?",allow="0123456789") or 1
        
        gesamtsumme = int(anzahl1)*int(IDNitem[index].cr)

    "Es kostet [gesamtsumme]"

menu Mkau:
    "Möchten sie es Kaufen"
    "Ja":
        if gesamtsumme<Portmonaie_credits:
            $ IDNitem[index].anzahl=int(anzahl1)+IDNitem[index].anzahl
            if G001.anzahl>0:
                $ about_ach5.locked=False 
        else:
            $ Fehlende_credits = gesamtsumme - Portmonaie_credits
            "Kauf Konnte nicht abgeschlossen werden. Es fehlen [Fehlende_credits]"
            $ Fehlende_credits = 0
    "Nein":
        "Okay, Kauf abgebrochen"

return()