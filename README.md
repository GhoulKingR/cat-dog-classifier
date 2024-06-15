# cat-dog-classifier
This project consists of a DNN that can distinguish between images of a cat and images of a Dog with 87% accuracy.

| ![Cat 1](https://github.com/GhoulKingR/cat-dog-classifier/assets/87097037/8975a495-36d0-46a2-bb31-c916c781c9a7) | ![Cat 2](https://github.com/GhoulKingR/cat-dog-classifier/assets/87097037/9a15d97b-8efa-42a3-b856-e4dab4ae4249) |
|---|---|
| ![Dog 1](https://github.com/GhoulKingR/cat-dog-classifier/assets/87097037/96ae8580-83a5-4121-80d9-7dab51c2f571) | ![Dog 2](https://github.com/GhoulKingR/cat-dog-classifier/assets/87097037/85b7121e-cd78-475e-85e4-94b1ba3058b2) |

# Importing the classifier

To import the classifier into your project, you'll need to do these things:
1. Install dependencies into your project:
```bash
pip install -r requirements.txt
```

2. Copy the weights file (`model_weights.weights.h5`) and the lib file (`lib.py`) to your project. You can rename the lib file and place it wherever you want in your project, you only need to make sure that the lib and weight files are in the same directory.
3. Import the `cat_or_dog` function to your project, and pass a path to the image file. Then you'll get an output `'dog'` if it's a dog and `'cat'` if it's a cat:
```python
from lib import cat_or_dog

result = cat_or_dog('./internet_images/images.jpeg')
print(result)        # -> dog
```
