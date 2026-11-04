# Python Learn — App Android para aprender Python

App educativa con **lecciones progresivas** (21 lecciones, 6 módulos) + **terminal REPL real de Python** embebida.

## Características

- **21 lecciones estructuradas**: Variables → POO → Archivos → Librería estándar
- **REPL real**: `code.InteractiveConsole` ejecuta Python de verdad en el dispositivo
- **Ejercicios interactivos**: Escribe código, ejecútalo, ve la salida al instante
- **Progreso persistente**: Se guarda automáticamente en almacenamiento local
- **UI nativa Kivy**: Material Design, modo oscuro, navegación por pestañas

## Estructura del proyecto

```
python-learn-app/
├── main.py                 # Entry point
├── buildozer.spec          # Configuración de build
├── .github/workflows/build.yml  # CI para compilar APK
├── assets/
│   ├── icon.png
│   └── presplash.png
├── lessons/
│   ├── __init__.py
│   └── curriculum.py       # 21 lecciones en 6 módulos
├── ui/
│   ├── __init__.py
│   ├── widgets.py          # Componentes reutilizables
│   └── terminal_screen.py  # Terminal REPL + PythonRunner
└── utils/
    ├── __init__.py
    ├── progress.py         # Persistencia JSON
    └── python_runner.py    # Ejecutor seguro de Python
```

## Currículum (21 lecciones)

| Módulo | Lecciones |
|--------|-----------|
| 🟢 Fundamentos | Variables, Operadores, Strings, Listas/Tuplas, Dicts/Sets |
| 🟡 Control de Flujo | If/Elif/Else, For, While, Comprensiones |
| 🟠 Funciones | Definir, *args/**kwargs, Lambdas + map/filter/sorted |
| 🔴 POO | Clases/__init__, Herencia/Polimorfismo, Métodos especiales |
| 🔵 Archivos/Excepciones | Lectura/Escritura, Try/Except, JSON/CSV |
| 🟣 Librería Estándar | Datetime, Pathlib, Collections/Itertools |

## Compilar APK (GitHub Actions — gratis, sin WSL)

1. **Crea repo en GitHub** y sube este proyecto:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/TU_USUARIO/python-learn-app.git
   git push -u origin main
   ```

2. **GitHub Actions compila solo**: Ve a la pestaña **Actions** → *Build APK* → *Run workflow*

3. **Descarga el APK**: Al terminar, en *Artifacts* → `python-learn-app-apk` → `python-learn-app-1.0.0-debug.apk`

4. **Instala en Android**: Transfiere el APK al móvil e instálalo (habilita "Fuentes desconocidas")

## Compilar localmente (requiere WSL2 Ubuntu)

```bash
# En WSL2 Ubuntu
sudo apt update && sudo apt install -y git zip unzip openjdk-17-jdk python3-pip build-essential
pip install buildozer==1.5.0
git clone https://github.com/TU_USUARIO/python-learn-app.git
cd python-learn-app
buildozer android debug
# APK en bin/
```

## Requisitos

- Android 5.0+ (API 21)
- Arquitecturas: arm64-v8a, armeabi-v7a
- ~25 MB APK (incluye Python 3.11 + Kivy)

## Personalizar

- **Añadir lecciones**: Edita `lessons/curriculum.py` (formato JSON-like)
- **Cambiar colores**: Modifica `theme_primary`, `theme_bg` en `main.py`
- **Añadir módulos Python**: Agrega a `requirements` en `buildozer.spec`

## Licencia

MIT — uso libre, también para apps privadas/comerciales.

---

**¿Problemas?** Revisa logs en GitHub Actions o abre issue.