import numpy as np
import torch

class Flickr_Data(object):

    def __init__(self,  all_text,imgs,img_f ,split):

        text_f = {}
        for name in imgs:
            text_f[name] = all_text[name]
        if split == "test":
                self.img_features, self.text_features, self.img_name, self.allcaps = self.flatten_dataset(img_f, text_f,split)
        else:

                self.img_features, self.text_features, self.img_name = self.flatten_dataset(img_f, text_f)



        self.split=split













    def flatten_dataset(self,  image_features, Text_features,split='train'):
        Img, Text, nams,all_caps = [], [], [],[]

        for img_name, cpts in Text_features.items():

            for cpt in cpts:
                Text.append(cpt)
                Img.append(image_features[img_name])
                nams.append(img_name)
                if split == "test":
                    all_caps.append(cpts)
        if split == "test":
            return Img,Text , nams,all_caps



        return Img,Text , nams







__factory = {
    'Flickr': Flickr_Data,
    'ERI': Flickr_Data,
    'FERI':Flickr_Data,
    'scol':Flickr_Data,
    'strt':Flickr_Data,
    'stsc':Flickr_Data,
    'coco':Flickr_Data,
}

def get_names():
    return __factory.keys()

def prepare_data(name, all_text,imgs, features,split, *args, **kwargs):
    if name not in __factory.keys():
        raise KeyError("Unknown dataset: {}".format(name))
    return __factory[name]( all_text=all_text,imgs=imgs, img_f=features,split=split, *args, **kwargs)
if __name__ == '__main__':
    dataset = Flickr_Data()