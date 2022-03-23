N = [1]
for i in range(5):
    L = N.copy()
    for j in range(len(L)):
        temp = str(L[j])
        L[j] = temp
    l = ' '.join(L).center(20)  # 列表转字符串，空格分割且居中表示
    print(l)
    N.append(0)
    N = [N[k] + N[k-1] for k in range(i+2)]
