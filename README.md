# Image Classification for a City Dog Show

## Project Overview

This project uses pretrained CNN architectures to classify pet images.
The program determines whether an image contains a dog and, when applicable,
compares the predicted dog breed with the actual breed from the filename.

## Models Tested

Three pretrained CNN architectures were evaluated:

- AlexNet
- ResNet
- VGG

## Results

| Model | Dog Accuracy | Not-Dog Accuracy | Breed Accuracy | Overall Match |
|------|--------------|------------------|----------------|---------------|
| AlexNet | 100% | 100% | 80.0% | 75.0% |
| ResNet | 100% | 90.0% | 90.0% | 82.5% |
| VGG | 100% | 100% | 93.3% | 87.5% |

## Best Model

VGG achieved the highest overall match at 87.5% and the highest breed
classification accuracy at 93.3% on the 40-image test set.

## How to Run

```bash
python check_images.py --dir pet_images --arch vgg --dogfile dognames.txt
