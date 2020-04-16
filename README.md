bigtan: 模块ddpie.english的词库.
===========================

# 如何记单词

## 带入情景记忆
1. 只有明白在汉语的意思才能明白在英语的意思 
1. China Daily,美剧等的上下文
1. 生活场景: 路牌,菜单

## 词意
1. 查询单词的同义词集
1. 英文定义等

## 词形  
1. 对比形似的单词: terrestrial/territorial
1. 使用的unix shell的匹配模式过滤单词
    *. `*`: 匹配0或多个字符  
    *. `?`: 匹配任意一个字符  
    *. `[list]`: 匹配list中的任意单一字符; `[c1-c2]`: 匹配c1-c2中的任意单一字符  
    *. `[!list]`: 匹配除list中的任意单一字符
1. 拼写错误=>拼写正确

## 构建自己的词汇表:
1. 明晰自己的词汇掌握程度
1. 构建自己的词汇表(熟悉/不熟悉)

## 听力
1. 将视频转化为音频  

# basic
01_zhongkao_bcz.ht: 2363
02_gaokao_bcz.ht: 4124
03_4ji_bcz.ht: 3486
04_6ji_bcz.ht: 3071
05_kaoyan_bcz.ht: 6279
06_zhuan4_bcz.ht: 5203
07_zhuan8_bcz.ht: 2838
08_yasihx.bcz.ht: 3272
09_tuofu_bcz.ht: 4686
10_jjxr_bcz.ht
11_sat_bcz.ht: 2947
12_gre3k_bcz.ht: 2904
13_gmat_bcz.ht: 3000
14_tuoyehx_bcz.ht: 1469
15_bec1_bcz.ht
16_bec2_bcz.ht
17_bec3_bcz.ht
21_5k_oxf.ht
22_spoken_oxf.ht
23_written_oxf.ht
81_toefl_ibt.包含不可覆盖的头部.txt: 不是标准的head-tail文件,其头部有重复;

# phrase.ht
短语词条,仍在完善当中

## spk1
1. Signposting and focusing in lectures/lessons,在论坛和讲座过程中引导方向和集中注意力;
2. Specifying topics and relations between ideas,指明话题和观点之间的联系
3. Drawing attention to something or focusing on it,吸引注意力
4. Clarifying and restating,阐明和重新开始
5. Giving examples,给出示例
6. Adding,另外
7. Using vague language,使用流行语
8. Classifying and comparing things,分类和比较
9. Making contrasts,对照
10. Expressing relationships between things and ideas,表达事物和注意之间的联系
11. Expressing aims, causes and effects,目标,事业,影响
12. Ordering content and making time references,订购内容和制作时间参考 
13. Hedging and expressing degrees of certainty,套期保值与确定度表达 
14. Marking a shift in or change of topic,改变话题
15. Direct address or instruction to students/audience,直接向学生/听众演讲或指导 
16. Expressing quantity and increase/decrease,表达数量递增或递减

## writen
1. Specifying topics and relations between ideas,
3. Hedging and expressing degrees of certainty,
4. Explaining and defining,
5. Giving examples or presenting evidence,
6. Expressing aims, causes and effects,
7. Making contrasts,
8. Comparing,
9. Adding,
10. Expressing quantity/degree and increase/decrease,
11. Expressing the existence/non-existence of something,
12. Referring to the text and to other texts,
13. Referring to time,
14. Phrases with (the) (noun) of,
15. Miscellaneous,

# word.ht
包含10万条纯文本的简易词条,来自参考


# 参考
1. [有道词典](http://dict.youdao.com/w/eng/tan/#keyfrom=dict2.index);
1. 百词斩词库: `lookup.db`
1. unix = nltk.corpus.words.words('en')
1. [2019年普通高等学校招生全国统一考试大纲](http://www.neea.edu.cn/res/Home/1901/d15ec0514666ac280810099f9595b557.pdf)
1. [2018 年全国硕士研究生招生考试英语(一)考试大纲(非英语专业)](http://www.hep.edu.cn/book/details?uuid=78396d2-1581-1000-ab16-55b34aba28f0&objectId=oid:7839755-1581-1000-ab17-55b34aba28f0)