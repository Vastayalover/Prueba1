define mujer = Character ("Marina", color="#d42845")
define hombre = Character ("Miguelin",color="#3343AA")
define jugador = Character ("Bautista",color="4E4C4E")


        #PUTO EL QUE LEA

        #TU VIEJA ES PUTA
        
        #xdxdxdxd lol

        #los del turno tarde se la comen


label start:

scene tren_fuera_dia
 
        "Te diriges de camino a la escuela en tren como todos los dias"
        "..."
        "preferirias no ir, el bullying por llamarte bautista esta presente todos los dias"
        "..."
        "aun asi vas, tal vez hoy sea un buen dia"

show miguelin3 
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
        show miguelin_llorando at right
        with dissolve
        hombre "puto"
        hide miguelin_llorando with dissolve
        mujer "vamonos"

if ir_con==False:
        hide miguelin_triste
        show miguelin3 at right
        hide marina_triste
        show marina_llorando at left
        with dissolve
        mujer "mogolico"
        hide marina_llorando with dissolve
        hombre "rajemos"

return #return del label start                                


label respuesta4:  
        
        hombre "joya pa, te veo a la salida de la escuela"
return

label respuesta5:
        
        hombre "bueno gato pero no te ortives, a la salida confirmame"
return                               



