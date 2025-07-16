value=[5,2,3,4,5,4,3,5]
max_value=value[0]
second_max=value[1]
for i in range(2,len(value)):
    if value[i]>max_value:
        second_max=max_value
        max_value=value[i]
    elif second_max<value[i] and value[i] != max_value:
        second_max=value[i]
print(second_max)