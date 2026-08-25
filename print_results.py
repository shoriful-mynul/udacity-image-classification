
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False,
                  print_incorrect_breed=False):
    """
    Prints summary results and optionally prints incorrectly classified
    dogs and incorrectly classified dog breeds.
    """

    print("\nResults Summary")
    print("-" * 40)
    print("Model architecture:", model)
    print("Total images:", results_stats_dic["n_images"])
    print("Dog images:", results_stats_dic["n_dogs_img"])
    print("Not-dog images:", results_stats_dic["n_notdogs_img"])
    print("Correct label matches:", results_stats_dic["n_match"])
    print("Correctly classified dogs:", results_stats_dic["n_correct_dogs"])
    print("Correctly classified not-dogs:",
          results_stats_dic["n_correct_notdogs"])
    print("Correctly classified breeds:",
          results_stats_dic["n_correct_breed"])

    print("\nAccuracy")
    print("-" * 40)
    print("Dog accuracy:",
          results_stats_dic["pct_correct_dogs"])
    print("Not-dog accuracy:",
          results_stats_dic["pct_correct_notdogs"])
    print("Breed accuracy:",
          results_stats_dic["pct_correct_breed"])
    print("Overall match:",
          results_stats_dic["pct_match"])

    # Print incorrectly classified dogs
    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs")
        print("-" * 40)

        for key, value in results_dic.items():

            # Actual image is a dog, but classifier says not dog
            if value[3] == 1 and value[4] == 0:
                print(
                    key,
                    "Pet label:", value[0],
                    "Classifier label:", value[1]
                )

            # Actual image is not a dog, but classifier says dog
            elif value[3] == 0 and value[4] == 1:
                print(
                    key,
                    "Pet label:", value[0],
                    "Classifier label:", value[1]
                )

    # Print incorrectly classified dog breeds
    if print_incorrect_breed:
        print("\nIncorrectly Classified Dog Breeds")
        print("-" * 40)

        for key, value in results_dic.items():

            # Actual image is a dog AND breed was classified incorrectly
            if value[3] == 1 and value[2] == 0:
                print(
                    key,
                    "Pet label:", value[0],
                    "Classifier label:", value[1]
                )
