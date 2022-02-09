Сделать решатель нонограммы, и получите эмблему PP, из сериала кремневая долина.

Японский кроссворд (по-другому нонограмма) — это головоломка, в которой зашифровано изображение

Дается поле с горизонатальными и вертикальными подсказками. Эти подсказки указывают количество клеток, которые надо закрасить, в столбце - при горизонтальных подсказках, в строке - при вертикальных. Если в подсказке одно число  n, то это значит, что надо закрасить n клеток подряд. Если несколько чисел, к примеру два числа n и k, то это значит что надо сначала закрасить n клеток подряд, потом должен быть хотябы один пробел, после чего закрашиваем  k клеток подряд. 

Задача закрасить клетки так, чтобы количество все подсказки сходились. 

![](../img/t15i1.png)

![](../img/t15i2.png)

Ваша задача написать решатель нонограммы размером 5 на 5.

Потренироваться в решении нонограмм можно тут: https://www.puzzle-nonograms.com/

Входные данные:  сначала горизонтальные подсказки, потом вертикальные

При горизонтальных подсказках, если пишется несколько цифр, то сначала написано количество закрашенных клеток, что расположены выше, потом ниже

При вертикальных, сначала слева, потом справа

Пример входных данных: 

4  
1,1  
5  
1,1  
3  

3  
1,3  
3,1  
1,3  
1  

Выходные данные: получившаяся картинка записанная в строчку, в пикселях, где X - это буквы эмблемы, пустое пространство обозначается прочерком - 

Пример выходных данных: 

XXX--  
X-XXX  
XXX-X  
X-XXX  
--X--