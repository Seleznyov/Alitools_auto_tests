# Создать актуальную версию crx 
https://standaloneinstaller.com/online-tools/crx-downloader
https://standaloneinstaller.com/online-tools/xpi-downloader
# Положить ее в текущую директорию                         - > назвать файл Alitools -> поправить пусть в conftest

# Использовать Python 3.8.0
# Запуск виртуального окружения (pipenv shell)
# Синхронизация пакетов (pipenv sync)

pytest -v test_main_page.py                              #Обычный запуск тестов
pytest -v test_general_settings.py::test_language_change # Запуск конкретного теста
pytest --alluredir=./my_allure_results  name_tests       #"Генерация отчета + запукс тестов"
pytest ./ --alluredir=./report_allure 			 # Запуск всех тестов из текущей директории
pytest -v test_general_settings.py::test_language_change # Запуск конкретного теста
pytest -s -v -m smoke					 # Запуск smoke тестов
pytest -s -v -m smoke -W ignore::DeprecationWarning       # Запуск smoke тестов для firefox

allure serve ./my_allure_results                         #"Просмотр"

-W ignore::DeprecationWarning                            # флаг игноррирования сообщений об ошибке "executable_path" - писать в конце -> использовать для firefox

Вовремя запуска тестов для firefox в файл settings добавить токен гит
