citations	= [3, 0, 6, 1, 5]
# 저 숫자 중의 하나가 나와야 하는데..
# 내림차순으로 비교해보는 것이 좋다. 
# 내림차순으로 비교할 때 인용과 같은 숫자가 있을 시 
# 답이 된다.

citations= sorted(citations,reverse=True)
print(citations)
for i in range(len(citations)):
    print( '숫자', citations[i])
    count = len(citations[ :i])
    print('비교',citations[ :i])
    print(count)
    # if count == citations[i]:
    #     return citations[i] 
    # elif 



# list  = []
# for i in citations:
#     print('----------')
#     count = 0
#     for j in citations[i:]:
#         if i <= j:
#             count += 1
#     if count >= i:
#         list.append(i)
#         print(list)

# print(list[0])
