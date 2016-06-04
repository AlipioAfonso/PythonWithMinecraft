import time
import math
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

executing = True

while(executing):
    pos = mc.player.getTilePos()
    x = pos.x
    z = pos.z

    homeX = -400
    homeZ = 150

    distanceZ = homeZ - z
    distanceX = homeX - x
    
    distance = math.sqrt((distanceX**2) + (distanceZ**2))

    mc.postToChat(str(distance))
    
    time.sleep(0.1)
