import re,execjs
import requests
from lxml import etree
import json
headers = {

                'User-Agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',
}


if __name__=="__main__":
    url=r'https://paper.seebug.org/category/threat-intelligence/?page={}'.format(str(1))
    my_session = requests.session()
    my_session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                            "like Gecko) Chrome/75.0.3770.100 Safari/537.36"})

    # 第一步由__jsluid_s获取__jsl_clearance_s=, 通过第一步请求返回的js(称js1)计算而来
    r = my_session.get(url).text.replace("<script>document.cookie=", "").replace(";location.href=location.pathname+location.search</script>", "")
    default = execjs.get()
    res = default.eval(r)
    my_session.headers.update({"Cookie": "__jsluid_s" + "=" + my_session.cookies.get("__jsluid_s") + ";" + res})
    r = my_session.get(url)
    print(r.text)
    go_para = json.loads(r.text.split("}};go(")[1].replace(")</script>", ""))

    #主要为了获取js代码
    print(go_para)



