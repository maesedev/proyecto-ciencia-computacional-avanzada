# gui/main_window.py
import tkinter as tk
from tkinter import ttk, messagebox

class MainWindow:
    """
    Ventana principal de la aplicación de simulación de lenguajes formales
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Lenguajes Formales")
        self.root.geometry("800x600")
        
        self.create_menu()
        self.create_main_frame()
    
    def create_menu(self):
        """
        Crea el menú de opciones principal
        """
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú de Lenguajes
        language_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Lenguajes", menu=language_menu)
        language_menu.add_command(label="Verificar Regularidad", command=self.open_language_checker)
        
        # Menú de Autómatas
        automata_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Autómatas", menu=automata_menu)
        automata_menu.add_command(label="Crear Autómata Finito", command=self.open_finite_automata)
        automata_menu.add_command(label="Reducir Autómata", command=self.open_automata_reducer)
        
        # Menú de Máquinas Especiales
        special_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Máquinas Especiales", menu=special_menu)
        special_menu.add_command(label="Autómata de Pila", command=self.open_pushdown_automata)
        special_menu.add_command(label="Máquina de Turing", command=self.open_turing_machine)
    
    def create_main_frame(self):
        """
        Crea el frame principal de la aplicación
        """
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        welcome_label = ttk.Label(main_frame, text="Simulador de Lenguajes Formales", font=("Arial", 16))
        welcome_label.grid(row=0, column=0, pady=20)
    
    def open_language_checker(self):
        """
        Abre la ventana de verificación de regularidad de lenguajes
        """
        LanguageCheckerWindow(tk.Toplevel(self.root))
    
    def open_finite_automata(self):
        """
        Abre la ventana de creación de autómatas finitos
        """
        FiniteAutomataWindow(tk.Toplevel(self.root))
    
    def open_automata_reducer(self):
        """
        Abre la ventana de reducción de autómatas
        """
        AutomataReducerWindow(tk.Toplevel(self.root))
    
    def open_pushdown_automata(self):
        """
        Abre la ventana de autómatas de pila
        """
        PushdownAutomataWindow(tk.Toplevel(self.root))
    
    def open_turing_machine(self):
        """
        Abre la ventana de máquina de Turing
        """
        TuringMachineWindow(tk.Toplevel(self.root))

# Clases auxiliares para ventanas específicas
class LanguageCheckerWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Verificador de Regularidad")
        self.create_widgets()
    
    def create_widgets(self):
        # Implementación de widgets para verificación de regularidad
        pass

class FiniteAutomataWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Autómatas Finitos")
        self.create_widgets()
    
    def create_widgets(self):
        # Implementación de widgets para autómatas finitos
        pass

# Continúan clases similares para otros módulos