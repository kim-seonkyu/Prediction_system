from django.shortcuts import render
import joblib

import pandas as pd

from bs4 import BeautifulSoup
from selenium.webdriver.common.alert import Alert
from selenium import webdriver  # 라이브러리(모듈) 가져오라
import chromedriver_autoinstaller
import re
from selenium.webdriver.common.keys import Keys

import urllib
from urllib.request import urlopen

from dateutil.relativedelta import relativedelta
import time

import json

# Create your views here.

def get_dis(x) :
    if 'CJ' in x or 'CGV' in x or '씨제이' in x :
        return 'CJ'
    elif '쇼박스' in x :
        return '쇼박스'
    elif 'SK' in x or '에스케이' in x:
        return 'SK'
    elif '리틀빅픽' in x :
        return '리틀빅픽처스'
    elif '스폰지' in x :
        return '스폰지'
    elif '싸이더스' in x :
        return '싸이더스'
    elif '에이원' in x :
        return '에이원'
    elif '마인스' in x :
        return '마인스'
    elif '마운틴픽' in x :
        return '마운틴픽처스'
    elif '디씨드' in x :
        return '디씨드'
    elif '드림팩트' in x :
        return '드림팩트'
    elif '메가박스' in x :
        return '메가박스'
    elif '마운틴' in x :
        return '마운틴'
    elif '롯데' in x :
        return '롯데'
    elif 'KBS' in x :
        return 'KBS'
    elif '제이앤씨미디어그룹' in x :
        return '제이앤씨미디어그룹'
    elif '월트디즈니' in x :
        return '월트디즈니'
    elif '그린나래' in x :
        return '그린나래'
    elif 'KTG상상마당' in x or 'KT'in x :
        return 'KTG상상마당'
    elif 'TJOY' in x or 'T-JOY' in x:
        return 'TJOY'
    elif '디오시네마' in x :
        return '디오시네마'
    elif '스톰픽쳐스' in x :
        return '스톰픽쳐스'
    elif '디스테이션' in x :
        return '디스테이션'
    elif '더블앤조이' in x :
        return '디스테이션'
    elif 'CBS' in x :
        return 'CBS'
    elif 'CBS' in x :
        return 'CBS'
    elif '더쿱' in x :
        return '더쿱'
    elif '더콘텐츠온' in x :
        return '더콘텐츠온'
    elif '소니픽쳐스' in x :
        return '소니픽쳐스'
    elif '이수' in x :
        return '이수'
    elif '워너' in x :
        return '워너브라더스'
    elif '삼백' in x :
        return '삼백상회'
    elif '폭스' in x :
        return '폭스코리아'
    elif '엣나인' in x :
        return '엣나인필름'
    elif '티캐스트' in x :
        return '티캐스트'
    elif '콘텐츠판다' in x :
        return '콘텐츠판다'
    elif '판씨네마' in x :
        return '판씨네마'
    elif '키다리' in x :
        return '키다리이엔티'
    elif '스마일이' in x :
        return '스마일이엔티'
    elif '팝엔' in x :
        return '팝엔터테인먼트' 
    elif '오퍼스' in x :
        return '오퍼스픽쳐스' 
    elif '와이드' in x :
        return '와이드릴리즈' 
    elif '오드' in x :
        return '오드' 
    elif '조이앤' in x :
        return '조이앤시네마' 
    elif '박수' in x :
        return '박수엔터테인먼트' 
    elif '찬란' in x :
        return '찬란'
    elif '얼리' in x :
        return '얼리버드'
    elif '영화사빅' in x :
        return '영화사빅'
    elif '에이스' in x :
        return '에이스메이커'
    elif '퍼스트런' in x :
        return '퍼스트런'
    elif 'MM' in x or 'M&M' in x:
        return 'MM인터내셔널'
    elif '드림웨스트' in x :
        return '드림웨스트픽쳐스'
    elif '홀리가든' in x :
        return '홀리가든'
    elif 'R&R' in x :
        return 'RR프로덕션'
    elif '머스트' in x :
        return '머스트씨무비'
    elif '블룸즈' in x :
        return '블룸즈베리'
    elif '모쿠' in x :
        return '모쿠슈라'
    elif '니버설' in x :
        return '유니버설픽쳐스'
    elif '시네마달' in x :
        return '시네마달'
    elif '(주)넥스트엔터테인먼트월드(NEW)' in x:
        return '넥스트엔터테이먼트월드'
    else :
        return x


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, 19431049)")
    time.sleep(1)

