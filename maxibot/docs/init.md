# Util
## class maxibot.__init__.MaxiBot(token)
Класс бота MAX  
**Методы:**
* **_build_handler_dict** (`handler` `**filters`) - Метод, которая формирует словарь для добавления в список обработчиков событий (handler)  
    * **handler** - Функция-обработчик события  
    * ****filters** - Фильтры для функции-обработчика событий  
* **polling** (`allowed_updates`) - Метод, который запускает корутину полинга событий  
* **start** (`allowed_updates`) - Метод, который запускает полинга событий по разрешённым событиям `allowed_updates` в ассинхронном режиме  
* **stop** - Метод, который останавлиявает полинг событий  
* **message_handler** (`commands`, `regexp`, `func`, `content_types`) - Декоратор для регистрации обработчика текстовых сообщений по шаблону  
    * **commands** - фильр по командам
    * **regexp** - фильр по регулярным выражениям
    * **func** - фильр по функции
    * **content_types** - фильр по типу контента
* **run_handler** (`context`, `message_handlers`) - Метод запуска обработчиков событий текстового сообщения  
    * **context** - Объект типа `Message`  
    * **message_handlers** - Список обработчиков событий  
* **_test_filter** (`message_filter`, `filter_value`, `context`) - Метод проверки соответствия сообщения всем фильтрам текстовых сообщений  
    * **message_filter** - Тип фильтра  
    * **filter_value** - Значение, которое надо сопоставить с фильтром  
    * **context** - Объект типа `Message`  
* **_check_filters** (`context`, `handler`) - Проверка текстового сообщения на фильтры  
    * **context** - Объект типа `Message`  
    * **handler** - Словарь обработчиков событий  
* **_process_text_message** (`context`) - Обрабатывает входящее сообщение  
    * **context** - Объект типа `Message`  
* **_process_update** (`update`) - Метод для обработки входящего полученного обновления  
    * **update** - Словарь, полученный от API MAX в процессе опроса API на обновления  
* **_process_update** (`update`) - Метод для обработки входящего полученного обновления  
    * **update** - Словарь, полученный от API MAX в процессе опроса API на обновления  
* **_check_text_length** (`text`) - Проверки длины строки `text`  
* **send_photo** (`chat_id`, `photo`, `caption`, `parse_mode`, `reply_markup`) - Отправляет сообщение с фото  
    * **chat_id** - Чат, куда надо отправить сообщение  
    * **photo** - Объект фото  
    * **caption** - Текст сообщения под фото  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
* **send_media_group** (`chat_id`, `media`, `caption`, `parse_mode`, `reply_markup`) - Отправляет сообщение с группой медиафайлов  
    * **chat_id** - Чат, куда надо отправить сообщение  
    * **media** - Список объектов медиа  
    * **caption** - Текст сообщения под фото  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
* **send_document** (`chat_id`, `document`, `caption`, `parse_mode`, `reply_markup`) - Отправляет сообщение с документом  
    * **chat_id** - Чат, куда надо отправить сообщение  
    * **document** - Объект документа  
    * **caption** - Текст сообщения под фото  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
    * **visible_file_name** - Объект клавиатуры  
* **send_document** (`chat_id`, `message_id`) - Метод удаления сообщения `message_id` в чате `chat_id`  
    * **chat_id** - Чат, куда надо отправить сообщение  
    * **message_id** - Уникальный идентификаторсообщения   
* **edit_message_text** (`text`, `chat_id`, `message_id`, `parse_mode`, `reply_markup`) - Редактирует текст сообщения  
    * **text** - Текст, на который надо заменить текущий  
    * **chat_id** - Чат, где надо изменить сообщение  
    * **message_id** - Идентификатор сообщения, которое надо поменять  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
* **edit_message_media** (`media`, `chat_id`, `message_id`, `parse_mode`, `reply_markup`) - Редактирует сообщение с медиа  
    * **media** - Медиа, на которое надо заменить текущее  
    * **chat_id** - Чат, где надо изменить сообщение  
    * **message_id** - Идентификатор сообщения, которое надо поменять  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
* **edit_message_reply_markup** (`chat_id`, `message_id`, `parse_mode`, `reply_markup`) - Редактирует клавиатуру сообщения  
    * **chat_id** - Чат, где надо изменить сообщение  
    * **message_id** - Идентификатор сообщения, которое надо поменять  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
* **send_message** (`chat_id`, `text`, `attachments`, `parse_mode`, `reply_markup`, `notify`) - Отправляет сообщение  
    * **chat_id** - Чат, где надо изменить сообщение  
    * **text** - Текст сообщения  
    * **attachments** - Вложения сообщения  
    * **parse_mode** - Формат сообщения  
    * **reply_markup** - Объект клавиатуры  
    * **notify** - Флаг звукового уведомления отправки сообщения  
* **get_message** (`message_id`) - Метод получения сообщения по айди  
    * **message_id** - Идентификатор сообщения, которое надо получить  
* **callback_query_handler** (`data` `**kwargs`) - Декоратор для регистрации обработчиков callback-запросов от inline-кнопок  
    * **data** - Данные кнопки для фильтрации  
    * **kwargs** - Дополнительные фильтры для обработчика  
* **add_callback_query_handler** (`handler_dict`) - Добавление обработчик callback-запросов напрямую  
    * **handler_dict** - Словарь обработчика событий  
* **_process_callback_query** (`callback`) - Обрабатывает входящий callback-запрос. Метод ищет подходящий обработчик среди зарегистрированных и вызывает первый соответствующий фильтрам  
    * **callback** - Объект callback-запроса  
