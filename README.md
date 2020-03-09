# English 字典

# revising.txt: 该文件用于修订其它列表中的词条.
1. 使用`to_revising`将某个修改后的词条追加到该文件.
2. 查找所有属于某个词表的词条,例如`[or]="zk"`,将其剪切到词表后面
3. 使用 `EngDict("01_zhongkao_bcz.txt").to_txt()`更新词表.

# word/
01_zhongkao_bcz: 2363
02_gaokao_bcz: 4124
03_4j_bcz: 3486
04_6j_bcz: 3071
05_kaoyan_bcz: 6279
06_zhuan4_bcz: 5203
07_zhuan8_bcz: 2838
08_yasihx_bcz: 3272
10_tuofu_bcz: 4686
11_sat_bcz: 2947
12_gre3k_bcz: 2904
13_gmat_bcz: 3000
14_tuoyehx_bcz: 1469
special: 专有名词等
names: 通过有道查的 corpus-names 词汇, 2741
unix: 通过有道查的 unix-words 词汇, 71086
toefl_ibt: 3465; 不要丢弃注释;


## URL
2019年普通高等学校招生全国统一考试大纲: http://www.neea.edu.cn/res/Home/1901/d15ec0514666ac280810099f9595b557.pdf

奥格登(Ogden)850词: `C:\Users\DELL\AppData\Roaming\nltk_data\corpora\words\en-basic`
未在`data/`词表中出现的词汇: `I, a, be, but, by, from, grey, of, when, where, who, with`;

names: corpus.names.words()

unix: corpus.words.words()

Oxford 词表


