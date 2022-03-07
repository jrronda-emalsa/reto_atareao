from os import path, scandir, system  
from getpass import getuser
# from gi.repository import Glib
# from pathlib import Path


def principal():

    usuario = getuser()
    ejemplo_dir = "/mnt/c/Users/" + usuario + "/downloads/"
    system("clear")
    # downloads_dir = Path(Glib.get_user_special_dir(Glib.UserDirectory.DIRECTORY_DOENLOAD))
    # print()
    # print(f"\nDirectorio: {downloads_dir}\n")
    print()
    print("Directorio: ", ejemplo_dir)
    print()
    with scandir(ejemplo_dir) as ficheros:
        [print(fichero.name) for fichero in ficheros if fichero.is_file()]
    print()

if __name__ == "__main__":
    principal()
    print()
    DIRECTORIO_BASE = path.dirname(__file__)
    print(DIRECTORIO_BASE)
 