import os
import pandas as pd



"""Create dataset"""
class Flickr8KDataset(object):
    images_root = 'data/Flicker8k_Dataset/'
    arabic_captions_path = 'data/Flickr8k_text/Flickr8k.arabic.full.txt'
    train_path = 'data/Flickr8k_text/Flickr_8k.trainImages.txt'
    test_path = 'data/Flickr8k_text/Flickr_8k.testImages.txt'
    dev_path = 'data/Flickr8k_text/Flickr_8k.devImages.txt'
    test_size=1000
    dev_size=1000
    def __init__(self,split):
        img_names = os.listdir(self.images_root) #get list of image names
        captions_file_text= self.load_file_text(self.arabic_captions_path)#read caption file
        captions=self.get_captions(captions_file_text) # get image-names,caption
        if split=='file':
            train_img = self.get_imgnames_file(self.load_file_text(self.train_path))
            test_img = self.get_imgnames_file(self.load_file_text(self.test_path))
            dev_img = self.get_imgnames_file(self.load_file_text(self.dev_path))
        else:
            tot_size=self.test_size+self.dev_size
            test_img=self.get_imgnames(img_names[:self.test_size])
            dev_img=self.get_imgnames(img_names[self.test_size:tot_size])
            train_img=self.get_imgnames(img_names[tot_size:])

        self.images=img_names
        self.captions=captions
        self.trainimg=train_img
        self.testimg = test_img
        self.devimg = dev_img




    def load_file_text(self,file_path):
        """reads arabic text and returns text in captions file """
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs=[line.split('.')[0] for line in file_text.split('\n')]
        imgs=imgs[0:-1]


        return imgs

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs

