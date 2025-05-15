import random

def generar_numero():
   num_azar = random.randint(1,100)
   return num_azar


tries = 0
def juego_adivinanza(num_guess,num_azar):
  
  if num_guess > num_azar:
        print("El numero es mayor, vuelva a intentarlo")
        return 1
  elif num_guess < num_azar:
        print("El numero es menor, vuelva a intentarlo")
        return -1
  elif num_guess == num_azar:
        return 0

             
         
    



    