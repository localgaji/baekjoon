# Brute Force (완전탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

완전탐색 중 백트래킹 있었던 문제와 최대한 겹치지 않도록 했습니다.

다른 알고리즘 풀었어도 완전탐색으로 풀어보시면 좋습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7271)
| 	          순번          	 |	        진행 상황         	|	        문제 이름         	|	         난이도          	|
| 	 :-----: 	 |	 :-----: 	|	 :-----: 	|	 :-----: 	|
| 	1	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/12919" target="_blank">A와 B 2</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> 	|
| 	2	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/1548" target="_blank">부분 삼각 수열</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> 	|
| 	3	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/1025" target="_blank">제곱수 찾기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> 	|
| 	4	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/15686" target="_blank">치킨 배달</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> 	|
| 	5	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/21278" target="_blank">호석이 두 마리 치킨</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> 	|
| 	6	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/21315" target="_blank">카드 섞기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> 	|
| 	7	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/14500" target="_blank">테트로미노</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> 	|
| 	8	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/16637" target="_blank">괄호 추가하기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> 	|
| 	9	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/14391" target="_blank">종이 조각</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> 	|
| 	10	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/18808" target="_blank">스티커 붙이기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> 	|
| 	11	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/22944" target="_blank">죽음의 비</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> 	|
| 	12	 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/21943" target="_blank">연산 최대로</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/2798" target="_blank">블랙잭</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/2231" target="_blank">분해합</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/19532" target="_blank">수학은 비대면강의입니다</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/18312" target="_blank">시각</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/22864" target="_blank">피로도</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/15721" target="_blank">번데기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/18511" target="_blank">큰 수 구성하기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/1969" target="_blank">DNA</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/2422" target="_blank">한윤정이 이탈리아에 가서 아이스크림을 사먹는데</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/5568" target="_blank">카드 놓기</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/16439" target="_blank">치킨치킨치킨</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/2503" target="_blank">숫자 야구</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/17626" target="_blank">Four Squares</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/14501" target="_blank">퇴사</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/16937" target="_blank">두 스티커</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/16508" target="_blank">전공책</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/9079" target="_blank">동전 게임</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/14620" target="_blank">꽃길</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/2961" target="_blank">도영이가 만든 맛있는 음식</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/2615" target="_blank">오목</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> 	|
| 		 |	  ![status][ToDo]  	|	 <a href="https://www.acmicpc.net/problem/15661" target="_blank">링크와 스타트</a> 	|	 <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> 	|


[TODO]: https://img.shields.io/badge/-TODO-DFFD26
[DOING]: https://img.shields.io/badge/-DOING-31AE0F
[DONE]: https://img.shields.io/badge/-DONE-0885CC
