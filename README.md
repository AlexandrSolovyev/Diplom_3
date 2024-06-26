## Дипломный проект. Задание 3: веб-приложение

*Проект автоматизации тестирования сайта заказа бургеров https://stellarburgers.nomoreparties.site/*

1. Основа для написания автотестов — фреймворк pytest, selenium.
2. Для отчетов используется Allure
3. Автотесты написаны в соответствии паттерна POM
4. Установить зависимости — `pip install -r requirements.txt`
5. Команда для запуска — `pytest -v`
6. Команда для запуска с записью отчета в allure_results: `pytest --alluredir=allure_results`
7. Генерация отчета в html страницу (находясь в дирректории allure_results): _`allure serve allure_results`_ 

### Директория проекта:

* `allure_results` - сожержит отчеты alure
 *  `locators` - дирректория локаторов
 * * `login_locators.py` - локаторы для авторизации 
 * * `main_page_locators.py` - локаторы для главной страницы 
 * * `order_feed_locators.py` - локаторы заказов
 * * `profile_locators.py` - локаторы профиля
 * * `recovery_locators.py` - локаторы восстановления пароля
 * `pages` - дирректория методов страниц
 * * `base_page.py` - общие методы
 * * `login_page.py` - методы авторизации
 * * `main_page.py` - методы для главной страницы
 * * `order_feed_page.py` - методы для страницы заказов 
 * * `profile_page.py` - методы для страницы профиля 
 * * `recovery_page.py` - методы для страницы восстановления пароля 
 * `tests` - дирректория тестов
 * * `test_main_page.py` - тесты для главной страницы
 * * `test_order_feed.py` - тесты для страницы поиска заказов
 * * `test_profile.py` - тесты для страницы профиля
 * * `test_recovery_password.py` - тесты для страницы восстановления пароля
 * `conftest.py` -  фикстуры
 * `date.py` - данные для параметризации
 * `README.md` - описание проекта
 * `requirements` - файл с внешними зависимостями
 *  `helper` - файл с генерациями данных
