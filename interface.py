import tkinter as tk
from tkinter import font
from translate_services import google_translate, albit_translator

# Функция для перевода текста с помощью API
def translate():
    text = input_text.get("1.0", tk.END).strip()
    google_result = google_translate(text)
    google_output.delete("1.0", tk.END)
    google_output.insert(tk.END, google_result)
    libre_result = albit_translator(text)
    libre_output.delete("1.0", tk.END)
    libre_output.insert(tk.END, libre_result)

# Главное окно приложения
root = tk.Tk()
root.title("Сравнение текстовых переводчиков")

# Настройка размеров окна
root.geometry("800x600")

#Шрифты
default_font = tk.font.Font(family="Arial", size=12)
label_font = font.Font(family="Arial", size=14, weight="bold")

# Поле для ввода текста
tk.Label(root, text="Введите текст для перевода:", font=label_font).pack(pady=10)
input_text = tk.Text(root, height=5, width=70, font=default_font)
input_text.pack(pady=10)

# Кнопка для запуска перевода
translate_button = tk.Button(root, text="Перевести", font=default_font, command=translate)
translate_button.pack(pady=15)

# Окно вывода для результата Google Translate
tk.Label(root, text="Результат Google Translate:", font=label_font).pack(pady=5)
google_output = tk.Text(root, height=5, width=70, font=default_font)
google_output.pack(pady=10)

# Окно вывода для результата Albit Translator
tk.Label(root, text="Результат Albit Translator:", font=label_font).pack(pady=5)
libre_output = tk.Text(root, height=5, width=70, font=default_font)
libre_output.pack(pady=10)

# Запуск основного цикла приложения
root.mainloop()
