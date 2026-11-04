"""
Pantalla de lecciones - vista de lista y detalle.
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.clock import Clock


class LessonListItem(Button):
    """Item individual de lección en la lista."""
    lesson = ObjectProperty(None)
    progress = NumericProperty(0)  # 0-100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.15, 0.15, 0.2, 1)
        self.halign = 'left'
        self.valign = 'middle'
        self.padding = [dp(16), dp(12)]
        self.bind(size=self._update_text)
        Clock.schedule_once(self._update_text, 0)

    def _update_text(self, *args):
        if self.lesson:
            status = "✓" if self.progress >= 100 else f"{int(self.progress)}%"
            self.text = f"[b]{self.lesson['title']}[/b]\n[size=12sp][color=#888]{status} completado[/color][/size]"
            self.markup = True
            self.text_size = (self.width - dp(32), None)


class CodeBlock(BoxLayout):
    """Bloque de código con resaltado simple y explicación."""
    code = StringProperty('')
    explanation = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(8)
        self.padding = [dp(12), dp(8)]
        self.size_hint_y = None
        Clock.schedule_once(self.build_content, 0)

    def build_content(self, dt):
        from kivy.uix.label import Label
        from kivy.metrics import dp

        # Explicación
        if self.explanation:
            exp = Label(
                text=f"[i]{self.explanation}[/i]",
                markup=True,
                size_hint_y=None,
                halign='left',
                valign='top',
                color=(0.6, 0.8, 1, 1),
                font_size='13sp'
            )
            exp.bind(texture_size=exp.setter('size'))
            exp.bind(width=lambda *x: exp.setter('text_size')(exp, (exp.width, None)))
            self.add_widget(exp)

        # Código en monospace
        code_label = Label(
            text=self.code,
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top',
            font_name='RobotoMono-Regular',
            font_size='13sp',
            color=(0.9, 0.9, 0.9, 1),
            line_height=1.4
        )
        code_label.bind(texture_size=code_label.setter('size'))
        code_label.bind(width=lambda *x: code_label.setter('text_size')(code_label, (code_label.width, None)))
        self.add_widget(code_label)

        # Fondo visual
        from kivy.graphics import Color, Rectangle
        with self.canvas.before:
            Color(0.1, 0.1, 0.15, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size