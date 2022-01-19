import requests
import threading

def consumir_servicio():
    res = requests.get('https://www.google.com/')
    if res.status_code == 200:
        print('Resultado ok')


if __name__ == '__main__': 
    for x in range(0,50):
        print(x)
        threading.Thread(target=consumir_servicio).start()
