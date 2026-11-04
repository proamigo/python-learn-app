#!/usr/bin/env python3
"""
Python Learn - App principal para aprender Python en Android.
Kivy + REPL real + lecciones progresivas.
"""
import os
import sys

# Configurar Kivy antes de importar módulos gráficos
os.environ['KIVY_NO_ARGS'] = '1'
os.environ['KIVY_NO_CONFIG'] = '1'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.logger import Logger

# Importar módulos locales
from ui.lesson_screen import LessonScreen
from ui.terminal_screen import TerminalScreen
from ui.widgets import LessonListItem, CodeBlock
from utils.progress import ProgressManager
from utils.python_runner import PythonRunner
from lessons.curriculum import CURRICULUM


# KV Language para la UI principal
KV = '''
<MainTabbedPanel>:
    do_default_tab: False
    tab_width: root.width / 2
    tab_height: dp(56)

    TabbedPanelItem:
        text: 'Lecciones'
        background_normal: ''
        background_down: ''
        color: 1, 1, 1, 1
        background_color: app.theme_primary
        
        BoxLayout:
            orientation: 'vertical'
            LessonListView:
                id: lesson_list
                curriculum: root.curriculum
                progress_mgr: root.progress_mgr
                on_lesson_select: root.on_lesson_selected(*args)

    TabbedPanelItem:
        text: 'Terminal'
        background_normal: ''
        background_down: ''
        color: 1, 1, 1, 1
        background_color: app.theme_primary
        
        TerminalScreen:
            id: terminal_screen
            python_runner: root.python_runner
            progress_mgr: root.progress_mgr


<LessonScreen>:
    curriculum: root.curriculum
    progress_mgr: root.progress_mgr
    lesson_id: root.lesson_id
'''


class MainTabbedPanel(TabbedPanel):
    curriculum = ListProperty([])
    progress_mgr = ObjectProperty(None)
    python_runner = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.curriculum = CURRICULUM
        self.progress_mgr = ProgressManager()
        self.python_runner = PythonRunner()

    def on_lesson_selected(self, lesson_id):
        """Navegar a la pantalla de lección."""
        lesson_screen = LessonScreen(
            name=f'lesson_{lesson_id}',
            lesson_id=lesson_id,
            curriculum=self.curriculum,
            progress_mgr=self.progress_mgr
        )
        self.parent.add_widget(lesson_screen)
        self.parent.current = f'lesson_{lesson_id}'
        self.parent.transition = SlideTransition(direction='left')


class LessonListView(BoxLayout):
    curriculum = ListProperty([])
    progress_mgr = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = ['16dp', '16dp', '16dp', '16dp']
        self.spacing = '12dp'
        Clock.schedule_once(self.build_list, 0)

    def build_list(self, dt):
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.gridlayout import GridLayout
        from kivy.metrics import dp

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=dp(12), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        for module in self.curriculum:
            # Header del módulo
            from kivy.uix.label import Label
            module_label = Label(
                text=f'[b]{module["title"]}[/b]',
                markup=True,
                size_hint_y=None,
                height=dp(40),
                halign='left',
                valign='middle',
                color=(0.2, 0.6, 1, 1),
                font_size='18sp'
            )
            module_label.bind(size=module_label.setter('text_size'))
            grid.add_widget(module_label)

            # Lecciones del módulo
            for lesson in module['lessons']:
                progress = self.progress_mgr.get_lesson_progress(lesson['id'])
                item = LessonListItem(
                    lesson=lesson,
                    progress=progress,
                    on_release=lambda x, lid=lesson['id']: self.dispatch('on_lesson_select', lid)
                )
                grid.add_widget(item)

        scroll.add_widget(grid)
        self.add_widget(scroll)

    def on_lesson_select(self, lesson_id):
        pass


