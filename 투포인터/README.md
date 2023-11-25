
# Two Pointers (투 포인터)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

최근 많이 나오는 유형이니 꼭 풀어보시길 바랍니다.

특히, 투 포인터는 부분합과 많이 연관되어 나오는 만큼, 투 포인터 문제는 아니지만 부분합을 연습할 수 있는 문제를 첫 문제로 넣어놨습니다.

광부 호석은 최근 제 2회 류호석배 코딩테스트에서 나온 문제로 코딩테스트 치곤 상당히 어려운 문제에 속하지만 한번 접해보면 매우 좋은 문제라 넣었습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6782)
|          순번          |        진행 상황         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11728" target="_blank">11728</a> | <a href="https://www.acmicpc.net/problem/11728" target="_blank">배열 합치기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 01 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/21921" target="_blank">21921</a> | <a href="https://www.acmicpc.net/problem/21921" target="_blank">블로그</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 02 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/20922" target="_blank">20922</a> | <a href="https://www.acmicpc.net/problem/20922" target="_blank">겹치는 건 싫어</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/two_pointer/20922">바로가기</a> |
| 03 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2470" target="_blank">2470</a> | <a href="https://www.acmicpc.net/problem/2470" target="_blank">두 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/two_pointer/2470">바로가기</a> |
| 04 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/22862" target="_blank">22862</a> | <a href="https://www.acmicpc.net/problem/22862" target="_blank">가장 긴 짝수 연속한 부분 수열 (large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 05 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/15961" target="_blank">15961</a> | <a href="https://www.acmicpc.net/problem/15961" target="_blank">회전 초밥</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/two_pointer/15961">바로가기</a> |
| 06 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1806" target="_blank">1806</a> | <a href="https://www.acmicpc.net/problem/1806" target="_blank">부분합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/two_pointer/1806">바로가기</a> |
| 07 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/3151" target="_blank">3151</a> | <a href="https://www.acmicpc.net/problem/3151" target="_blank">합이 0</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 08 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/22945" target="_blank">22945</a> | <a href="https://www.acmicpc.net/problem/22945" target="_blank">팀 빌딩</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 09 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/20366" target="_blank">20366</a> | <a href="https://www.acmicpc.net/problem/20366" target="_blank">같이 눈사람 만들래?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 10 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/7453" target="_blank">7453</a> | <a href="https://www.acmicpc.net/problem/7453" target="_blank">합이 0인 네 정수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 11 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/20442" target="_blank">20442</a> | <a href="https://www.acmicpc.net/problem/20442" target="_blank">ㅋㅋ루ㅋㅋ</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 12 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/21279" target="_blank">21279</a> | <a href="https://www.acmicpc.net/problem/21279" target="_blank">광부 호석</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/> |                      |

[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
