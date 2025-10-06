values_1_to_100 = []
values_101_to_200 = []
total_values = []

for i in range(1,101):
    values_1_to_100.append(i)
for values in values_1_to_100:
        total_values.append(values)

for i in range(101,201):
    values_101_to_200.append(i)
for values in values_101_to_200:
        total_values.append(values)

for i in range(0,len(total_values)):
    if total_values[i] % 10 == 0:
        total_values[i] = 999
print(total_values)

for values in total_values:
    if values % 10 == 0:
        print("A bug has been detected!")
        break