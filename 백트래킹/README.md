# Backtracking (백트래킹)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

백트래킹 문제를 뽑았습니다.

백트래킹의 기본 연습 문제인 N과 M 시리즈 모든 문제를 진행 상황로 뽑았습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7135)
|           순번           |        진행 상황         |        문제 이름         |         난이도          |
|  :-----:  | :-----: | :-----: | :-----: |
| 1 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/16987" target="_blank">계란으로 계란치기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 2 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/14712" target="_blank">넴모넴모 (Easy)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 3 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1174" target="_blank">줄어드는 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 4 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/3980" target="_blank">선발 명단</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 5 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/6443" target="_blank">애너그램</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 6 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/18430" target="_blank">무기 공학</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 7 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/9663" target="_blank">N-Queen</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 8 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2580" target="_blank">스도쿠</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 9 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1062" target="_blank">가르침</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 10 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2661" target="_blank">좋은수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 11 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/22944" target="_blank">죽음의 비</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 12 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/17136" target="_blank">색종이 붙이기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |
| 13 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1799" target="_blank">비숍</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15649" target="_blank">N과 M (1)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15650" target="_blank">N과 M (2)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15651" target="_blank">N과 M (3)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15652" target="_blank">N과 M (4)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15654" target="_blank">N과 M (5)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15655" target="_blank">N과 M (6)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15656" target="_blank">N과 M (7)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15657" target="_blank">N과 M (8)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15663" target="_blank">N과 M (9)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15664" target="_blank">N과 M (10)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15665" target="_blank">N과 M (11)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15666" target="_blank">N과 M (12)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1182" target="_blank">부분수열의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/10971" target="_blank">외판원 순회 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
|  |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/14888" target="_blank">연산자 끼워넣기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |


[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
