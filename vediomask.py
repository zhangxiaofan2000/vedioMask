from copy import deepcopy
import numpy as np
from PIL import Image
from moviepy.editor import *

video = VideoFileClip('./data/视频.mp4')
mask = np.array(Image.open('./data/视频mask.png').convert('RGB'))
mask = np.array(Image.fromarray(mask).resize((video.w, video.h)))

invisible = mask!=[255,255,255]

def add_mask(frame):
    image_new = deepcopy(frame)
    image_new[invisible] = mask[invisible]
    return image_new

video.fl_image(add_mask).write_videofile('./data/测试视频_图片mask.mp4')
