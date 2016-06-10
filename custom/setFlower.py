import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


flower = True

while(flower):
    pos = mc.player.getTilePos()

    x = pos.x
    y = pos.y
    z = pos.z
    
    blockType = 37

    downBlock = mc.getBlock(x, y-1, z)

    if(downBlock == 3 or downBlock == 2):
        mc.setBlock(x, y, z, blockType)

    time.sleep(0.5)
