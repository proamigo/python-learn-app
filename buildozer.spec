[app]

# (str) Title of your application
title = Python Learn

# (str) Package name
package.name = pythonlearn

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let buildozer find them)
source.include_exts = py,png,jpg,kv,atlas,json,md,txt

# (str) Application versioning
version = 1.0.0

# (int) Application version code
version.code = 1

# (list) Application requirements
requirements = python3,kivy==2.3.0,plyer

# (str) Presplash of the application
presplash.filename = assets/presplash.png

# (str) Icon of the application
icon.filename = assets/icon.png

# (str) Supported orientations
orientation = portrait

# (bool) Enable AndroidX
android.enable_androidx = True

# (str) Android SDK version
android.api = 33

# (int) Min SDK version
android.minapi = 21

# (str) Android NDK version
android.ndk = 25c

# (str) Python version to use
android.python_version = 3.11

# (bool) If True, skip compiling .py files to .pyc
android.skip_pyc = False

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (str) Intent filters for main activity
android.intent_filters =

# (bool) Copy libs instead of making a apk with them
android.copy_libs = 1

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) Number of parallel build jobs
android.gradle_jobs = 4

# (bool) Enable AAB (Android App Bundle)
android.build_app_bundle = False

#
# p4a (python-for-android) specific
#

# (list) p4a extra arguments
p4a.extra_args = --verbose

#
# Buildozer specific
#

# (int) Log level (2 = verbose)
log_level = 2

# (bool) Warn if buildozer is run as root
warn_on_root = 1