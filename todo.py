import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

# ==================== ФУНКЦИИ ====================
def addition():
    text = ent.get()

    if text.strip():
        listbox.insert(tk.END, text)
    else:
        messagebox.showwarning("ОШИБКА", 'Поле не может быть пустым, введите задачу')

def removal():
    list_index = listbox.curselection()
    if list_index:
        listbox.delete(list_index)
    else:
        messagebox.showwarning("ОШИБКА", "выберите задачу для удаления")

def completed():
    list_index = listbox.curselection()
    
    if list_index:
        index = list_index[0]
        current_text = listbox.get(index)
        if "[ВЫПОЛНЕНО]" not in current_text:
            listbox.delete(index)
            listbox.insert(index, f"[ВЫПОЛНЕНО] {current_text}")
        elif "[ВЫПОЛНЕНО]" in current_text:
            clean = current_text.replace("[ВЫПОЛНЕНО]", "").strip()
            listbox.delete(index)
            listbox.insert(index, clean)

# ==================== ГРАФИЧЕСКИЙ ИНТЕРФЕЙС ====================
root = tk.Tk()
root.title('ToDo List')
root.geometry('400x480')
root.configure(bg='lightgray')

# ==================== СОЗДАНИЕ ВИДЖЕТОВ ====================
add = tk.Button(root, text = 'Добавить', command=addition, width=13, height=2 )#----------- добавление 
delete = tk.Button(root, text = 'Удалить', command=removal, width=13, height=2 )#----------- удаление 
comp = tk.Button(root, text = 'Выполнено', command=completed, width=13, height=2)#----------- статус выполнено 

ent = tk.Entry(root, width=50,)

#список задач и скроллинг 
listbox = Listbox(root, width=50, height=20)
scrollbar = Scrollbar(root, command=listbox.yview,)

# ==================== РАЗМЕЩЕНИЕ ВИДЖЕТОВ ====================
add.place(relx=0.08, rely=0.06,)
delete.place(relx=0.37, rely=0.06,)
comp.place(relx=0.65, rely=0.06,)
ent.place(relx=0.1, rely=0.15,)
listbox.place(relx=0.1, rely=0.2)
scrollbar.place(relx=0.88, rely=0.22, width=20, height=300)

# ==================== ЗАПУСК ПРИЛОЖЕНИЯ ====================
root.mainloop()