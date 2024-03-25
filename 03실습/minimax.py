# 미니맥스 알고리즘의 의사코드

#  function minimax(node, depth, maxPlayer)
#     if depth == 0 or node가 단말 노드 then
#         return node의 휴리스틱값
#     if maxPlayer then # 최대화 노드
#      value <- -
#      for each child of node do
#         value <- max(valu, minimasx(child,depth -1, FALSE))
#     return value
#     else
#         vale <-
#     for each child of node do
#         value <- min(claue, minimax(child, depth -1, TRUE))
#     return