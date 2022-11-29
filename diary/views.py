from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from diary.forms import MemoryForm, ImgForm
from .models import Memory
from diary.forms import MemoryForm, KeywordForm
from diary.models import KeywordPost, Memory, ImageFields, FinImg

#데이터 연동
import pymysql

# 자연어 처리
from hanspell import spell_checker  #git clone으로 로컬설치
from googletrans import Translator
from konlpy.tag import Okt
# from PyKomoran import *
# import pyokt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np
import matplotlib.pyplot as plt
import itertools
import pandas as pd
import time
import random

#이미지 변환
import openai
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
def memory_writing(request):
    return render(request, "diary/memory_writing.html")

# class MemoryList(ListView):
#     model = Memory
#     ordering = '-pk'

def index(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    memory_qs = Memory.objects.all()
    keyword_qs = ImageFields.objects.all()
    print(keyword_qs)


    return render(request, "diary/memory_list.html", {
        "memory_list": memory_qs,
        "keywords_list": keyword_qs,
    })


def memory_detail(request, pk):
    memory = Memory.objects.get(pk=pk)

    
    return render(request, "diary/memory_detail.html", {
        "memory": memory,
    })

import logging
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def memory_new(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        logger.info(request.POST)
        logger.info(form.is_valid)

        if form.is_valid():
            # form.cleaned_data
            form.save()
            conn = pymysql.connect(host='localhost', user='admin', password='admin', db='project_test2')
            start = time.time()

            try:
                with conn.cursor() as curs:
                    emotions = {
                        '쾌활': 'Cheerful',
                        '기쁨': 'Happy',
                        '보통': 'Neutral',
                        '우울': 'Depressed',
                        '화남': 'Angry'
                       }
                    drawings ={
                        '디지털 아트': 'Digital Art',
                       '유화': 'Oil and Canvas',
                       '스케치': 'Sketched',
                       '인상주의': 'Impressionism',
                       'MZ세대 스타일':'VaperWave',
                    }
                    sql = "SELECT * FROM diary_memory ORDER BY created_at DESC"
                    curs.execute(sql) # 실행할 쿼리분 넣기
                    rs = curs.fetchall() #sql문 실행해서 데이터 가져오기
                    # print(rs)  # 쿼리문 출력해보기
                    main_cont = rs[0][1]
                    drawing = drawings[rs[0][4]]
                    emotion = emotions[rs[0][5]]

            finally:
                conn.close()

            

                main_cont_300 = main_cont[:301]
                spelled_cont = spell_checker.check(u'{}'.format(main_cont_300)).as_dict()['checked']
                print(spelled_cont)
                print('='*10)
                # 2) 키워드 추출
                okt = Okt()

                tokenized_doc = okt.pos(spelled_cont)
                # print(tokenized_doc)

                # print('m')
                # print([word for word in tokenized_doc])

                # print([word[0] for word in tokenized_doc if word[1] == 'Noun'])
                # print('m')
                tokenized_nouns = ' '.join([word[0] for word in tokenized_doc if word[1] == 'Noun'])

                # print('품사 태깅 10개만 출력 :',tokenized_doc[:10])
                # print('명사 추출 :',tokenized_nouns)


                # 단어 합치기
                n_gram_range = (2, 3)

                count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
                candidates = count.get_feature_names_out()

                # print('trigram 개수 :',len(candidates))
                # print('trigram 다섯개만 출력 :',candidates[:4])


                # 유사 키워드 추출
                model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
                doc_embedding = model.encode([main_cont])
                candidate_embeddings = model.encode(candidates)

                top_n = 4
                distances = cosine_similarity(doc_embedding, candidate_embeddings)
                keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
                print(keywords)


                # 후보 간 유사성 최소화
                def max_sum_sim(doc_embedding, candidate_embeddings, words, top_n, nr_candidates):
                    # 문서와 각 키워드들 간의 유사도
                    distances = cosine_similarity(doc_embedding, candidate_embeddings)

                    # 각 키워드들 간의 유사도
                    distances_candidates = cosine_similarity(candidate_embeddings,
                                                            candidate_embeddings)

                    # 코사인 유사도에 기반하여 키워드들 중 상위 top_n개의 단어를 pick.
                    words_idx = list(distances.argsort()[0][-nr_candidates:])
                    words_vals = [candidates[index] for index in words_idx]
                    distances_candidates = distances_candidates[np.ix_(words_idx, words_idx)]

                    # 각 키워드들 중에서 가장 덜 유사한 키워드들간의 조합을 계산
                    min_sim = np.inf
                    candidate = None
                    for combination in itertools.combinations(range(len(words_idx)), top_n):
                        sim = sum([distances_candidates[i][j] for i in combination for j in combination if i != j])
                        if sim < min_sim:
                            candidate = combination
                            min_sim = sim

                    return [words_vals[idx] for idx in candidate]


                fin_keyword = max_sum_sim(doc_embedding, candidate_embeddings, candidates, top_n=top_n, nr_candidates=30)
                kor_keywords = ', '.join([word for word in fin_keyword])


                # print(fin_keyword)
                # print('키워드 추출 : ', end)

                #번역 및 입력
                translator = Translator()
                eng_keywords = ', '.join([translator.translate(word, dest='en').text for word in fin_keyword])
                # print(eng_keywords)
                # print('번역 : ', start-time.time())

                search_keyword = eng_keywords + ', ' + emotion + ', ' + drawing
                print()
                print('='*10)
                print(f'마지막 키워드 : {kor_keywords}')
                print(f'마지막 키워드 : {search_keyword}')
                print('='*10)
                print()
                end = (time.time() - start)
                print(end)

                save_db = ImageFields(keywords=kor_keywords)
                save_db.save()



                


            
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            openai.api_key = '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'

            #함수
            response = openai.Image.create(
                # 입력받은 키워드 입력
                prompt = search_keyword,
                
                # 출력할 그림 개수
                n = 4,

                # 출력할 그림 사이즈
                size = '256x256'
            )

            image_url_1 = response['data'][0]['url']
            image_url_2 = response['data'][1]['url']
            image_url_3 = response['data'][2]['url']
            image_url_4 = response['data'][3]['url']

            save_db.url1 = image_url_1
            save_db.url2 = image_url_2
            save_db.url3 = image_url_3
            save_db.url4 = image_url_4
            save_db.save()

            end = (time.time() - start)
            print(end)


            return redirect('/diary/select/')
            
    
    else:
        form = MemoryForm()

    return render(request, "diary/memory_form.html", {
            "form": form,
        })



def image_extraction(request):
    #이미지 추출 과정
    conn = pymysql.connect(host='localhost', user='admin', password='admin', db='project_third')
    start = time.time()

    try:
        with conn.cursor() as curs:
            sql = "SELECT * FROM diary_memory ORDER BY created_at DESC"
            curs.execute(sql) # 실행할 쿼리분 넣기
            rs = curs.fetchall() #sql문 실행해서 데이터 가져오기
            # print(rs)  # 쿼리문 출력해보기
            main_cont = rs[0][1]
            drawing = rs[0][4]
            emotion = rs[0][5]

    finally:
        conn.close()

    

        main_cont_300 = main_cont[:301]
        spelled_cont = spell_checker.check(u'{}'.format(main_cont_300)).as_dict()['checked']
        print(spelled_cont)
        print('='*10)
        # 2) 키워드 추출
        okt = Okt()

        tokenized_doc = okt.pos(spelled_cont)
        # print(tokenized_doc)

        # print('m')
        # print([word for word in tokenized_doc])

        # print([word[0] for word in tokenized_doc if word[1] == 'Noun'])
        # print('m')
        tokenized_nouns = ' '.join([word[0] for word in tokenized_doc if word[1] == 'Noun'])

        # print('품사 태깅 10개만 출력 :',tokenized_doc[:10])
        # print('명사 추출 :',tokenized_nouns)


        # 단어 합치기
        n_gram_range = (2, 3)

        count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
        candidates = count.get_feature_names_out()

        # print('trigram 개수 :',len(candidates))
        # print('trigram 다섯개만 출력 :',candidates[:4])


        # 유사 키워드 추출
        model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
        doc_embedding = model.encode([main_cont])
        candidate_embeddings = model.encode(candidates)

        top_n = 4
        distances = cosine_similarity(doc_embedding, candidate_embeddings)
        keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
        print(keywords)


        # 후보 간 유사성 최소화
        def max_sum_sim(doc_embedding, candidate_embeddings, words, top_n, nr_candidates):
            # 문서와 각 키워드들 간의 유사도
            distances = cosine_similarity(doc_embedding, candidate_embeddings)

            # 각 키워드들 간의 유사도
            distances_candidates = cosine_similarity(candidate_embeddings,
                                                    candidate_embeddings)

            # 코사인 유사도에 기반하여 키워드들 중 상위 top_n개의 단어를 pick.
            words_idx = list(distances.argsort()[0][-nr_candidates:])
            words_vals = [candidates[index] for index in words_idx]
            distances_candidates = distances_candidates[np.ix_(words_idx, words_idx)]

            # 각 키워드들 중에서 가장 덜 유사한 키워드들간의 조합을 계산
            min_sim = np.inf
            candidate = None
            for combination in itertools.combinations(range(len(words_idx)), top_n):
                sim = sum([distances_candidates[i][j] for i in combination for j in combination if i != j])
                if sim < min_sim:
                    candidate = combination
                    min_sim = sim

            return [words_vals[idx] for idx in candidate]


        fin_keyword = max_sum_sim(doc_embedding, candidate_embeddings, candidates, top_n=top_n, nr_candidates=30)
        kor_keywords = ', '.join([word for word in fin_keyword])


        # print(fin_keyword)
        # print('키워드 추출 : ', end)

        #번역 및 입력
        translator = Translator()
        eng_keywords = ', '.join([translator.translate(word, dest='en').text for word in fin_keyword])
        # print(eng_keywords)
        # print('번역 : ', start-time.time())

        search_keyword = eng_keywords + ', ' + emotion + ', in the style of ' + drawing
        print()
        print('='*10)
        print(f'마지막 키워드 : {kor_keywords}')
        print(f'마지막 키워드 : {search_keyword}')
        print('='*10)
        print()
        end = (time.time() - start)
        print(end)

        #키워드 db 저장
        save_db = ImageFields(keywords=kor_keywords)
        save_db.save()

    # finally:
    #    pass

    # try:
    #     with conn.cursor() as curs:
    #         sql = f"INSERT INTO dairy_imagefields (keywords) VALUES ({kor_keywords})"
    #         curs.execute(sql) # 실행할 쿼리분 넣기
    #         # rs = curs.fetchall() #sql문 실행해서 데이터 가져오기
    #         # # print(rs)  # 쿼리문 출력해보기
    #         # main_cont = rs[0][1]
    #         # emotion = rs[0][6]
    #         # drawing = rs[0][5]
    # finally:
    #     conn.close()
        
    print('end')

    # 3) 이미지 전환 및 추출
    # token keys
    openai.api_key = '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'

    #함수
    response = openai.Image.create(
        # 입력받은 키워드 입력
        prompt = search_keyword,
        
        # 출력할 그림 개수
        n = 4,

        # 출력할 그림 사이즈
        size = '256x256'
    )

    image_url_1 = response['data'][0]['url']
    image_url_2 = response['data'][1]['url']
    image_url_3 = response['data'][2]['url']
    image_url_4 = response['data'][3]['url']

    save_db.url1 = image_url_1
    save_db.url2 = image_url_2
    save_db.url3 = image_url_3
    save_db.url4 = image_url_4
    save_db.save()

    end = (time.time() - start)
    print(end)


    return redirect('http://localhost:8000/diary/select/')

import urllib.request
from pathlib import Path

def select(request):
    image_qs = ImageFields.objects.values().order_by('-id')[0]

    print('='*10)
    print(image_qs)
    print('='*10)
    number = image_qs['id']

    if request.method == "POST":

        url = request.POST['finImg']
        filename = f'{number}.jpg'
        image_path = f'do_it_django_prj/static/dalle/{filename}'

        path = Path(image_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        urllib.request.urlretrieve(url, image_path)

        # resource = urllib.request.urlopen(url)
        # output = open(filename,"wb")
        # output.write(resource.read())
        # output.close()

        FinImg.objects.create(finImg=filename)
#        form = ImgForm(request.POST)
#        form.save()

        return redirect(f'/diary/{number}/')
    else:
        form = MemoryForm()


    return render(request, "diary/memory_photo_confirm.html", {
        "image_list" : image_qs,
    })



def memory_edit(request, pk):
    memory = Memory.objects.get(pk=pk)


    if request.method == "POST":
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "일기를 저장했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm(instance=memory)

    return render(request, "diary/memory_form.html", {
        "form": form,
    })


def memory_delete(request, pk):
    memory = Memory.objects.get(pk=pk)

    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "일기를 삭제했습니다.")
        return redirect("/diary/gallery/")

    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })

