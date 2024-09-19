# E2E_UI
Приложение для тестирования функций сайта [saucedemo.com](https://www.saucedemo.com/)
## Запуск
### Запуск через редактор кода
_Предполагается, что у читающего установлен Python и любой редактор кода (VS Code, PyCharm и т.д.). Если это не так, то 
пройдите инструкции по этой [ссылке](https://translated.turbopages.org/proxy_u/en-ru.ru.398046b3-66ec146a-79cf2422-74722d776562/https/code.visualstudio.com/docs/Python/Python-tutorial)._\
**_Также убедитесь, что вы используете Python версии 3.12._**
1. Создайте и/или откройте папку в редакторе кода
2. Создайте виртуальное окружение через команду 
#### 
    python -m venv venv
####
или любым другим предоставляемым редактором способом как [тут](https://pythonchik.ru/okruzhenie-i-pakety/virtualnoe-okruzhenie-python-venv?ysclid=m199wu2rd0890071228)

3. Перенесите файлы из репозитория в папку любым удобным способом (скачав файлы или через `git clone`)
4. Установите все зависимости командой
####
    pip install -r requirements.txt
5. Перетащите или скопируйте папку `chromedriver` в диск `C:\`
6. Запустите командную строку от имени администратора и введите
####
    setx /M path "%path%;C:\chromedriver"
для записи пути до драйвера в переменную %PATH%
7. Запустите исполняемый файл командой
####
    python test_e2e_ui.py