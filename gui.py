import tkinter as tk
from tkinter import messagebox
import os
import shutil

# Función para organizar el folder
def organize_folder(folder):
    file_types = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.webp'],
        'Videos': ['.mp4', '.avi', '.mov', '.wlmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.csv', '.doc', '.odt'],
        'Archives': ['.zip', '.rar', '.cab', '.json'],
        'Setup Archives': ['.exe', '.msi']
    }

    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                for folder_name, extensions in file_types.items():
                    if ext in extensions:
                        target_folder = os.path.join(folder, folder_name)
                        os.makedirs(target_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(target_folder, filename))
                        print(f'Moved {filename} to {folder_name}')
        # Mensaje de éxito al organizar el folder
        messagebox.showinfo("Éxito", "¡Los archivos fueron organizados exitosamente!")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Función que se llama al presionar el botón
def on_button_click():
    folder_path = folder_entry.get()  # Obtener la ruta del input de texto
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        organize_folder(folder_path)  # Llamar a la función para organizar los archivos
    else:
        messagebox.showerror("Error", "La carpeta no existe. Por favor, verifique la ruta.")

def clear_input():
    folder_entry.delete(0, tk.END) 

# Crear la ventana principal
root = tk.Tk()
root.title("File Organizer 📁")

# Etiqueta para el campo de texto
label = tk.Label(root, text="Introduce la ruta del folder:")
label.pack(pady=10)

# Campo de texto para ingresar la ruta del folder
folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=10)

# Botón para organizar el folder
organize_button = tk.Button(root, text="Organizar Archivos", command=on_button_click)
organize_button.pack(pady=20)


# Botón para limpiar el campo de texto
clear_button = tk.Button(root, text="Borrar", command=clear_input)
clear_button.pack(pady=5)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
