# def merge(L):
#     merged = []
#     for i in range(0, len(L), 3):
#         merged.append(L[i] + L[i + 1] + L[i + 2])
#     return merged

# print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# def mystery(s):
#     """ (str) -> bool
#     """
#     matches = 0
#     for i in range(len(s) // 2):
#         if s[i] == s[len(s) - 1 -
#                      i]:  # <--- How many times is         this line reached?
#             print(i)
#             matches = matches + 1

#     return matches == (len(s) // 2)

# mystery('civil')


# def mystery(s):
#     """ (str) -> bool
#     """
#     matches = 0
#     for i in range(len(s) // 2):
#         if s[i] == s[len(s) - 1 - i]:
#             matches = matches + 1

#     return matches == (len(s) // 2)


# print(mystery('civil'))


# def shift_right(L):
#     ''' (list) -> NoneType

#     Shift each item in L one position to the rightand shift the    last item to the first position.

#     Precondition: len(L) >= 1
#     '''

#     last_item = L[-1]

#     # MISSING CODE GOES HERE
#     for i in range(1, len(L)):
#         L[len(L) - i] = L[len(L) - i - 1]

#     L[0] = last_item

#     return L


# print(shift_right([1, 2, 3]))


# def make_pairs(list1, list2):
#     ''' (list of str, list of int) -> list of [str, int] list

#     Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

#     Precondition: len(list1) == len(list2)

#     >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
#     [['A', 1], ['B', 2], ['C', 3]]
#     '''

#     pairs = []

#     # CODE MISSING HERE
#     # for i in range(len(list1)):
#     #     pairs.append([list1[i], list2[i]])

#     # for i in range(len(list1)):
#     #     inner_list = []
#     #     inner_list.append(list1[i])
#     #     inner_list.append(list2[i])
#     # pairs.append(inner_list)

#     # for i in range(len(list1)):
#     #     inner_list = []
#     #     inner_list.append(list1[i])
#     #     inner_list.append(list2[i])
#     #     pairs.append(inner_list)

#     # inner_list = []
#     # for i in range(len(list1)):
#     #     inner_list.append(list1[i])
#     #     inner_list.append(list2[i])
#     #     pairs.append(inner_list)

#     return pairs


# print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))


# values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(values[1][1])

# breakfast = [['French', 'toast'], [
#     'blueberry', 'pancakes'], ['scrambled', 'eggs']]
# print(breakfast[-2][-2])


# for i in range(2, 5):
#     for j in range(4, 9):
#         print(i, j)

# 15


# def contains(value, lst):
#     """ (object, list of list) -> bool

#     Return whether value is an element of one of the nested        lists in lst.

#     >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
#     True
#     """

#     found = False  # We have not yet found value in the list.

#     # CODE MISSING HERE
#     # for i in range(len(lst)):
#     #     for j in range(len(lst[i])):
#     #         if lst[i][j] == value:
#     #             found = True

#     # for item in lst:
#     #     if value == item:
#     #         value = True

#     for sublist in lst:
#         if value in sublist:
#             found = True

#     return found


# print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]]))


'''A file has a section at the top that has a preamble describing the contents of the file, then a blank line, then a list of high temperatures for each day in January all on one line, then a list of high temperatures for each day in February all on one line, then lists for March, April, and so on through December, each on one line. There are thousands of lines of information after that temperature data that you aren't currently interested in.

You want to write a program that prints the average of the high temperatures in January. Which of the four file-reading approaches should you use?

Hint: review the Reading Files lecture.'''

# The readline approach


# data_file refers to a file open for reading.
# for line in data_file:
#     print(line)

# print(line-’\n’)
# print(line.rstrip(’\n’))


# def lines_startswith(file, letter):
#     """ (file open for reading, str) -> list of str

#     Return the list of lines from file that begin with letter.
#     The lines should have the newline removed.

#     Precondition: len(letter) == 1
#     """

#     matches = []

#     # CODE MISSING HERE
#     # for line in file:
#     #     if letter == line[0]:
#     #         matches.append(line.rstrip('\n'))

#     # for line in file:
#     #     if line.startswith(letter):
#     #         matches.append(line.rstrip('\n'))

#     return matches


# def write_to_file(file, sentences):
#     """ (file open for writing, list of str) -> NoneType

#     Write each sentence from sentences to file, one per line.

#     Precondition: the sentences contain no newlines.
#     """

#     # CODE MISSING HERE
