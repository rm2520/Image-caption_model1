
import torch
import models
import torchvision.models as models_v
from torchvision import transforms as T
from PIL import Image
import pickle
import torch.nn as nn
from gtts import gTTS

import os
import argparse
parser = argparse.ArgumentParser(description='Train image with captian')
parser.add_argument('--img_size', type=int, default=224, help='size for randomly cropping images')
parser.add_argument('--model_path', type=str, default='logs/LSTM', help='path for saving trained models')
parser.add_argument('--model_checkpoint_file', type=str, default='ERI_best.pth', help='checkpoint file name')
parser.add_argument('--model_vocab', type=str, default='ERI_ vocab_3 .pkl', help='vocab of model')
parser.add_argument('--test_img', type=str, default='strt_00769.jpeg', help='vocab of model')
args = parser.parse_args()
import os
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
def main():
    #get model parameter
    checkpoint = torch.load( os.path.join(args.model_path,args.model_checkpoint_file))
    img_dim=checkpoint['img_embedding.weight'].shape[1]
    text_dim=checkpoint['text_embedding.weight'].shape[0]
    # define model
    model = models.init_model(name='sabri', num_classes=text_dim, img_dim=img_dim).cuda()
    #load model parameter
    model.load_state_dict(checkpoint)
    model.eval()
    transform = T.Compose([
        T.Resize((args.img_size, args.img_size)),
        T.RandomHorizontalFlip(),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    #load vocab
    vocab = pickle.load(open(os.path.join(args.model_path, args.model_vocab), 'rb'))

    ########
    # get mobilenet model
    images_root = 'data/wasef_Dataset/wasef_img'

    mobilenet_model = models_v.mobilenet_v2(pretrained=True).cuda()

    removed = list(mobilenet_model.children())[:-1]
    mobilenet_model = nn.Sequential(*removed)
    mobilenet_model.eval()



    #get caption
    get_caption(images_root, args.test_img, transform, mobilenet_model, model, vocab.vocab)
    #get_caption('data/Flicker8k_Dataset/', '2501968935_02f2cd8079.jpg', transform, vgg_model, model, vocab.vocab)



def get_caption(images_root,images_name,transform,Img_model,model,vocab):
    """reads image and returns caption"""
    img_path = os.path.join(images_root,images_name)
    image = Image.open(img_path).convert('RGB')
    image = transform(image)
    image = torch.unsqueeze(image, 0).cuda()
    feat = Img_model(image)
    caption = model.caption_image(feat.cuda(), vocab)
    mytext=desegment(" ".join(caption))
    print(mytext)
    index=len(caption)-1
    voice=desegment(" ".join(caption[1:index]))

    language = 'ar'

    myobj = gTTS(text=voice, lang=language, slow=False)
    myobj.save("output.mp3")

    os.system("start output.mp3")

def desegment(line):
    line = line.replace("+ ", "")
    line = line.replace(" +", "")
    line=line.replace("+", "")
    return line

if __name__ == '__main__':
     main()