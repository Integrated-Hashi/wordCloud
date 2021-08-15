# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:58:49 2021

@author: integrated_hashi
"""
import re
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS

file = open(r"message.txt",encoding='utf-8').read()
file = re.sub('[^\u4e00-\u9fa5]+',"", file)
default_mode =jieba.cut(file)
text = " ".join(default_mode)

stopwords = set(STOPWORDS)
content = [line.strip() for line in open('hit_stopwords.txt','r',encoding='utf-8').readlines()]
stopwords.update(content)
stopwords

alice_mask = np.array(Image.open(r"20190131160157591.png"))
#stopwords = set(STOPWORDS)
stopwords.add("图片")
stopwords.add("赵")
stopwords.add("三岁")
stopwords.add("微信")
stopwords.add("版本")
stopwords.add("最新")
stopwords.add("微博")
stopwords.add("国际版")
stopwords.add("消息")
wc = WordCloud(
    font_path=r'苹方黑体-准-简.ttf',
    background_color="white",
    max_words=500,
    mask=alice_mask,
    scale=32,
    stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file("01.jpg")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
