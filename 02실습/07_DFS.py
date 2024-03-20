#깊이 우선 탐색(DFS: Depth-First Search)
open = [A]; closed = []
open = [B,C]; closed = [A]
open = [D,E,C]; closed = [B,A]
open = [H,I,E,C]; closed = [D,B,A]
open = [I,E,C]; closed = [H,D,B,A]
open = [E,C]; closed = [I,H,D,B,A]
open = [C]; closed = [E,H,D,B,A] # I는  이미 closed 리스트에 있으므로 open 리스트에 추가되지 않는다.
open = [F,G]; closed = [C,H,D,B,A]
open = [U,G]; closed = [F,C,H,D,B,A]