def naver_expectation(title):
    
    chrome_path = chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('windows-size=1920x1080')
    driver = webdriver.Chrome(chrome_path, options=options)
    
    driver.get('https://movie.naver.com/')
    time.sleep(1)

    name = driver.find_element_by_css_selector('.ipt_tx_srch')
    name.clear()
    time.sleep(0.5)
    name.send_keys(title)
    time.sleep(1)

    # 영화 클릭 
    movie = driver.find_element_by_css_selector('.thumb_spec')
    movie.click()
    time.sleep(2)

    # 기대지수 
    movie_score = driver.find_element_by_css_selector('.exp_cnt').get_attribute('textContent')
    time.sleep(1)

    extract = re.compile('[0-9]*,*[0-9]+')
    str_num = extract.findall(movie_score)
    str_num = str_num[0]
    if ',' in str_num:
        str_num = str_num.split(',')
        str_num = int(str_num[0] + str_num[1])
        num = int(str_num)
    else:
        num = int(str_num)
    
    driver.close()
    
    return num

def naver_starbuzz(title, actor, date):
    actor = actor.split(',')
    actor = actor[:5]

    act_cnt = []
    star_buzz = []

    end_date = date - relativedelta(days=1) 
    end_date = end_date.strftime('%Y%m%d') 

    start_date = date - relativedelta(months=1) 
    start_date = start_date.strftime('%Y%m%d') 


    for a in actor:
        query_txt = (title + a).strip()

        chrome_path = chromedriver_autoinstaller.install()
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('windows-size=1920x1080')
        driver = webdriver.Chrome(chrome_path, options=options)
        # 사이트 주소는 네이버
        url = f'https://search.naver.com/search.naver?where=blog&query={query_txt}&sm=tab_opt&nso=so:r,p:from{start_date}to{end_date}'
        driver.get(url)
        time.sleep(2) 

        articles = ".api_txt_lines.total_tit"
        article_raw = driver.find_elements_by_css_selector(articles)

        if not article_raw:
            act_cnt.append(0)
        else:
            n = 20  # 스크롤 1번 당 30개씩
            i = 0
            while i < n: # 이 조건이 만족되는 동안 반복 실행
                scroll_down(driver) # 스크롤 다운
                i = i+1

            articles = ".api_txt_lines.total_tit"
            article_raw2 = driver.find_elements_by_css_selector(articles)

            act_cnt.append(len(article_raw2))

    star_buzz.append(sum(act_cnt))
    
    driver.close()
    
    return star_buzz

def search_title(title):
    client_id = 'Lk7LFAa6MYxfjen14u8y'
    client_secret = 'IvkNjQZHUR'
    encText = urllib.parse.quote(title)
    url = 'https://openapi.naver.com/v1/search/movie.json?display=100&query=' + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        d = json.loads(response_body.decode('utf-8'))
        if (len(d['items']) > 0):
            return d['items']
        else:
            return None

    else:
        print("Error Code:" + rescode)

def naver_moviecode(title, director):
    m = search_title(title)
    for n in (range(len(m))):
        if m[n]['director'][:-1] == director:
            link = m[n]['link']
            spl = str(link).split("=")
            it = spl[1]
    return it

def naver_moviebuzz(code):
    date_list = []
    title_list2 = []
    url = f'https://movie.naver.com/movie/bi/mi/review.naver?code={code}'
    html =urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    w = str(soup.select('div>div>div>div>div>div>div>span>em'))
    try:
        reg = re.compile('\d')
        per_result = reg.findall(w)
        y = ''.join(per_result)
        z = int(y)//10 +2

        date_2 = []
        for page in range(1,z):
            url2 = f'https://movie.naver.com/movie/bi/mi/review.naver?code={code}&page={page}'
            html2 =urlopen(url2)
            soup = BeautifulSoup(html2,'html.parser')
            date_num = soup.select('li>span>em')
            date_2.extend(date_num)
            time.sleep(2)
        y = str(date_2).split(',')
        reg = re.compile('[^a-zA-Z가-힣\>]\d*\.\d*\.\d*')
        e = ''.join(y)
        per_result = reg.findall(e)
        datetime_result = pd.to_datetime(per_result)
        date_list.append(datetime_result)

    except:
        url = f'https://movie.naver.com/movie/bi/mi/review.naver?code={code}'
        html =urlopen(url)
        soup = BeautifulSoup(html,'html.parser')
        tit = soup.select('title')
        a = str(tit).split(":")
        b =a[0].replace('[','').replace('<','').replace('title','').replace('>','').replace(' ','')
        title_list2.append(b)

    return date_list

