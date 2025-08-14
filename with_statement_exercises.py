"""
- La instruccion with de python te ayuda a trabajar de forma segura con recursos externos (como archivos, conexiones de red o bases de datos, configuraciones temporales (como los warnings), etc.)
- Para que un objeto funcione con with, debe implementar lo que en Python se llama el "protocolo de context manager". Esto significa que debe tener los metodos especiales __enter__ y __exit__.
- Estos objetos se encargan automáticamente de:
    Setup: Preparar el recurso (por ejemplo, abrir el archivo) cuando entras al bloque with.
    Cleanup: Liberar el recurso (por ejemplo, cerrar el archivo) cuando sales del bloque, aunque haya ocurrido un error.
    Esto evita olvidos y errores que pueden suceder si abres un recurso y lo olvidas cerrar.

Fuente: https://realpython.com/python-with-statement/

A veces, un programa usa cierta capacidad de memoria que luego no libera cuando no lo requiere mas.
"""

# El siguiente codigo no garatiza que el archivo se cerrará si ocurre una excepción durante el llamado de .write()
# En ese caso, el codigo podria nunca llamar a .close(), por lo que el archivo podría no quedar disponible para otro programa o codigo.
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()

"""
En python, se pueden ocupar un par de enfoques para lidiar con el maje de recursos.
1. Se puede ocupar el constructor try... finally
2. Se puede ocupar el contructor with.
"""