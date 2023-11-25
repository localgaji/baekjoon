# Prefix Sum (누적 합)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

누적합은 단순히 이 알고리즘만 사용하는 문제보다 누적합과 다른 알고리즘을 섞어 쓰는 경우가 많습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7274)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/14929" target="_blank">14929</a> | <a href="https://www.acmicpc.net/problem/14929" target="_blank">귀찮아 (SIB)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/prefix_sum/14929">바로가기</a> |
| 01 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2167" target="_blank">2167</a> | <a href="https://www.acmicpc.net/problem/2167" target="_blank">2차원 배열의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/prefix_sum/2167">바로가기</a> |
| 02 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/20438" target="_blank">20438</a> | <a href="https://www.acmicpc.net/problem/20438" target="_blank">출석체크</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | <a href="./../solution/prefix_sum/20438">바로가기</a> |
| 03 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/11660" target="_blank">11660</a> | <a href="https://www.acmicpc.net/problem/11660" target="_blank">구간 합 구하기 5</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/prefix_sum/11660">바로가기</a> |
| 04 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/21318" target="_blank">21318</a> | <a href="https://www.acmicpc.net/problem/21318" target="_blank">피아노 체조</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/prefix_sum/21318">바로가기</a> |
| 05 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/2015" target="_blank">2015</a> | <a href="https://www.acmicpc.net/problem/2015" target="_blank">수들의 합 4</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/prefix_sum/2015">바로가기</a> |
| 06 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/1749" target="_blank">1749</a> | <a href="https://www.acmicpc.net/problem/1749" target="_blank">점수따먹기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/prefix_sum/1749">바로가기</a> |
| 07 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/10986" target="_blank">10986</a> | <a href="https://www.acmicpc.net/problem/10986" target="_blank">나머지 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> | <a href="./../solution/prefix_sum/10986">바로가기</a> |
| 08 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/20440" target="_blank">20440</a> | <a href="https://www.acmicpc.net/problem/20440" target="_blank">🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> | <a href="./../solution/prefix_sum/20440">바로가기</a> |
| 09 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/21757" target="_blank">21757</a> | <a href="https://www.acmicpc.net/problem/21757" target="_blank">나누기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/prefix_sum/21757">바로가기</a> |
| 10 |  ![status][ToDo]  | <a href="https://www.acmicpc.net/problem/20543" target="_blank">20543</a> | <a href="https://www.acmicpc.net/problem/20543" target="_blank">폭탄 던지는 태영이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> | <a href="./../solution/prefix_sum/20543">바로가기</a> |
