def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    while True:
        print("\n--- Menu de Conversion de Température ---")
        print("1. Convertir une température de Celsius en Fahrenheit")
        print("2. Convertir une température de Fahrenheit en Celsius")
        print("3. Quitter le programme")
        
        choix = input("Entrez votre choix (1, 2 ou 3) : ")
        
        if choix == '1':
            try:
                temp_c = float(input("Entrez la température en Celsius : "))
                resultat = celsius_to_fahrenheit(temp_c)
                print(f"{temp_c}°C est égal à {resultat:.2f}°F")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")
                
        elif choix == '2':
            try:
                temp_f = float(input("Entrez la température en Fahrenheit : "))
                resultat = fahrenheit_to_celsius(temp_f)
                print(f"{temp_f}°F est égal à {resultat:.2f}°C")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")
                
        elif choix == '3':
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break
            
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    menu()



