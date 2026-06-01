import torch
import torchvision.transforms as transforms
import torch.utils.data as data
import os
import pickle
import numpy as np
import nltk
from PIL import Image
from torch.utils.data import Dataset




class Load_Data(Dataset):
    def __init__(self, dataset):

       self.dataset=dataset



    def __getitem__(self, index):



        text_features = self.dataset.text_features[index]
        img_name = self.dataset.img_name[index]
        img_features = self.dataset.img_features[index]


        if self.dataset.split == "test":
            all_caps=self.dataset.allcaps[index]
            return img_features,text_features,img_name,all_caps


        return img_features,text_features,img_name



    def __len__(self):
            return len(self.dataset.img_name)








