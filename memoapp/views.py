from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemoForm
from .models import Memo


def memo(request):
    memos = Memo.objects.all()
    return render(request, 'memoapp/memo.html', {"memos": memos})

def memo_create(request):
    if request.method == "POST": # HTTP 메소드 - post 요청일 경우 데이터 처리 (폼제출)
        form = MemoForm(request.POST) # 제출된 데이터를 폼에 넣음 -> MemoForm에 전달 -> 폼 인스턴스 생성 / request.POST : 사용자가 제출한 폼 데이터를 담는 객체
        if form.is_valid(): # 폼이 유효한지 검사
            form.save() # 데이터 저장 - ModelForm에서 제공하는 메소드, 폼 데이터를 Memo의 인스턴스로 저장 -> 새로운 메모가 DB에 추가
            return redirect("memo") # 저장 후 다른 페이지로 페이지 이동 (메모 목록으로)
    else: # GET 요청 처리 - 요청이 POST가 아닌 경우
        form = MemoForm # 비어 있는 폼 인스턴스 생성

    return render(request, "memoapp/memobody.html", {"memo": form})
                                                                # 컨텍스트 데이터가 뭐지... (지피티 사용) -> 암묵적인 룰 (디폴트값)

def memo_update(request, memo_id): # pk : 수정하려는 메모의 고유 ID
    memo = get_object_or_404(Memo, pk=memo_id)
    if request.method == "POST": # 사용자가 폼을 제출했을 때
        form = MemoForm(request.POST, instance=memo) # 사용자가 제출한 데이터를 MemoForm에 넣되, 기존 메모 데이터 기반으로 폼 생성
                                                     # instance=memo : 수정할 메모 객체를 폼에 전달해 기존 데이터를 채워 넣음
        if form.is_valid(): # 폼 유효성 검사
            form.save() # 수정 데이터 저장
            return redirect("memo") # 저장 후 다른 페이지로 페이지 이동 (메모 목록으로) / memo_id는 우리가 세팅한 것 - DB 받아오는 것 주기
    else: # GET 요청 처리 - 요청이 POST가 아닌 경우
        form = MemoForm(instance=memo) # GET 요청이면 기존 메모 데이터를 폼에 채워 넣음

    return render(request, "memoapp/memobody.html", {"memo": form}) # 랜더링

def memo_detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, "memoapp/memodetail.html", {"memo": memo})

def memo_delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return redirect("memo")


# GET(데이터를 보내다보니 body를 보낼 수 없음-세부내용은 쿼리사용),
# POST(body의 데어터가 전부 보낼때), PUT(body의 데이터의 일부만 변경할 때) 의 차이 (데이터 바꿀때) <-면접 단골질문
# DELETE(post와 거의 똑같으나 이름만 그럼)