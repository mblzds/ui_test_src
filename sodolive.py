def restartPlay(platform="ios"):
    if platform == "ios":
        d(label="icon tabbar assist normal").click()
        time.sleep(3)
        d(label="开启直播", name="GLstartLiveBtn").click()
        time.sleep(10)
        d(label="GLExitLiveModule").click()
        time.sleep(1)
        d.click(0.67, 0.57)
        time.sleep(1)
        d(label="返回首页", name="backButton").click()
        time.sleep(1)
    if platform == "android":
        d(resourceId="com.sodo.live:id/start_live_button").click()
        time.sleep(3)
        d(resourceId="com.sodo.live:id/start_live_btn").click()
        time.sleep(10)
        d(resourceId="com.sodo.live:id/close_btn").click()
        time.sleep(1)
        d(resourceId="com.sodo.live:id/tv_confirm").click()
        time.sleep(1)
        d(resourceId="com.sodo.live:id/close_btn").click()
        time.sleep(1)        


def repalyWatch(i):
    if i % 2 == 0:
        d.click(0.296, 0.265)
    else:
        d.click(0.744, 0.46)
    time.sleep(8)
    d(label="GLExitLiveModule").click()
    time.sleep(1)
   
def up_loop_down():
    d.swipe(0.495, 0.747,0.497, 0.119)
    time.sleep(1)
    d.swipe(0.497, 0.119,0.495, 0.747)
    time.sleep(1)
    
for i in range(100):
    print(i)
    up_loop_down()
