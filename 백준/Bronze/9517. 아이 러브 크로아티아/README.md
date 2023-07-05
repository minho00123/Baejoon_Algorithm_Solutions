# [Bronze III] 아이 러브 크로아티아 - 9517 

[문제 링크](https://www.acmicpc.net/problem/9517) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>Croatia's national television programme is broadcasting an entertainment show titled "I Love Croatia", modeled on the licensed format I love my country. In this show two teams of celebrities and public figures play various games which require knowledge about Croatia. One of the games is Happy Birthday, which will be used in this task, although somewhat altered. </p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/croatia.png" style="float:right; height:96px; width:100px">Eight players numbered one through eight are seated in a circle (see picture). One of them is holding a box which will explode after 3 minutes and 30 seconds from the beginning of the game when some colorful confetti will be blown out. The game begins with a question to the player holding the box. If the players answers incorrectly or skips the question, he is immediately given the next question. If the player answers correctly, he passes the box to the first player seated on his left and then that player gets the next question. </p>

<p>You are given the numbered label of the player who has the box in the beginning and the outcomes of the first N questions asked. Determine the numbered label of the player who had the box when it finally exploded. The question outcome is described with the following data - time passed from the beginning of the question being asked to the moment an answer was given and whether the answer was true ("T"), false ("N") or skipped ("P"). The time between giving the answer and asking the next question shouldn't be taken into consideration, as well as time necessary for the box to be passed to the next player. The box will surely explode on a player's turn. </p>

### 입력 

 <p>The first line of input contains a positive integer K (1 ≤ K ≤ 8), the numbered label of the player who has the box initially. </p>

<p>The second line of input contains a positive integer N (1 ≤ N ≤ 100), the number of questions asked during the game. </p>

<p>Each of the following N lines contains a positive integer T (1 ≤ T ≤ 100), time passed from the beginning of the ith question being asked to the moment an answer was given, measured in seconds, and a single character Z ('T', 'N' or 'P'), the type of answer given. </p>

### 출력 

 <p>The first and only line of output must contain the numbered label of the player who had the box when it finally exploded. </p>

