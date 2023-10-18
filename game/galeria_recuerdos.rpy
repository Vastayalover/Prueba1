#galeria de replays 

#galeria base

#define config.enter_replay_transition = Dissolve #transicion entrada

#define config.exit_replay_transition = fade #tramsicion salida



screen replay_g:
    

    tag menu

    #add "tren_vacio_tarde.png" #aca no se porque no funciona el fondo

    frame:

        add "aula_vacia.jpg" #aca si funciona el fondo

        textbutton "volver" action Return() xalign 0.5 yalign 1.0 #boton para voler al main menu

        imagebutton: #boton good ending marina
            align(0.2, 0.2)
            hover "good_ending_marina_mini.png" 
            idle "corazon_idle.png" 
            insensitive"img_bloqueada.jpg"
            action Replay("campeon_lanus")
        
        imagebutton: #boton bad ending marina
            align(0.8, 0.2)
            hover "bad_ending_marina_mini.png" 
            idle "corazon_idle.png" 
            insensitive"img_bloqueada.jpg"
            action Replay("mufa_lanus")

        imagebutton: #boton good ending miguelin
            align(0.2, 0.9)
            hover "good_ending_miguelin_mini.png" 
            idle "corazon_idle.png" 
            insensitive"img_bloqueada.jpg"
            action Replay("campeon_velez")
        
        imagebutton: #boton bad ending miguelin
            align(0.8, 0.9)
            hover "bad_ending_miguelin_mini.png" 
            idle "corazon_idle.png" 
            insensitive"img_bloqueada.jpg"
            action Replay("mufa_velez")

        



    #textbutton "ver recuerdo 01" align(0.5, 0.5) action Replay("campeon_lanus")
    #textbutton "ver recuerdo 02" align(0.5, 0.6) action Replay("mufa_lanus")
    #textbutton "ver recuerdo 03" align(0.5, 0.7) action Replay("campeon_velez")
    #textbutton "ver recuerdo 04" align(0.5, 0.8) action Replay("mufa_velez")
    
    
    #imagebutton: "good_ending_marina_mini.png" insensitive"img_bloqueada.jpg" align(0.3, 0.2) action Replay("campeon_lanus")
    #imagebutton auto"bad_ending_marina_mini.png" insensitive"img_bloqueada.jpg" align(0.6, 0.2) action Replay("mufa_lanus")
    #imagebutton auto"good_ending_miguelin_mini.png" insensitive"img_bloqueada.jpg" align(0.3, 0.9) action Replay("campeon_velez")
    #imagebutton auto"bad_ending_miguelin_mini.png" insensitive"img_bloqueada.jpg" align(0.6, 0.9) action Replay("mufa_velez")