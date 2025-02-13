# # Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# # стран. Определить какие марки машин были доставлены во все указанные страны, какие в
# # некоторые из стран и какие не доставлены ни в одну страну.

all_cars = {'Toyota', 'Ford', 'BMW', 'Audi', 'Honda', 'Nissan'}
print(f'\nСписок всех марок машин:\n{all_cars}')

Russia = {'Toyota', 'Ford'}
China = {'Ford', 'BMW', 'Audi'}
USA = {'Toyota', 'Audi', 'Ford'}

some_countries_models_union = Russia | China | USA
all_countries_models_intersection = Russia & China & USA
not_delivered_anywhere = all_cars - some_countries_models_union

print(
    f'\nМарки автомобилей которые были доставлены в некоторые из указанных стран:\n{some_countries_models_union}')

if not_delivered_anywhere:
    print(f'\nМодели не доставленные никуда:\n{not_delivered_anywhere}')
else:
    print("\nВсе модели из списка были доставлены как минимум в одну страну.")

if all_countries_models_intersection:
    print(f'\nМодели доставленные во все страны:\n{all_countries_models_intersection}')
else:
    print("\nНет моделей доставленных всем трем странам.")
