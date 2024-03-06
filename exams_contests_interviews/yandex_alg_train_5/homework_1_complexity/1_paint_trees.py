v_0, v = list(map(int, input().split()))
m_0, m = list(map(int, input().split()))

if m_0 > v_0:
    v_0, v, m_0, m = m_0, m, v_0, v

v_left = v_0 - v
v_right = v_0 + v
m_left = m_0 - m
m_right = m_0 + m


if m_right >= v_left:
    print(max(v_right, m_right) - min(m_left,v_left) + 1)
else:
    print(m_right - m_left + v_right - v_left + 2)



