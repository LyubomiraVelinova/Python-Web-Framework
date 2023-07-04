from django.shortcuts import render


# Create your views here.

# http: // localhost: 8000 / - homepage
# http: // localhost: 8000 / login / - login page
# http: // localhost: 8000 / signup / - signup page
# http: // localhost: 8000 / about  - about us page
# http: // localhost: 8000 / campaign / details / < id > / - campaign details page
# http: // localhost: 8000 / donation / make  - make donation page
# http: // localhost: 8000 / profile / details / - profile details page
# http: // localhost: 8000 / profile / delete / - delete profile page

def index(request):
    return render(request, 'common/home-page.html')
