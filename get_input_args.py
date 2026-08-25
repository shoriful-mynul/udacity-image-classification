#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dir',
        type=str,
        default='pet_images',
        help='path to the folder of pet images'
    )

    parser.add_argument(
        '--arch',
        type=str,
        default='vgg',
        help='CNN model architecture'
    )

    parser.add_argument(
        '--dogfile',
        type=str,
        default='dognames.txt',
        help='text file containing dog names'
    )

    return parser.parse_args()
