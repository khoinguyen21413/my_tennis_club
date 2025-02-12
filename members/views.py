from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    # Get toan bo data tu database
    my_members = Member.objects.all().order_by('first_name').values() # "first_name": A->Z; "-first_name": Z->A
    template = loader.get_template("tennis_player.html")
    context = {
        "my_members": my_members
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_member = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "my_member": my_member
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def queryset(request):
    # yeu cau: chi show cot firstname : values_list
    my_data = Member.objects.values_list('first_name')
    my_phone = Member.objects.values_list('phone')

    # Loc du lieu
    my_data2 = Member.objects.filter(last_name='Nguyễn').values()
    template = loader.get_template('queryset.html')
    context = {
       "my_data" : my_data,
       "my_phone" : my_phone,
       "my_data2" : my_data2
    }
    return HttpResponse(template.render(context, request))
