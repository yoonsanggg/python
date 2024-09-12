import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 한글 폰트 경로 (윈도우의 경우 Malgun Gothic 폰트 경로)

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
# d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# text = open(path.join(d, 'constitution.txt')).read()
f = open("ex/게티즈버그한글.txt",'r',encoding="utf-8")
text = f.read()
# Generate a word cloud image
wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf").generate(text)
# Display the generated image:
# the matplotlib way:
# plt.imshow(wordcloud, interpolation='bilinear')
# 축 만드는애
# plt.axis("off")

# lower max_font_size <==폰트 최대크기 지정
# wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
# 이미지 만드는거
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()