# def calendar(request):
#     return render(request, "diary/calendar.html")

def info(request):
    return render(request, "diary/info.html")


# keyword diary--------------------------------------------------------------------------------------

# 목록 페이지는 위와 같음. 갤러리 or 달력으로 보여줌.


# 상세페이지
def k_detail_page(request, pk):
    keyword_memory = KeywordPost.objects.get(pk=pk)
    return render(request, "diary/keyword_detail.html", {
        "keyword_post": keyword_memory,
    })



# 키워드로 일기쓰기 (생성)

def keyword_new(request):
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "일기를 생성했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = KeywordForm()

    return render(request, "diary/keyword_form.html", {
        "form": form,
    })


def key_edit(request, pk):
    memory = KeywordPost.objects.get(pk=pk)

    if request.method == "POST":
        form = KeywordForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm(instance=memory)

    return render(request, "diary/memory_form.html", {
        "form": form,
    })


def key_delete(request, pk):
    memory = KeywordPost.objects.get(pk=pk)

    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "일기를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })

def dashboard(request):
    return render(request, "diary/dashboard.html")


def bar_chart(request) :
    memorys = Memory.objects.values()
    dbCon = pymysql.connect(host='localhost', user='admin', password='admin', db='project_test2')
    cursor = dbCon.cursor()
    
    emotions = []
    for memory in memorys:
        
        emotions.append(memory['Emotion'])
        

    emotion_count ={
        '쾌활' : 0,
        '기쁨' : 0,
        '보통' : 0,
        '우울' : 0,
        '화남' : 0,
    }

    
    for emotion in emotions:

        if emotion == '쾌활' :
            emotion_count['쾌활'] += 1
        elif emotion == '기쁨':
            emotion_count['기쁨'] += 1
        elif emotion == '보통':
            emotion_count['보통'] += 1
        elif emotion == '우울':
            emotion_count['우울'] += 1
        elif emotion == '화남' :
            emotion_count['화남'] += 1



    with dbCon :
        cursor.execute("SELECT * FROM diary_memory")
        diary_data = cursor.fetchall()
    
    return render(request, "diary/dashboard.html", {
        'emotion_count' : emotion_count,
        })

def makeWordCloud(request):
    memorys = Memory.objects.values('content')
    dbCon = pymysql.connect(host='localhost', user='admin', password='admin', db='project_test2')
    cursor = dbCon.cursor()
    print(memorys)
    df = pd.DataFrame('memorys')
    mask = Image.open('\static\cloud.png')
    mask = np.array(mask)

    plt.subplots(figsize=(25, 15))

    wordcloud = WordCloud(background_color='white', width=1000, height=700, mask=mask, font_path=fontpath,
                          stopwords=STOPWORDS).generate(df)  # 워드클라우드 설정

    plt.axis('off')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()
    return render(request, 'diary/dashboard.html', {'content': df.content})
    