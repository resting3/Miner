import json






print("Benvenuto nella Console delle impostazioni")
print("Scrivi help per avere tutti i comandi")
while True:
    command = input("> ")
    if command == "help":
        print("coord {x} {y} (Questo comando serve per inserire le coordinate della singola cella)")
    elif "coord" in command:
        a,x,y = command.split()
        print(x)
        print(y)    
        with open("coord.json","w") as f:
            dict = {
                "x":x,
                "y":y
            }
            json.dump(dict,f,indent=4)




        

