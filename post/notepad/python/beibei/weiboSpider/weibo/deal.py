'''
Author: Firefly
Date: 2020-10-09 23:08:26
Descripttion: 
LastEditTime: 2020-10-10 00:10:07
'''

import json


with open('allarticle.txt',encoding='GBK') as f:
    deal_file = f.read()
    deal_file = deal_file.replace('[仅好友圈可见]','').replace('\xa0','').replace('\u2022','').replace('\U0001f47f','')
    deal_file = deal_file.replace('\U0001f3b6','').replace('\U0001f680','').replace('\U0001f968','').replace('\U0001f942','')
    deal_file = deal_file.replace('原图','')
    list_info =  deal_file.split('\n\n')
    # print(deal_file[0:300])
    print(len(list_info))

    dict_info = {}
    for k,v in enumerate(list_info):
        # print(k,v)
        one_info_list = v.split('\n')
        one_info_dict = {}
        one_info_dict["text"] = one_info_list[0]
        one_info_dict["post_time"] = one_info_list[2]
        one_info_dict["good_nums"] = one_info_list[3]
        one_info_dict["resend_nums"] = one_info_list[4]
        one_info_dict["comments"] = one_info_list[5]
        one_info_dict["send_tool"] = one_info_list[6]

        dict_info[k] = one_info_dict

    dealed_info = json.dumps(dict_info,indent=2,ensure_ascii=False)

    with open('dealed.json', mode='a') as wf:
        wf.write(dealed_info)