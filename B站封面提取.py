#!/usr/bin/python3
# -*- coding: utf-8 -*-

import automation
from re import findall
import asyncio
from bilibili_api import video
from gooey import Gooey, GooeyParser


"""
感谢passkon
"""

# 正则表达式<img data-v-3421314f="" src="//[a-zA-z]+[^\s]*"

headers = {"User-Agent":'Mozilla/5.0'}


#@automation.count_time
def download(urls, headers, path):
    automation.imgsave(urls, headers, path)


#@automation.count_time
async def bamain(bv):
    # 实例化 Video 类
    v = video.Video(bvid=bv)
    # 获取信息
    info = await v.get_info()
    # 打印信息
    return info


@Gooey
def main():
    parser = GooeyParser(description="Bilibili videoImg save - v0.0 (test)")
    parser.add_argument('BVid', widget="TextField")
    parser.add_argument('path', widget="DirChooser")  # 目录选择框
    args = parser.parse_args()
    bvid = args.BVid
    path = args.path
    print(bvid,path)
    infodict = asyncio.get_event_loop().run_until_complete(bamain(bvid))
    download([infodict['pic']], headers, path)                   


if __name__ == '__main__':
    main()
