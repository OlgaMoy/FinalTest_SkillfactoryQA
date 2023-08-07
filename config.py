valid_email = "olgamoys@rambler.ru"
valid_pass = "M30Ol87!"

invalid_email = 'olgamoys15@rambler.ru'
invalid_pass = 'M30Ol87?'

name = 'Ольга'
surname = 'Мохова'
region = 'Тульская обл'
email = 'vish_enka07@mail.ru'
password = 'Add12345'

false_email = '345678'
false_mobile_max = '891275643437'
false_mobile_mini = '8953785652'
false_name_mini = 'B'
name_two_letters = "Ау"
thirty_letters = 'Вецезиабобонпгкзарордоенеопрнь'
thirty_one_letters = 'Вецезиабобонпгкзарордоенеопрньк'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'E-mail или мобильный телефон'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Продолжить'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'