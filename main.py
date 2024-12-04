# main.py
import tkinter as tk
from main_window import MainWindow
from language_checker import LanguageChecker
from finite_automata import FiniteAutomata

class FormalLanguageSimulator:
    """
    Clase principal que inicializa y coordina 
    componentes del simulador
    """
    def __init__(self):
        # Inicializar componentes principales
        self.root = tk.Tk()
        self.main_window = None
        self.language_checker = LanguageChecker
        self.finite_automata = FiniteAutomata
    
    def initialize_gui(self):
        """
        Configura la interfaz gráfica principal
        """
        self.main_window = MainWindow(self.root)
    
    def run(self):
        """
        Inicia la aplicación
        """
        self.initialize_gui()
        self.root.mainloop()

def main():
    """
    Punto de entrada del programa
    """
    simulator = FormalLanguageSimulator()
    simulator.run()

if __name__ == "__main__":
    main()
    