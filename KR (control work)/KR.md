# A. Сдача
Товар стоит a руб. b коп. За него заплатили c руб. d коп. Сколько сдачи требуется получить?
# B. Обращение фрагмента
Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную между первым и последнием появлением буквы h, в противоположном порядке.
Решения, в которых не формируется изменненая строка (а только выводится ответ по кускам) будут оценены в 0 баллов. В качестве ответа нужно выводить одну строковую переменную.
Решения, в которых используются циклы, будут оценены в 0 баллов.
# C. Треугольники
Дан набор из N отрезков различной длины. Сколькими способами можно выбрать из этих отрезков три, из которых можно составить различные невырожденные треугольники?
Невырожденным называется любой треугольник с ненулевой площадью.
В данной задаче запрещается пользоваться itertools.combinations
# D. Максимальный балл по классам
В олимпиаде по информатике принимало участие несколько человек. Победителем олимпиады становится человек, набравший больше всех баллов. Победители определяются независимо по каждому классу. Определите количество баллов, которое набрал победитель в каждом классе. Гарантируется, что в каждом классе был хотя бы один участник.
Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид: фамилия имя класс балл.
Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.
Выведите три числа: баллы победителя олимпиады по 9 классу, по 10 классу, по 11 классу. Входной файл в кодировке utf-8 (В Python используйте open('input.txt', 'r', encoding='utf-8')).
# E. Проходной балл
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
В конкурсе участвует N человек, при этом количество мест равно K. Определите проходной балл, то есть такое количество баллов, что количество участников, набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов, набравших наибольшее количество баллов среди непринятых абитуриентов, общее число принятых абитуриентов станет больше K.
Программа получает на вход количество мест K. Далее идут строки с информацией об абитуриентах, каждая из которых состоит из имени (текстовая строка содержащая произвольное число пробелов) и трех чисел от 0 до 100, разделенных пробелами.
Программа должна вывести проходной балл в конкурсе. Выведенное значение должно быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
Также возможны две ситуации, когда проходной балл не определен.
Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.
Если количество абитуриентов, имеющих равный максимальный балл больше чем K, программа должна вывести число 1.
# F. Сортировка по близости к K
Вводится число N — размер двумерной квадратной целочисленной матрицы и число K, затем построчно все элементы этой матрицы. Нужно отсортировать каждый столбец матрицы по близости элементов к числу K (сначала самые близкие к K). Вывести полученную матрицу.
Примечание: при одинаковой близости сначала должен располагаться меньший элемент.
В первой строке числа N и K.
В следующих N строках по N целых чисел.
Матрица размером N на N.