from juego_adivinanza import generar_numero, juego_adivinanza

if __name__ == "__main__":
    tries =0
    num_azar = generar_numero()
    while True:
      try:
        num_guess= int(input("Ingrese un valor(1-100):"))
      except ValueError:
        continue
      if num_guess == num_azar:
          
          break
          
      
      juego_adivinanza(num_azar,num_guess)
      tries +=1
      
    print(f"Felicidades, adivinaste el numero {num_guess} en {tries} intentos")   