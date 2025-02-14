# audi, volvo, bmw, honda
#  toyota honda bmw audi
def create_car_sets():
    all_cars_input = input('Введите все возможные марки машин через запятую: ')
    all_cars_set = set(car.strip() for car in all_cars_input.split(','))

    n = int(input('Введите количество стран: '))

    car_sets = {}
    for i in range(n):
        country = input(f'Введите название {i + 1} страны: ')
        cars_in_country_input = input(
            f'Введите марки машин, поставляемых в {country}, разделенные запятой: ')
        if cars_in_country_input:
            cars_in_country_set = set(car.strip() for car in cars_in_country_input.split(','))
            if not cars_in_country_set.issubset(all_cars_set):
                print("Предупреждение: введены машины не из списка всех возможных моделей.")
                print("Используем только те модели которые есть в списке.")
                cars_in_country_set &= all_cars_set  # Пересечение с множеством всех возможных моделей
            car_sets[country] = cars_in_country_set
        else:
            car_sets[country] = set()
    return all_cars_set, car_sets
all_possible_models, country_car_sets = create_car_sets()
all_countries_models_intersection \
    = set.intersection(*country_car_sets.values())
some_countries_models_union \
    = set.union(*country_car_sets.values())
not_delivered_anywhere \
    = all_possible_models - some_countries_models_Union
print(f'\nМарки автомобилей которые были поставлены во все указанные страны:\n{all_countries_models_intersection}')
print(
    f'\nМарки автомобилей которые были поставлены хотя бы в некоторые из указанных стран:\n{some_countries_models_union}')
if not_delivered_anywhere:
    print(
        f'\nМодели автомобилей которые не были поставлены никуда:\n{not_delivered_anywhere}')
else:
    print("\nВсе модели из списка были поставлены как минимум в одну страну.")







