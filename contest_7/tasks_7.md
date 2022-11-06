# A. Четные индексы
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). Программа должна быть эффективной и не выполнять лишних действий! Вводится список чисел. Все числа списка находятся на одной строке.
# B. Четные элементы
Выведите все четные элементы списка. Вводится список чисел. Все числа списка находятся на одной строке.
# C. Количество положительных
Найдите количество положительных элементов в данном списке.
# D. Больше предыдущего
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# E. Соседи одного знака
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей несколько - выведите первую пару.
# F. Больше своих соседей
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов.
# G. Наибольший элемент
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
# H. Наименьший положительный
Выведите значение наименьшего из всех положительных элементов в списке. Известно, что в списке есть хотя бы один положительный элемент, а значения всех элементов списка по модулю не превосходят 1000.
# I. Наименьший нечетный
Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.
# J. Шеренга
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать. Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200. Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
# K. Количество различных элементов
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
# L. Вывести в обратном порядке
Выведите элементы данного списка в обратном порядке, не изменяя сам список.
# M. Переставить в обратном порядке
Переставьте элементы данного списка в обратном порядке, затем выведите элементы полученного списка. Эта задача отличается от предыдущей тем, что вам нужно изменить значения элементов самого списка, поменяв местами A[0] c A[n-1], A[1] с A[n-2], а затем вывести элементы списка подряд.
# N. Переставить соседние
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.). Если элементов нечетное число, то последний элемент остается на своем месте.
# O. Циклический сдвиг вправо
Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ..., последний элемент переходит на место A[0]). Используйте минимально возможное количество операций присваивания.
# P. Переставить min и max
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Q. Удалить элемент
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop().
Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список.
# R. Вставить элемент
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы имевшие индекс не менее k вправо.
Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
# S. Количество совпадающих пар
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# T. Уникальные элементы
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# U. Кегельбан
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от l_i до r_i включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел l_i, r_i, при этом 1 ≤ l_i ≤ r_i ≤ N ≤ 100
Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
# V. Ферзи
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
# W. Сжатие списка
Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые элементы в левую часть списка, не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
# X. Самое частое число
Дан список. Не изменяя его и не используя дополнительные списки, определите, какое число в этом списке встречается чаще всего. Если таких чисел несколько, выведите любое из них.