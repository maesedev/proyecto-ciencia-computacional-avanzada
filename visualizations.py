# gui/visualizations.py
import graphviz

class AutomataVisualizer:
    """
    Clase para visualizar autómatas usando Graphviz
    """
    @staticmethod
    def visualize_automata(automata):
        """
        Renderiza un autómata como un grafo
        """
        dot = graphviz.Digraph(comment='Autómata')
        
        # Lógica de renderizado de autómata
        return dot

# Punto de entrada principal
# main.py
import tkinter as tk
from main_window import MainWindow

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()