from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while(True):
    pos = mc.player.getTilePos()

    x = pos.x
    y = pos.y
    z = pos.z

    buildX = -269
    buildY = 64
    buildZ = 189

    width = 10
    height = 5
    length = 6

    inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length

    if(inside):
        mc.postToChat("Voce esta dentro de casa")
    else:
        mc.postToChat("Voce esta fora de casa")
    time.sleep(0.5)
