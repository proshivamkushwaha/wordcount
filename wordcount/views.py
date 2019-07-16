from django . shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['text']
    word_list = data.split()
    list_lenth = len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1


    return render(request, 'count.html', {'fulltext':data, 'listlenth':list_lenth, 'worddictionary' : worddictionary.items()})