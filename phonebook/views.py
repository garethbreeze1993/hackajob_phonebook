from django.shortcuts import render
import requests

def whole_list(request):
    r = requests.get('http://www.mocky.io/v2/581335f71000004204abaf83')
    whole_data = r.json()['contacts']
    search_query = request.GET.get('search_query', None)
    topic = request.GET.get('topic', None)
    print('what in need to see')
    print(search_query)
    print(topic)
    if search_query is None:
        return render(request, 'home.html', {'whole_data': whole_data})
    else:
        searched_data = []
        for data in whole_data:
            if search_query in data[topic]:
                searched_data.append(data)
        return render(request, 'home.html', {'whole_data': searched_data})


