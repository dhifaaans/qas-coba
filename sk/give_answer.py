import unicodedata
import wolframalpha
from nltk import word_tokenize, pos_tag, ne_chunk, conlltags2tree, tree2conlltags
import wikipedia
import collections

#===============================================================#================================================================
# Determine the type of question i.e location, date, person ,definiton
# def classify_question(question):
#     q = question.lower().split()
#     #print(q[0] ,q[1])
#     if q[0] == 'where':
#         return 'Location'
#     elif 'year'  in question:
#             return 'Date'
#     elif 'country' in question:
#         return 'Country'
#     elif q[0] == 'who':
#         return 'Person'
#     elif q[0] == 'what':
#         return 'Definition'
#     else:

#         return 'None'

def classify_question(question):
    q = question.lower().split()
    if q[0] == 'dimana':
        return 'Location'
    elif 'kapan' in question:
        return 'WorkingHour'
    elif 'berapa' in question:
        return 'Price'
    elif 'menu' in question:
        return 'Menu'
    elif 'fasilitas' in question:
        return 'Facility'
    elif 'spesial' in question:
        return 'SpecailMenu'
    elif 'diskon' in question:
        return 'Discount'
    elif 'sponsor' in question:
        return 'namaSponsor'
    else:
        return 'None'

# def wiki_search(question):
#     l = question.split(' ')
#     if len(l) > 2:
#         ques = " ".join(l[2:])
#     try:
#         print 'inside wiki search'
#         ans = (wikipedia.summary(question, sentences=1)).encode('ascii', 'ignore')
#         #ans=re.sub('([(].*?[)])',"",ans)
#         #print(ans)
#         link = wikipedia.page(ques)
#         ans = ans + '\n For more information: '+link.url
#         #print ('Refernce: ',link.url)
#         #print ans
#     except:
#         print 'wiki_search_failed_google'
#         #google_search(question)
#     return ans

def json_search(question):
    l = question.split(' ')
    if len(l) > 2:
        ques = " ".join(l[2:])
    try:
        print 'json searching'
        ans = 

def answer_question(question):
    try:
        app_id = ''    # add your app id into this
        if not app_id:
            print 'Add your app id in line no. 110'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        ans = str(next(res.results).text).replace('.', '.\n')

        if ans == 'None':
            print 'ans is none'
            q_type = classify_question(question)
            if q_type == 'Definition' or q_type == 'Location':
                print 'except-wiki'
                ans = wiki_search(question)
            #if len(question.split())<=5:
            #    print 'none-wiki'
            #    ans = wiki_search(question)
            else:
                print 'none-google'
                #ans = google_search(question)
                print 'google answ: ',ans

        return ans

    except:
        try:
            print 'Exception at first run'
            q_type = classify_question(question)
            if q_type == 'Definition' or q_type == 'Location':
                print 'except-wiki'
                ans = wiki_search(question)
            #if len(question.split())<=5:
            #    print 'except-wiki'
            #    ans = wiki_search(question)
            else:
                print 'except-google'
                #ans = google_search(question)
                print 'google answ: ',ans



            return ans
        except:
               return "Oops! I don't know. Try something else"
