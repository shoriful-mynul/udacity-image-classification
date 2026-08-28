# Image Classification for a City Dog Show

## Project Overview

This project uses pretrained Convolutional Neural Network (CNN) architectures to classify images of pets.

The program performs two main tasks:

1. Determines whether an image contains a dog.
2. If the image contains a dog, compares the predicted dog breed with the actual breed identified from the image filename.

Three pretrained CNN architectures were evaluated to compare their classification performance.

## Models Tested

- AlexNet
- ResNet
- VGG

## Dataset

The project was evaluated using a test set of 40 pet images:

- 30 dog images
- 10 non-dog images

The images include several different dog breeds as well as cats and other non-dog animals.

## Results

| Model | Dog Accuracy | Not-Dog Accuracy | Breed Accuracy | Overall Match |
|---|---:|---:|---:|---:|
| AlexNet | 100.0% | 100.0% | 80.0% | 75.0% |
| ResNet | 100.0% | 90.0% | 90.0% | 82.5% |
| VGG | 100.0% | 100.0% | 93.3% | 87.5% |

## Model Comparison

### AlexNet

- Dog accuracy: 100.0%
- Not-dog accuracy: 100.0%
- Breed accuracy: 80.0%
- Overall match: 75.0%

AlexNet correctly identified all dog and non-dog images in this test set, but its breed classification accuracy was lower than ResNet and VGG.

### ResNet

- Dog accuracy: 100.0%
- Not-dog accuracy: 90.0%
- Breed accuracy: 90.0%
- Overall match: 82.5%

ResNet performed better than AlexNet for breed classification, although it incorrectly classified one of the non-dog images as a dog.

### VGG

- Dog accuracy: 100.0%
- Not-dog accuracy: 100.0%
- Breed accuracy: 93.3%
- Overall match: 87.5%

VGG achieved the strongest overall performance on this 40-image test set.

## Best Performing Model

Based on the results above, **VGG** was the best-performing model among the three tested architectures.

It achieved:

- 100.0% dog accuracy
- 100.0% not-dog accuracy
- 93.3% breed accuracy
- 87.5% overall match

## Incorrectly Classified Dog Breeds

Although VGG achieved the highest breed accuracy, some individual dog breeds were still classified incorrectly. Examples from the test output include:

- `Great_pyrenees_05367.jpg` — actual label: `great pyrenees`; classifier label: `kuvasz`
- `Beagle_01170.jpg` — actual label: `beagle`; classifier label: `walker hound, walker foxhound`

These results show that the classifier can correctly recognize an image as a dog even when it does not identify the exact breed.

## How to Run

Run the main evaluation program from the project directory:

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

You can replace `vgg` with `alexnet` or `resnet` to evaluate another architecture:

```bash
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

The program reports the number of images, dog and non-dog classification results, breed classification results, accuracy values, and incorrectly classified examples.

## Running All Three Models

The included batch script can run all three architectures and save their outputs to separate text files:

```bash
sh run_models_batch.sh
```

This produces:

- `resnet_pet-images.txt`
- `alexnet_pet-images.txt`
- `vgg_pet-images.txt`

These generated result files are useful for reviewing and comparing the model outputs.

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
```

## Required Files

The main project components include:

- `classifier.py` — image classification using pretrained CNN models.
- `classify_images.py` — runs image classification for each image.
- `check_images.py` — runs the complete evaluation pipeline.
- `get_pet_labels.py` — obtains expected labels from image filenames.
- `get_input_args.py` — handles command-line arguments.
- `calculates_results_stats.py` — calculates classification statistics.
- `adjust_results4_isadog.py` — determines dog versus non-dog classification.
- `print_results.py` — displays classification results.
- `dognames.txt` — contains accepted dog breed names and classifier labels.
- `pet_images/` — contains the test images.

## Technologies Used

- Python
- PyTorch
- Torchvision
- Pretrained Convolutional Neural Networks
- AlexNet
- ResNet
- VGG

## Conclusion

The project evaluates three pretrained CNN architectures for pet image classification. All three models achieved 100.0% dog classification accuracy on the 30 dog images in the test set. VGG achieved the highest breed classification accuracy at 93.3% and the highest overall match at 87.5%.

Based on this test set, VGG was the best-performing model among the three evaluated architectures.
