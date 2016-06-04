import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

executing = True

while(executing):
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z

    highestBlockY = mc.getHeight(x, z)
    if(y >= highestBlockY):
        mc.postToChat(str(highestBlockY))
        mc.postToChat("Voce esta no topo, weeeee")
    else:
        mc.postToChat("Voce esta aonde, vei?  :(")
        mc.postToChat(str(highestBlockY))
    time.sleep(2)
