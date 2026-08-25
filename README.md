# Image Classification for a City Dog Show

## Project Overview

This project uses pretrained Convolutional Neural Network (CNN) architectures
to classify images of pets.

The program performs two main tasks:

1. Determines whether an image contains a dog.
2. If the image contains a dog, compares the predicted dog breed with the
   actual breed identified from the image filename.

Three pretrained CNN architectures were evaluated to compare their
classification performance.

## Models Tested

The following pretrained CNN architectures were tested:

- AlexNet
- ResNet
- VGG

## Dataset

The project was evaluated using a test set of 40 pet images:

- 30 dog images
- 10 non-dog images

The images include several different dog breeds as well as cats and other
non-dog animals.

## Results

| Model | Dog Accuracy | Not-Dog Accuracy | Breed Accuracy | Overall Match |
|------|--------------|------------------|----------------|---------------|
| AlexNet | 100% | 100% | 80.0% | 75.0% |
| ResNet | 100% | 90.0% | 90.0% | 82.5% |
| VGG | 100% | 100% | 93.3% | 87.5% |

## Best Model

VGG achieved the best overall performance on the 40-image test set.

It achieved:

- **100% dog classification accuracy**
- **100% non-dog classification accuracy**
- **93.3% breed classification accuracy**
- **87.5% overall match**

Based on these results, VGG performed better than AlexNet and ResNet on
this test set.

## Incorrectly Classified Dog Breeds

The VGG model incorrectly classified two dog breeds in the test set:

- `Great_pyrenees_05367.jpg`
  - Actual breed: Great Pyrenees
  - Predicted breed: Kuvasz

- `Beagle_01170.jpg`
  - Actual breed: Beagle
  - Predicted breed: Walker Hound / Walker Foxhound

These results show that the model was able to correctly identify most dogs,
but some visually similar dog breeds can still be difficult to distinguish.

## Project Structure

```text
udacity-image-classification/
│
├── pet_images/
│   ├── Basenji_00963.jpg
│   ├── Beagle_01125.jpg
│   ├── Boston_terrier_02259.jpg
│   ├── ...
│
├── adjust_results4_isadog.py
├── calculates_results_stats.py
├── check_images.py
├── classifier.py
├── classify_images.py
├── create_images.txt
├── dognames.txt
├── get_input_args.py
├── get_pet_labels.py
├── imagenet1000_clsid_to_human.txt
├── print_functions_for_lab_checks.py
├── print_results.py
├── test_classifier.py
├── run_models_batch.sh
├── run_models_batch.bat
└── README.md

Results

The three CNN architectures were evaluated using the same 40-image test set.

Model	Dog Accuracy	Not-Dog Accuracy	Breed Accuracy	Overall Match
AlexNet	100.0%	100.0%	80.0%	75.0%
ResNet	100.0%	90.0%	90.0%	82.5%
VGG	100.0%	100.0%	93.3%	87.5%
Model Comparison
AlexNet

AlexNet correctly classified all 30 dog images and all 10 non-dog images.

Its results were:

Dog accuracy: 100.0%
Not-dog accuracy: 100.0%
Breed accuracy: 80.0%
Overall match: 75.0%

The model correctly identified whether the image contained a dog, but its
breed classification performance was lower than the other two models.

ResNet

ResNet correctly classified all 30 dog images.

Its results were:

Dog accuracy: 100.0%
Not-dog accuracy: 90.0%
Breed accuracy: 90.0%
Overall match: 82.5%

ResNet performed better than AlexNet for dog breed classification, although
its non-dog classification accuracy was lower.

VGG

VGG achieved the strongest overall performance among the three tested models.

Its results were:

Dog accuracy: 100.0%
Not-dog accuracy: 100.0%
Breed accuracy: 93.3%
Overall match: 87.5%

VGG achieved both perfect dog/non-dog classification on this test set and the
highest breed classification accuracy.

Best Performing Model

Based on the results from the 40-image test set, VGG performed the best.

VGG Performance
Metric	Result
Dog Accuracy	100.0%
Not-Dog Accuracy	100.0%
Breed Accuracy	93.3%
Overall Match	87.5%

VGG achieved the highest breed classification accuracy and the highest
overall match among the three tested architectures.

Incorrectly Classified Dog Breeds

Although VGG achieved the highest breed accuracy, some individual dog breeds
were still incorrectly classified.

The incorrectly classified dog breeds included:

Great_pyrenees_05367.jpg
Pet label: great pyrenees
Classifier label: kuvasz

Beagle_01170.jpg
Pet label: beagle
Classifier label: walker hound, walker foxhound

These results show that the classifier can correctly identify that an image
contains a dog even when it cannot identify the exact breed.

How to Run

The project can be executed from the project directory using Python.

Run the Image Classification Program
python classify_images.py --dir pet_images --arch vgg --dogfile dognames.txt

The --arch argument specifies the CNN architecture.

For example:

AlexNet
python classify_images.py --dir pet_images --arch alexnet --dogfile dognames.txt
ResNet
python classify_images.py --dir pet_images --arch resnet --dogfile dognames.txt
VGG
python classify_images.py --dir pet_images --arch vgg --dogfile dognames.txt
Check Image Classification Results

The project also includes check_images.py, which can be used to evaluate
the classifier results against the expected labels.

For example:

python check_images.py --dir pet_images --arch vgg --dogfile dognames.txt

The program reports:

Total number of images
Number of dog images
Number of non-dog images
Correct label matches
Correctly classified dogs
Correctly classified non-dogs
Correctly classified breeds
Dog accuracy
Non-dog accuracy
Breed accuracy
Overall match
Required Files

The main project components include:

classifier.py for image classification using pretrained CNN models.
classify_images.py for running image classification.
check_images.py for checking classification results.
get_pet_labels.py for obtaining expected labels from image filenames.
get_input_args.py for handling command-line arguments.
calculates_results_stats.py for calculating classification statistics.
adjust_results4_isadog.py for adjusting results based on whether an image
contains a dog.
print_results.py for displaying classification results.
dognames.txt containing dog breed names.
pet_images/ containing the test images.
Technologies Used
Python
PyTorch
Torchvision
Pretrained Convolutional Neural Networks
AlexNet
ResNet
VGG
Conclusion

The project successfully evaluates pretrained CNN architectures for pet image
classification.

All three tested models achieved 100% dog classification accuracy on the
30 dog images in the test set. VGG achieved the highest overall performance,
with a breed classification accuracy of 93.3% and an overall match of 87.5%.

Based on the results from this test set, VGG was the best-performing model
among the three evaluated architectures.
