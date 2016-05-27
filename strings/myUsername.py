from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username = input("What's your username?")
message = input("Say something to world:")
mc.postToChat(username + ": " + message)

