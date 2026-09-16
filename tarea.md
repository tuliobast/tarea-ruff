2) hay 8 errores de las siguientes reglas: ["PTH", "B", "E", "UP", "I", "F"].
3) aplicando `uv run ruff check --fix`, se corriegieron los erroes "I001" y "F401". 
4) corrige el error "B006", sustituyendo un argumento mutable por defecto por un valor None lo cual considero que es mas legible para luego comprovar si el argumento esta realmente vacio.
5) lo que no corrigio directamente ruff fueron los errores "PTH118" y "PTH109", sustituyendo la libreria os por pathlib y `os.path.join()` por `PATH()` y `os.getwcd()` por `Path.cwd()` en las lineas 8 y 9 de main.py, respectivamente.
6) la regla UP031, solo porque la tarea exige que excluya una regla, pero en lo personal me parece engorroso el estilo printf.