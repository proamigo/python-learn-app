"""
Gestión de progreso del usuario — persistencia local.
Usa JSON en app_user_data_dir (Kivy).
"""
import json
import os
from pathlib import Path
from kivy.utils import platform
from kivy.logger import Logger


def get_data_dir():
    """Directorio de datos de la app (multiplataforma)."""
    if platform == 'android':
        # En Android: /data/data/org.example.pythonlearn/files
        from android import activity
        from jnius import autoclass
        Environment = autoclass('android.os.Environment')
        context = activity.getApplicationContext()
        files_dir = context.getFilesDir()
        return Path(files_dir.getAbsolutePath())
    else:
        # Desktop: ~/.local/share/python-learn
        home = Path.home()
        data_dir = home / '.local' / 'share' / 'python-learn'
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir


class ProgressManager:
    """Maneja progreso de lecciones, ejercicios y estadísticas."""

    def __init__(self):
        self.data_dir = get_data_dir()
        self.progress_file = self.data_dir / 'progress.json'
        self.data = self.load()

    def load(self):
        """Cargar progreso desde archivo."""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                Logger.warning(f'ProgressManager: Error cargando progreso: {e}')
        return {
            'lessons_completed': {},
            'exercise_attempts': {},
            'stats': {
                'total_exercises': 0,
                'correct_exercises': 0,
                'lessons_finished': 0
            }
        }

    def save(self):
        """Guardar progreso a archivo."""
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            Logger.error(f'ProgressManager: Error guardando progreso: {e}')

    # --- Lecciones ---
    def get_lesson_progress(self, lesson_id):
        """Obtener progreso de una lección (0-100)."""
        return self.data['lessons_completed'].get(lesson_id, 0)

    def mark_lesson_complete(self, lesson_id):
        """Marcar lección como completada (100%)."""
        if self.data['lessons_completed'].get(lesson_id, 0) < 100:
            self.data['lessons_completed'][lesson_id] = 100
            self.data['stats']['lessons_finished'] += 1
            self.save()

    def update_lesson_progress(self, lesson_id, percent):
        """Actualizar progreso parcial (0-100)."""
        self.data['lessons_completed'][lesson_id] = max(0, min(100, percent))
        self.save()

    def is_lesson_complete(self, lesson_id):
        return self.data['lessons_completed'].get(lesson_id, 0) >= 100

    def get_completed_count(self):
        return sum(1 for v in self.data['lessons_completed'].values() if v >= 100)

    # --- Ejercicios ---
    def save_exercise_attempt(self, lesson_id, code, success):
        """Registrar intento de ejercicio."""
        if lesson_id not in self.data['exercise_attempts']:
            self.data['exercise_attempts'][lesson_id] = []
        
        self.data['exercise_attempts'][lesson_id].append({
            'code': code[:500],  # limitar tamaño
            'success': success,
            'timestamp': __import__('time').time()
        })
        
        self.data['stats']['total_exercises'] += 1
        if success:
            self.data['stats']['correct_exercises'] += 1
        self.save()

    def get_exercise_history(self, lesson_id):
        return self.data['exercise_attempts'].get(lesson_id, [])

    # --- Estadísticas ---
    def get_stats(self):
        return self.data['stats'].copy()

    def get_completion_rate(self):
        total = self.data['stats']['total_exercises']
        if total == 0:
            return 0
        return (self.data['stats']['correct_exercises'] / total) * 100

    # --- Reset ---
    def reset_all(self):
        """Borrar todo el progreso."""
        self.data = {
            'lessons_completed': {},
            'exercise_attempts': {},
            'stats': {
                'total_exercises': 0,
                'correct_exercises': 0,
                'lessons_finished': 0
            }
        }
        self.save()