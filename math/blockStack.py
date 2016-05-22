from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = 188
y = 64 
z = -119

blockType = 103

mc.setBlock(x, y, z, blockType)
