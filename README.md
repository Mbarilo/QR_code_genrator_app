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
<p style="font-size: 25px; display: inline; position: relative; top: 3px; left: 5px">Windows</p>
</summary>
<p></p>

4. Create a virtual environment
```sh
python -m venv venv
```

5. Activate the virtual environment
```sh
.\venv\Scripts\activate
```

6. Install dependencies from the requirements.txt file
```sh
pip install -r requirements.txt
```

7. Run the project
```sh
python manage.py runserver
```
</details>

<details>
<summary>
<p style="font-size: 25px; display: inline; position: relative; top: 3px; left: 5px">MacOS</p>
</summary>
<p></p>

4. Create a virtual environment
```sh
python3 -m venv venv
```

5. Activate the virtual environment
```sh
source venv/bin/activate
```

6. Install dependencies from the requirements.txt file
```sh
pip3 install -r requirements.txt
```

7. Run the project
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

#### Десктопна підписка
Для зручності можна реалізувати десктопну версію сервісу з підпискою, що дозволяє зробити окремі "desktop" qr-коди, які можуть зберігати якийсь текст, контактну інформацію ...

---

# Висновок
Працюючи над QR-code Generator App, наша команда здобула цінний досвід у розробці веб-додатків на Django. Ми краще розібралися у структурі цього фреймворку, налаштуванні маршрутів, роботі з формами та взаємодії із зовнішніми бібліотеками для генерації та кастомізації QR-кодів.

Окремим викликом стало впровадження гнучких налаштувань дизайну QR-кодів — зміна кольорів, форм та додавання логотипів. Це дало нам змогу глибше зрозуміти роботу з графічними форматами та оптимізацією зображень.

Загалом, QR-code Generator App став для нас чудовим практичним кейсом, який допоміг не лише закріпити знання з Django, а й освоїти нові підходи до роботи з графікою, інтеграцією кастомних функцій та покращення користувацького досвіду.