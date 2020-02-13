# Automatically fixes integrity of VRZONE asset library based on the README specs #

from tkinter.filedialog import askdirectory
import os


def replace_string_in_files(files, a, b) -> None:
    for f in files:
        if a in f:
            os.rename(f, f.replace(a, b))


def remove_spaces(files) -> None:
    replace_string_in_files(files, ' ', '_')


def fix_texture_suffixes(files) -> None:
    corrections = {'AmbientOcclusion': ['ao', 'ambientocclusion', 'ambient_occlusion', 'AO', 'occlusion'],
                   'Normal': ['normal', 'normal_map', 'normals', 'n'],
                   'BaseColor': ['diffuse', 'basecolor', 'base_color', 'color'],
                   'Roughness': ['roughness'],
                   'Metallic': ['metallic'],
                   'OcclusionRoughnessMetallic': ['orm'],
                   'Specular': ['spec', 'specular'],
                   'Emissive': ['emissive']
                   }

    pass


if __name__ == '__main__':
    actions = [help, remove_spaces, fix_texture_suffixes]
    action = input('Please select an action:\n'
                   '0. Help\n'
                   '1. Remove spaces\n'
                   '2. Fix texture suffixes\n\n'
                   '> ')

    try:
        action = actions[int(action)]

        if action != help:
            root_dir = askdirectory()
            all_files = os.walk(root_dir)
            action(all_files)

        else:
            print('TODO: write help')

    except ValueError:
        print('Invalid action. Terminating.')






