"""
######
SELECT - выборка данных
select * from table_name; - выборка всех полей
select column_name from table_name - выборка определенных данных
WHERE - aфильтрация


ОПЕРАТОРЫ

AND - и 
OR - или 
IN - в 
BETWEEN - между 
LIKE - как (какое то слово)с
ILIKE - бех учета регистра 
'%a%' - в слове есть слово "а"
'a%' - слово начинается с "а"
'%a%' - слово заканчивается на "а"
_ - определяет колл-во символов

IS NULL - проверка на пустое значение
NOT -  отрицания условия 
LINIT (10) - установка колл-во записей, 10 записей с данных
ORDER BY - сортировка по полю
GROUP BY - группировка по определенному столбцу 
DESK  - по убыванию 
ASK - по возрастанию(по умолчанию)


######
INSERT - доьавление данных
INSERT INTO table_name (column_name) VALUES (values_for_colums);


######
UPDATE - обновление данных 
UPDATE table_name SET column_name = value, column2=value2 WHERE условие;



######
DELETE - удаление данных
DELETE from table_name; очистка всей таблицы 
DELETE from table_name where условие; - очистка данных подходяхих под условие



Функции в PostgreSQL
АГРЕГАЦИОННЫЕ ФУНКЦИИ
COUNT() - функция для счета колл-во записей\вхождений  
AVG() - среднее значение 
MAX() - макс значение 
NIN() - мин значение 
SUMM - поиск результата сложения всех значений 

(|| ' ' ||) as... - конкaтенация  
ROUND() - округление значений           
CASE WHEN - подстановка значений в зависимости от условия 
Select column_name CASE WHEN condiction THEN value1 ELSE value2 END FROM table_name


JOIN - связи между таблицами 
FULL JOIN - связываются все таблицы
LEFT JOIN -- соединение из левой таблицы
RIGHT JOIN - соединение из прравой таблицы 
INNER JOIN - соединение только тех данных, которые имеют пересечение 

"""