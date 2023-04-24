# MongoDB

Архитектура на основе свободно сопряжённых сервисов с ограниченными контекстами. (Loosely coupled service oriented architecture with bounded contexts.)

микросервис должен соответствовать ограниченному контексту, который способен полностью понять один человек. То есть чем шире функциональность приложения, тем больше должно быть микросервисов. 

Компонентное представление через сервисы

Компонент — это элемент системы, который можно независимо заменить, усовершенствовать (Мартин Фаулер) и масштабировать (Ребекка Парсонс).

При разработке ПО мы используем два типа компонентов:

А. Библиотеки: куски кода, применяемые в приложениях, которые могут дополняться или заменяться другими библиотеками, желательно без воздействия на остальную часть приложения. Взаимодействие происходит через языковые конструкты. Однако если интересующая нас библиотека написана на другом языке, мы не можем использовать этот компонент.

Б. Сервисы: части приложений, по факту представляющие собой маленькие приложения, выполняющиеся в собственных процессах. Взаимодействие выполняется за счёт межпроцессной связи, вызовов веб-сервисов, очереди сообщений и т. д. Мы можем использовать сервис, написанный на другом языке, поскольку он выполняется в собственном процессе (этот подход предпочитает Чед Фаулер). Про использование модулей на Golang в питоне есть ресурс: https://www.ardanlabs.com/blog/2020/07/extending-python-with-go.html

Независимая масштабируемость — каждый сервис может быть масштабирован независимо от остального приложения.

статья с теорией и ссылками: https://habr.com/ru/companies/vk/articles/320962/


референс для содания сокета: https://github.com/TiagoValdrich/python-socket-chat/blob/master/server.py

Статьи:

стр.1057: https://elibrary.ru/download/elibrary_49273592_71600015.pdf

стр.68: https://research-journal.org/wp-content/uploads/2011/10/5-1-24.pdf

контекстуально тоже подходит (как подтверждение актуальности задачи): https://elibrary.ru/item.asp?id=49617827

хранение разнородных данных (подходы): https://elibrary.ru/item.asp?id=42490745
