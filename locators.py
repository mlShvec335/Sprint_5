from selenium.webdriver.common.by import By


class TestLocators:
    NANE_INPUT = By.XPATH, ".//label[text()='Имя']/following-sibling::input"  # Поле ввода имени
    EMAIL_INPUT = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # Поле ввода почты
    PASSWORD_INPUT = By.XPATH, ".//input[@name='Пароль']"  # Поле ввода пароля
    REGISTRATION_BTN = By.XPATH, ".//button[text()='Зарегистрироваться']"   # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = By.XPATH, ".//p[contains(@class, 'input__error')]"  # Сообщение об некорректном пароле
    LOGIN_IN_ACC_BTN = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"
    ACCOUNT_BTN = By.XPATH, ".//p[text()='Личный Кабинет']"  # Кнопка "Личный кабинет"
    LOGIN_BTN = By.XPATH, ".//button[text()='Войти']"  # Кнопка "Войти"
    LOGIN_LINK_BTN = By.XPATH, ".//a[@href='/login']"  # Кнопка(ссылка) "Войти"
    CONSTRUCTOR_BTN = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка "Конструктор"
    CONSTRUCTOR_TITLE = By.XPATH, ".//h1[text()='Соберите бургер']"  # Заголовок страницы Конструктор
    LOGO_BTN = By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]"  # Лого страницы
    LOGOUT_BTN = By.XPATH, ".//button[text()='Выход']"  # Кнопка "Выход"
    BUNS_BTN = By.XPATH, ".//span[text()='Булки']"  # Кнопка "Булки"
    BUNS_SECTION = By.XPATH, ".//h2[text()='Булки']"  # Раздел "Булки"
    BUNS_CURRENT = By.XPATH, ".//span[text()='Булки']/.."  # Выбранный раздел "Булки"
    SAUCE_BTN = By.XPATH, ".//span[text()='Соусы']"  # Кнопка "Соус"
    SAUCE_SECTION = By.XPATH, ".//h2[text()='Соусы']"  # Раздел "Соус"
    SAUCE_CURRENT = By.XPATH, ".//span[text()='Соусы']/.."  # Выбранный раздел "Соус"
    TOPPING_BTN = By.XPATH, ".//span[text()='Начинки']"  # Кнопка "Начинки"
    TOPPING_SECTION = By.XPATH, ".//h2[text()='Начинки']"  # Раздел "Начинки"
    TOPPING_CURRENT = By.XPATH, ".//span[text()='Начинки']/.."  # Выбранный раздел "Начинки"
