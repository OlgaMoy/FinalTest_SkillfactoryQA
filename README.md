# FinalTest_SkillfactoryQA
Итоговый проект по курсу Тестировщик-автоматизатор от Skillfactiry

Необходимо было протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии. Были предоставлены требования требования к сайту и ссылка на объект тестирования: https://b2c.passport.rt.ru 

По проекту выполнены тест-кейсы и описаны возможные баги. Сылка на документацию https://docs.google.com/spreadsheets/d/1Y-PQceDUqrvi8KS1hj8AIgpziPWUbb94exdOIbO7q7Y/edit?usp=sharing
Так же были протестированы требования к проекту в формате комментариев к тексту (в комментарии указано, на что заменить): https://docs.google.com/document/d/1gP_sEo17767tZ6WxY9lTn2zHq7Rxz2GJrBmlI-nq9Bg/edit?usp=sharing. Стоит отметить, что так же можно поправить оформление в тексте и описать недостающие функции (например способы авторизации через соц.сети).

Так же написаны 20 автотестов (один тест иногда падает из-за Капчи, не смогла ее победить)

В корневом каталоге проекта содержаться:
config.py - содержит переменные используемые в проекте;
README.md - содержит информацию в целом о проекте;
requirements.txt - содержит все библиотеки и зависимости проекта

Директория tests содержит:
conftest.py - условия для запуска браузера
test_rostelecom.py - автотесты по проекту
chromedricer.exe - файл драйвера для хром версии 109

Директория pages содержит:
Base_page.py - основные методы работы со страницей
Main_page.py - локаторы по проекту

В работе над проектом были использованы следующие техники тест-дизайна:
1. Анализ граничных значений (так как в требованиях были указаны ограничения по символам в определенных полях)
2. Предугадывание ошибок (так как пользователь может ошибиться при вводе данных)
3. Эквивалентное разбиение (так же в связи с ограничением по вводу символов)

Инструменты, примененные для тестрования:
Для тестирования сайта был использован интсрумент Selenium;
Для определения локаторов использовались следующие инструменты: DevTools, ChroPath.

Для запуска тестов необходимо установить все библиотеки, указанные в файле requirements.txt, скачать соответсвующий вышему окружению вебдрайвер для Chrome с сайта https://chromedriver.chromium.org/ и выполнить запуск через команду python -m pytest -v tests/test_rostelecom.py. 
В проекте использована версия драйвера 109.0.5414.25. Проект выполнен на Windows7 Chrome 109

