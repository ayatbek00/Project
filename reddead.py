from tkinter import *
from tkinter import messagebox

root = Tk()
root.attributes("-fullscreen", True)
root.configure(bg="red")  # синий экран

def close(event):
    root.destroy()

# смайлик как в BSOD
sad = Label(root, text=":(", fg="white", bg="red", font=("Segoe UI", 120))
sad.pack(anchor="nw", padx=100, pady=(50, 0))

# основной текст
text = Label(
    root,
    text="Ваш компьютер столкнулся с проблемой и должен быть перезагружен.\n"
         "Мы лишь собираем некоторые сведения об ошибке.\n"
         "Затем будет выполнена автоматическая перезагрузка.",
    fg="white",
    bg="red",
    font=("Segoe UI", 24),
    justify="left"
)
text.pack(anchor="nw", padx=100, pady=20)

# проценты
percent = Label(root, text="0%", fg="white", bg="red", font=("Segoe UI", 28))
percent.pack(anchor="nw", padx=100, pady=20)

# код ошибки
bottom = Label(
    root,
    text="Если хотите узнать больше, найдите: TEBE_POLNIY_PIZDEC",
    fg="white",
    bg="red",
    font=("Segoe UI", 18),
    justify="left"
)
bottom.pack(anchor="nw", padx=100, pady=80)

def update_percent(i=0):
    if i <= 100:
        percent.config(text=f"{i}%")

        # зависание на 99%
        if i == 99:
            root.after(2000, update_percent, i + 1)
            return

        # сообщение на 100%
        if i == 100:
            messagebox.showerror("ERROR 404", "Не получилось перезагрузить компьютер")
            return

        root.after(120, update_percent, i + 1)

update_percent()

root.bind("<Escape>", close)

root.mainloop()