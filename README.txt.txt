# Создать актуальную версию crx 
https://standaloneinstaller.com/online-tools/crx-downloader
https://standaloneinstaller.com/online-tools/xpi-downloader
# Положить ее в текущую директорию - > назвать файл Alitools - поправить пусть в conftest

# Использовать Python 3.8.0
# Запуск виртуального окружения (pipenv shell)
# Синхронизация пакетов (pipenv sync)


pytest -v test_main_page.py                #Обычный запуск тестов
pytest --alluredir=./my_allure_results  name_tests    #"Генерация отчета + запукс тестов"
allure serve ./my_allure_results           #"Просмотр"
