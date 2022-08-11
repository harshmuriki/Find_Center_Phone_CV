This is a repo that uses Computer Vision algorithms like Harr Cascade (Classifying technique) which is pre-trained on a given dataset (Files in ...) that finds the coordinates of the center of a phone in any given image.
The accuracy of this model is 78% (accurate upto 0.05 units). The ground truths are given in a separate file: ./../......

Ways to improve data collection:
    1. One of the best way to get even more accurate results is to avoid making the background the same colour as the main image. For example,
    as the phone was of black and white colour, it would be much easier and would result in more accurate results if everything else is of different color.

    2. More training data on which more advanced Deep learning techniques could be implemented to get better results.
    
Steps to test an image:
    1) Get the path of the image that you want to test on.
    2) run: find_python.py file_name

The output is given in (x,y) coordinates.

Thank you!
