<H1>Парсер электронной почты с сайтов и отправка на них писем</H1>
Парсер разбит на функции.

1.Функция открывает файл, который загружает пользователь (в моем случае файл из другого парсера - 2гис)
Достает из этого файла колонку, которую я задаю, и собирает данные из этой колонки в список 
(в моём случае это адреса страниц компаний)

2.Функция открывает сайт и ищет по маске имейл, собирает списки имейлов найденные на сайте.

3.Запускает 1 и 2, плюс обрабатывает списки имейлов, добавлят по одному без повторений в новый список
и в файл output.txt построчно, для дальнейшей рассылки

4.Функция рассылки писем на почты из файла output.txt 