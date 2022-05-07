from unicodedata import category
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import random
import os
import shutil


plt.style.use("seaborn-white")


train_path = "original_data/train/train/"


def pick_random_imgs(data_path, n_of_images=10):

    image_names= os.listdir(data_path)
    image_names_picked = random.sample(image_names, n_of_images)
    return image_names_picked

def get_label(image_names_picked):
    labels=[]
    images=[]

    for image_name in image_names_picked:
        label = image_name.split('.')[0]
        if label == 'cat':
            labels.append(0)
        else:
            labels.append(1)
        img = plt.imread(f"{data_path}{image_name}")
        images.append(img)
    
        
    return images, labels

def plot_imgs(images, labels, ncols = 5, figsize = (20,20), n_of_images=10):
    nrows = int(n_of_images/ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize = figsize)
	
    for i, ax, label in zip(range(n_of_images), axes.flatten(), labels):
        ax.imshow(images[i])
        ax.axis("off")
        if label==0:
            ax.set(title=f'{label}:cat')
        else:
            ax.set(title=f'{label}:dog')

    fig.subplots_adjust(wspace=0.1, hspace=0.1, bottom=0.01, top=0.4)


def save_images(processed_images_path, data):
    for img_name in data:
        source_path = f"{train_path}{img_name}"
        target_path = f"{processed_images_path}{img_name}"
        shutil.copyfile(source_path, target_path)