cities_canada = input("Largest cities in Canada: ")
#Largest cities in Canada: ["Toronto", "Montreal", "Calgara", "Ottawa"]
print(cities_canada, type(cities_canada))
#["Toronto", "Montreal", "Calgara", "Ottawa"] <class 'str'>

cities_canada = eval(input("Largest cities in Canada: "))
#Largest cities in Canada: ["Toronto", "Montreal", "Calgara", "Ottawa"]
print(cities_canada, type(cities_canada))
#['Toronto', 'Montreal', 'Calgara', 'Ottawa'] <class 'list'>

population = input("Population of Toronto? ")
#Population of Toronto? 2615069
print(population, type(population))
#2615069 <class 'str'>

population = int(input("Population of Toronto? "))
#Population of Toronto? 2615069
print(population, type(population))
#2615069 <class 'int'>