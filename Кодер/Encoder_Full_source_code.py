# Кодування за допомогою бібліотеки Base64, яка вбудована в Python

import base64

#Фунція закодовування
def encode_base64(text):
    # Конвертуємо текст в байтовий формат
    text_bytes = text.encode('utf-8')

    # Кодуємо байти у форматі Base64
    encoded_bytes = base64.b64encode(text_bytes)

    # Перетворюємо закодовані байти у строку
    encoded_text = encoded_bytes.decode('utf-8')

    # Повертаємо закодований текст
    return encoded_text

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

# Запитуємо текст у користувача
message = input("Введіть текст для кодування: ")

# Закодовуємо текст
encoded_message = encode_base64(message)
print("Закодований текст:", encoded_message)

# Декодуємо закодований текст
decoded_message = decode_base64(encoded_message)
print("Розкодований текст:", decoded_message)

input("Натисніть Enter для закриття програми")