from django.shortcuts import render

posts = [
    {
        'author': 'Siren',
        'title': 'Blog1',
        'content':'First',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Smiley',
        'title': 'Blog2',
        'content':'Second',
        'date_posted': 'August 90, 2019',
    }
]


def home(request):
	context = {
	    'posts': posts
	}
	return render(request, 'blog/home.html', context)
    #return HttpResponse("<h1>Blog Home</h1>") 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    #return HttpResponse("<h1>About</h1>") 



