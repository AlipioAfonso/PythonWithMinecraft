from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = 188
y = 100 
z = -119

blockType = 1

while(z<=-96):
    mc.setBlock(x, y, z, blockType)
    blockType+=1
    x+=1
    z+=1
    y-=1
