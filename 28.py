#if문을 한 줄로 작성하는 법
if 'money' in pocket:
    pass
else:
    print("현금을 꺼내라")
#다음과 같은 방법으로 더 간단하게 표현 가능
pocket=['paper','money','cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

