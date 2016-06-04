import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

executing = True

while(executing):
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z

    blockType = mc.getBlock(x, y, z)
    
    if(blockType == 8 or blockType == 9):
        mc.postToChat("Voce esta nadando, weeeee")
    else:
        mc.postToChat("Voce nao esta nadando  :(")
    time.sleep(2)
