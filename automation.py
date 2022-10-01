#!/usr/bin/python3
# -*- coding: utf-8 -*-



"""
Automation
~~~~~~~~~~
常用函数
"""

def replace(s,bf,af)->str:
    """
    替换字符:\n
    s string str 待替换的字符串;\n
    bf before str 需要替换的字符;\n
    af after str 新的字符;
    """
    return af.join(s.split(bf))

def count_time(fun):
    """
    统计时间:\n
    统计一个函数执行所需时间;\n
    使用方法:\n
    ```
    @automation.count_time
    def xxx():
    ```
    """
    from time import perf_counter
    
    start_time=perf_counter()

    def improved_func(*args,**kwargs):
        ret=fun(*args,**kwargs)
        return ret

    end_time=perf_counter()
    print(f"{end_time-start_time:1f}")

    return improved_func

def download_image(urls: list, headers: dict, path: str) -> int:
    """
    保存网络上的图片
    - urls
    图片地址列表
    - headers
    请求头
    - path
    保存路径(本地)
    """
    i = 0
    for url in urls:
        file_type = url.split(".")[-1]  # 解析文件类型
        r = requests.get(url, headers)  # 获取
        if r.status_code != 200:
            print(f"状态码:{r.status_code}")
        with open(f"{path}/{i}.{file_type}", "wb+") as f1:
            f1.write(r.content)
        i += 1
    print(f"下载完毕(共{0}张)", i)
    return 0




