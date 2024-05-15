import customtkinter as ctk
import logic

#проверка выпадающего списка
def handle_pressing_widget_button():
    text = widget_entry.get()
    if widget_combobox.get() == "1. Шифр Атбаша":
        answer = logic.atbash(text)
        widget_unactive_entry.configure(state="normal")
        widget_unactive_entry.delete(0, "end")
        widget_unactive_entry.insert(0, answer)
        widget_unactive_entry.configure(state="readonly")
    elif widget_combobox.get() == "2. Шифр Цезаря":
        answer = logic.cezar(text)
        widget_unactive_entry.configure(state="normal")
        widget_unactive_entry.delete(0, "end")
        widget_unactive_entry.insert(0, answer)
        widget_unactive_entry.configure(state="readonly")
    else:
        answer = logic.morza(text)
        widget_unactive_entry.configure(state="normal")
        widget_unactive_entry.delete(0, "end")
        widget_unactive_entry.insert(0, answer)
        widget_unactive_entry.configure(state="readonly")

# цветовое оформление
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk() # создаём окно и привязываем его переменной root
root.title("creating a cipher") # название приложения
root.geometry("1000x500") # размер окна
my_font = ctk.CTkFont(family="Roboto", size=20) # шрифт

# текстовый виджет - Label
widget_label = ctk.CTkLabel(master=root)
widget_label.configure(text="Программа для шифрования текста", font=my_font)

# кнопка - Button
widget_button = ctk.CTkButton(master=root)
widget_button.configure(text="Зашифровать", font=my_font, command=handle_pressing_widget_button)

# однострочное поле для ввода - Entry
widget_entry = ctk.CTkEntry(master=root)
widget_entry.configure(font=my_font)

# выпадающий список для выбора одного элемента - ComboBox
elems = ["1. Шифр Атбаша", "2. Шифр Цезаря", "3. Азбука Морзе"]
widget_combobox = ctk.CTkComboBox(master=root)
widget_combobox.configure(font=my_font, values=elems, state="readonly")
widget_combobox.set("1. Шифр Атбаша")

# неактивное однострочное поле для ввода - Entry
widget_unactive_entry = ctk.CTkEntry(master=root)
widget_unactive_entry.configure(font=my_font)
widget_unactive_entry.insert(0, " ")
widget_unactive_entry.configure(
    state="readonly")
label_input, label_output = ctk.CTkLabel(master=root), ctk.CTkLabel(master=root)
label_input.configure(text="Ввод:", font=my_font)
label_output.configure(text="Вывод:", font=my_font)

# распологаем элементы в сетке
rows, columns = 7, 5
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
widget_label.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
widget_combobox.grid(row=1, column=1, columnspan=3, sticky="ew")
label_input.grid(row=2, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
label_output.grid(row=2, column=3, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
widget_entry.grid(row=3, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
widget_unactive_entry.grid(row=3, column=3, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
widget_button.grid(row=4, column=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
root.mainloop()
