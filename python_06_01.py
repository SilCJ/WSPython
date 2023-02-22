age = input ("Captura tu edad")
height= input("Captura tu estatura")
age = int(age)
height = float(height)

year = 2009
height_permitted = 1.62

if age >= year and height >= height_permitted:
    print ("Puedes ingresar a la montaña rusa Push-Pull")
elif age < year and height >= height_permitted:
    print ("No puede ingresar a Push-Pull por que eres menor a 14 años")
elif height < height_permitted:
    print ("No puede ingresar a Push-Pull por que mides menos de 1.62")