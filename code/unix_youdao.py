# F:/Git2/English/test/unix_youdao.py
import requests
from bs4 import BeautifulSoup
def unix_adding(word):    
    try:
        url_yd = "http://dict.youdao.com/w/%s/#keyfrom=dict2.top" % word
        r = requests.get(url=url_yd)

        # 利用BeautifulSoup将获取到的文本解析成HTML
        soup = BeautifulSoup(r.text, "lxml")
        # 获取字典的标签内容
        s = soup.find(class_="trans-container")("ul")[0]("li")
        additional = soup.find(class_="additional").get_text()
        phonetic = soup.find(class_="phonetic").get_text()
        phonetic = '[a]'+'/'+phonetic[1:len(phonetic)-1]+'/;'
        additional=additional.replace('\n','/').replace(' ','')
        additional = additional.strip('[').strip(']').strip('/').split('/')
        add1=additional[0::2]
        add2=additional[1::2]

        add = '[add]'
        for i,j in zip(add1,add2):
            add = add+i+'/'+j+','
        meanings = ''
        for item in s:
            if item.text:
                meanings = meanings+biaodian(item.text)+'; '
        meanings = meanings.replace('n. ','[n]').replace('vt. ','[vt]').replace('adj. ','[adj]').replace('adv. ','[adv]')
        return "{}: {} {}{}".format(word,phonetic,meanings,add+';')
    except Exception: return 0

#######################################################
## 26个单词列表对应的单词 a,b,...,z
for alpha in Alphabet:
    unix_alpha='unix_'+alpha.lower()
    fn="F:/Git2/English/unix/{}.txt".format(alpha)
    wds = set(EngDict(fn).words)
    exec("{}={}".format(unix_alpha,'wds'))
print("="*32)

## 已知单词
know1 = set(EngDict('all').words)
know2 = set(EngDict('F:/Git2/English/unix/unix_meanings.txt').words)
know=know1.union(know2)
print("="*32)

#######################################################
## 选定待查的范围
unix_alpha = unix_x
fn_out='F:/Git2/English/test/{}.txt'.format('unix_test')
fn_out2=fn_out+'.nomeaning'
## 待查单词,排除已知含义的单词
lookuping = unix_alpha.difference(know) 
lookuping = list(lookuping)[:20]
#######################################################
len_lookuping=len(lookuping)
with open(fn_out,mode='w',encoding='utf-8') as fn1: 
    print("Writing: {}".format(fn_out))
    print("Writing: {}".format(fn_out2))
    with open(fn_out2,mode='w',encoding='utf-8') as fn2:  #with不要放进循环
        for i,word in enumerate(lookuping):
            line = unix_adding(word)
            if line==0: fn2.write(word+'\n')
            else: fn1.write(line+'\n')
            num=i+1
            print("{}/{}: {}".format(num,len_lookuping,word))

################################
# 查找科目标签
with open('F:/Git2/English/test/unix_simple.txt','r',encoding='utf-8') as fn:
    raw=fn.readlines()
with open('F:/Git2/English/test/unix_simple.txt','r',encoding='utf-8') as fn2:
    string=fn2.read()

subject=[]
for line in raw:
    pat="^.*\]\[(\w{1,20})\].*$"
    ex=re.findall(pat,line)
    if ex!=[]:
        for i in ex:
            subject.append(i)
subject=list(set(lt).difference(set({'adj','n'})))

# 替换科目标签
for word in subject: 
    old='['+word+']'
    new='<'+word+'>'
    string = string.replace(old,new)
    
with open('F:/Git2/English/test/unix_simple_new.txt','w',encoding='utf-8') as fn3:
    fn3.write(string)