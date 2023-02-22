month = input ("Captura tu mes de nacimiento del 1 al 12 ")
day = input("Captura tu día de nacimiento")
year = input("Captura tu año de nacimiento a 4 dígitos")
month = int(month)
day = int(day)
year = int(year)

month_a = 2
year_a = 2023
day_a = 21
generation_silence = 1939
generation_babyboomers = 1959
generation_x = 1979
generation_y = 1989
generation_z = 2023

age_a = year_a - year

if month <= month_a and day <= day_a:
    print (f"Ya cumpliste  {age_a} años ")
elif month > month_a or day > day_a:
    print (f"Aún no cumples {age_a} años")

if year <= generation_silence and year >= 1920:
    print ("Eres generación silenciosa")
elif year <= generation_babyboomers and year >= 1940:
    print ("Eres generación baby boomers")
elif year <= generation_x and year >= 1960:
    print ("Eres generación X")
elif year <= generation_y and year >= 1980:
    print("Eres generación y o millennials")
elif year <= generation_z and year >= 1990:
    print ("Eres generación z")