
#Stack operations using lists(LIFO)
st=[1,2,3,4,5]
st.append(6)
print(st)
st.pop()
print(st)

#Queue operations using lists(FIFO)
from collections import deque
qu=["Tito","Luis","Ted","Martha","Abby"]
dqu=deque(qu) #deque initiates queue framework for faster pop from left for FIFO
print(dqu)
dqu.popleft()
print(dqu)

