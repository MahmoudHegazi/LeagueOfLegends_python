
class zed:
    attack = 98
    defence = 10
    slow = 20
    health = 850
    mobilty = 90
    Damge = round(attack + defence + slow + mobilty / 400 * 100)	
    status = "attak" + str(attack) + "\n"
    "defence" + str(defence) + "%" + "\n"
    "Slow"  + str(slow) + "%" + "\n"
    "mobilty" + str(mobilty) + "%" + "\n"
    "Final_Damge : " + str(Damge)
    player_KDA = 100


class lux:
        
    attack = 100
    defence = 30
    health = 1000
    slow = 70
    mobilty = 10
    Damge = round(attack + defence + slow + mobilty / 400 * 100)	
    status = "attak" + str(attack) + "\n"
    "defence" + str(defence) + "%" + "\n"
    "Slow"  + str(slow) + "%" + "\n"
    "mobilty" + str(mobilty) + "%" + "\n"
    "Final_Damge : " + str(Damge)
    player_KDA = 12
Lux = lux()
Zed = zed()

def fight():           
    	
    print("Lux KDA : " + str(Lux.player_KDA))
    print("Zed KDA : " + str(Zed.player_KDA))
    print("Zed VS Lux")
    print("LUX Damge : " + str(Lux.Damge))
    print("Zed Damge : " + str(Zed.Damge))
    Zed.Damge = round(98 + 10 + 20 + 90 + 100 / 230 * 100)
    Lux.Damge = round(100 + 30 + 70 + 10 + 12 / 230 * 100)
    hit_zed = Zed.Damge - Lux.defence
    hit_lux = Lux.Damge - zed.defence
    collect_zed = 0
    collect_lux = 0
    collectZ = 0
    collectL = 0
	

    for side in range(100):
	    if collect_zed > Zed.health:
		    print("Zed Has Been Dead :")
		    print("Lux Says: Easy")
		    return "Last Damge From Lux  " + str(Zed.health)
	    elif collect_lux > Lux.health:
		    print("Lux Has Been Dead :")
		    print("Zed Says: Enrease The Shadows")
		    return "Last Damge From Lux" + str(collectZ)
	    else:

		    collectZ = Zed.health - hit_lux
		    collect_zed += collectZ
		    print("Zed Has Damged Lux By : " + str(hit_zed))
		    print("Lux Health = " + str(collectL))			
		    collectL = Lux.health - hit_zed
		    collect_lux += collectL
		    print("Lux Has Damged Zed By : " + str(hit_lux))
		    print("Zed Health = " + str(collectZ))
fight()		