class ERI_Dataset(object):
    images_root = 'data/wasef_dataset/wasef_img/'
    arabic_captions_path = 'data/wasef_dataset/wasef_txt/final_text_caption.txt'
    train_path = 'data/wasef_dataset/wasef_txt/wasef_train80.txt'
    test_path = 'data/wasef_dataset/wasef_txt/wasef_test20.txt'
    # dev_path = 'data/ERI_text/ERI.devImages.txt'
    test_size = 2073
    dev_size = 889
    dev_size = 1000
    def __init__(self,split):
        img_names = os.listdir(self.images_root)
        captions_file_text= self.load_file_text(self.arabic_captions_path)
        captions=self.get_captions(captions_file_text)
        if split=='file':
            train_img = self.get_imgnames_file(self.load_file_text(self.train_path))
            test_img = self.get_imgnames_file(self.load_file_text(self.test_path))
            #dev_img = self.get_imgnames_file(self.load_file_text(self.dev_path))
        else:
            tot_size=self.test_size+self.dev_size
            test_img=self.get_imgnames(img_names[:self.test_size])
            #dev_img=self.get_imgnames(img_names[self.test_size:tot_size])
            train_img=self.get_imgnames(img_names[tot_size:])

        self.images=img_names
        self.captions=captions
        self.trainimg=train_img
        self.testimg = test_img
        #self.devimg = dev_img





    def load_file_text(self,file_path):
        """reads and returns text in captions file"""
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs=[line.split('.')[0] for line in file_text.split('\n')]
        imgs=imgs[0:-1]


        return imgs

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs
class coco_Dataset(object):
    images_root = 'data/coco_dataset/'
    arabic_captions_path = 'data/coco_text/coco_caption.txt'
    train_path = 'data/coco_text/coco_train.txt'
    test_path = 'data/coco_text/coco_test.txt'
    #dev_path = 'data/ERI_text/ERI.devImages.txt'
    test_size = 16500
    dev_size = 889
    def __init__(self,split):
        img_names = os.listdir(self.images_root)
        captions_file_text= self.load_file_text(self.arabic_captions_path)
        captions=self.get_captions(captions_file_text)
        if split=='file':
            train_img = self.get_imgnames_file(self.load_file_text(self.train_path))
            test_img = self.get_imgnames_file(self.load_file_text(self.test_path))
            #dev_img = self.get_imgnames_file(self.load_file_text(self.dev_path))
        else:
            tot_size=self.test_size+self.dev_size
            test_img=self.get_imgnames(img_names[:self.test_size])
            #dev_img=self.get_imgnames(img_names[self.test_size:tot_size])
            train_img=self.get_imgnames(img_names[tot_size:])

        self.images=img_names
        self.captions=captions
        self.trainimg=train_img
        self.testimg = test_img
        #self.devimg = dev_img





    def load_file_text(self,file_path):
        """reads and returns text in captions file"""
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs=[line.split('.')[0] for line in file_text.split('\n')]
        imgs=imgs[0:-1]


        return imgs

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs
class Flickr_ERI_Dataset(object):

    images_root = 'data/FERI_Dataset/FERI_imgs/'
    arabic_captions_path = 'data/FERI_Dataset/FERI_text/final_text_caption.txt'
    train_path = 'data/FERI_Dataset/FERI_text/wasef_train80.txt'
    test_path = 'data/FERI_Dataset/FERI_text/wasef_test20.txt'

    arabic_captions_path2 = 'data/FERI_Dataset/FERI_text/Flickr8k.arabic.full.txt'
    train_path2 = 'data/FERI_Dataset/FERI_text/Flickr_8k.trainImages.txt'
    test_path2 = 'data/FERI_Dataset/FERI_text/Flickr_8k.testImages.txt'
    dev_path2 = 'data/FERI_Dataset/FERI_text/Flickr_8k.devImages.txt'



    def __init__(self,split):

        wasef_file_text= self.load_file_text(self.arabic_captions_path)
        fliker_file_text = self.load_file_text(self.arabic_captions_path2)
        caption_file=wasef_file_text + fliker_file_text



        Fliker_train_ID,Fliker_train_nme=self.get_imgnames_file(self.load_file_text(self.train_path2))
        Fliker_test_ID,Fliker_test_nme = self.get_imgnames_file(self.load_file_text(self.test_path2))
        ERI_train_ID,ERI_train_nme = self.get_imgnames_file(self.load_file_text(self.train_path))
        ERI_test_ID,ERI_test_nme = self.get_imgnames_file(self.load_file_text(self.test_path))

        FERI_captions=self.get_captions(caption_file) # get image-names,caption
        train_img=Fliker_train_ID+ERI_train_ID


        test_img=ERI_test_ID+Fliker_test_ID
        img_names = os.listdir(self.images_root)








        self.images=img_names
        self.captions=FERI_captions
        self.trainimg=train_img
        self.testimg = test_img





    def load_file_text(self,file_path):
        """reads arabic text and returns text in captions file """
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs_ID=[line.split('.')[0] for line in file_text.split('\n')]
        imgs_ID=imgs_ID[0:-1]
        imgs_nme = [line for line in file_text.split('\n')]
        imgs_nme = imgs_nme[0:-1]


        return imgs_ID,imgs_nme

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs

class scol_Dataset(object):
    images_root = 'data/FERI_Dataset/FERI_imgs'
    scol_captions_path = 'data/FERI_Dataset/FERI_text/text_caption.txt'
    train_path_scol = 'data/FERI_Dataset/FERI_text/scol_train_img.txt'
    test_path_scol = 'data/FERI_Dataset/FERI_text/scol_test_img.txt'



    def __init__(self,split):

        scol_file_text= self.load_file_text(self.scol_captions_path)




        train_img,scol_train_nme=self.get_imgnames_file(self.load_file_text(self.train_path_scol))
        test_img,scol_test_nme = self.get_imgnames_file(self.load_file_text(self.test_path_scol))


        FERI_captions=self.get_captions(scol_file_text) # get image-names,caption




        img_names=scol_train_nme+scol_test_nme








        self.images=img_names
        self.captions=FERI_captions
        self.trainimg=train_img
        self.testimg = test_img





    def load_file_text(self,file_path):
        """reads arabic text and returns text in captions file """
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs_ID=[line.split('.')[0] for line in file_text.split('\n')]
        imgs_ID=imgs_ID[0:-1]
        imgs_nme = [line for line in file_text.split('\n')]
        imgs_nme = imgs_nme[0:-1]


        return imgs_ID,imgs_nme

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs

