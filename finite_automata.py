# src/finite_automata.py
import networkx as nx

class FiniteAutomata:
    """
    Clase para crear y manipular autómatas finitos
    Métodos:
    - create_dfa(): Crear Autómata Finito Determinista
    - create_nfa(): Crear Autómata Finito No Determinista
    - validate_string(): Verificar aceptación de cadena
    """
    def __init__(self, states, initial_state, alphabet, final_states):
        self.states = states
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.final_states = final_states
        self.transition_function = {}
    
    def create_dfa(self):
        """
        Crea un Autómata Finito Determinista
        """
        # Lógica de construcción de AFD
        pass
    
    def validate_string(self, string):
        """
        Verifica si una cadena es aceptada por el autómata
        """
        # Algoritmo de validación de cadena
        pass