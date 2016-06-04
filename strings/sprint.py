import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

tick = True
while(tick):
    
    time.sleep(2)
    
    pos = mc.player.getTilePos()
    x1 = pos.x
    y1 = pos.y
    z1 = pos.z

    time.sleep(4)

    pos = mc.player.getTilePos()
    x2 = pos.x
    y2 = pos.y
    z2 = pos.z

    x = x2-x1
    y = y2-y1
    z = z2-z1

    mc.postToChat("O jogador se moveu x: "+str(x)+"  y: "+str(y)+"  z:"+str(z))
