from urllib import request,error
if __name__ == '__main__':
    url = 'https://weibo.com/1847093910/profile'
    headers = {'Cookie':"UOR=www.ci123.com,widget.weibo.com,stock.eastmoney.com; SINAGLOBAL=9443068097679.125.1522229184676; ULV=1532513081604:5:2:1:374923209495.84546.1532513081596:1531719038679; UM_distinctid=1626c086cd4ada-0ab6f93b6ba71f-495861-13c680-1626c086cd6ef6; SUHB=0M2EKzcfra_mNL; SCF=Av2FTn4Sd4CA5L5c2sAXw8fAxVuauIWi0BwRgHY27kdy15lamw382eI2_8eN12B1iSPp0wivyZQ-xj-DWIx5YDY.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWvulp67zhR-Skm4jmd6gyl5JpX5KzhUgL.Fo2RShM71Ke4eK52dJLoI0WTC.QLxKqL1-eLBKnLxK-LB-BL1K5LxK.L1KeLBK5LxK-L1K5L1h.LxK-L1K5L1h.t; ALF=1564146157; SUB=_2A252XbY-DeRhGedG71UR-S3FyjyIHXVVKqD2rDV8PUNbmtBeLVbMkW9NUVs-A42WnsIrl1kn5OEcP5P0vgMub3tW; _s_tentry=-; Apache=374923209495.84546.1532513081596; login_sid_t=cac10d856185e25e8710ef068a79ad07; cross_origin_proto=SSL; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; YF-V5-G0=a53c7b4a43414d07adb73f0238a7972e; wb_view_log=1440*9002; SSOLoginState=1532610158; wvr=6; YF-Page-G0=b9004652c3bb1711215bacc0d9b6f2b5; wb_view_log_1847093910=1440*9002"}

    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open('rspp.html','w') as f:
        f.write(html)