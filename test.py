#encoding=utf-8
import jieba.posseg as pseg

f = open('sample1.txt', 'r')
txt = f.read()
seg_list = pseg.cut(txt)  # 默认是精确模式
for seg in seg_list:
    print(seg.word, seg.flag)
