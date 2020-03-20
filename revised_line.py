# -*- coding: utf-8 -*-

impor pyerclip
#pyperclip.copy() #用于向计算机的剪贴板发送文本;
#pyperclip.paste() #用于从计算机剪贴板接收文本;

def revise_lines(ptn="*",fn="F:/Git2/English/test/bigtan.txt"):
    """修订词条"""
    fn="F:/Git2/English/test/unix.txt"

    dt=English_Dictionary().load(fn) #待分裂的词典

# re在old行中匹配,n个
# 将匹配到的行写入粘贴,
# new=input("Revised:") #使用Ctrl+V复制old,然后修改
将新行
# 
    words = dt.match(ptn)

    if len(words)==0:  
        return "模式<{}>未匹配到单词! 请重新设置!".format(ptn)
    else: 
        print("\n共匹配到单词: {}个!".format(len(words)))
    
    if flag: random.shuffle(words) #是否对单词进行随机筛选
    
    
    for word in words:
        print("#"*64)
        printf_word(dt.to_line(word))
        
        cmd=input(">>>bad/good[!空]:") #默认将该单词条分类到哪个文件
        
        ln=omit_line(dt.to_line(word)) #缩略行
        
        if cmd=="exit" or cmd=="0":         
            dt.to_txt(fn,mod='w')
            bad.to_txt(bf,mod='a+') #保存到文件才算完成这项工作,放到循环外
            good.to_txt(gf,mod='w') #避免频繁的保存文件
            return "Save and Exit!" #但是也要保证在程序自动退出之前,也必须要保存
        
        elif cmd=="": 
            bad.edt[word]=dt.edt[word] #cmd为空,放到无用文件
            print("`{}`; (+){}".format(bf.split('/')[-1],ln))
        else:
            good.edt[word]=dt.edt[word] #cmd非空,放到有用文件
            print("`{}`; (+){}".format(gf.split('/')[-1],ln))
            
        del dt.edt[word] #删除原始文件中的词条
        print("`{}`; (-){}".format(fn.split('/')[-1],ln))
    
    #所有单词遍历完之后也要保存
    dt.to_txt(fn,mod='w')
    bad.to_txt(bf,mod='a+') #保存到文件才算完成这项工作,放到循环外
    good.to_txt(gf,mod='a+') #避免频繁的保存文件
    return "Done and Exit!" #但是也要保证在程序自动退出之前,也必须要保存



# def see_you_again(fn="F:/Git2/English/test/unix.txt",matcher="*",flag=False):
#     """将一个文件将文件进行二分类: good/bad;"""
#     backup(fn)
#     fn="F:/Git2/English/test/unix.txt"
#     bf = fn+'.bad'
#     gf = fn+'.good'

#     for file in [bf,gf]: #不存在的时候创建空白文件
#         if os.path.exists(file)==False:
#             with open(file,'w',encoding='utf-8') as fp: pass
#     bad = English_Dictionary().load(bf)
#     good = English_Dictionary().load(gf)

#     dt=English_Dictionary().load(fn) #待分裂的词典
#     words = dt.match(matcher)
#     if len(words)==0:  
#         return "模式<{}>未匹配到单词! 请重新设置!".format(matcher)
#     else: 
#         print("\n共匹配到单词: {}个!".format(len(words)))
    
#     if flag: random.shuffle(words) #是否对单词进行随机筛选
    
    
#     for word in words:
#         print("#"*64)
#         printf_word(dt.to_line(word))
        
#         cmd=input(">>>bad/good[!空]:") #默认将该单词条分类到哪个文件
        
#         ln=omit_line(dt.to_line(word)) #缩略行
        
#         if cmd=="exit" or cmd=="0":         
#             dt.to_txt(fn,mod='w')
#             bad.to_txt(bf,mod='a+') #保存到文件才算完成这项工作,放到循环外
#             good.to_txt(gf,mod='w') #避免频繁的保存文件
#             return "Save and Exit!" #但是也要保证在程序自动退出之前,也必须要保存
        
#         elif cmd=="": 
#             bad.edt[word]=dt.edt[word] #cmd为空,放到无用文件
#             print("`{}`; (+){}".format(bf.split('/')[-1],ln))
#         else:
#             good.edt[word]=dt.edt[word] #cmd非空,放到有用文件
#             print("`{}`; (+){}".format(gf.split('/')[-1],ln))
            
#         del dt.edt[word] #删除原始文件中的词条
#         print("`{}`; (-){}".format(fn.split('/')[-1],ln))
    
#     #所有单词遍历完之后也要保存
#     dt.to_txt(fn,mod='w')
#     bad.to_txt(bf,mod='a+') #保存到文件才算完成这项工作,放到循环外
#     good.to_txt(gf,mod='a+') #避免频繁的保存文件
#     return "Done and Exit!" #但是也要保证在程序自动退出之前,也必须要保存
