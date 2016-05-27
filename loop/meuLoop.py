from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time




pos = mc.player.getTilePos()
while(pos.x >= 0):
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.postToChat("Sua posicao e: x: "+str(x)+", y: " + str(y)+", z: " + str(z))
    time.sleep(1)
