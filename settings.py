currency_list = ["USD", "EUR", "RUB", "UAH", "PLN", "GBP", "BRL", "CAD", "SGD", "NZD", "AUD", "INR", "JPY", "MXN",
                 "IDR", "TRY", "KRW", "SEK", "CLP", "CHF"]

languages = ["ru", "en", "pl", "es", "fr", "pt"]

# Стартовые урлы "Расширения"
recommendedProductUrls = ['https://www.aliexpress.com/item/4000203522848.html',
                          'https://www.aliexpress.com/item/4001294911152.html',
                          'https://www.aliexpress.com/item/32855791603.html',
                          'https://www.aliexpress.com/item/32990667602.html',
                          'https://www.aliexpress.com/item/32818399081.html']

# Урлы для товаров с количеством обзоров =0
url_zero_reviews = ['https://aliexpress.ru/item/1005004774771440.html',
                    'https://aliexpress.ru/item/1005004720630952.html',
                    'https://aliexpress.ru/item/1005004242353824.html']

# Урлы случайных товаров
url_random_four_product = {"1": "1005004946487223.html",
                           "2": "1005001883884598.html",
                           "3": "32949830845.html",
                           "4": "4000238008009.html"}

# Урлы для теста sku
url_sku = ["https://aliexpress.ru/item/1005003891185800.html"]

# Урлы с разным рейтингом
url_seller_rating = {"High": "4001294911152.html",
                     "Medium": "1005003710294306.html",
                     "Low": "1005003982735469.html"}

profile = {"Email": "stanislav.seleznev@bdtech.by", "Password": "Stefler_1992"}

# Список валют которые обрабатывают тесты
currency_processing = {"US": "USD", "€": "EUR", "руб": "RUB"}
currencies = ["USD", "EUR", "RUB"]

# ID_extension тестовая "ibocngjdimaiblnckndicocclenmnmjo", прод "eenflijjbchafephdplkdmeenekabdfb"
extension = {"id": "eenflijjbchafephdplkdmeenekabdfb"}

# Поиск по картинке -> "САЙТЫ С ВЫКЛЮЧЕННОЙ КНОПКОЙ"
disabled_site_list = ["youtube.com", "vk.com", "facebook.com", "instagram.com", "google.com", "twitch.tv",
                      "wikipedia.org", "auto.ru",
                      "letyshops.com"]

setting_tabs = ["Общее", "Поиск по картинке", "Советник", "История", "Синхронизация"]

# Страницы разных товаров для разных магазинов- для которых поиск активен по умолчанию
# "sportmaster": "https://www.sportmaster.ru/product/18138670299/",
# "svyaznoy": "https://www.svyaznoy.ru/catalog/accessories/8936/7721411",
clear = "https://webcache.googleusercontent.com/search?q=cache:"
sites_active = {"mvideo": "https://www.mvideo.ru/products/stiralnaya-mashina-uzkaya-daewoo-wm610t2wu9ru-20084006",
                "sportmaster": clear + "https://www.sportmaster.ru/product/18138670299/",
                "svyaznoy": clear + "https://www.svyaznoy.ru/catalog/accessories/8936/7721411"}

# Страницы разных товаров для разных магазинов- для которых поиск не активен по умолчанию
sites_not_active = {"youtube": "https://www.youtube.com/",
                    "wikipedia": "https://en.wikipedia.org/wiki/Alexander_the_Great"}
