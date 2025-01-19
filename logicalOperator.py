# and or not

temp = 27
is_raining = True
is_sunny = True

#if temp > 35 or temp < 0 or is_raining:
#    print("Cancel the outdoor event")
#else:
#    print("The outdoor event is as scheduled")


if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <=0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp and is_sunny:
    print("It is warm outside")
    print("It is sunny ")