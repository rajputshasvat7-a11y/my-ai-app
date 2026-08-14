[app]
# (str) Title of your application
title = My AI Chatbot

# (str) Package name
package.name = myaichatbot

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code directory where main.py lives
source.dir = .

# (list) Source files to include (let's include all python files)
source.include_exts = py

# (str) Application versioning
version = 0.1

# (list) Application requirements (Crucial: This tells GitHub to download your packages)
requirements = python3, kivy, google-genai

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) Permissions (Crucial: This lets your phone use Wi-Fi to load Gemini)
android.permissions = INTERNET

# (int) Target Android API (leave blank for default auto-detection)
android.api = 34

# (int) Minimum Android API your app will support
android.minapi = 21

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

[buildozer]
# (int) Log level (1 = error only, 2 = informational)
log_level = 2
