# Graph Traversal (그래프 탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

BFS, DFS 유형을 다양하게 골랐습니다. 

문제를 보고 어떤 알고리즘을 써야할지 잘 판단하셔야 합니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6853)

|           순번           |        진행 상황         |        문제 이름         |         난이도          |
|  :-----:  | :-----: | :-----: | :-----: |
| 1 |  ![status][Done]  | <a href="https://www.acmicpc.net/problem/7576" target="_blank">토마토</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 2 |  ![status][Done]  | <a href="https://www.acmicpc.net/problem/7569" target="_blank">토마토</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 3 |  ![status][Done]  | <a href="https://www.acmicpc.net/problem/16234" target="_blank">인구 이동</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 4 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/13549" target="_blank">숨바꼭질 3</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 5 |  ![status][Done]  | <a href="https://www.acmicpc.net/problem/17836" target="_blank">공주님을 구해라!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 6 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2668" target="_blank">숫자고르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 7 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/13023" target="_blank">ABCDE</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 8 |  ![status][Done]  | <a href="https://www.acmicpc.net/problem/5547" target="_blank">일루미네이션</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 9 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/14502" target="_blank">연구소</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 10 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2636" target="_blank">치즈</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 11 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/16973" target="_blank">직사각형 탈출</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 12 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/18513" target="_blank">샘터</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 13 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2573" target="_blank">빙산</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 14 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/4179" target="_blank">불!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 15 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1967" target="_blank">트리의 지름</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 16 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1600" target="_blank">말이 되고픈 원숭이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 17 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/16954" target="_blank">움직이는 미로 탈출</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 18 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2206" target="_blank">벽 부수고 이동하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 19 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/16932" target="_blank">모양 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 20 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/9466" target="_blank">텀 프로젝트</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 21 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/22868" target="_blank">산책 (small)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 22 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/22948" target="_blank">원 이동하기 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 23 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/22946" target="_blank">원 이동하기 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2606" target="_blank">바이러스</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1260" target="_blank">DFS와 BFS</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11725" target="_blank">트리의 부모 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1325" target="_blank">효율적인 해킹</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2178" target="_blank">미로 탐색</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2667" target="_blank">단지번호붙이기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/16918" target="_blank">봄버맨</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
|  |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/14940" target="_blank">쉬운 최단거리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |


[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
