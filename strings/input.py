from mcpi.minecraft import Minecraft
mc = Minecraft.create()

name = input("What's your name?")
mc.postToChat(name)
