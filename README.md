# Instagram-scraper-python
Python script to collect information from instagram
####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################
# 
# 
#                                                       Инструкция по использованию скрипта скрапера инстаграмма
# 
# 
#                                                                       Версия скрипта V 0.1 (beta)
# 
# 
#                        Перед ипользованием необходимо установить плагин в гугл под названием "FastSave для Instagram". Файл с расширением предлагается.
# 
# 
####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################
#################################################################################################################################################################### 
########################################################--------------------------------------------################################################################
########################################################------Инструкция по настройкам скрипта------################################################################
# 
# 
# 
# 
# 
# 
# 
# sliptime=3------------------------------------------------------------------> Атрибут отвечающий за задержку кода
#                                                                               рекомендуется ставить задержку от 1 до 2 секунд при прямом подключении
#                                                                               Если вы пользуетесь VPN для доступа в Инстаграмм то рекомендуется ставить.
#                                                                               задержку от 2 до 5 секунд.
#                                                                               Задержка устанавливается в зависимости от скорости соединения интернета
#                                                                               Изначально стоит оптимальная задержка в 3 секунды
#                                                                                       
# 
#                                                                                       Рекомендуемый диапазон от 2 до 5 секунд  
# 
#                                                                                                   ****Warning**** 
#                                                                               1)  Не рекомендуется ставить задержку в 0 или 1 секунду
#                                                                                   имеется риск БАНА аккаунта за подозрительную деятельность      
# 
#                                  
# way_to_chrom='C:\Program Files\Google\Chrome\Application\chrome.exe' -------> Атрибут отвечающий за драйвер хрома
#                                                                               Здесь необходимо указать путь до вашего хром браузера
#                                                                               его необходимо устанавливать так как при его отсутствии будет
#                                                                               открываться чистый хром браузер без настроек и аккаунтов.
#                                                                               по этому будет невозможно оперативно входить в Инстаграмм аккаунт
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# Accaunt_link='https://www.instagram.com/borodidanil/' -----------------------> Атрибут отвечающий за аккаунт который будет скрапиться
#                                                                               Здесь необходимо указать ссылку на аккаунт формата: 
#                                                                               "https://www.instagram.com/" + Название аккаунта
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# Folder_forscraping_results_name="Folder_"  ---------------------------------> Атрибут отвечающий за название папки в которую будет скачиваться пост. 
#                                                                               Создается папка с названием и индексом поста
#                                                                               в нее закидывается картинка и текст(в зависимости от настроек) и так по кругу
#                                                                               По умолчанию стоит имя папки "Folder_"+ индекс поста 
#                                                                                                   ****Warning****
#                                                                               1) Необходимо, что бы название папки начиналось с латинской буквы 
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# DIR_save="E:/texttttt/" ----------------------------------------------------> Атрибут отвечающий за директорию скачивания всех результатов скраппинга
#                                                                               На данный момент не реализована гибкая настройка выбора директории
#                                                                               по этому для успешной работы необходимо в настройках хром поставить
#                                                                               вашу пустую папку для загрузки файлов и поставить там же не нужность 
#                                                                               запроса пути скачивания файлов
#                                                                                          Рекомендуется создать отдельную папку для 
# 
# 
# 
#                                                                                                   ****Warning****
#                                                                               1) Путь не должен содержать пробелов и должен состоять 
#                                                                                   из латинских букв и цифр
#                                                                               2) Путь скачивания хрома и этот атрибут должны совпадать
#                                                                               
#                                                                               
#                                                                                
# public_count_posts=-1 ------------------------------------------------------> Атрибут отвечающий за количество постов которое необходимо проскрапить.
#                                                                               Отсчет начинается с последнего выложенного поста.
#                                                                               По умольчанию атрибут стоит на все посты на странице, но вы можете выбрать 
#                                                                               необходимое вам количество.
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# like_file=True -------------------------------------------------------------> Атрибут отвечающий за создание файла с ведением логов лайков постов
#                                                                               при значении "TRUE" будет создан файл в который будет записываться
#                                                                               количество лайков под постами
#                                                                               Может принимать значения:
#                                                                               ----"TRUE"- Создается файл с ведением логов лайков под постами
#                                                                               ----"FALSE"- Не создается файл с ведением логов лайков под постами
#                                                                               По умолчанию атрибут стоит в позиции "TRUE" 
#                                                                               
#                                                                               
#                                                                                
# like_text=True -------------------------------------------------------------> Атрибут отвечающий за вид ведения логов лайков
#                                                                               Может принимать значения:
#                                                                               ----"TRUE"-Принимает вид для лучшей наглядности
#                                                                                           ПРИМЕР: Название папки поста' --> 'количество лайков                                                                              
#   
#                                                                               ----"FALSE"-Принимает вид удобного конвертирования в CSV формат и работы с данными
#                                                                                           ПРИМЕР: Индекс поста' ; 'количество лайков
#                                                                               По умолчанию атрибут стоит в позиции "TRUE"
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# closing_chrom_window=False -------------------------------------------------> Атрибут отвечающий за закрытие хрома после выполнения функции
#                                                                               Может принимать значения:
#                                                                               ----"TRUE"- Закрывает вкладку хрома, где ввелась деятельность
#                                                                               ----"FALSE"- Не закрывает вкладку хрома, где ввелась деятельность
#                                                                               По умолчанию атрибут стоит в позиции "FALSE"
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# getting_text_under_post=True -----------------------------------------------> Атрибут отвечающий за запись текста под постом
#                                                                               После создания папки поста туда записывается  txt файл
#                                                                               в котором хранится текст
#                                                                               оставленный под картинкой.
#                                                                               Может принимать значения:
#                                                                               ----"TRUE"- Создает файл с текстом поста
#                                                                               ----"FALSE"- Не создает файл с текстом поста
#                                                                               По умолчанию атрибут стоит в позиции "TRUE"
#                                                                               
#                                                                               
#                                                                               
#                                                                               
#                                                                                
# getting_pic_post=True ------------------------------------------------------> Атрибут отвечающий за сохранение картинки
#                                                                               сохраняет картинку поста и переносит ее в папку с его названием и индексом 
#                                                                               Может принимать значения:
#                                                                               ----"TRUE"- Сохраняет картинку
#                                                                               ----"FALSE"- Не сохраняет картинку
#                                                                               По умолчанию атрибут стоит в позиции "TRUE"







####################################################################################################################################################################
################################################################################   #################################################################################
############################################################################### P.S. ###############################################################################
################################################################################   ################################################################################# 
####################################################################################################################################################################



 

#                                          От разработчика
# Данный скрипт все еще находится в разработке. С каждым релизом я буду добавлять новые функции и возможности.
# Если вы имеете предложение для добавления функционала для скрипта я буду рад вас выслушать =)

# Мои контакты:
# VK: https://vk.com/id535168445
# instagram: https://www.instagram.com/borodidanil/
# Telegram: @Borodin_Danila
# Мой сайт: https://data-scientist-borodin-danila.ru
# Не бойтесь моих закрытых страниц я с удовольствием добавлю вас =)






####################################################################################################################################################################
####################################################################################################################################################################
############################################################ Дайте мне работу, я безработный  =(  ##################################################################
####################################################################################################################################################################
####################################################################################################################################################################
