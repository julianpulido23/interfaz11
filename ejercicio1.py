import tkinter as tk
from tkinter import ttk, messagebox

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo, self.isbn, self.autor, self.categoria = titulo, isbn, autor, categoria

    def mostrar_info(self):
        return f"Libro: {self.titulo}, ISBN: {self.isbn}, Autor: {self.autor.nombre} {self.autor.apellido}, Categoría: {self.categoria.nombre}"

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre, self.apellido = nombre, apellido

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre, self.apellido, self.id_usuario = nombre, apellido, id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido} (ID: {self.id_usuario})"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro, self.usuario = libro, usuario
        self.fecha_prestamo, self.fecha_devolucion = fecha_prestamo, fecha_devolucion

class Biblioteca:
    def __init__(self):
        self.libros, self.usuarios, self.prestamos = [], [], []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)

    def devolver_libro(self, prestamo, fecha_devolucion):
        prestamo.fecha_devolucion = fecha_devolucion

    def mostrar_libros(self):
        return [libro.mostrar_info() for libro in self.libros]

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class App:
    def __init__(self, root, biblioteca):
        self.root = root
        self.biblioteca = biblioteca
        self.root.title("Gestión de Biblioteca")
        self.root.configure(bg='black')
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('Black.TFrame', background='black')
        style.configure('Black.TLabel', background='black', foreground='white')
        style.configure('Black.TButton', background='black', foreground='white')
        style.configure('Black.TEntry', background='white', foreground='black')
        style.configure('Black.TNotebook', background='black')

        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=1, fill='both')

        # Frame for managing books
        frame_books = ttk.Frame(notebook, style='Black.TFrame')
        notebook.add(frame_books, text='Libros')
        self.create_book_frame(frame_books)

        # Frame for managing users
        frame_users = ttk.Frame(notebook, style='Black.TFrame')
        notebook.add(frame_users, text='Usuarios')
        self.create_user_frame(frame_users)

        # Frame for managing loans
        frame_loans = ttk.Frame(notebook, style='Black.TFrame')
        notebook.add(frame_loans, text='Préstamos')
        self.create_loan_frame(frame_loans)

        notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def create_book_frame(self, frame):
        ttk.Label(frame, text="Título:", style='Black.TLabel').grid(row=0, column=0, padx=5, pady=5)
        self.titulo_entry = ttk.Entry(frame, style='Black.TEntry')
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="ISBN:", style='Black.TLabel').grid(row=1, column=0, padx=5, pady=5)
        self.isbn_entry = ttk.Entry(frame, style='Black.TEntry')
        self.isbn_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Autor (Nombre Apellido):", style='Black.TLabel').grid(row=2, column=0, padx=5, pady=5)
        self.autor_entry = ttk.Entry(frame, style='Black.TEntry')
        self.autor_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Categoría:", style='Black.TLabel').grid(row=3, column=0, padx=5, pady=5)
        self.categoria_entry = ttk.Entry(frame, style='Black.TEntry')
        self.categoria_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Registrar Libro", command=self.registrar_libro, style='Black.TButton').grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.libros_listbox = tk.Listbox(frame, bg='black', fg='white')
        self.libros_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    def create_user_frame(self, frame):
        ttk.Label(frame, text="Nombre:", style='Black.TLabel').grid(row=0, column=0, padx=5, pady=5)
        self.nombre_usuario_entry = ttk.Entry(frame, style='Black.TEntry')
        self.nombre_usuario_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Apellido:", style='Black.TLabel').grid(row=1, column=0, padx=5, pady=5)
        self.apellido_usuario_entry = ttk.Entry(frame, style='Black.TEntry')
        self.apellido_usuario_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="ID Usuario:", style='Black.TLabel').grid(row=2, column=0, padx=5, pady=5)
        self.id_usuario_entry = ttk.Entry(frame, style='Black.TEntry')
        self.id_usuario_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Registrar Usuario", command=self.registrar_usuario, style='Black.TButton').grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.usuarios_listbox = tk.Listbox(frame, bg='black', fg='white')
        self.usuarios_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    def create_loan_frame(self, frame):
        ttk.Label(frame, text="Libro (ISBN):", style='Black.TLabel').grid(row=0, column=0, padx=5, pady=5)
        self.libro_prestamo_entry = ttk.Entry(frame, style='Black.TEntry')
        self.libro_prestamo_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Usuario (ID):", style='Black.TLabel').grid(row=1, column=0, padx=5, pady=5)
        self.usuario_prestamo_entry = ttk.Entry(frame, style='Black.TEntry')
        self.usuario_prestamo_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Fecha Préstamo:", style='Black.TLabel').grid(row=2, column=0, padx=5, pady=5)
        self.fecha_prestamo_entry = ttk.Entry(frame, style='Black.TEntry')
        self.fecha_prestamo_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Fecha Devolución:", style='Black.TLabel').grid(row=3, column=0, padx=5, pady=5)
        self.fecha_devolucion_entry = ttk.Entry(frame, style='Black.TEntry')
        self.fecha_devolucion_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Realizar Préstamo", command=self.realizar_prestamo, style='Black.TButton').grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.prestamos_listbox = tk.Listbox(frame, bg='black', fg='white')
        self.prestamos_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    def registrar_libro(self):
        titulo = self.titulo_entry.get()
        isbn = self.isbn_entry.get()
        autor_nombre, autor_apellido = self.autor_entry.get().split()
        categoria_nombre = self.categoria_entry.get()

        autor = Autor(autor_nombre, autor_apellido)
        categoria = Categoria(categoria_nombre)
        libro = Libro(titulo, isbn, autor, categoria)

        self.biblioteca.registrar_libro(libro)
        self.actualizar_libros_listbox()

        messagebox.showinfo("Éxito", "Libro registrado exitosamente")

    def registrar_usuario(self):
        nombre = self.nombre_usuario_entry.get()
        apellido = self.apellido_usuario_entry.get()
        id_usuario = self.id_usuario_entry.get()

        usuario = Usuario(nombre, apellido, id_usuario)
        self.biblioteca.registrar_usuario(usuario)
        self.actualizar_usuarios_listbox()

        messagebox.showinfo("Éxito", "Usuario registrado exitosamente")

    def realizar_prestamo(self):
        isbn = self.libro_prestamo_entry.get()
        id_usuario = self.usuario_prestamo_entry.get()
        fecha_prestamo = self.fecha_prestamo_entry.get()
        fecha_devolucion = self.fecha_devolucion_entry.get()

        libro = next((libro for libro in self.biblioteca.libros if libro.isbn == isbn), None)
        usuario = next((usuario for usuario in self.biblioteca.usuarios if usuario.id_usuario == id_usuario), None)

        if libro and usuario:
            self.biblioteca.realizar_prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
            self.actualizar_prestamos_listbox()
            messagebox.showinfo("Éxito", "Préstamo realizado exitosamente")
        else:
            messagebox.showerror("Error", "Libro o Usuario no encontrado")

    def actualizar_libros_listbox(self):
        self.libros_listbox.delete(0, tk.END)
        for libro_info in self.biblioteca.mostrar_libros():
            self.libros_listbox.insert(tk.END, libro_info)

    def actualizar_usuarios_listbox(self):
        self.usuarios_listbox.delete(0, tk.END)
        for usuario in self.biblioteca.usuarios:
            self.usuarios_listbox.insert(tk.END, usuario.mostrar_info())

    def actualizar_prestamos_listbox(self):
        self.prestamos_listbox.delete(0, tk.END)
        for prestamo in self.biblioteca.prestamos:
            prestamo_info = (f"Libro: {prestamo.libro.titulo}, Usuario: {prestamo.usuario.nombre} {prestamo.usuario.apellido}, "
                             f"Fecha de Préstamo: {prestamo.fecha_prestamo}, Fecha de Devolución: {prestamo.fecha_devolucion}")
            self.prestamos_listbox.insert(tk.END, prestamo_info)

    def on_tab_change(self, event):
        self.update_tab_style(event)

    def update_tab_style(self, event):
        notebook = self.root.nametowidget(event.widget)
        for tab_index in range(len(notebook.tabs())):
            notebook.tab(tab_index, background='black')

if __name__ == "__main__":
    root = tk.Tk()
    biblioteca = Biblioteca()
    app = App(root, biblioteca)
    root.mainloop()
