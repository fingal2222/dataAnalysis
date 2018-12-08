# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:27:19 2018

@author: zhaof
"""

#动态数据采集：拉勾网
import json
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
def lagou_dynamic_crawl():
    headers={"Cookie": "WEBTJ-ID=20181207101105-167866ec366ac2-0e1b51d88fdb5f-4313362-1327104-167866ec367344; _ga=GA1.2.2008298386.1544148665; _gid=GA1.2.221880220.1544148665 Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544148666; user_trace_token=20181207101107-5b5203e0-f9c5-11e8-8ce7-5254005c3644; LGUID=20181207101107-5b520b45-f9c5-11e8-8ce7-5254005c3644; X_HTTP_TOKEN=123420d9462b72f1a61c2aee4c55681b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167866edef1671-018024588c6814-4313362-1327104-167866edef24ca%22%2C%22%24device_id%22%3A%22167866edef1671-018024588c6814-4313362-1327104-167866edef24ca%22%7D; sajssdk_2015_cross_new_user=1; LGSID=20181207105430-6ade7fd1-f9cb-11e8-8ce7-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fservice%3Dhttps%253a%252f%252fwww.lagou.com%252f; ab_test_random_num=0; JSESSIONID=ABAAABAAAFCAAEG566B454EE4FC4A050C046BD484172B3F; sm_auth_id=ibnvcsg128e9g79r; _gat=1; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; LGRID=20181207105645-bb5c9c9b-f9cb-11e8-8ce7-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544151404; SEARCH_ID=d0371bada1fd498c9b9098b2d5da92c6",
             "Host": "www.lagou.com",
             "Origin": "https://www.lagou.com",
             "Referer": "https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
             "X-Anit-Forge-Code": "0",
             "X-Anit-Forge-Token": None,
             "X-Requested-With": "XMLHttpRequest"
             }
    #创建一个职位列表容器
    positions=[]
    url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    #30页循环遍历抓取
    for page in range(1,31):
        print("还在抓取第{}页...".format(page))
        #构建请求表单参数
        params={
                'first':'true',
                'pn':page,
                'kd':'机器学习'
                }
        #构造请求并返回结果
        resut=requests.post(url,headers=headers,params=params)
        #将请求结果转为json        
        json_result=resut.json()
        #解析json数据结构获取目标信息
        position_info=json_result['content']['positionResult']['result']
        #获取当前页第一个职位信息，再去抓职位详情页面
        for position in position_info:
            #把我们要拉取信息放入字典
            position_dict={
                    'position_name':position['positionName'],
                    'work_year':position['workYear'],
                    'education':position['education'],
                    'salary':position['salary'],
                    'city':position['city'],
                    'company_name':position['companyFullName'],
                    'address': position['businessZones'],
                    'label':position['companyLabelList'],
                    'stage':position['financeStage'],
                    'size':position['companySize'],
                    'advantage':position['positionAdvantage'],
                    'industry':position['industryField'],
                    'industrylabels':position['industryLables']                                                
                    }
            position_id=position['positionId']
            position_dict['position_detail']=result_detail(position_id)
            positions.append(position_dict)
            
        time.sleep(7)
    print("全部数据采集完毕")
    return positions 

def result_detail(position_id):
    url="https://www.lagou.com/jobs/%s.html" %position_id
    headers={"Cookie": "WEBTJ-ID=20181207101105-167866ec366ac2-0e1b51d88fdb5f-4313362-1327104-167866ec367344; _ga=GA1.2.2008298386.1544148665; _gid=GA1.2.221880220.1544148665 Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544148666; user_trace_token=20181207101107-5b5203e0-f9c5-11e8-8ce7-5254005c3644; LGUID=20181207101107-5b520b45-f9c5-11e8-8ce7-5254005c3644; X_HTTP_TOKEN=123420d9462b72f1a61c2aee4c55681b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167866edef1671-018024588c6814-4313362-1327104-167866edef24ca%22%2C%22%24device_id%22%3A%22167866edef1671-018024588c6814-4313362-1327104-167866edef24ca%22%7D; sajssdk_2015_cross_new_user=1; LGSID=20181207105430-6ade7fd1-f9cb-11e8-8ce7-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fservice%3Dhttps%253a%252f%252fwww.lagou.com%252f; ab_test_random_num=0; JSESSIONID=ABAAABAAAFCAAEG566B454EE4FC4A050C046BD484172B3F; sm_auth_id=ibnvcsg128e9g79r; _gat=1; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; LGRID=20181207105645-bb5c9c9b-f9cb-11e8-8ce7-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544151404; SEARCH_ID=d0371bada1fd498c9b9098b2d5da92c6",
             "Host": "www.lagou.com",
             "Origin": "https://www.lagou.com",
             "Referer": "https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
             "X-Anit-Forge-Code": "0",
             "X-Anit-Forge-Token": None,
             "X-Requested-With": "XMLHttpRequest"
             }
    result=requests.get(url,headers=headers)
    time.sleep(10)
    #解析职位要求text
    soup=BeautifulSoup(result.text,'html.parser')
    job_jd=soup.find(class_="job_bt")
    #通过尝试发现部分记录描述存在空的情况，所以这里需要判断处理一下
    if job_jd!=None:
        job_jd=job_jd.text
    else:
        job_jd="null"
    return job_jd

if __name__=='__main__':
    positions=lagou_dynamic_crawl();
    df=pd.DataFrame(positions)
    df.head()
    df.to_csv("machine_learning.csv")