from django.shortcuts import render

# Create your views here.
def get_base_ctx(pagetitle):
    return {
        'pagetitle': pagetitle
    }

def index(request):
    return render(request, 'pages/index.html', context=get_base_ctx('QuizyPeasy'))