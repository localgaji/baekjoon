# Dynamic Programming 2 (동적계획법 2)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

다이나믹 프로그래밍 유형 문제 위주로 뽑았습니다.

다이나믹 프로그래밍은 점화식을 세우면 절반 이상은 풀었다고 볼 수 있습니다.

점화식 세우는 건 금방 익히기 힘들어 코딩테스트에 나올만한 문제들,   
다이나믹 프로그래밍을 공부할만한 문제들을 최대한 뽑았습니다.


<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7021)
|           순번           |        진행 상황         |        문제 이름         |         난이도          |
|  :-----:  | :-----: | :-----: | :-----: |
| 1 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/15724" target="_blank">주지수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |
| 2 |  ![status][Done]  | <a href="http://www.acmicpc.net/problem/9084" target="_blank">동전</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 3 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/12865" target="_blank">평범한 배낭</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 4 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/9251" target="_blank">LCS</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 5 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2225" target="_blank">합분해</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 6 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/5557" target="_blank">1학년</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 7 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2624" target="_blank">동전 바꿔주기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 8 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/14567" target="_blank">선수과목 (Prerequisite)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 9 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/17485" target="_blank">진우의 달 여행 (Large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |
| 10 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/18427" target="_blank">함께 블록 쌓기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 11 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1915" target="_blank">가장 큰 정사각형</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 12 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2631" target="_blank">줄세우기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 13 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2758" target="_blank">로또</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 14 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2073" target="_blank">수도배관공사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 15 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2056" target="_blank">작업</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 16 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1695" target="_blank">팰린드롬 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 17 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/10942" target="_blank">팰린드롬?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 18 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/21923" target="_blank">곡예 비행</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 19 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/21941" target="_blank">문자열 제거</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |
| 20 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2629" target="_blank">양팔저울</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 21 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/2228" target="_blank">구간 나누기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 22 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1520" target="_blank">내리막 길</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 23 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/20542" target="_blank">받아쓰기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 24 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1005" target="_blank">ACM Craft</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 25 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/11049" target="_blank">행렬 곱셈 순서</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 26 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/1823" target="_blank">수확</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |
| 27 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/20181" target="_blank">꿈틀꿈틀 호석 애벌레 - 효율성</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |
| 28 |  ![status][ToDo]  | <a href="http://www.acmicpc.net/problem/3687" target="_blank">성냥개비</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |



[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
