#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine whether the pet image and
    classifier label are dogs or not dogs.

    The pet-image label is checked against all individual names/aliases in
    dognames.txt. The classifier label is kept intact and is matched against
    the complete ImageNet label stored in dognames.txt. This is important for
    labels such as "eskimo dog, husky" where the complete classifier label is
    one entry in dognames.txt.
    """

    # Keep the complete lines from dognames.txt for classifier-label matching,
    # while also building an alias set for labels extracted from filenames.
    dog_labels = set()
    dog_aliases = set()

    with open(dogfile, "r") as f:
        for line in f:
            label = line.strip().lower()
            if label:
                dog_labels.add(label)
                dog_aliases.update(name.strip() for name in label.split(",") if name.strip())

    for key in results_dic:
        # Determine whether the actual pet is a dog. Filename labels can use
        # one of the aliases contained in a dognames.txt entry.
        pet_label = results_dic[key][0].strip().lower()
        is_pet_dog = 1 if pet_label in dog_aliases else 0

        # Keep the classifier's complete label intact. Do NOT split it by
        # comma: ImageNet labels such as "eskimo dog, husky" are represented
        # as one complete entry in dognames.txt.
        classifier_label = results_dic[key][1].strip().lower()
        is_classifier_dog = 1 if classifier_label in dog_labels else 0

        # Add dog/not-dog results at indexes 3 and 4.
        results_dic[key].extend([is_pet_dog, is_classifier_dog])
