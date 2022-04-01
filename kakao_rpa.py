import pyautogui
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

na_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\nana.png", confidence=0.5)
pyautogui.doubleClick(na_kaka)

time.sleep(3)

with open(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt", "r", encoding="utf8") as fp:
    def my_write(text):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')
    my_write(fp.read())
    
# time.sleep(3)

# trans = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\trans.png", confidence=0.7)
# pyautogui.click(trans)

time.sleep(3)

# family_kaka = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\family.png", confidence=0.5)
# pyautogui.doubleClick(family_kaka)

# time.sleep(3)

# with open(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\weather.txt", "r", encoding="utf8") as fp:
#     def my_write(text):
#         pyperclip.copy(text)
#         pyautogui.hotkey("ctrl", "v")
    #    pyautogui.sleep(2)
#        pyautogui.keyDown('esc')

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
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')

    my_write(fp.read())
    
time.sleep(3)

# trans = pyautogui.locateOnScreen(r"C:\Users\Kim Dae Sung\Desktop\PythonWorkspace\trans.png", confidence=0.7)
# pyautogui.click(trans)