#este es el sistema de puntos para las citas
#no supe como aplicarlo a la historia central 


init:
    #define mujer = Character ("Marina", color="#d42845") #ff7f07 5e178d
    define marron = Character ("Matilde")
    define rojo = Character ("Ema")
    define violeta = Character ("Violeta")



    $marr_points = 0 #puntos de matilde
    $rojo_points = 0 #puntos de ema
    $viol_points = 0 #puntos de violeta


label citas_p:

    scene aula_vacia


    show pelo_marron2

    show pelo_rojo2 at right

    show pelo_violeta2 at left
    with dissolve

marron "bienvenido al club de lectura, antes de que entres te tenemos que hacer un par de praguntas"

rojo "¿que genero te gusta leer?"

menu:
    "Slice of life":
        $marr_points +=1

    "Shonen":
        $rojo_points +=1
    
    "Gore":
        $viol_points +=1

if viol_points >=1:
    violeta "me caes bien"

elif rojo_points >=1:
    rojo "sos de los mios"

elif marr_points >=1:
    marron "a mi igual"


return