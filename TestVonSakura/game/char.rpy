# Character Sakura (Sakura schreien, Sakura flüstern, Sakura normal) Sak1
define sa = Character(
    "Sakura",
    image="sakura",
    who_color="#e20dd8",
    what_color="#ffffffbb")
define sa1 = Character(
    kind=sa,
    what_color="#fc0000ff",
    what_size= 120,
    what_bold=True,
    what_textalign= 0.5,
    what_xalign= 0.5,)
define sa2 = Character(
    kind=sa,
    what_italic=True,
    what_size=20)


# Charakter Akane (Akane normal)
define ak = Character(
    "Akane", 
    image="akane",
    who_color= "#260c52",
    what_color= "#ffffffff")
# Charakter Marta (Marta normal)
define ma = Character(
    "Marta",
    image="marta",
    who_color= "#2f6e4f", 
    what_color= "#ffffffff")
# Charakter Hana
define Hana = Character(
    "Hana",
    image="hana",
    who_color= "#ff0000",
    what_color= "#ffffff")
#Erzähler (? )
define narrator = Character(
    None, 
    what_italic=True,
    what_xalign=0.5,
    what_yaligh=0.0,
    what_textalign=0.5,)
define Park_narrator = Character(
    None,
    what_italic=True,
    what_xalign=0.5,
    what_yaligh=0.0,
    what_textalign=0.5,)
define warning = Character(
    kind= narrator,
    what_color= "#ff0000ff",
    what_italic=True,)
define sys = Character(
    None, 
    window_background= None,
    who_color= "#ffffff",
    what_color = "#ffffff" ,
    what_xalign=0.5,
    what_yaligh=0.0,
    what_textalign=0.5,
    )
define shop = Character(
    "Ladenmitarbeiter",
    kind=narrator,
    )


