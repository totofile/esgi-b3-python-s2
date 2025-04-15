#!/usr/bin/env python3
# filepath: /home/toplu/Bureau/ESGI/B3/S2/PythonMalinge/Exercices/RecupFichiers20Min.py
import os
import shutil
import datetime
import re
from pathlib import Path

def restore_recent_files(minutes=20):
    """Restaure les fichiers supprimés depuis les dernières 'minutes' minutes"""
    
    # Chemins de la corbeille
    trash_files = os.path.expanduser("~/.local/share/Trash/files")
    trash_info = os.path.expanduser("~/.local/share/Trash/info")
    
    if not os.path.isdir(trash_files) or not os.path.isdir(trash_info):
        print("Erreur: les dossiers de la corbeille n'existent pas.")
        return
    
    # Calculer le timestamp limite (20 minutes dans le passé)
    now = datetime.datetime.now()
    cutoff_time = now - datetime.timedelta(minutes=minutes)
    
    # Compteurs pour les statistiques
    restored_count = 0
    skipped_count = 0
    
    # Parcourir les fichiers d'information de la corbeille
    for info_file in os.listdir(trash_info):
        if not info_file.endswith('.trashinfo'):
            continue
            
        file_name = info_file[:-10]  # Enlever l'extension .trashinfo
        info_path = os.path.join(trash_info, info_file)
        file_path = os.path.join(trash_files, file_name)
        
        # Vérifier si le fichier existe dans la corbeille
        if not os.path.exists(file_path):
            continue
            
        # Lire le fichier .trashinfo
        original_path = None
        deletion_date = None
        
        with open(info_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('Path='):
                    # Décoder le chemin URL-encoded
                    path_encoded = line[5:].strip()
                    original_path = path_encoded.replace('%20', ' ')
                    # Gérer d'autres caractères encodés au besoin
                    for code in re.findall('%[0-9A-Fa-f]{2}', original_path):
                        char = chr(int(code[1:], 16))
                        original_path = original_path.replace(code, char)
                        
                elif line.startswith('DeletionDate='):
                    date_str = line[13:].strip()
                    try:
                        # Format standard: 2023-04-15T14:30:45
                        deletion_date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
                    except ValueError:
                        # En cas de format différent
                        continue
        
        # Vérifier si le fichier a été supprimé dans les 20 dernières minutes
        if deletion_date and deletion_date > cutoff_time:
            if original_path:
                # Créer les dossiers parents si nécessaire
                original_dir = os.path.dirname(original_path)
                if not os.path.exists(original_dir):
                    os.makedirs(original_dir, exist_ok=True)
                    
                try:
                    # Restaurer le fichier
                    if os.path.exists(original_path):
                        # Si un fichier de même nom existe déjà, ajouter un suffixe
                        base, ext = os.path.splitext(original_path)
                        original_path = f"{base}_recovered{ext}"
                        
                    shutil.move(file_path, original_path)
                    # Supprimer le fichier d'information
                    os.remove(info_path)
                    print(f"Restauré: {original_path}")
                    restored_count += 1
                    
                except Exception as e:
                    print(f"Erreur lors de la restauration de {file_name}: {e}")
                    skipped_count += 1
            else:
                skipped_count += 1
    
    print(f"\nRécupération terminée. {restored_count} fichiers restaurés, {skipped_count} fichiers ignorés.")

if __name__ == '__main__':
    print("Récupération des fichiers supprimés dans les 20 dernières minutes...")
    restore_recent_files(20)