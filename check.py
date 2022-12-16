import time
import json
import pyscreenshot

print("Tester bot")
print("Tra 4 secondi inizia l'analisi")


time.sleep(4)





with open("coord.json","r") as f:
    data = json.load(f)




x1 = 690
x2 = 750


pic = pyscreenshot.grab(bbox=(x1, int(data["x"]), x2, int(data["y"])))
pic.show()
pic.save("base.png")