def naver_movienum(date_list, dates):
    a = []
    data = []
    end_date = dates - relativedelta(days=1) 
    for i in date_list[0]:
        if i < end_date:
            a.append(i)
            num = a.count(True)
            data.append(num)
    return len(data)
    

def google_trend(title, date):
    end_date = date - relativedelta(days=1) 
    end_date = end_date.strftime('%Y.%m.%d') 

    start_date = date - relativedelta(months=1) 
    start_date = start_date.strftime('%Y.%m.%d')
    

    chrome_path = chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('windows-size=1920x1080')
    driver = webdriver.Chrome(chrome_path, options=options)
    driver.get('https://trends.google.com/trends/?geo=KR')
    time.sleep(2)
    
    search_input = driver.find_element_by_xpath('//*[@id="input-1"]')
    search_input.clear()
    search_input.send_keys(title)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)
    
    # 12개월 옵션 클릭
    month_click = driver.find_element_by_css_selector('._md-text')
    month_click.click()
    time.sleep(1)
    
    # 맞춤기간 클릭 
    select_click = driver.find_elements_by_css_selector('.custom-date-picker-select-option.md-ink-ripple ._md-text')[-1]
    select_click.click()
    time.sleep(1)
    
    # 시작 기간 설정
    start_day = driver.find_element_by_css_selector('.custom-date-picker-dialog-range-from .md-datepicker-input')
    start_day.clear()
    start_day.send_keys(start_date)
    time.sleep(1)
    
    # 종료 기간 설정
    end_day = driver.find_element_by_css_selector('.custom-date-picker-dialog-range-to .md-datepicker-input')
    end_day.clear()
    end_day.send_keys(end_date)
    time.sleep(1)
    
    # 기간 설정 확인 클릭
    enter_btn = driver.find_elements_by_css_selector('.custom-date-picker-dialog-actions.layout-row .custom-date-picker-dialog-button.md-button.md-ink-ripple')[-1]
    enter_btn.click()
    time.sleep(2)
    
    # 총 숫자 횟수 
    lennum = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/ng-include/div/ng-include/div/line-chart-directive/div[1]/div/div[1]/div/div/table/tbody/tr')
    lennum = len(lennum)
    time.sleep(1)
    
    # 그래프에 있는 숫자(조회수? 클릭수?) 가져오기 
    gnum_list = []
    for i in range(1,lennum+1):
        gnum = driver.find_element_by_xpath(f'/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/ng-include/div/ng-include/div/line-chart-directive/div[1]/div/div[1]/div/div/table/tbody/tr[{i}]/td[2]').get_attribute('textContent')
        gnum_list.append(gnum)
    time.sleep(1)    
    gnum_df = pd.DataFrame(gnum_list, columns=[title])
    gnum_df = pd.to_numeric(gnum_df[title])
    time.sleep(1)
    df_num = gnum_df.sum()
    time.sleep(1)
    
    driver.close()
    
    return df_num

def naver_image(title):
    chrome_path = chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('windows-size=1920x1080')
    driver = webdriver.Chrome(chrome_path, options=options)
    
    driver.get('https://movie.naver.com/')
    time.sleep(2)
    
    name = driver.find_element_by_css_selector('.ipt_tx_srch')
    name.clear()
    name.send_keys(title)
    time.sleep(1)
    
    movie = driver.find_element_by_css_selector('.thumb_spec')
    movie.click()
    time.sleep(2)
    
    imgUrl = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/a/img').get_attribute('src')
    time.sleep(0.5)
    filename = 'movie/static/img/{0}.jpg'.format(title)
    time.sleep(0.5)
    urllib.request.urlretrieve(imgUrl, filename)



