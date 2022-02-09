Ричард и Эрлих идут на переговоры с k инвесторами. У них два метода ведения переговоров, либо вести себя по-хамски, тем самым не дать прогнуть себя, либо вести себя прилично. У них только n дней, для того, чтобы представить свой проект, всем инвесторам. 

Они понимают, что если вести себя по-хамски, то инвесторы не будут посылать их на повторные переговоры, но успех при этом будет сомнителен. Если же они будут себя вести прилично, то инвесторы будут наглеть и устраивать больше встреч. 

Они изначально составляют план, сколько времени они готовы тратить на каждого инвестора. Если они готовы рискнуть, то они будут вести себя максимально неприлично, на этого инвестора планируют немного дней. Если же инвестор стоит того, и они готовы тратить время, чтобы представлять проект снова и снова, то они будут терпеливы, и планируют больше дней. Так как у них ограничено время, то они могут просто не пойти на встречу. 

Ричард для каждого инвестора составил функцию зависимости вероятности успеха ведения переговоров от количества дней, потраченных на инвестора. Функции неубывающие.  Смотрите таблицу. Таблица составлена для 5 дней, и 4 инвесторов. 

|          | 0 <br/>day | 1 <br/>day | 2 <br/>day | 3 <br/>day | 4 <br/>day | 5 <br/>day |
|----------|-------|-------|-------|-------|-------|-------|
|1 Инвестор|   0   |   1   |   2   |   3   |   4   |   6   |
|2 Инвестор|   0   |   2   |   3   |   3   |   4   |   6   |
|2 Инвестор|   0   |   3   |   4   |   5   |   5   |   5   |
|4 Инвестор|   0   |   6   |   7   |   7   |   7   |   9   |

Ричард считает успешной стратегию, при которой сумма вероятностей успехов максимальна. 

Для данных из таблицы выше успешная стратегия следующая: 


|            | Количество <br/> дней | Вероятность<br/>успеха |
|------------|-----------------|--------------------|
| 1 инвестор |0|0|
| 2 инвестор |1|2|
| 3 инвестор |2|4|
| 4 инвестор |2|7|

При этом максимальная суммарная вероятность равна 13. 

Ваша задача найти максимальную суммарную вероятность, для входных данных. 

Задача подразумевает решение методом динамического программирования. 

Входные данные: k, n, функции успеха 

Пример входных данных: 

4

5

1,2,3,4,6

2,3,3,4,6

3,4,5,5,5

6,7,7,7,9

k ≤ 20, n ≤ 20

Выходные данные: максимальная суммарная вероятность