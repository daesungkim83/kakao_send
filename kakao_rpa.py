import pyautogui
import time
import datetime
import sys
import pyperclip
from bs4 import BeautifulSoup
import requests

# def create_soup(url):
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     return soup


# def scrape_weather():
#     print("[오늘의 날씨]")
#     url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8"
#     soup = create_soup(url)
#     cast = soup.find("p", attrs={"class":"summary"}).get_text()
#     curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
#     min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().strip()
#     max_temp = soup.find("span", attrs={"class":"highest"}).get_text().strip()import pyautogui
import time
import datetime
import sys
import pyperclip
from bs4 import BeautifulSoup
import requests
import re

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().strip()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text().strip()
    rain_rate = soup.find("div", attrs={"class":"cell_weather"})
    morning = rain_rate.find_all("span", attrs={"class":"rainfall"})[0].get_text().strip()
    afternoon = rain_rate.find_all("span", attrs={"class":"rainfall"})[1].get_text().strip()
    sunset = soup.find("li", attrs={"class":"item_today type_sun"}).get_text().strip()
    etc = soup.find("dl", attrs={"class":"summary_list"})
    humidity = etc.find_all("dd", attrs={"class":"desc"})[1].get_text().strip()
    wind1 = etc.find_all("dt", attrs={"class":"term"})[2].get_text().strip()
    wind2 = etc.find_all("dd", attrs={"class":"desc"})[2].get_text().strip()





    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print(cast)    
    print("오전 강수확률 {} / 오후 강수확률 {}".format(morning, afternoon))
    print("습도 {}  /  {} {}".format(humidity, wind1, wind2))
    print(sunset)
    print()
        

def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어지문)")
    for sentence in sentences[len(sentences)//2:]: #8문장이 있다고 가정할때, index 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()
    print("(한글지문)")
    for sentence in sentences[:len(sentences)//2:]: #8문장이 있다고 가정할때, index 기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print()



    
temp = sys.stdout

sys.stdout = open(r'C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt','w',encoding="utf8")
scrape_weather() # 오늘의 날씨 정보 가져오기
scrape_english()

sys.stdout.close()

time.sleep(3)

sys.stdout = temp   


w = pyautogui.getWindowsWithTitle("카카오톡")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

pyautogui.sleep(3)

# na_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\nana.png", confidence=0.9, region=(1241, 103, 1644-1241, 160-103))
na_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\nana.png", confidence=0.5)
pyautogui.doubleClick(na_kaka)
# # pyautogui.moveTo(na_kaka)


time.sleep(3)

with open(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt", "r", encoding="utf8") as fp:
    def my_write(text):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    my_write(fp.read())
    
time.sleep(3)

trans = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\trans.png", confidence=0.7)
pyautogui.click(trans)

time.sleep(3)

# family_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\family.png", confidence=0.5)
# pyautogui.doubleClick(family_kaka)

# time.sleep(3)

# with open(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt", "r", encoding="utf8") as fp:
#     def my_write(text):
#         pyperclip.copy(text)
#         pyautogui.hotkey("ctrl", "v")

#     my_write(fp.read())
    
# time.sleep(3)

# trans = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\trans.png", confidence=0.7)
# pyautogui.click(trans)

friend_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\friend.png", confidence=0.5)
pyautogui.doubleClick(friend_kaka)

time.sleep(3)

with open(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt", "r", encoding="utf8") as fp:
    def my_write(text):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    my_write(fp.read())
    
time.sleep(3)

trans = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\trans.png", confidence=0.7)
pyautogui.click(trans)

# stock_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\stock.png", confidence=0.5)
# pyautogui.doubleClick(stock_kaka)

# time.sleep(2)

# with open(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt", "r", encoding="utf8") as fp:
#     def my_write(text):
#         pyperclip.copy(text)
#         pyautogui.hotkey("ctrl", "v")

#     my_write(fp.read())
    
# time.sleep(2)

# trans = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\trans.png", confidence=0.7)
# pyautogui.click(trans)
#     rain_rate = soup.find("div", attrs={"class":"cell_weather"})
#     morning = rain_rate.find_all("span", attrs={"class":"rainfall"})[0].get_text().strip()
#     afternoon = rain_rate.find_all("span", attrs={"class":"rainfall"})[1].get_text().strip()
#     sunset = soup.find("li", attrs={"class":"item_today type_sun"}).get_text().strip()
#     etc = soup.find("dl", attrs={"class":"summary_list"})
#     humidity = etc.find_all("dd", attrs={"class":"desc"})[1].get_text().strip()
#     wind1 = etc.find_all("dt", attrs={"class":"term"})[2].get_text().strip()
#     wind2 = etc.find_all("dd", attrs={"class":"desc"})[2].get_text().strip()





#     print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
#     print(cast)    
#     print("오전 강수확률 {} / 오후 강수확률 {}".format(morning, afternoon))
#     print("습도 {}  /  {} {}".format(humidity, wind1, wind2))
#     print(sunset)
# #     print()




# sys.stdout = open('weather.txt','w',encoding="utf8")
# scrape_weather() # 오늘의 날씨 정보 가져오기

# sys.stdout.close()

# time.sleep(2)

# pyautogui.moveTo(1206, 93) 
# time.sleep(2)
# pyautogui.moveTo(1591, 172) 

# pyautogui.mouseInfo()



w = pyautogui.getWindowsWithTitle("카카오톡")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

# if w.isMaximized == False: # 현재 최대화가 되지 않았다면
#     w.maximize() # 최대화

pyautogui.sleep(5)



# na_kaka = pyautogui.locateOnScreen("nana.png")
na_kaka = pyautogui.locateOnScreen("nana.png", confidence=0.5)
# na_kaka = pyautogui.locateOnScreen("nana.png", confidence=0.5, region=(1183, 101, 1518-1183, 171-101))
# na_kaka = pyautogui.locateOnScreen("nana.png", region=(1206, 93, -217, -79))
# print(na_kaka)
pyautogui.doubleClick(na_kaka)
# pyautogui.moveTo(na_kaka)



#643,301 30,30,30 #1E1E1E

time.sleep(5)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881 - 1349,148))

with open("weather.txt", "r", encoding="utf8") as fp:
    def my_write(text):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    my_write(fp.read())
    
time.sleep(2)

# trans = pyautogui.locateOnScreen("trans.png", confidence=0.7)
# pyautogui.click(trans)



#pyautogui.doubleClick()



# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881 - 1488, 137))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
#file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
#pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
# import time
# import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

# def find_target(img_file, timeout=30):
#     start = time.time()
#     target = None
#     while target is None:
#         target = pyautogui.locateOnScreen(img_file)
#         end = time.time()
#         if end - start > timeout:
#             break
#     return target

# def my_click(img_file, timeout=30):
#     target = find_target(img_file, timeout)
#     if target:
#         pyautogui.click(target)
#     else:
#         print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
#         sys.exit()

# #pyautogui.click(file_menu_notepad)

# my_click("file_menu_notepad.png", 10)
# print
