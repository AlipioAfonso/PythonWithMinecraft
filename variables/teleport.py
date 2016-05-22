from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x = 280
y = 64
z = 174

time.sleep(1)

mc.player.setTilePos(x, y, z)

x *= 2
z *= -1

time.sleep(1)

mc.player.setTilePos(x, y, z)

x *= 2
z *= -1

time.sleep(1)

mc.player.setTilePos(x, y, z)
