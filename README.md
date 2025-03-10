# QR-code generator app

<details>
<summary>
English version
</summary>
<p></p>
QR-code generator app is an app for generating QR codes with the ability to create both standard and desktop codes. It supports customization: changing colors, shapes, and the option to add a logo to the QR code. A convenient tool for creating unique QR codes for various purposes.

---
### Information
- [Installation and Setup](#installation-and-setup)
- [Contributors](#contributors)
- [Technologies We Used](#technologies-we-used)
- [QR Codes](#qr-codes)
- [Conclusion](#conclusion)
---

# Installation and Setup

1. Get the repository link

![](media/readme/clone.png)

2. Clone the repository
```sh
git clone https://github.com/dimachep1408/QR-code_generator_app.git
```

3. Navigate to the project directory
```sh
cd QR-code_generator_app
```

<details>
<summary>
Windows
</summary>
<p></p>

1. Create a virtual environment
```sh
python -m venv venv
```

1. Activate the virtual environment
```sh
.\venv\Scripts\activate
```

1. Install dependencies from the requirements.txt file
```sh
pip install -r requirements.txt
```

1. Run the project
```sh
python manage.py runserver
```
</details>

<details>
<summary>
MacOS
</summary>
<p></p>

1. Create a virtual environment
```sh
python3 -m venv venv
```

1. Activate the virtual environment
```sh
source venv/bin/activate
```

1. Install dependencies from the requirements.txt file
```sh
pip3 install -r requirements.txt
```

1. Run the project
```sh
python3 manage.py runserver
```
</details>
<p></p>

# Contributors
1. [Dmytro Chepikov](https://github.com/dimachep1408)
2. [Dmytro Lomako](https://github.com/DmytroLomako)
3. [Misha Barylo](https://github.com/Mbarilo)
4. [Feliks Denga](https://github.com/Feliks2010)

---

# Technologies We Used

* Django – framework for backend and request processing.
* qrcode – generation and customization of QR codes.
* Pillow – working with images, saving QR codes.
* os – file system management, saving images.
* datetime – storing the creation time of the QR code.

---

# QR Codes

#### When generating a QR code, you can customize the following parameters:

* Data – link.
* Color – you can change the background and foreground colors.
* Logo – you can insert an image in the center of the QR code (e.g., a company logo).
* Dots form – shape of the QR code dots.
* Eye form – shape of the "eyes" (large squares in the corners of the QR code).

#### Desktop Subscription
For convenience, a desktop version of the service with a subscription can be implemented, allowing the creation of special "desktop" QR codes that can store text, contact information, and more.

---

# Conclusion

While working on the QR-Code Generator App, our team gained valuable experience in developing web applications with Django. We deepened our understanding of the framework’s structure, route configuration, form handling, and integration with external libraries for generating and customizing QR codes.

One of the main challenges was implementing flexible design settings for QR codes—changing colors, shapes, and adding logos. This allowed us to better understand working with graphic formats and image optimization.

Overall, the QR-Code Generator App became a great practical project for us, helping not only to reinforce our knowledge of Django but also to explore new approaches to working with graphics, integrating custom features, and improving the user experience.

---
</details>
<p></p>


QR-code generator app - додаток для генерації QR-кодів з можливістю створення стандартних та десктопних кодів. Підтримує кастомізацію: зміна кольору, форми та можливісь додати логотип до qr-коду. Зручний інструмент для створення унікальних QR-кодів для різних потреб.

---
### Інформація
- [Інсталяція та налаштування](#інсталяція-та-налаштування)
<!-- toc-disable -->
- [Учасники проекту](#учасники-проекту)
<!-- toc-disable -->
- [Технології які ми використовували](#технології-які-ми-використовували)
<!-- toc-disable -->
- [QR-коди](#qr-коди)
<!-- toc-disable -->
- [Висновок](#висновок)
---

# Інсталяція та налаштування

1. Отримання посилання на репозиторій

![](media/readme/clone.png)

2. Клонування репозиторію
```sh
git clone https://github.com/dimachep1408/QR-code_generator_app.git
```

3. Перехід до директорії проекту
```sh
cd QR-code_generator_app
```

<details>
<summary>
Windows
</summary>
<p></p>

4. Створення віртуального оточення
```sh
python -m venv venv
```

5. Активація віртуального оточення
```sh
.\venv\Scripts\activate
```

6. Встановлення залежностей з файлу requirements.txt
```sh
pip install -r requirements.txt
```

7. Запуск проекту
```sh
python manage.py runserver
```
</details>

<details>
<summary>
MacOS
</summary>
<p></p>

4. Створення віртуального оточення
```sh
python3 -m venv venv
```

5. Активація віртуального оточення
```sh
source venv/bin/activate
```

6. Встановлення залежностей з файлу requirements.txt
```sh
pip3 install -r requirements.txt
```

7. Запуск проекту
```sh
python3 manage.py runserver
```
</details>
<p></p>

---

**Віддалено (на PythonAnywhere):**
   - Увійдіть у свій акаунт на [PythonAnywhere](https://www.pythonanywhere.com/).
   - Перейдіть на вкладку "Consoles"
    ![](image-3.png)
   - Нажміть на bash ![](image-4.png)
   - Копіювати посилання проекта![](image-5.png)
   - Повернутися у консоль та написати `cd mysite`
   - Повирнутися у консоль та написати `git clone (Вставити ссилку)`
   - Повернутися у вкладку web та заминити "Code" як на зображені [](image-6.png)
   - Та нажати на вкладку "wsgi configuration"
   - Тепер треба замінити 16 рядок як на фото
   - ![](image-7.png)
   - Нажати на save Справа зверху, та повертаємось на сторінку назад
   - Повертаємось у консоль та прописуємо `cd ../.virtualenvs` та натискаємо Enter, пишемо `python -m venv shop_venv`, `cd bin` і `source activate`

   - Далі встановлюємо всі модулі які прописані вищє за допомогою `pip install назва модуля`
   - повернутися до web та оновити![](image-8.png)
   - натиснути на силку ![](image-9.png)

---

# Учасники проекту
1. [Dmytro Chepikov](https://github.com/dimachep1408)
2. [Dmytro Lomako](https://github.com/DmytroLomako)
3. [Misha Barylo](https://github.com/Mbarilo)
4. [Feliks Denga](https://github.com/Feliks2010)

---

# Технології, які ми використовували

* Django - фреймворк для бекенду та обробки запитів.
* qrcode – генерація та кастомізація QR-кодів.
* Pillow – робота із зображеннями, збереження QR-кодів.
* os – керування файловою системою, збереження зображень.
* datetime – збереження часу створення QR-коду.

---

# QR-коди

#### При генерації QR-коду можна налаштовувати такі параметри:

* Дані – посилання.
* Колір – можна змінювати колір фону та переднього плану.
* Логотип – можна вставити зображення у центр QR-коду (наприклад, логотип компанії).
* Dots form – форма точок QR-коду:
* Eye form – форма «очей» (великих квадратів у кутах QR-коду):

---

#### Десктопна підписка
Для зручності можна реалізувати десктопну версію сервісу з підпискою, що дозволяє зробити окремі "desktop" qr-коди, які можуть зберігати якийсь текст, контактну інформацію ...

---

# Висновок
Працюючи над QR-code Generator App, наша команда здобула цінний досвід у розробці веб-додатків на Django. Ми краще розібралися у структурі цього фреймворку, налаштуванні маршрутів, роботі з формами та взаємодії із зовнішніми бібліотеками для генерації та кастомізації QR-кодів.

Окремим викликом стало впровадження гнучких налаштувань дизайну QR-кодів — зміна кольорів, форм та додавання логотипів. Це дало нам змогу глибше зрозуміти роботу з графічними форматами та оптимізацією зображень.

Загалом, QR-code Generator App став для нас чудовим практичним кейсом, який допоміг не лише закріпити знання з Django, а й освоїти нові підходи до роботи з графікою, інтеграцією кастомних функцій та покращення користувацького досвіду.

---

## Проблематика
### Дизайн
Спочатку у нас були проблеми з дизайном. 1-й варіант нам не сподобався, 2-й був зовсім не практичний і ми довго не могли вирішити, який саме дизайн ми будемо використовувати, але ми зупинись на такому красивому и практичному варіанті дизайну.
### Створення QR-code
Ми дуже довго тестували функцію створення QR-кодів та видів їх змінювання. Але ми, все ж таки змогли це зробити