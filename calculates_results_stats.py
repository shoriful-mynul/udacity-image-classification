
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculates_results_stats(results_dic):
    """
    Calculates statistics from the results dictionary.
    """

    results_stats_dic = {}

    # Total number of images
    n_images = len(results_dic)
    results_stats_dic["n_images"] = n_images

    # Initialize counters
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0

    # Process every image
    for key in results_dic:

        # Breed/label match
        if results_dic[key][2] == 1:
            n_match += 1

        # Actual image is a dog
        if results_dic[key][3] == 1:
            n_dogs_img += 1

            # Classifier correctly identified it as a dog
            if results_dic[key][4] == 1:
                n_correct_dogs += 1

                # Correct breed
                if results_dic[key][2] == 1:
                    n_correct_breed += 1

        # Actual image is NOT a dog
        else:
            n_notdogs_img += 1

            # Classifier correctly identified it as NOT a dog
            if results_dic[key][4] == 0:
                n_correct_notdogs += 1

    # Store counts
    results_stats_dic["n_dogs_img"] = n_dogs_img
    results_stats_dic["n_notdogs_img"] = n_notdogs_img
    results_stats_dic["n_match"] = n_match
    results_stats_dic["n_correct_dogs"] = n_correct_dogs
    results_stats_dic["n_correct_notdogs"] = n_correct_notdogs
    results_stats_dic["n_correct_breed"] = n_correct_breed

    # Calculate percentages
    results_stats_dic["pct_match"] = (n_match / n_images) * 100

    if n_dogs_img > 0:
        results_stats_dic["pct_correct_dogs"] = (
            n_correct_dogs / n_dogs_img
        ) * 100

        results_stats_dic["pct_correct_breed"] = (
            n_correct_breed / n_dogs_img
        ) * 100
    else:
        results_stats_dic["pct_correct_dogs"] = 0.0
        results_stats_dic["pct_correct_breed"] = 0.0

    if n_notdogs_img > 0:
        results_stats_dic["pct_correct_notdogs"] = (
            n_correct_notdogs / n_notdogs_img
        ) * 100
    else:
        results_stats_dic["pct_correct_notdogs"] = 0.0

    return results_stats_dic
