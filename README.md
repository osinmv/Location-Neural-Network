# How to run 
Download Supplimental materials like testing datasets, the original dataset, weights from [Google Drive](https://drive.google.com/file/d/16PcN2LsWytY0eCCd4rarH5lQdy_LzVcr/view?usp=share_link). Unpack everything in root directory of this project.

You need conda with `tensorflow` and `matplotlib`.

If something doesn't work, there is `requirements.txt`

To to see how Convolution NN classifies images from `TestingDataset/TestData2` just run  ` classify_and_sort.py`

To run some training on `LoadingScreensDataset` just run `classifiernn.py`

If you got some footage that has some static frames, you could probably repurpose `split_images_by_loadscreen.py` with some minor changes.



# Scripts
`classifiernn.py` - basic script for training CNN. The base models for it was ZFnet, but I experimented with different models as much as I can. I am not claiming that it is the best. It is what I used for my last 3 models in `Weights` folder.

`classify_and_sort.py` - basic script that sorts images by category into folders usign one of the weights in the `Weights` folder.

`predict.py` - a script I used to evaluate large sets of weights to find the best performing. It was for a different type of models. I tried to create a CNN that classifies photos of game level, didn't work out.

`split_images_by_loadscreen.py` - script that extracts gameplay screenshots from a sequence of images, based on the fact that loading screens are very similar in color. Although, it can be repurposed to extract only loading screens from a sequence of images (commenting and uncommenting some parts should suffice)

# Folders
There is tiny `LoadingScreensDataset` folder you can train your neural networks on.

There is also `TestingDataset` folder  which can be used for testing CNN on real data.

There is `Weights` folder containing 3 weights files used in `classify_and_sort.py`.

There is empty `TestDataResults` folder, it will contain classified images after you run `classift_and_sort.py`
