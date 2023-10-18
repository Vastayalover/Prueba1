
#codigo de la galeria

#la galeria se define con la letra g

init python: #comando para usar python puro 
    
    g = Gallery()
    
    

    g.button("end1")
    g.condition("persistent.end1")
    g.image("good_ending_marina.jpg")
    
    g.button("end2")
    g.condition("persistent.end2")
    g.image("bad_ending_marina.jpg")

    g.button("end3")
    g.condition("persistent.end3")
    g.image("good_ending_miguelin.jpg")

    g.button("end4")
    g.condition("persistent.end4")
    g.image("bad_ending_miguelin.png")

    
    
##### esta seccion es el menu galeria
screen CG_imagenes:

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "tren_vacio_tarde.png"
    
    textbutton "Return" action Return() xalign 0.5 yalign 1.0

    # esta parte controla la cantidad de elementos en columnas y los separara automaticamente
    grid 2 2: 
        

        xfill True
        yfill True

        add g.make_button("end1","good_ending_marina_mini.png", locked = "img_bloqueada.jpg", xalign=0.5, yalign=0.5)
        add g.make_button("end2", "bad_ending_marina_mini.png", locked = "img_bloqueada.jpg", xalign=0.5, yalign=0.5)       
        
        add g.make_button("end3", "good_ending_miguelin_mini.png", locked = "img_bloqueada.jpg", xalign=0.5, yalign=0.5)
        add g.make_button("end4", "bad_ending_miguelin_mini.png", locked = "img_bloqueada.jpg", xalign=0.5, yalign=0.5)