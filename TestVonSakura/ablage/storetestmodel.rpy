init python:
    class Gegenstand:
        def __init__(Gegst, Gname, ID,Erhalten=False, tx="Keine Info vorhanden",Pckt=True,Book=False,):
            super(Gegenstand, Gegst).__init__()
            Gegst.Gname = Gname
            Gegst.ID = ID
            Gegst.Erhalten = Erhalten
            Gegst.Pckt = Pckt
            Gegst.Book = Book
            Gegst.tx = tx
        def __str__(Gegst):
            return Gegst.Gname + Gegst.ID + Gegst.tx 

    
define G000 = Gegenstand("Test", "000", True,)
define G001 = Gegenstand("Regenschirm", "001",False, "Ein Schirm, der vor Regen und Sonne schützt")
define G002 = Gegenstand("Messer", "002",False, "Frauen mit Messer sind meistens Gefährlich" )
define G003 = Gegenstand("Wunderkerzen", "003",False, "Leuchtet schön in der Nacht")
define G004 = Gegenstand("Getränkedose", "004",False, "`Verleiht Fittiche` steht auf der Dose")
define G005 = Gegenstand("Schreibstift", "005",False, "Um eine Nachricht zu hinterlassen")
define G006 = Gegenstand("Leeres Papier", "006",False,False,True, "Ideal zum Beschriften")



init python:
    class Tasche(Gegenstand):
        def __init__(self, Gname="Noname", ID="Keine ID vorhanden",Erhalten=False, tx="Keine Info vorhanden"):
            super(Tasche, self,).__init__(Gegenstand, ID)
            self.Gname = Gname
            self.ID = ID
            self.Erhalten = Erhalten
            self.tx = tx
        def __str__(self):
            return self.Gname + self.ID + self.Erhalten + self.tx
  
define P000 = Tasche("Handtasche", "P0", "test", "Wie viel in so eine Tasche passen kann. Fazinierend" )        


define P001 = Tasche("Portmonaie", "P1","test","Ein Portmonee voller Geld und Karten" )

define P002 = Tasche("Verband", "002", "test", "Für eine Schnelle Verartztung" )

init python:
    class Buch:
        def __init__(self, Gname, ID,Erhalten=False, tx="Keine Info vorhanden"):
            super(Buch, self).__init__()
            self.Gname = Gname
            self.ID = ID
            self.Erhalten = Erhalten
            self.tx = tx
        def __str__(self):
            return self.Gname + self.ID + self.Erhalten + self.tx

define B001 = Buch("Handbuch", "B1",False, "Ein Handbuch zum lesen")
define B002 = Buch("Brief", "B2",False, "Ein Brief. Von Wem könnte er nur Stammen?" )
define B003 = Buch("Beschriebenes Papier", "B3",False, "Nicht entzifferbare Buchstaben stehen auf den Papier")