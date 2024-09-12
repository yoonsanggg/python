text = open("ex/게티즈버그.txt",'r',encoding="utf-8")
here ={}
while True :
    read = text.readline()
    if not read :
        break
    go = read.replace(".","").replace(",","").replace("\n","").split(" ")
    
    for list in go:
        print(f"list:{list}")
        ho = list.strip()
        print (f"ho:{ho}")
        if ho in here:
            here[ho] += 1
        else :
            here[ho] = 1
res = sorted(here.items(),key=lambda x:x[1],reverse=True)
print(res)
        
        
    
words = read.strip().replace(",","").replace(".","").split(" ")



"""
text = open("ex/게티즈버그.txt",'r',encoding='utf-8')
dic ={}
value = 1
# search = input("단어:")
while True :
    line = text.readline()
    if not line :
        break
    line = line.strip().replace(".","").replace(",","")
    word = line.split(" ")
    for list in word :
        if list in dic:
            dic[list] +=1
        else :
            dic[list] = 1
            # 키 값 쌍으로 가져 나오는겨
            # 정렬에 쓰일 값을 키로 가져나오는교
            # 거꾸로 정렬
end = sorted(dic.items(),key= lambda item:item[1], reverse=True)

print(end)
print(len(end))
"""



# for line in text.readlines():
#     dic = line.replace("\n","").replace(",","").replace(".","").replace("","").split(" ")
#     print(dic)



# word = input("찾을 단어 : ")

# if word in dic :
#     for k in dic:
#         dic.update(word)
#         dic[word] += 1
#         print(dic)
#         if k == len(word):
#             break