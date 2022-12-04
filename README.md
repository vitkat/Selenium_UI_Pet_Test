# Selenium_UI_Pet_Test

Проект TestingPets организованный с помощью Page Object. В данном проекте созданы автотесты для тестирования сайта домашних животных. Проект имеет папки:
  <PAGES> - В данном каталоге лежат тестовые страницы.
  <TESTS> - В данном каталоге лежат тесты по кажной из страниц те сайта.

В каталоге <PAGES> лежат следующие файлы:
  *base_page.py - с описанием тестового метода;
  *login_page.py - с описанием тестового метода для страницы авторизации;
  *main_page.py - с описанием тестовых методов доступного функционала данной страницы;
  *profile_page - с описанием тестовых методов доступного функционала данно страницы;
  *init.py
  *locators.py - файл, в который сложены все локаторы данного проекта.

В каталоге <TESTS> лежат следуюющие файлы:
  *init.py
  *test_login_pages.py - файл, в который сложены все тесты относящиеся к странице авторизации;
  *test_profile_pages.py - файл, в который сложены все тесты относящиеся к странице профиля;
  *test_main_pages.py - файл, в который сложены все тесты относящиеся к главной странице.
  
Каталог <VENV>

В корне проекта лежат следующие файлы:
  *init.py
  *conftest.py - файл, в котором прописана фикстура;
  *pytest.ini - файл, в котором прописаны маркеры для тестов;
  *requiruments - файл, в котором прописаны все использованные библиотеки, для данного проекта.
