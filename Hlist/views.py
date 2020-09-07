from django.shortcuts import render,redirect
from .models import mileage,vacation,used_vacation,memo,evening,dawn
from django.core.exceptions import ObjectDoesNotExist

def main(request):
    mil=mileage.objects.all()
    vac=vacation.objects.all()
    uvac=used_vacation.objects.all()
    memos=memo.objects.all()
    ev=evening.objects.all()
    da=dawn.objects.all()
    
    return render(request,'Hlist/main.html',{'mileage':mil, 'vacation':vac, 'used_vacation':uvac, 'memo':memos,'evening':ev,'dawn':da})


def postmemo(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        if (request.POST['memoid'] != "==선택==" and request.POST['memotext'] != "") :
            objects=memo.objects.filter(memoid=request.POST['memoid']).first() #필터로 검색 해서 없으면 None반환
            if(objects!=None):
                delete_object=memo.objects.get(memoid=request.POST['memoid'])
                delete_object.delete()
            new_article = memo.objects.create(
                memoid=request.POST['memoid'],
                memotitle=request.POST['memotitle'],
                memotext=request.POST['memotext']
                )
            return redirect('/')

        # 새글 등록 끝
    return render(request, 'Hlist/post.html')

def postdelete(request,pk):
    objects=memo.objects.get(memoid=pk)
    objects.delete()
    return redirect('/')
        
    
def SaveEveningCheckBox(request):
    print(request.POST.getlist("tag[]"))
    check_values=request.POST.getlist('tag')
    ev=evening.objects.all()
    print(check_values)
    for i in ev:
        i.find_check=False
    for x in check_values:
        evening.objects.get(evening.id==x).find_check=True
        evening.save()
    return redirect('/')
