from PIL import Image, ImageOps
import pandas as pd
import os

 
dir = ['./Klikun/', './Shipun/', './Bewick/']
ans_dir = './All/'
# for el in dir:
#     for index, filename in enumerate(os.listdir(el)):
#         img = Image.open(os.path.join(el, filename))
#         new_img = img.convert('RGB')
#         new_img = ImageOps.pad(new_img, (900, 600), color= '#42AAFF', method=Image.LANCZOS)
#         new_img.save(os.path.join(ans_dir,filename))
        #os.rename(os.path.join(el, filename), os.path.join(el, f'{el.lower()[2:-1]}-{index}.jpg'))

images = os.listdir(ans_dir)
df = pd.DataFrame()
df['images']=[ans_dir+x for x in images]
df['labels']=[x[:6] for x in images]
df.to_csv('Swans.csv')