from machine import I2C
import LSM6DSO
import time
import bluetooth
import ble_sensor
import struct

def demo():
    i2c = I2C(1)	# On utilise l'I2C n°1 de la carte NUCLEO-W55 pour communiquer avec le capteur
    intertial_sensor = LSM6DSO.LSM6DSO(i2c)	# le nom du capteur

    ble = bluetooth.BLE()
    ble_device = ble_sensor.BLESensor(ble)

    while True:
        timestamp = time.time()

# Première lecture des capteurs
        gx=intertial_sensor.gx()	# résultat en rad/s
        gy=intertial_sensor.gy()
        gz=intertial_sensor.gz()
        ax=intertial_sensor.ax() - 45	# résultat en mg (g intensité de la pesenteur)
        ay=intertial_sensor.ay() + 9
        az=intertial_sensor.az()-1008


    # Attente
        time.sleep_ms(1000)


        #ble_device.set_data_accelerometer(timestamp, gx, gy, gz, notify=1)
        #ble_device.set_data_gyroscope(timestamp, ax, ay, az, notify=1)
        ble_device.set_data_mixte(timestamp, ax, ay, az, gx, gy, gz, notify=1)

demo()
