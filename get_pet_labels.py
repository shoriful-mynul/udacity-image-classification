
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames
    of the image files.
    """

    results_dic = {}

    for filename in listdir(image_dir):

        if filename.lower().endswith(".jpg"):

            pet_label = filename.lower()
            pet_label = pet_label[:-4]

            pet_name = pet_label.rsplit('_', 1)[0]

            pet_name = pet_name.replace('_', ' ').strip()

            results_dic[filename] = [pet_name]

    return results_dic
