#--list-extractors                List all supported extractors 列出支持的
#--hls-prefer-ffmpeg 使用ffmpeg下载
#--user-agent xx;--add-header
import os
import subprocess
import multiprocessing
import sys
import time


def download(url):
    try:
        while True:
            print("正在下载"+url+"上面的视频")
            os.system("youtube-dl" + " " + url + " " + "--config-location ./config.txt ")
            #print(url+"执行完了")
            # 十分钟后再次执行
            time.sleep(600);
        return True
    except KeyboardInterrupt:
        sys.exit(1)



if __name__ == '__main__':
    baseurl="https://zh.chaturbate.com/"
    names=["annabellasweet98","kishorny_99","aimilu","diamond_jackson","chinesesweety"]
    fullurls=map(lambda x:baseurl+x, names)
    #开启尽量多的核心
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    
    #同步调用
    # for name in names:
    #     url="https://zh.chaturbate.com/"+name
    #     download(url)
    #多进程
    # for name in names:
    #     url="https://zh.chaturbate.com/"+name
    #
    #     pool.apply_async(download,args=(url,))

    for fullurl in fullurls:
        pool.apply_async(download,args=(fullurl,))

    pool.close()
    pool.join()   #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