class LessonScreen(Screen):
    curriculum = ListProperty([])
    progress_mgr = ObjectProperty(None)
    lesson_id = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lesson = self.find_lesson(self.lesson_id)
        self.build_ui()

    def find_lesson(self, lesson_id):
        for module in self.curriculum:
            for lesson in module['lessons']:
                if lesson['id'] == lesson_id:
                    return lesson
        return None

    def build_ui(self):
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.metrics import dp

        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=dp(16), spacing=dp(12))

        # Header con botón volver
        header = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        back_btn = Button(
            text='← Volver',
            size_hint_x=None,
            width=dp(100),
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        back_btn.bind(on_release=self.go_back)
        title = Label(
            text=self.lesson['title'] if self.lesson else 'Lección',
            font_size='20sp',
            bold=True,
            halign='left',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        title.bind(size=title.setter('text_size'))
        header.add_widget(back_btn)
        header.add_widget(title)
        layout.add_widget(header)

        # Contenido de la lección
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', spacing=dp(16), size_hint_y=None, padding=[0, dp(8)])
        content.bind(minimum_height=content.setter('height'))

        if self.lesson:
            # Teoría
            theory_label = Label(
                text=self.lesson['theory'],
                markup=True,
                size_hint_y=None,
                halign='left',
                valign='top',
                color=(0.9, 0.9, 0.9, 1),
                font_size='15sp',
                line_height=1.5
            )
            theory_label.bind(texture_size=theory_label.setter('size'))
            theory_label.bind(width=lambda *x: theory_label.setter('text_size')(theory_label, (theory_label.width, None)))
            content.add_widget(theory_label)

            # Ejemplos de código
            for example in self.lesson.get('examples', []):
                code_block = CodeBlock(code=example['code'], explanation=example.get('explanation', ''))
                content.add_widget(code_block)

            # Ejercicio
            if 'exercise' in self.lesson:
                from kivy.uix.textinput import TextInput
                exercise_box = BoxLayout(orientation='vertical', spacing=dp(8), size_hint_y=None)
                exercise_box.bind(minimum_height=exercise_box.setter('height'))

                ex_label = Label(
                    text=f'[b]Ejercicio:[/b] {self.lesson["exercise"]["prompt"]}',
                    markup=True,
                    size_hint_y=None,
                    halign='left',
                    valign='top',
                    color=(1, 0.8, 0.2, 1)
                )
                ex_label.bind(texture_size=ex_label.setter('size'))
                exercise_box.add_widget(ex_label)

                code_input = TextInput(
                    hint_text='Escribe tu código aquí...',
                    size_hint_y=None,
                    height=dp(150),
                    font_name='RobotoMono-Regular',
                    font_size='14sp',
                    background_color=(0.1, 0.1, 0.15, 1),
                    foreground_color=(0.9, 0.9, 0.9, 1),
                    cursor_color=(0.2, 0.8, 1, 1)
                )
                exercise_box.add_widget(code_input)

                run_btn = Button(
                    text='▶ Ejecutar',
                    size_hint_y=None,
                    height=dp(48),
                    background_normal='',
                    background_color=(0.2, 0.7, 0.3, 1)
                )
                run_btn.bind(on_release=lambda x: self.run_exercise(code_input.text))
                exercise_box.add_widget(run_btn)

                self.exercise_output = Label(
                    text='',
                    markup=True,
                    size_hint_y=None,
                    halign='left',
                    valign='top',
                    color=(0.5, 1, 0.5, 1),
                    font_size='13sp',
                    font_name='RobotoMono-Regular'
                )
                self.exercise_output.bind(texture_size=self.exercise_output.setter('size'))
                exercise_box.add_widget(self.exercise_output)

                content.add_widget(exercise_box)

            # Botón completar lección
            complete_btn = Button(
                text='✓ Marcar como completada',
                size_hint_y=None,
                height=dp(48),
                background_normal='',
                background_color=(0.3, 0.6, 0.9, 1)
            )
            complete_btn.bind(on_release=self.complete_lesson)
            content.add_widget(complete_btn)

        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def run_exercise(self, code):
        """Ejecutar código del ejercicio en el REPL real."""
        result = self.parent.python_runner.run_code(code)
        if result['success']:
            self.exercise_output.text = f'[b]Salida:[/b]\n{result["output"]}'
            self.progress_mgr.save_exercise_attempt(self.lesson_id, code, True)
        else:
            self.exercise_output.text = f'[b]Error:[/b]\n{result["error"]}'
            self.progress_mgr.save_exercise_attempt(self.lesson_id, code, False)

    def complete_lesson(self, *args):
        self.progress_mgr.mark_lesson_complete(self.lesson_id)
        self.go_back()

    def go_back(self, *args):
        self.parent.current = 'main'
        self.parent.transition = SlideTransition(direction='right')
        Clock.schedule_once(lambda dt: self.parent.remove_widget(self), 0.3)


class PythonLearnApp(App):
    theme_primary = ListProperty([0.2, 0.4, 0.8, 1])
    theme_bg = ListProperty([0.08, 0.08, 0.12, 1])
    theme_surface = ListProperty([0.12, 0.12, 0.18, 1])

    def build(self):
        # Cargar KV
        Builder.load_string(KV)

        # Configurar tema
        from kivy.core.window import Window
        Window.clearcolor = self.theme_bg

        # Pantalla principal
        from kivy.uix.screenmanager import ScreenManager, Screen
        sm = ScreenManager()
        main_screen = Screen(name='main')
        main_screen.add_widget(MainTabbedPanel())
        sm.add_widget(main_screen)

        return sm


if __name__ == '__main__':
    PythonLearnApp().run()