
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PROGRAMMER: Shoriful Islam
# DATE CREATED: 2026-08-24
# REVISED DATE: 2026-08-24

# Imports python modules
from time import time

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():

    # Start timer
    start_time = time()

    # Get command line arguments
    in_arg = get_input_args()

    # Check command line arguments
    check_command_line_arguments(in_arg)

    # Create pet image labels
    results = get_pet_labels(in_arg.dir)

    # Check pet image labels
    check_creating_pet_image_labels(results)

    # Classify images and compare labels
    classify_images(in_arg.dir, results, in_arg.arch)

    # Check classifier results
    check_classifying_images(results)

    # Determine whether images are dogs or not-dogs
    adjust_results4_isadog(results, in_arg.dogfile)

    # Check dog/not-dog classification
    check_classifying_labels_as_dogs(results)

    # Calculate statistics
    results_stats = calculates_results_stats(results)

    # Check calculated statistics
    check_calculating_results(results, results_stats)

    # Print results
    print_results(
        results,
        results_stats,
        in_arg.arch,
        True,
        True
    )

    # End timer
    end_time = time()

    # Calculate total runtime
    tot_time = end_time - start_time

    print(
        "\n** Total Elapsed Runtime:",
        str(int(tot_time / 3600)) + ":" +
        str(int((tot_time % 3600) / 60)) + ":" +
        str(int((tot_time % 3600) % 60))
    )


# Run main function
if __name__ == "__main__":
    main()
