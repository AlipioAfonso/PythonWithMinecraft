from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

x=x+1
y=y+1
z=z+1

height=10
width=5
length=3


blockType=1

mc.setBlocks(x, y, z, x+width, y+height, z+length, blockType)



mc.setBlocks(x, y+height, z, x, y+height+2, z, blockType)

mc.setBlocks(x, y+height, z+length, x, y+height+2, z+length, blockType)

mc.setBlocks(x+width, y+height, z, x+width, y+height+2, z, blockType)

mc.setBlocks(x+width, y+height, z+length, x+width, y+height+2, z+length, blockType)
