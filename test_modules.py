# tests/test_modules.py
import pytest
from language_checker import LanguageChecker
from finite_automata import FiniteAutomata
from automata_reducer import AutomataReducer

class TestLanguageSimulator:
    def test_language_regularity(self):
        """
        Prueba la verificación de regularidad de lenguajes
        """
        checker = LanguageChecker("(ab)*")
        assert checker.check_regularity() == True
    
    def test_finite_automata(self):
        """
        Prueba la creación y validación de autómatas finitos
        """
        states = {'q0', 'q1', 'q2'}
        automata = FiniteAutomata(
            states=states,
            initial_state='q0',
            alphabet={'a', 'b'},
            final_states={'q2'}
        )
        assert automata.validate_string("aba") == True
    
    def test_automata_reduction(self):
        """
        Prueba la reducción de autómatas
        """
        # Implementar lógica de prueba de reducción
        pass

# Ejecutar pruebas
def test_suite():
    pytest.main([__file__])