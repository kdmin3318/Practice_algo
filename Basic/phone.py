m = int(input())
n = list(map(int, input().split()))
y_cost, m_cost = 0,0
for i in range(m):
    y_cost += (n[i]//30+1)*10
for i in range(m):
    m_cost += (n[i]//60+1)*15
if y_cost<m_cost:
    print('Y', end=" ")
    print(y_cost)
elif y_cost>m_cost:
    print('M', end=" ")
    print(m_cost)
else:
    print('Y M')
    print(y_cost)
