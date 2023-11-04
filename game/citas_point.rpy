#este es el sistema de puntos para las citas
#no supe como aplicarlo a la historia central 


init:
    #define mujer = Character ("Marina", color="#d42845") #ff7f07 5e178d
    define marron = Character ("Mati", color = "#ffaf0f")
    define rojo = Character ("Ema", color = "#d42845")
    define violeta = Character ("Violeta", color = "#930fff")



    $marr_points = 0 #puntos de matilde
    $rojo_points = 0 #puntos de ema
    $viol_points = 0 #puntos de violeta


    screen puntos_marr:
        frame xpos 500 ypos 0:
            text "Mati: [marr_points] <3" xalign 0.1 yalign 0.1

screen puntos_rojo:
    frame xpos 800 ypos 0:
        text "Ema [rojo_points] <3" xalign 0.1 yalign 0.1

screen puntos_viol:
    frame xpos 70 ypos 0:
        text "Violeta:[viol_points] <3" xalign 0.1 yalign 0.1



label citas_p:

    scene aula_vacia


    show pelo_marron2

    show pelo_rojo2 at right

    show pelo_violeta2 at left
    with dissolve

marron "bienvenido al club de lectura, antes de que entres te tenemos que hacer un par de praguntas"

show screen puntos_marr
show screen puntos_rojo
show screen puntos_viol
with dissolve

rojo "¿que genero te gusta leer?"

menu:
    "Slice of life":
        $marr_points +=1
        

    "Shonen":
        $rojo_points +=1
    
    "Gore":
        $viol_points +=1

    "Moe":
        $marr_points -=2
        $rojo_points -=2
        $viol_points -=2


if viol_points >=1:
    violeta "me caes bien"

elif rojo_points >=1:
    rojo "sos de los mios"

elif marr_points >=1:
    marron "a mi igual"

elif viol_points & rojo_points & marr_points <=0:
    violeta "agh"
    rojo "aich"
    marron "uhm"


violeta "ademas de leer que mas sueles hacer?"

$torta_ele=False
$bateria_ele=False
$cos_ele=False


menu: 
    "me gusta hacer tortas":
        $marr_points +=1
        $torta_ele=True
        marron "sameeeee"

    "toco la bateria":
        $rojo_points +=1
        $bateria_ele=True
        rojo "oh genial"
    
    "hacer cosplay":
        $viol_points +=1
        $cos_ele=True
        violeta "jeje"

    "jugar genshin impact":
        jump baneado

marron "cual es tu pokemon favorito?"

menu:
    "Dedenne":
        $marr_points +=1

    "Arcanine":
        $rojo_points +=1
    
    "Mismagius":
        $viol_points +=1

    "Gardevoir":
        $marr_points -=2
        $rojo_points -=2
        $viol_points -=2




violeta "por ultimo, la mas importante"
violeta "cual es tu signo?"

menu: 
    "Libra":
        $marr_points +=1
        marron "somos compatibles :D"

    "Capricornio":
        $rojo_points +=1
        rojo "nostros siempre re facha"

    "Geminis":
        $viol_points +=1
        violeta "nos vamos a llevar bien"

    "no me jodas":
        $marr_points -=2
        $rojo_points -=2
        $viol_points -=2
        marron ":c"

marron "bueno eso fue todo"

if marr_points >=2:
    marron "estas aceptado, puedes sentarte al lado mio"
    if torta_ele == True:
        marron "y hacemos tortas juntos"

elif rojo_points >=2:
    rojo "bien, estas dentro, veni conmigo"
    if bateria_ele == True:
        rojo "a la salida acompañame que nececitamos un batero"

elif viol_points >=2:
    violeta "podes quedarte, solo si te sentas conmigo"
    if cos_ele == True:
        violeta "despues vamos a mi casa y hacemos un cospla juntos"

elif marr_points & rojo_points & viol_points <=0 :
    marron "tal vez deberias irte"
    rojo "raja de aca virgo"

if marr_points ==4:
    marron "sos muy tierno ¿podemos salir juntos?"

if rojo_points ==4:
    rojo "y sos muy capo seamos novios"

if viol_points ==4:
    violeta "y ahora sos mi novio"

return

label baneado:

violeta "no capo raja de aca, enfermo de mierda"

return