def index(request):
    return render(request, 'movie/index.html')

def ver1(request):
    
    model = joblib.load('model.pkl')
    
    director_list = pd.read_csv('director.csv', encoding='utf-8', index_col=0)
    distributor_list = pd.read_csv('distributor.csv', encoding='utf-8', index_col=0)
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        title = request.POST.get('movie_title', '')
        date = request.POST.get('movie_date', '')
        director = request.POST.get('movie_director', '')
        actor = request.POST.get('movie_actor', '')
        genre = request.POST.get('movie_genre', '')
        distributor = request.POST.get('movie_distributor', '')
        budget = request.POST.get('movie_budget', '')

        movie_df = pd.DataFrame({'user': name, 'title': title, 'date': date, 'director': director, 'actor': actor, 
                                 'genre': genre, 'distributor': distributor, 'budget': budget}, index=[0])

        # 배급사 전처리
        movie_df['distributor'] = movie_df['distributor'].apply(lambda x: get_dis(x))
        
        def func(distributor):
            if distributor in distributor_list:
                return distributor
            else:
                return '기타'

        movie_df['distributor'] = movie_df['distributor'].apply(lambda x: func(x))
        
        for movie_df['distributor'] in distributor_list['배급사']:
            movie_df['distributor_rank'] = distributor_list['dist_rank']
        
        
        # 감독 전처리
        def cont_func(director):
            if director in director_list:
                return director
            else:
                return '기타'
            
        movie_df['director'] = movie_df['director'].apply(lambda x : cont_func(x))    
        
        for movie_df['director'] in director_list['directors']:
            movie_df['director_rank'] = director_list['direct_rank']
        
        
        # 장르 전처리
        movie_df['genre_rank'] = movie_df.genre.map({'뮤지컬' : 16,'다큐멘터리' : 15, '가족' : 14, '드라마' : 13, 'SF' : 12, '공포(호러)' : 11, '멜로/로맨스' : 10, '미스터리' : 9, '코미디':8,'스릴러':7,'판타지':6,'액션':5,'전쟁':4,'범죄':3,'사극':2,'어드벤처':1})       
        
        # 날짜 전처리
        dates = pd.to_datetime(movie_df['date'])
        dates = dates[0]
        
        naver_image(title)
        time.sleep(1)
        
        naver_expectation_num = naver_expectation(title)
        movie_df['naver_기대지수'] = naver_expectation_num
        time.sleep(1)
        
        star_buzz = naver_starbuzz(title, actor, dates)
        movie_df['naver_starbuzz'] = star_buzz
        time.sleep(1)
        
        naver_code = naver_moviecode(title, director)
        date_list = naver_moviebuzz(naver_code)
        movie_buzz = naver_movienum(date_list, dates)
        movie_df['naver_moviebuzz'] = movie_buzz
        time.sleep(1)
        
        googletrend = google_trend(title, dates)
        movie_df['google_trend'] = googletrend
        time.sleep(1)
        
        starbuzz = movie_df['naver_starbuzz'][0]
        naverexpect = movie_df['naver_기대지수'][0]
        gtrend = movie_df['google_trend'][0]
        moviebuzz = movie_df['naver_moviebuzz'][0]
        income = int(budget) * 3
        time.sleep(1)
        
        movie_df.drop(['user', 'date', 'distributor', 'director', 'genre', 'title', 'actor', 'budget'],
                      axis=1, inplace=True)
        
        time.sleep(1)
        # sc = StandardScaler()
        # sc.fit(movie_df)
        # movie_df_std = sc.transform(movie_df)
        
        # result = model.predict(movie_df_std)
        
        result = model.predict(movie_df)
        
        if result == 1:
            result = '손익분기점이 넘을 것으로 예상됩니다'
        else:
            result = '손익분기점이 안 넘을 것으로 예상됩니다'
        
        
        return render(request, 'movie/ver1_result.html',
                      {'name': name, 'title': title, 'director': director, 'date': date,
                       'actor': actor, 'genre': genre, 'distributor': distributor, 'result': result,
                       'budget': budget, 'income': income, 'starbuzz': starbuzz, 'naverexpect': naverexpect, 'gtrend': gtrend, 'moviebuzz': moviebuzz})
    else:
        return render(request, 'movie/ver1.html')