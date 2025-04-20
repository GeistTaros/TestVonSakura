#definitionen
define player1_screen_close="player1_screen_close"
define player1_screen_open="player1_screen_open"
define player1_items="player1_items"

define G000S="G000S"
define G000B="G000B"

define G001S="G001S"
define G001B="G001B"

define G002S="G002S"
define G002B="G002B"

define G003S="G003S"
define G003B="G003B"

define G004S="G004S"
define G004B="G004B"

define G005S="G005S"
define G005B="G005B"

define G006S="G006S"
define G006B="G006B"

define G007S="G007S"
define G007B="G007B"

define G008S="G008S"
define G008B="G008B"

define G009S="G009S"
define G009B="G009B"

define G010S="G010S"
define G010B="G010B"

define G011S="G011S"
define G011B="G011B"

define G012S="G012S"
define G012B="G012B"

#menü offen
screen player1_screen_open():
    tag tag_screen
    frame:
        xalign 0 ypos 0
        vbox:
            text "Spielername: [name1]"
            text "Geburtstag: [bday].[bmonth].[byear]"
            text "Punktestand [Happyending]"
            textbutton "Gegenstände":
                action ShowMenu(player1_items)
            textbutton "Exit":
                action Return(True) 
#menü geschlossen
screen player1_screen_close():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            textbutton "Mehr":
                action ShowMenu(player1_screen_open)

#item menü
screen player1_items():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            if G000.Erhalten :
                textbutton "[G000.Gname]":
                    action ShowMenu(G000S)
            if G001.Erhalten :
                textbutton "[G001.Gname]":
                    action ShowMenu(G001S)
            if G002.Erhalten :
                textbutton "[G002.Gname]":
                    action ShowMenu(G002S)
            if G003.Erhalten :
                textbutton "[G003.Gname]":
                    action ShowMenu(G003S)
            if G004.Erhalten :
                textbutton "[G004.Gname]":
                    action ShowMenu(G004S)
            if G005.Erhalten :
                textbutton "[G005.Gname]":
                    action ShowMenu(G005S)
            if G006.Erhalten :
                textbutton "[G006.Gname]":
                    action ShowMenu(G006S)
#            if G007.Erhalten :
#                textbutton "[G007.Gname]":
#                    action ShowMenu(G007S)
#            if G008.Erhalten :
#                textbutton "[G008.Gname]":
#                    action ShowMenu(G008S)
#            if G009.Erhalten :
#                textbutton "[G009.Gname]":
#                    action ShowMenu(G009S)
#            if G010.Erhalten :
#                textbutton "[G010.Gname]":
#                    action ShowMenu(G010S)
#            if G011.Erhalten :
#                textbutton "[G011.Gname]":
#                    action ShowMenu(G011S)
#            if G012.Erhalten :
#                textbutton "[G012.Gname]":
#                    action ShowMenu(G012S)
#            if G000.Erhalten or G001.Erhalten or G002.Erhalten or G003.Erhalten or G004.Erhalten or G005.Erhalten or G006.Erhalten or G007.erhalten or G008.Erhalten or G009.Erhalten or G010.Erhalten or G011.Erhalten or G012.Erhalten :
            if G000.Erhalten or G001.Erhalten or G002.Erhalten or G003.Erhalten or G004.Erhalten or G005.Erhalten:
                textbutton "Zurück":
                    action ShowMenu(player1_screen_open)  

#Testscreenitem
screen G000S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G000.ID]"
            text "Name:[G000.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G000B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G000B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G000.tx] "
            textbutton "Zurück":
                action ShowMenu(G000S)
#screen für G001 
screen G001S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G001.ID]"
            text "Name:[G001.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G001B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G001B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G001.tx]"
            textbutton "Zurück":
                action ShowMenu(G001S)
#G002
screen G002S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G002.ID]"
            text "Name:[G002.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G002B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G002B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G002.tx]"
            textbutton "Zurück":
                action ShowMenu(G002S)
#G003
screen G003S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G003.ID]"
            text "Name:[G003.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G003B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G003B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G003.tx]"
            textbutton "Zurück":
                action ShowMenu(G003S)
#G004
screen G004S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G004.ID]"
            text "Name:[G004.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G004B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G004B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G004.tx]"
            textbutton "Zurück":
                action ShowMenu(G004S)
#G005
screen G005S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G005.ID]"
            text "Name:[G005.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G005B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G005B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G005.tx]"
            textbutton "Zurück":
                action ShowMenu(G005S)
#G006
screen G006S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G006.ID]"
            text "Name:[G006.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G006B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G006B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G006.tx]"
            textbutton "Zurück":
                action ShowMenu(G006S)
#G007
screen G007S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G007.ID]"
            text "Name:[G007.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G007B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G007B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G007.tx]"
            textbutton "Zurück":
                action ShowMenu(G007S)
#G008
screen G008S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G008.ID]"
            text "Name:[G008.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G008B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G008B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G008.tx]"
            textbutton "Zurück":
                action ShowMenu(G008S)
#G009
screen G009S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G009.ID]"
            text "Name:[G009.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G009B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G009B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G009.tx]"
            textbutton "Zurück":
                action ShowMenu(G009S)
#G010
screen G010S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G010.ID]"
            text "Name:[G010.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G010B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G010B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G010.tx]"
            textbutton "Zurück":
                action ShowMenu(G010S)
#G011
screen G011S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G011.ID]"
            text "Name:[G011.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G011B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G011B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G011.tx]"
            textbutton "Zurück":
                action ShowMenu(G011S)
#G012
screen G012S():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "ID: [G012.ID]"
            text "Name:[G012.Gname]" 
            textbutton "Bezeichnung":
                action ShowMenu(G012B)
            textbutton "Zurück":
                action ShowMenu(player1_items)                
screen G012B():
    tag tag_screen
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "[G012.tx]"
            textbutton "Zurück":
                action ShowMenu(G012S)





