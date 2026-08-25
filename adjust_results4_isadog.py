
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine whether the pet image
    and classifier label are dogs or not dogs.
    """

    # Read all dog names from the dog names file
    with open(dogfile, "r") as f:
        dognames = set(line.strip().lower() for line in f)

    # Process each image
    for key in results_dic:

        # Determine whether the actual pet is a dog
        pet_label = results_dic[key][0]

        if pet_label in dognames:
            is_pet_dog = 1
        else:
            is_pet_dog = 0

        # Determine whether the classifier thinks it is a dog
        classifier_label = results_dic[key][1]

        classifier_labels = classifier_label.split(",")

        is_classifier_dog = 0

        for label in classifier_labels:
            if label.strip() in dognames:
                is_classifier_dog = 1
                break

        # Add dog/not-dog results
        results_dic[key].extend([is_pet_dog, is_classifier_dog])
