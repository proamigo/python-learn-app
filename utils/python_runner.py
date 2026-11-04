"""
Ejecutor de Python seguro para ejercicios y terminal.
Aísla namespace, captura stdout/stderr, timeout opcional.
"""
import code
import io
import sys
import traceback
import threading
import time
from contextlib import redirect_stdout, redirect_stderr
from typing import Dict, Any, Optional


class PythonRunner:
    """
    Ejecutor de código Python con namespace aislado.
    Usa code.InteractiveConsole para soportar bloques multilínea.
    """

    def __init__(self, timeout: float = 5.0):
        self.timeout = timeout
        self._namespace = self._create_safe_namespace()
        self._console = code.InteractiveConsole(self._namespace)

    def _create_safe_namespace(self) -> Dict[str, Any]:
        """Crear namespace seguro con builtins permitidos."""
        return {
            '__name__': '__main__',
            '__doc__': None,
            '__builtins__': {
                # Funciones básicas
                'print': print,
                'len': len,
                'range': range,
                'list': list,
                'dict': dict,
                'set': set,
                'tuple': tuple,
                'str': str,
                'int': int,
                'float': float,
                'bool': bool,
                'type': type,
                'isinstance': isinstance,
                'hasattr': hasattr,
                'getattr': getattr,
                'setattr': setattr,
                'dir': dir,
                'help': help,
                
                # Iteradores y funcionales
                'enumerate': enumerate,
                'zip': zip,
                'map': map,
                'filter': filter,
                'sorted': sorted,
                'reversed': reversed,
                'iter': iter,
                'next': next,
                'all': all,
                'any': any,
                
                # Matemáticas
                'sum': sum,
                'min': min,
                'max': max,
                'abs': abs,
                'round': round,
                'pow': pow,
                'divmod': divmod,
                
                # Excepciones
                'Exception': Exception,
                'ValueError': ValueError,
                'TypeError': TypeError,
                'KeyError': KeyError,
                'IndexError': IndexError,
                'FileNotFoundError': FileNotFoundError,
                'ZeroDivisionError': ZeroDivisionError,
                'AttributeError': AttributeError,
                'ImportError': ImportError,
                'NameError': NameError,
                'SyntaxError': SyntaxError,
                'RuntimeError': RuntimeError,
                'StopIteration': StopIteration,
                
                # Entrada/salida (limitado)
                'input': input,
                'open': open,
                
                # Otros
                'object': object,
                'property': property,
                'staticmethod': staticmethod,
                'classmethod': classmethod,
                'super': super,
            }
        }

    def run_code(self, code_text: str) -> Dict[str, Any]:
        """
        Ejecutar código y retornar resultado.
        
        Returns:
            dict: {'success': bool, 'output': str, 'error': str|None}
        """
        if not code_text.strip():
            return {'success': True, 'output': '', 'error': None}

        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                more = self._console.push(code_text)
            
            stdout = stdout_capture.getvalue()
            stderr = stderr_capture.getvalue()
            
            if stderr and not stdout:
                return {'success': False, 'error': stderr.strip(), 'output': ''}
            
            return {
                'success': True, 
                'output': stdout.rstrip('\n'), 
                'error': None,
                'incomplete': more  # True si el bloque está incompleto (ej. def sin cerrar)
            }
            
        except SystemExit:
            return {'success': False, 'error': 'SystemExit: no permitido', 'output': ''}
        except KeyboardInterrupt:
            return {'success': False, 'error': 'KeyboardInterrupt', 'output': ''}
        except Exception as e:
            return {'success': False, 'error': traceback.format_exc(), 'output': ''}

    def run_code_with_timeout(self, code_text: str) -> Dict[str, Any]:
        """Ejecutar con timeout en hilo separado (para código potencialmente infinito)."""
        result = {'done': False}
        
        def target():
            result['value'] = self.run_code(code_text)
            result['done'] = True
        
        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()
        thread.join(self.timeout)
        
        if not result['done']:
            # Timeout - no hay forma limpia de matar el hilo en Python
            return {
                'success': False, 
                'error': f'Timeout ({self.timeout}s) — posible bucle infinito', 
                'output': ''
            }
        
        return result['value']

    def reset(self):
        """Reiniciar namespace limpio."""
        self._namespace = self._create_safe_namespace()
        self._console = code.InteractiveConsole(self._namespace)

    def get_namespace(self) -> Dict[str, Any]:
        """Obtener copia del namespace actual (para inspección)."""
        return self._namespace.copy()

    def set_variable(self, name: str, value: Any):
        """Inyectar variable en el namespace."""
        self._namespace[name] = value

    def get_variable(self, name: str) -> Any:
        """Obtener variable del namespace."""
        return self._namespace.get(name)


class SafePythonRunner(PythonRunner):
    """
    Versión más restrictiva: sin acceso a filesystem, red, etc.
    Útil para evaluar código de usuarios no confiables.
    """
    
    def _create_safe_namespace(self) -> Dict[str, Any]:
        ns = super()._create_safe_namespace()
        # Remover funciones peligrosas
        dangerous = ['open', 'input', '__import__', 'eval', 'exec', 'compile']
        for d in dangerous:
            ns['__builtins__'].pop(d, None)
        return ns