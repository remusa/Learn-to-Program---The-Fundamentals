# print('3' in [1, 2, 3])
# print(len('mom') in [1, 2, 3])
# print('a' in ['mom', 'dad'])
# print(int('3') in [len('a'), len('ab'), len('abc')])
# print(len([1, 2, 3]) == len(['a', 'b', 'c']))

# def secret(s):
# i = 0
# result = ''
#
# while s[i].isdigit():
# result = result + s[i]
# i = i + 1
#
# return result

# print(secret('abc123'))
# print(secret('abc'))
# print(secret('123'))
# print(secret('123abc'))

# Return a \color{black}{\verb|list|}list containing every third item from \color{black}{\verb|L|}L starting at index 0.

# def compress_list(L):
#     """ (list of str) -> list of str

#     Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

#     Precondition: len(L) >= 2 and len(L) % 2 == 0

#     >>> compress_list(['a', 'b', 'c', 'd'])
#     ['ab', 'cd']
#     """
#     compressed_list = []
#     i = 0

#     while i < len(L):
#         compressed_list.append(L[i] + L[i + 1])
#         i = i + 2

#     return compressed_list

# sum = 0
# i = 524
# while i <= 10508:
#     if i % 2 == 0:
#         sum += i
#     i += 2

# print(sum)

# sum = 0
# for i in range(524, 10510, 2):
#     if i % 2 == 0:
#         sum += i

# print(sum)

# def while_version(L):
#     """ (list of number) -> number
#     """
#     i = 0
#     total = 0

#     while i < len(L) and L[i] % 2 != 0:
#         total = total + L[i]
#         i = i + 1

#     return total

# print(while_version([1, 3, 5, 15, 2, 7]))

# def for_version(L):
#     found_even = False
#     total = 0

#     for num in L:
#         if num % 2 != 0 and not found_even:
#             total = total + num
#         else:
#             found_even = True

#     return total

# print(for_version([1, 3, 5, 15, 2, 7]))

# numbers = [1, 4, 3]
# numbers = numbers.reverse()
# print(numbers)

# fruits = ['banana', 'apple', 'pear', 'peach']
# fruits.insert(fruits.index('pear'), 'watermelon')
# print(fruits)

# def cap_song_repetition(playlist, song):
#     '''(list of str, str) -> NoneType

#     Make sure there are no more than 3 occurrences of song in playlist.

#     '''

#     # while playlist.count(song) > 3:
#     #     playlist.remove(playlist.index(song))

#     # while playlist.count(song) > 3:
#     #     playlist.remove(song)

#     # while playlist.count(song) > 3:
#     #     playlist.pop(playlist.index(song))

#     # while playlist.count(song) > 3:
#     #     playlist.pop(song)

#     # while playlist.count(song) >= 3:
#     #     playlist.remove(song)

#     print(playlist)
#     return playlist

# cap_song_repetition([
#     'Lola', 'Venus', 'Lola', 'Lola', 'LetItBe', 'Lola', 'ABC', 'Cecilia',
#     'Lola', 'Lola'
# ], 'Lola')

# a = [1, 2, 3]
# b = a

# # a = [1, 'A', 3]
# # b = [1, 'A', 3]

# # a[1] = 'A'

# # b[-2] = 'A'

# b[1] = 'AB'
# a[1] = a[1][0]

# print(a, b)
a = [1, 2, 3]
b = [1, 2, 3]

# a[1] = 'A'

# b[-2] = 'A'

# b[1] = 'AB'
# a[1] = a[1][0]

# a = [1, 'A', 3]
# b = [1, 'A', 3]

# print(a, b)

# def increment_items(L, increment):
#     i = 0
#     while i < len(L):
#         L[i] = L[i] + increment
#         i = i + 1

# values = [1, 2, 3]
# print(increment_items(values, 2))
# print(values)

# values = []
# for num in range(3, 10, 3):
#     values.append(num)
# print(values)

# values = []
# for num in range(3, 9, 3):
#     values.append(num)
# print(values)

# values = []
# for num in range(1, 3):
#     values.append(num * 3)
# print(values)

# values = []
# for num in range(1, 4):
#     values.append(num * 3)
# print(values)

# for num in range(3, 23, 8):
#     print(num)