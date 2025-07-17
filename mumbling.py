
# my_dict = {1:'a', 2: 'b', 3 : 's'}
# my_dict()
#
#
# print(my_dict)

#
# def accum(string):
#     my_dict ={}
#     num = 1
#     for letters in string:
#         my_dict[num] = letters
#         num += 1


def accum (string):
    result_list = []
    for symbol in string:

        # print(symbol)
        # print(string.index(symbol))
        ss = ((string.index(symbol)+1) * symbol).capitalize()
        result_list.append(ss)
    return '-'.join(result_list)


print(accum('abs'))
