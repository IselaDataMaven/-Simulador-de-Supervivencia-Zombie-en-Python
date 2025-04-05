import random
import time

#Calles del mapa (True = infestada de zombies, False = segura)
calles ={ 

"Calle 1":random.choice([True, False]),
"Calle 2":random.choice([True, False]),
"Calle 3":random.choice([True, False]),
"Calle 4":random.choice([True, False])
}

#Lista de suministros

suministros = ["Agua", "Comida", "Botiquín", "Linterna"]
mochila = []

def busca_ruta():
    print("Buscando una ruta segura...")
    time.sleep(1)
    ruta_segura = [calle for calle, infestada in calles.items() if not infestada]

    if not ruta_segura: 
        print("¡No hay rutas seguras! Debes arriesgarte...")
        return list(calles.keys())[0]  #Elegimos una aleatoria
    else:
        print(f"Ruta segura encontrada: {ruta_segura[0]}")
        return ruta_segura[0]
    

def recoger_suministros():
    print("Buscando suministros...")
    time.sleep(1)
    encontrado = random.choice(suministros)
    mochila.append(encontrado)
    print(f"Has encontrado: {encontrado}")


def llegar_refugio():
    print("Corriendo al refugio...")
    time.sleep(2)
    print("¡Has llegado al refugio sano y salvo!")

#"Secuencia del juego"
ruta =  busca_ruta()
print(f"Tomando {ruta}...")

if calles[ruta]: #Si la calle está infestada
    print("¡Cuidado! Hay zombies en esta calle. ¡Corre!")
else:
    print("La calle está despejada.")

recoger_suministros()
llegar_refugio()

#Mostrar los suministros recolectados
print("\nResumen de tu aventura:")
print(f"Ruta tomada: {ruta}")
print(f"Suministreos recolectados: {mochila}")