class street_Dataset(object):
    images_root = 'data/FERI_Dataset/FERI_imgs'
    st_captions_path = 'data/FERI_Dataset/FERI_text/text_caption.txt'
    train_path_st = 'data/FERI_Dataset/FERI_text/street_train_img.txt'
    test_path_st = 'data/FERI_Dataset/FERI_text/street_test_img.txt'



    def __init__(self,split):

        st_file_text= self.load_file_text(self.st_captions_path)




        train_img,st_train_nme=self.get_imgnames_file(self.load_file_text(self.train_path_st))
        test_img,st_test_nme = self.get_imgnames_file(self.load_file_text(self.test_path_st))


        FERI_captions=self.get_captions(st_file_text) # get image-names,caption




        img_names=st_train_nme+st_test_nme








        self.images=img_names
        self.captions=FERI_captions
        self.trainimg=train_img
        self.testimg = test_img





    def load_file_text(self,file_path):
        """reads arabic text and returns text in captions file """
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs_ID=[line.split('.')[0] for line in file_text.split('\n')]
        imgs_ID=imgs_ID[0:-1]
        imgs_nme = [line for line in file_text.split('\n')]
        imgs_nme = imgs_nme[0:-1]


        return imgs_ID,imgs_nme

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs

class stsc_Dataset(object):
    images_root = 'data/FERI_Dataset/FERI_imgs'
    scst_captions_path = 'data/FERI_Dataset/FERI_text/text_caption.txt'
    train_path_scst = 'data/FERI_Dataset/FERI_text/scst_train_img.txt'
    test_path_scst = 'data/FERI_Dataset/FERI_text/scst_test_img.txt'



    def __init__(self,split):

        scst_file_text= self.load_file_text(self.scst_captions_path)




        train_img,scst_train_nme=self.get_imgnames_file(self.load_file_text(self.train_path_scst))
        test_img,scst_test_nme = self.get_imgnames_file(self.load_file_text(self.test_path_scst))


        FERI_captions=self.get_captions(scst_file_text) # get image-names,caption




        img_names=scst_train_nme+scst_test_nme








        self.images=img_names
        self.captions=FERI_captions
        self.trainimg=train_img
        self.testimg = test_img





    def load_file_text(self,file_path):
        """reads arabic text and returns text in captions file """
        file = open(file_path, 'r', encoding='utf-8')
        all_text = file.read()
        file.close()
        return all_text

    def get_captions(self,file_text):

        cpts = {}
        # loop through lines
        for line in file_text.split('\n'):  # each line contains image name & its caption separated by tab
            # split by tabs
            img_cpt = line.split('\t')
            if len(img_cpt) < 2: continue
            img, cpt = img_cpt
            # remove image extension & index (remove everything befor the dot)
            img_name = img.split('.')[0]
            # add to dictionary
            if img_name not in cpts:
                cpts[img_name] = [cpt]
            else:
                cpts[img_name].append(cpt)
        return cpts
    def get_imgnames_file(self,file_text):


        imgs_ID=[line.split('.')[0] for line in file_text.split('\n')]
        imgs_ID=imgs_ID[0:-1]
        imgs_nme = [line for line in file_text.split('\n')]
        imgs_nme = imgs_nme[0:-1]


        return imgs_ID,imgs_nme

    def get_imgnames(self, imgs_name):

        imgs = [img.split('.')[0] for img in imgs_name]
        return imgs
__factory = {
#names of datset
    'Flickr': Flickr8KDataset,
    'ERI': ERI_Dataset,
    'FERI':Flickr_ERI_Dataset,
    'scol':scol_Dataset,
    'strt':street_Dataset,
    'stsc':stsc_Dataset,
    'coco':coco_Dataset,


}

def get_names():
    return __factory.keys()

def init_dataset(name,split, *args, **kwargs):
    if name not in __factory.keys():
        raise KeyError("Unknown dataset: {}".format(name))
    return __factory[name](split,*args, **kwargs)



if __name__ == '__main__':
    # test

    dataset = Flickr8KDataset()
