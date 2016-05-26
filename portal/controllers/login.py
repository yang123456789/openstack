from db.models import Register
from db.views import *

def validate(request):
    params = request.POST
    # print params
    return render(request, 'homepage/login.html')