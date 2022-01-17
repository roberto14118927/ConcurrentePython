import time
import multiprocessing


# proceso hijo
def primer_proceso(data = 10):
    print("Iniciamos el proceso")
    time.sleep(data)
    print("Fin de proceso")

# Proceso principal
def main():

    proceso = multiprocessing.Process(target=primer_proceso, name='', args=(1,), daemon=False)
    proceso.start()
    proceso.join()

    print("Fin proceso principal")

if __name__ == '__main__':
    main()


