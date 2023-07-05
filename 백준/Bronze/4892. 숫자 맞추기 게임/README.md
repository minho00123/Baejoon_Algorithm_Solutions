# [Bronze III] 숫자 맞추기 게임 - 4892 

[문제 링크](https://www.acmicpc.net/problem/4892) 

### 성능 요약

메모리: 31256 KB, 시간: 64 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>Number guessing is a popular game between elementary-school kids. Teachers encourage pupils to play the game as it enhances their arithmetic skills, logical thinking, and following-up simple procedures. We think that, most probably, you too will master in few minutes. Here’s one example of how you too can play this game: Ask a friend to think of a number, let’s call it n<sub>0</sub>. Then:</p>

<ol>
	<li>Ask your friend to compute n<sub>1</sub> = 3 * n<sub>0</sub> and to tell you if n<sub>1</sub> is even or odd</li>
	<li>If n<sub>1</sub> is even, ask your friend to compute n<sub>2</sub> = n<sub>1</sub>/2. If, otherwise, n<sub>1</sub> was odd then let your friend compute n<sub>2</sub> = (n<sub>1</sub> + 1)/2.</li>
	<li>Now ask your friend to calculate n<sub>3</sub> = 3 * n<sub>2</sub>.</li>
	<li>Ask your friend to tell tell you the result of n<sub>4</sub> = n<sub>3</sub>/9. (n<sub>4</sub> is the quotient of the division operation. In computer lingo, ’/’ is the integer-division operator.)</li>
	<li>Now you can simply reveal the original number by calculating n<sub>0</sub> = 2 * n<sub>4</sub> if n<sub>1</sub> was even, or n<sub>0</sub> = 2 * n<sub>4</sub> + 1 otherwise.</li>
</ol>

<p>Here’s an example that you can follow: If n<sub>0</sub> = 37, then n<sub>1</sub> = 111 which is odd. Now we can calculate n<sub>2</sub> = 56, n<sub>3</sub> = 168, and n<sub>4</sub> = 18, which is what your friend will tell you. Doing the calculation 2 × n<sub>4</sub> + 1 = 37 reveals n<sub>0</sub>.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. Each test case is made of a single positive number (0 < n<sub>0</sub> < 1, 000, 000).</p>

<p>The last line of the input ﬁle has a single zero (which is not part of the test cases.)</p>

### 출력 

 <p>For each test case, print the following line:</p>

<pre>k. B Q</pre>

<p>Where k is the test case number (starting at one,) B is either ’even’ or ’odd’ (without the quotes) depending on your friend’s answer in step 1. Q is your friend’s answer to step 4.</p>

