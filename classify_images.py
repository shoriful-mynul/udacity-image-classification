#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    classifier labels, and adds the classifier label and comparison to the
    results dictionary.
    """

    for key in results_dic:
        # Build the image path safely regardless of whether images_dir ends
        # with a slash.
        image_path = os.path.join(images_dir, key)

        # Get the classifier label for the current image.
        classifier_label = classifier(image_path, model)
        classifier_label = classifier_label.lower().strip()

        # Compare pet label with classifier label.
        pet_label = results_dic[key][0]

        if pet_label in classifier_label:
            results_dic[key].extend([classifier_label, 1])
        else:
            results_dic[key].extend([classifier_label, 0])
