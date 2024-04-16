# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def solution():
  global width_to_rightside
  res = 0

  width_to_rightside = [[0]*C for _ in range(R)]
  set_width_to_rightside()

  for i in range(R):
    for j in range(C):
      res = max(res, get_people_count_for_table(i, j))

  return res

def set_width_to_rightside():     
  global width_to_rightside

  for i in range(R):
    j = 0
    while(j<C):
      if(layout[i][j] == '.'):
        width = get_width_to_rightside(i, j)

        # . . . . . 에서 5를 구했으므로 아래와 같이 처리해준다.
        # 5 4 3 2 1
        while(width > 0):
          width_to_rightside[i][j] = width

          width -= 1
          j += 1
      else:     
        j += 1

def get_width_to_rightside(x, y):
  # (x, y) -> (x, C)
  for j in range(y, C):
    if(layout[x][j] == 'X'):
      j -= 1
      break                        

  return j - y + 1

def get_people_count_for_table(x_start, y_start):
  if(layout[x_start][y_start] == 'X'): return 0 
  
  global width_to_rightside         
  res = 0

  # 테이블: (x_start, y_start) ~ (x_end, y_start + 'width - 1')  
  # 사전에 만들어둔 width_to_rightside을 통해, 특정 좌표에서
  # 오른쪽으로의 width를 바로 알 수 있다.      
  width = float('inf')
  for x_end in range(x_start, R):
    if(layout[x_end][y_start] == 'X'): break

    width = min(width, width_to_rightside[x_end][y_start])
    height = (x_end - x_start) + 1

    res = max(res, 2*width + 2*height - 1)
           
  return res        
    

if __name__ == '__main__':
  R, C = map(int, input().split())
  layout = [list(input().rstrip()) for _ in range(R)]
       
  print(solution())