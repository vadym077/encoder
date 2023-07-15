# Кодування за допомогою бібліотеки Base64, яка вбудована в Python

import base64

#Функція декодування
def decode_base64(encoded_text):
    # Конвертуємо закодований текст у байтовий формат
    encoded_bytes = encoded_text.encode('utf-8')

    # Декодуємо байти у форматі Base64
    decoded_bytes = base64.b64decode(encoded_bytes)

    # Перетворюємо декодовані байти у строку
    decoded_text = decoded_bytes.decode('utf-8')

    # Повертаємо розкодований текст
    return decoded_text

# Запитуємо закодований текст у користувача
encoded_message = input("Введіть закодований текст: ")

# Декодуємо закодований текст
decoded_message = decode_base64(encoded_message)
print("Розкодований текст:", decoded_message)

input("Натисніть Enter для закриття програми")