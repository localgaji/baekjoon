# Dynamic Programming 1 (동적계획법 1)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

다이나믹 프로그래밍 유형 쉬운 문제 위주로 뽑았습니다.

다이나믹 프로그래밍은 점화식을 세우면 절반 이상은 풀었다고 볼 수 있습니다.

점화식 세우는 건 금방 익히기 힘들어 코딩테스트에 나올만한 문제들,   
다이나믹 프로그래밍을 공부할만한 문제들을 최대한 뽑았습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7020)
|           순번           |        진행 상황         |        문제 이름         |         난이도          |
|  :-----:  | :-----: | :-----: | :-----: |
| 1 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1010" target="_blank">다리 놓기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |
| 2 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/9655" target="_blank">돌 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |
| 3 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2839" target="_blank">설탕 배달</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |
| 4 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/17626" target="_blank">Four Squares</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 5 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1463" target="_blank">1로 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 6 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/9095" target="_blank">1, 2, 3 더하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 7 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/11726" target="_blank">2×n 타일링</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 8 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2579" target="_blank">계단 오르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 9 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/11727" target="_blank">2×n 타일링 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 10 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2407" target="_blank">조합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 11 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/11053" target="_blank">가장 긴 증가하는 부분 수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
| 12 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1912" target="_blank">연속합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
| 13 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/11055" target="_blank">가장 큰 증가하는 부분 수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
| 14 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/22857" target="_blank">가장 긴 짝수 연속한 부분 수열 (small)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |
| 15 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/9465" target="_blank">스티커</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 16 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/1890" target="_blank">점프</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 17 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/2156" target="_blank">포도주 시식</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 18 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/10844" target="_blank">쉬운 계단 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 19 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/11660" target="_blank">구간 합 구하기 5</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 20 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/21317" target="_blank">징검다리 건너기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 21 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/22869" target="_blank">징검다리 건너기 (small)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 22 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15486" target="_blank">퇴사 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 23 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1106" target="_blank">호텔</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 24 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2293" target="_blank">동전 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 25 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2294" target="_blank">동전 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |



[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
