from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z


try:
    blockType = int(input("Que bloco quer colocar?"))
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("Voce nao digitou um numero! Digite um numero da proxima vez!")



