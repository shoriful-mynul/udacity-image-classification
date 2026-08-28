#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine whether the pet image
    and classifier label are dogs or not dogs.
    """

    # Read each complete dog-label entry from dognames.txt.
    # Some entries contain commas because they represent one classifier
    # label with multiple accepted names, for example:
    # "eskimo dog, husky".
    with open(dogfile, "r") as f:
        dognames = set(line.strip().lower() for line in f if line.strip())

    for key in results_dic:
        # Determine whether the actual pet is a dog.
        pet_label = results_dic[key][0].strip().lower()
        is_pet_dog = 1 if pet_label in dognames else 0

        # Determine whether the classifier thinks the image is a dog.
        # Match the complete classifier label against the complete entries
        # in dognames.txt instead of splitting comma-separated labels.
        classifier_label = results_dic[key][1].strip().lower()
        is_classifier_dog = 1 if classifier_label in dognames else 0

        # Add dog/not-dog results.
        results_dic[key].extend([is_pet_dog, is_classifier_dog])
