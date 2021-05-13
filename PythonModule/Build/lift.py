from fotosfera import moveTo, getStatus, Up,Down,Stop

task = 'DOWN'

while True:
    if task=="UP":
        print("UP we go")
        Up()
    elif task=="DOWN":
        print("DOWN we go")
        Down()
    else:
        print("stop")
        Stop()
        break

                    
                    

                    