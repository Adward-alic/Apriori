# -*- coding: utf-8 -*-
# @Author  : Mr.Y
# @Time    : 2022/9/28 10:55
# @Email   : 1480921330@qq.com
# @Github  : https://github.com/Adward-alic

# 数据库 D； C 候选集（数据结构为列表，元素为集合，集合内为各个项）；L 频繁项集的集合，元素为列表; Support_min  最小支持度；sup_C 字典，候选集及其支持度;sup_data 所有的候选集及其支持度数据

#

#录入数据
def GetDataBase():
    return [[1,2,5],
            [2,4],
            [2,3],
            [1,2,4],
            [1,3],
            [2,3],
            [1,3],
            [1,2,3,5],
            [1,2,3]]

#原始数据，并且得到频繁一项集，输入是最小支持度和数据库
#输出是列表，列表中的元素为集合，每个集合内元素为项
def GetFrenquent_1(D,support_min):
    #获得了所有商品项集
    C1=[]
    for transction in D:
        for item in transction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    #计算机所有商品的支持度
    #构建一个元素不可变集合
    return list(map(frozenset,C1))


#扫描函数，输入候选项集，输出符合支持度的频繁项集，以及所有候选项集的支持度
#s实现对总体数据的扫描；并且滤除不符合支持度的项集,生成一个符合支持度的项集list，以及一个完整的频繁项集字典
def ScanDataBase(D,CK,support_min):
    #Scan是扫描过后的项集字典，key是项集，数是支持度计数
    Scan={}
    for Transction in D:
        for can in CK:
            if can.issubset(Transction):
               if not can in Scan:
                   Scan[can]=1
               else:
                   Scan[can]+=1
   #有多少交易数量
    num_tranction=len(list(D))
   #合格项集
    nice_list=[]
    support_data={}
    for key in Scan:
        support=Scan[key]/num_tranction
        if support >= support_min:
            nice_list.insert(len(list(CK)),key)
        support_data[key]=support

    return nice_list,support_data

# 剪枝，拼接操作
# 输入是频繁项集，输出是一个候选项集集
def apriori_gen(Lk,k):
    #返回一个剪枝后的项集
    reList=[]
    for i in range(len(Lk)):
        # for j in range(len(Lk)):
        j=1
        while(j+i<len(Lk)):
            #进行剪枝操作的时候要保证
            L1=list(Lk[i])[:k-2]
            L2=list(Lk[j+i])[:k-2]
            if L1 == L2 :
                reList.append(Lk[i]|Lk[j+i])
            j += 1

    print(reList)
    return reList

if __name__ == '__main__':
    #接口用于处理数据，数据格式参照自定义返回值
    min_support=float(input("please input the min_support="))
    DataBase=GetDataBase()
    C1=GetFrenquent_1(DataBase,support_min=min_support)
    L1,sup_data=ScanDataBase(DataBase,C1,support_min=min_support)
    L=[L1]
    k=2
    while(len(L[k-2])>0):
        Ck=apriori_gen(L[k-2],k)
        Lk,sup_c=ScanDataBase(DataBase,Ck,min_support)
        sup_data.update(sup_c)
        L.append(Lk)
        k+=1
    print(sup_data)
    print(L)

