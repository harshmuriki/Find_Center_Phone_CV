Hello. This is my code to get the coordinates of the center of a phone in a given image.
I have trained this model (by using cascade classifying techniques) based on the dataset I had been given earlier.
According to my tests, I have accurately got the coordinates of the centers of phones of around 99 of the given 130 images (Upto an accuracy of 0.05), which is an accuracy of 78%.

Ways to improve data collection:
    1. One of the best way to get even more accurate results is to avoid making the background the same colour as the main image. For example,
    as the phone was of black and white colour, it would be much easier and would result in more accurate results if everything else is of different color.

    2. I had used around 70 image sets to train my model. If I could get more 'different' images, I could train my model even more would would lead to in better
    accuracy.
    
Note: As I have already trained the model on the images I had been given, I don't need to train it again with train_phone_finder.py. So that file has no useful code in it.
You can directly test the image with find_phone.py file.

Thank you!