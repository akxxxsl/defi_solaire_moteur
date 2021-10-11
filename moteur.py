# Période : 20 ms
# Fréquence : 50 Hz
# Rapport cyclique : 1/10
# Pin 5 : D1

from machine import Pin,PWM 
import time

freq = 50
# De 52 à 105 pour faire varier entre 1 et 2ms
duty = 80

moteur=PWM(Pin(5))

def start(freq, duty):
  # Démarrage à vitesse initiale
  moteur.freq(freq)
  moteur.duty(duty)
  
def stop():
  # Arrêt des moteurs
  moteur.freq(0)
  moteur.duty(0)

def main():
  # Démarrage des moteurs
  start(freq, duty)
  # On fait tourner les moteurs pendant 2 sec
  #time.sleep(2)
  # On arrête tout
  #stop()

if __name__ == "__main__":
  main()
