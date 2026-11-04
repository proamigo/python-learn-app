"""
Terminal REPL real de Python embebido en Kivy.
Usa code.InteractiveConsole para ejecución real.
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import code
import sys
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr


class TerminalScreen(BoxLayout):
    """Terminal interactiva con REPL real de Python."""
    python_runner = ObjectProperty(None)
    progress_mgr = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(8)
        self.spacing = dp(8)
        self.console = code.InteractiveConsole()
        self.history = []
        self.history_index = 0
        self.current_input = ''
        Clock.schedule_once(self.build_ui, 0)

    def build_ui(self, dt):
        # Área de salida (scrollable)
        self.output_scroll = ScrollView(
            size_hint_y=1,
            do_scroll_x=False,
            bar_width=dp(4)
        )
        self.output_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=dp(4),
            padding=[dp(8), dp(8)]
        )
        self.output_layout.bind(minimum_height=self.output_layout.setter('height'))
        self.output_scroll.add_widget(self.output_layout)
        self.add_widget(self.output_scroll)

        # Línea de entrada
        input_box = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(8))
        
        self.prompt_label = Label(
            text='>>> ',
            size_hint_x=None,
            width=dp(50),
            font_name='RobotoMono-Regular',
            font_size='14sp',
            color=(0.2, 0.8, 1, 1),
            halign='right',
            valign='middle'
        )
        self.prompt_label.bind(size=self.prompt_label.setter('text_size'))

        self.input_field = TextInput(
            hint_text='Escribe código Python...',
            multiline=False,
            font_name='RobotoMono-Regular',
            font_size='14sp',
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(0.9, 0.9, 0.9, 1),
            cursor_color=(0.2, 0.8, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1),
            padding=[dp(8), dp(8)]
        )
        self.input_field.bind(on_text_validate=self.execute_input)
        self.input_field.bind(on_key_down=self.on_key_down)

        input_box.add_widget(self.prompt_label)
        input_box.add_widget(self.input_field)
        self.add_widget(input_box)

        # Botones de control
        controls = BoxLayout(size_hint_y=None, height=dp(44), spacing=dp(8))
        for text, callback in [
            ('Limpiar', self.clear_output),
            ('Reset REPL', self.reset_repl),
            ('Ejemplos', self.show_examples)
        ]:
            btn = Button(
                text=text,
                background_normal='',
                background_color=(0.2, 0.3, 0.5, 1),
                font_size='12sp'
            )
            btn.bind(on_release=callback)
            controls.add_widget(btn)
        self.add_widget(controls)

        # Mensaje de bienvenida
        self.append_output(
            "[color=#4ec9b0]Python Learn Terminal[/color]\n"
            "[color=#888]REPL real de Python 3.11 — escribe código y presiona Enter[/color]\n"
            "[color=#888]Comandos: limpiar, reset, ejemplos[/color]\n",
            is_system=True
        )
        Clock.schedule_once(lambda dt: setattr(self.input_field, 'focus', True), 0.1)

    def execute_input(self, instance):
        """Ejecutar código ingresado."""
        code_text = self.input_field.text.strip()
        if not code_text:
            return

        self.input_field.text = ''
        self.append_output(f">>> {code_text}", is_input=True)

        # Comandos especiales
        if code_text.lower() in ('limpiar', 'clear', 'cls'):
            self.clear_output()
            return
        elif code_text.lower() in ('reset', 'reiniciar'):
            self.reset_repl()
            return
        elif code_text.lower() in ('ejemplos', 'examples', 'help'):
            self.show_examples()
            return

        # Guardar en historial
        self.history.append(code_text)
        self.history_index = len(self.history)

        # Ejecutar en el REPL real
        result = self.python_runner.run_code(code_text)
        if result['success']:
            if result['output']:
                self.append_output(result['output'])
        else:
            self.append_output(f"[color=#ff6b6b]{result['error']}[/color]", is_error=True)

        # Actualizar prompt (>>> vs ...)
        self.update_prompt()

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        """Navegar historial con flechas arriba/abajo."""
        if keycode[1] == 'up' and self.history:
            self.history_index = max(0, self.history_index - 1)
            self.input_field.text = self.history[self.history_index]
            self.input_field.cursor = len(self.history[self.history_index])
        elif keycode[1] == 'down' and self.history:
            self.history_index = min(len(self.history), self.history_index + 1)
            if self.history_index >= len(self.history):
                self.input_field.text = ''
            else:
                self.input_field.text = self.history[self.history_index]
                self.input_field.cursor = len(self.history[self.history_index])

    def append_output(self, text, is_input=False, is_error=False, is_system=False):
        """Agregar línea al output."""
        label = Label(
            text=text,
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top',
            font_name='RobotoMono-Regular',
            font_size='13sp',
            line_height=1.3,
            color=(
                (0.5, 1, 0.5, 1) if is_error else
                (0.2, 0.8, 1, 1) if is_input else
                (0.6, 0.9, 0.6, 1) if is_system else
                (0.9, 0.9, 0.9, 1)
            )
        )
        label.bind(texture_size=label.setter('size'))
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width - dp(16), None)))
        self.output_layout.add_widget(label)
        # Auto-scroll
        Clock.schedule_once(lambda dt: setattr(self.output_scroll, 'scroll_y', 0), 0)

    def update_prompt(self):
        """Actualizar prompt según estado del REPL (>>> vs ...)."""
        # Simple: siempre >>> para code.InteractiveConsole
        self.prompt_label.text = '>>> '

    def clear_output(self, *args):
        """Limpiar área de salida."""
        self.output_layout.clear_widgets()
        self.append_output("[color=#888]Terminal limpiada[/color]", is_system=True)

    def reset_repl(self, *args):
        """Reiniciar el REPL (nuevo namespace)."""
        self.console = code.InteractiveConsole()
        self.python_runner.reset()
        self.clear_output()
        self.append_output("[color=#4ec9b0]REPL reiniciado — namespace limpio[/color]", is_system=True)

    def show_examples(self, *args):
        """Mostrar ejemplos rápidos."""
        examples = [
            ("2 + 2", "Aritmética básica"),
            ("'hola'.upper()", "Métodos de string"),
            ("[x**2 for x in range(5)]", "List comprehension"),
            ("def saludo(n): return f'Hola {n}'", "Definir función"),
            ("saludo('Mundo')", "Llamar función"),
        ]
        self.append_output("[color=#ffd700]Ejemplos rápidos:[/color]", is_system=True)
        for code, desc in examples:
            self.append_output(f"  [color=#888]# {desc}[/color]")
            self.append_output(f"  [color=#4ec9b0]{code}[/color]")
        self.append_output("[color=#888]Copia y pega en la terminal[/color]", is_system=True)


class PythonRunner:
    """Ejecutor de código Python seguro con captura de stdout/stderr."""

    def __init__(self):
        self.namespace = {
            '__name__': '__main__',
            '__doc__': None,
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
            'enumerate': enumerate,
            'zip': zip,
            'map': map,
            'filter': filter,
            'sorted': sorted,
            'sum': sum,
            'min': min,
            'max': max,
            'abs': abs,
            'round': round,
            'isinstance': isinstance,
            'hasattr': hasattr,
            'getattr': getattr,
            'setattr': setattr,
            'type': type,
            'Exception': Exception,
            'ValueError': ValueError,
            'TypeError': TypeError,
            'KeyError': KeyError,
            'IndexError': IndexError,
            'FileNotFoundError': FileNotFoundError,
            'ZeroDivisionError': ZeroDivisionError,
        }
        self.console = code.InteractiveConsole(self.namespace)

    def run_code(self, code_text):
        """Ejecutar código y capturar salida."""
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # code.InteractiveConsole maneja bloques multilínea
                more = self.console.push(code_text)
            
            stdout = stdout_capture.getvalue()
            stderr = stderr_capture.getvalue()
            
            if stderr:
                return {'success': False, 'error': stderr.strip(), 'output': stdout}
            
            return {'success': True, 'output': stdout.strip(), 'error': None}
            
        except Exception as e:
            return {'success': False, 'error': traceback.format_exc(), 'output': ''}

    def reset(self):
        """Reiniciar namespace."""
        self.__init__()