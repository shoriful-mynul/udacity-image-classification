#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine whether the pet image
    and classifier label are dogs or not dogs.
    """

    # dognames.txt may contain several accepted names on one line, separated
    # by commas. Expand each line into individual accepted names, while
    # keeping the classifier label itself intact.
    dognames = set()
    with open(dogfile, "r") as f:
        for line in f:
            for name in line.strip().lower().split(","):
                name = name.strip()
                if name:
                    dognames.add(name)

    for key in results_dic:
        # Determine whether the actual pet is a dog.
        pet_label = results_dic[key][0].strip().lower()
        is_pet_dog = 1 if pet_label in dognames else 0

        # Determine whether the classifier thinks the image is a dog.
        # Do NOT split the classifier label. A label such as
        # "eskimo dog, husky" is one classifier result and must be matched
        # against the accepted names as a complete label or alias.
        classifier_label = results_dic[key][1].strip().lower()
        is_classifier_dog = 1 if classifier_label in dognames else 0

        # Add dog/not-dog results.
        results_dic[key].extend([is_pet_dog, is_classifier_dog])
