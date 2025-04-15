import os

def create_arborescence(cwd):
    if not os.access(cwd, os.W_OK):
        try:
            os.chmod(cwd, 0o755)
            print("Permissions modifiées pour le répertoire:", cwd)
        except Exception as e:
            print("Erreur lors de la modification des permissions du répertoire", cwd, ":", e)

    for year in range(2010, 2031):
        for month in range(1, 13):
            for day in range(1, 4):
                dir_path = os.path.join(cwd, str(year), str(month), str(day))
                try:
                    os.makedirs(dir_path, exist_ok=True)
                    print("Created:", dir_path)
                except Exception as e:
                    print("Error creating", dir_path, ":", e)

# Utilisation du répertoire du script (et non du terminal courant du terminal)
script_dir = os.path.abspath(os.path.dirname(__file__))
create_arborescence(script_dir)
