﻿define mujer = Character ("Marina", color="#d42845")
define hombre = Character ("Miguelin",color="#3343AA")
define jugador = Character ("Bautista",color="4E4C4E")


        #PUTO EL QUE LEA

        #TU VIEJA ES PUTA
        
        #xdxdxdxd lol

        #los del turno tarde se la comen
        
        #son re giles loco


label start:       

#Primera escena

scene tren_fuera_dia
 
show olimpia_escudo
 
"Te diriges de camino a la escuela en tren como todos los dias"
"..."
"preferirias no ir, el bullying por llamarte bautista esta presente todos los dias"
"..."
"aun asi vas, tal vez hoy sea un buen dia"

show miguelin3:

play music "la_cumbia.mp3" fadeout 5.0 fadein 5.0

hombre "quionda bautizardo"
jugador "todo bien pa?"
hombre "estoy re manija"
hombre "hoy juega veleeeeeeeez"
hombre "te pinta la previa con unos choris en mi casa? :D"


$ir_con_miguelin = True
menu: 
        "De una wacho":
                        call respuesta4
                        $ir_con_miguelin =True

        "Dejame que lo piense":
                                call respuesta5
                                $ir_con_miguelin = False

stop music
hide miguelin3 with dissolve
    
"que buen amigo que es :D"

        #cambia la escena al tren vacio
        
scene tren_vacio_dia

"al menos alcanze a tener un buen lugar"

        #cambia la escena a la entrada de la escuela
scene entrada_escuela

"parece que llege temprano esta vez"

#entra marina

mujer "Holiiiiii :3"
"??"
show marina2 with dissolve
"ah, solo es marina, dios,cada vez que la veo esta mas linda"  
mujer "queria preguntarte algo"
mujer "hoy en mi casa van a ver un partido ¿te gustaria venir conmigo?"

$ir_con_marina=True 

menu: 
        "bueno":
                $ir_con_marina=True 

        "dejame que lo piense":
                $ir_con_marina=False 

mujer "mmnm oki"
mujer "nos vemos mas tarde"
       
hide marina2
scene escuela_afuera_tarde

"al fin terminaron las clases"

show miguelin3 at right
show marina2 at left
with dissolve

"mierda"
hombre "vamos a casa mono?"

if ir_con_marina==True:
                hide marina2
                show marina_triste at left
                with dissolve
                mujer "dijiste que ibas a ir conmigo"
    
if ir_con_miguelin==True:
                hide miguelin3
                show miguelin_triste at right
                with dissolve
                hombre "a mi tambien me dijiste que venias"



"que hago?"

$ir_con=True #true es ir con marina y false miguelin

menu:
                
        "ir con marina":
                $ir_con=True
                

        "ir con miguelin":
                $ir_con=False
        

if ir_con==True:
        hide marina_triste
        show marina2 at left
        hide miguelin_triste
        hide miguelin3 
        show miguelin_llorando at right
        with dissolve
        hombre "puto"
        hide miguelin_llorando with dissolve
        mujer "vamonos"
        call run_marina

if ir_con==False:
        hide miguelin_triste
        show miguelin3 at right
        hide marina_triste
        hide marina2
        show marina_llorando at left
        with dissolve
        mujer "mogolico"
        hide marina_llorando with dissolve
        hombre "rajemos"
        call run_miguelin

return #return del label start                                


label respuesta4:  
        
        hombre "joya pa, te veo a la salida de la escuela"
return

label respuesta5:
        
        hombre "bueno gato pero no te ortives, a la salida confirmame"
return                               

label run_marina:
        #ruta de marina
        scene casa_marina
        show marina2 with dissolve
        mujer "bienvenido a mi casa :3"
        mujer "como pensas que vamos a salir hoy?"

        menu: 
                "seguro ganamos 3 a 0":
                        jump mufa_lanus 
        
                "con suerte empatamos":
                        jump campeon_lanus
return

label mufa_lanus:
        scene bad_ending_marina
        "sos un mufa hermano, marina no te quiere ver nunca mas,bad ending"
return

label campeon_lanus:
        scene good_ending_marina
        "no la mufaste, lanus salio campeon por penales y ahora ven todos los partidos juntos, good ending"
return

label run_miguelin:
        #ruta de miguelin
        scene casa_miguelin
        show miguelin3 with dissolve
        play music "la_cumbia.mp3" fadein 5.0
        hombre "bienvenido al rancho pa"
        hombre "como pensas que salios hoy?"

        menu:
                "seguro ganamos 3 a 0":
                        jump mufa_velez

                "con suerte empatamos":
                        jump campeon_velez
return

label mufa_velez:
        scene bad_ending_miguelin
        #basicamente un dissolve pero controlado
        show miguelin_llorando:
                parallel:
                        0.2 #tiempo de espera
                        xalign 0.5 yalign 0.0 #centrar imagen
                        ease 0.25 zoom 2.0 #animacion donde la imagen hace zoom
                parallel:
                        alpha 0 #opacidad 0
                        0.2 #tiempo de espera
                        linear 0.15 alpha 1.0 #comienza a mostrarce
                        1.0 #tiempo de espera
                        linear 0.10 alpha 0 #comienza a desaparecer


        "sos un mufa hermano, miguelin y sus 7 hermanos te cagaron a palo por salame,bad ending"
return

label campeon_velez:
        scene good_ending_miguelin
        "no la mufaste, velez salio campeon por penales y disfrutaste tremendo azado, good ending"
        
