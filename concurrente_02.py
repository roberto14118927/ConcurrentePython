# from de_donde  import que_estas_importando
import time
import threading

def primer_metodo():
    time.sleep(5)
    resultado = 3 + 10
    print('Total suma uno: ',resultado)

def segundo_metodo():
    time.sleep(3)
    resultado = 3 + 11
    print('Total suma dos: ',resultado)

def tercer_metodo():
    time.sleep(3)
    resultado = 3 + 12
    print('Total suma tres: ',resultado)

# primer_metodo()
# segundo_metodo()
# tercer_metodo()

threading.Thread(target=primer_metodo).start()
threading.Thread(target=segundo_metodo).start()
threading.Thread(target=tercer_metodo).start()
