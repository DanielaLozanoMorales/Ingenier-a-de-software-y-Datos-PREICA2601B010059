# Actualización de código fuente del proyecto. 

import tkinter as tk
from tkinter import ttk, messagebox

class AutosColombiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autos Colombia - Iteración 2")
        self.root.geometry("800x500")
        self.root.configure(bg="#27ae60") # Fondo verde principal

        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background="#27ae60")
        style.configure("TFrame", background="#ffffff")

        # Pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill='both')

        self.tab_usuarios = ttk.Frame(self.notebook)
        self.tab_celdas = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_usuarios, text="Gestión de Usuarios")
        self.notebook.add(self.tab_celdas, text="🅿Mapa de Celdas")

        self.setup_tab_usuarios()
        self.setup_tab_celdas()

    # --- MÓDULO 1: GESTIÓN DE USUARIOS ---
    def setup_tab_usuarios(self):
        lbl_titulo = tk.Label(self.tab_usuarios, text="Registro de Mensualidades", font=("Arial", 16, "bold"), bg="white", fg="#27ae60")
        lbl_titulo.pack(pady=10)

        # Formulario
        frame_form = tk.Frame(self.tab_usuarios, bg="white")
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nombre:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(frame_form)
        self.ent_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Placa:", bg="white").grid(row=0, column=2, padx=5, pady=5)
        self.ent_placa = ttk.Entry(frame_form)
        self.ent_placa.grid(row=0, column=3, padx=5, pady=5)

        btn_registrar = tk.Button(frame_form, text="+ Registrar Usuario", bg="#27ae60", fg="white", command=self.registrar_usuario)
        btn_registrar.grid(row=0, column=4, padx=15, pady=5)

        # Tabla de usuarios
        columnas = ("Nombre", "Placa", "Estado")
        self.tree_usuarios = ttk.Treeview(self.tab_usuarios, columns=columnas, show="headings")
        for col in columnas:
            self.tree_usuarios.heading(col, text=col)
        self.tree_usuarios.pack(fill='both', expand=True, padx=20, pady=10)

    def registrar_usuario(self):
        nombre = self.ent_nombre.get()
        placa = self.ent_placa.get()
        if nombre and placa:
            self.tree_usuarios.insert("", tk.END, values=(nombre, placa.upper(), "Activo 🟢"))
            self.ent_nombre.delete(0, tk.END)
            self.ent_placa.delete(0, tk.END)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        else:
            messagebox.showwarning("Error", "Por favor complete todos los campos.")

    # --- MÓDULO 2: MAPA DE CELDAS ---
    def setup_tab_celdas(self):
        lbl_titulo = tk.Label(self.tab_celdas, text="Mapa de Disponibilidad", font=("Arial", 16, "bold"), bg="white", fg="#27ae60")
        lbl_titulo.pack(pady=10)

        frame_grid = tk.Frame(self.tab_celdas, bg="white")
        frame_grid.pack(pady=10)

        self.botones_celdas = []
        # Crear 10 celdas de ejemplo
        for i in range(10):
            btn = tk.Button(frame_grid, text=f"Celda {i+1}\nLibre", bg="#2ecc71", fg="white", width=12, height=4, 
                            command=lambda c=i: self.asignar_celda(c))
            btn.grid(row=i//5, column=i%5, padx=10, pady=10)
            self.botones_celdas.append(btn)

    def asignar_celda(self, index):
        btn = self.botones_celdas[index]
        estado_actual = btn.cget("text")

        if "Libre" in estado_actual:
            # Simular ingreso
            btn.config(text=f"Celda {index+1}\nOCUPADA", bg="#e74c3c")
        else:
            # Simular salida
            if messagebox.askyesno("Liberar Celda", "¿Desea registrar la salida y liberar esta celda?"):
                btn.config(text=f"Celda {index+1}\nLibre", bg="#2ecc71")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutosColombiaApp(root)
    root.mainloop()