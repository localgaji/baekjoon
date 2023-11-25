# Shortest Path (최단거리)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

최단거리 문제를 해결할 때 사용하는 알고리즘 중 다익스트라, 벨만-포드, 플로이드 위주로 뽑았습니다.

문제를 읽어보고 문제를 해결하기 위해 필요한 무엇인지 생각해봐야 합니다.

위 알고리즘들의 차이와 각 알고리즘의 특성을 이해하지 못한 상황에서 문제를 푸는 것은 도움이 안된다고 생각합니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7273)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/18352" target="_blank">18352</a> | <a href="https://www.acmicpc.net/problem/18352" target="_blank">특정 거리의 도시 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 01 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11403" target="_blank">11403</a> | <a href="https://www.acmicpc.net/problem/11403" target="_blank">경로 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 02 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/13549" target="_blank">13549</a> | <a href="https://www.acmicpc.net/problem/13549" target="_blank">숨바꼭질 3</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 03 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11265" target="_blank">11265</a> | <a href="https://www.acmicpc.net/problem/11265" target="_blank">끝나지 않는 파티</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 04 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1753" target="_blank">1753</a> | <a href="https://www.acmicpc.net/problem/1753" target="_blank">최단경로</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 05 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/14938" target="_blank">14938</a> | <a href="https://www.acmicpc.net/problem/14938" target="_blank">서강그라운드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 06 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1277" target="_blank">1277</a> | <a href="https://www.acmicpc.net/problem/1277" target="_blank">발전소 설치</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 07 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2224" target="_blank">2224</a> | <a href="https://www.acmicpc.net/problem/2224" target="_blank">명제 증명</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 08 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11404" target="_blank">11404</a> | <a href="https://www.acmicpc.net/problem/11404" target="_blank">플로이드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 09 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1956" target="_blank">1956</a> | <a href="https://www.acmicpc.net/problem/1956" target="_blank">운동</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 10 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/10159" target="_blank">10159</a> | <a href="https://www.acmicpc.net/problem/10159" target="_blank">저울</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 11 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11657" target="_blank">11657</a> | <a href="https://www.acmicpc.net/problem/11657" target="_blank">타임머신</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 12 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/22865" target="_blank">22865</a> | <a href="https://www.acmicpc.net/problem/22865" target="_blank">가장 먼 곳</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 13 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1719" target="_blank">1719</a> | <a href="https://www.acmicpc.net/problem/1719" target="_blank">택배</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> | <a href="./../solution/shortest_path/1719">바로가기</a> |
| 14 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1238" target="_blank">1238</a> | <a href="https://www.acmicpc.net/problem/1238" target="_blank">파티</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 15 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1613" target="_blank">1613</a> | <a href="https://www.acmicpc.net/problem/1613" target="_blank">역사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 16 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1865" target="_blank">1865</a> | <a href="https://www.acmicpc.net/problem/1865" target="_blank">웜홀</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 17 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1507" target="_blank">1507</a> | <a href="https://www.acmicpc.net/problem/1507" target="_blank">궁금한 민호</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |

[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
