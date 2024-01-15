# Binary Search (이분탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

진행 상황 아닌 나머지는 나머지를 난이도 섞었습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7277)
|           순번           |        진행 상황         |        문제 이름         |         난이도          |
|  :-----:  | :-----: | :-----: | :-----: |
| 1 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/3079" target="_blank">입국심사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 2 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2470" target="_blank">두 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 3 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/20444" target="_blank">색종이와 가위</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 4 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2110" target="_blank">공유기 설치</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 5 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1477" target="_blank">휴게소 세우기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 6 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/13397" target="_blank">구간 나누기 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 7 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2412" target="_blank">암벽 등반</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 8 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1939" target="_blank">중량제한</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 9 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2473" target="_blank">세 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 10 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1300" target="_blank">K번째 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |
| 11 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/7453" target="_blank">합이 0인 네 정수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1789" target="_blank">수들의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/10815" target="_blank">숫자 카드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2417" target="_blank">정수 제곱근</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2512" target="_blank">예산</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/19637" target="_blank">IF문 좀 대신 써줘</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/11663" target="_blank">선분 위의 점</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2805" target="_blank">나무 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1654" target="_blank">랜선 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/22871" target="_blank">징검다리 건너기 (large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |


[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
