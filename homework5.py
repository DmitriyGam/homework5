immutable_var = 1, 2, 3, 'one', 'two', 'three', True
print(immutable_var)
#immutable_var[3] = 'zero' #кортеж нельзя изменить так как они ислозуются для хранилища и их не трогали
mutable_list = [1, 2, 3, 'one', 'two', 'three', True]
mutable_list[3] = 'zero'
print(mutable_list)