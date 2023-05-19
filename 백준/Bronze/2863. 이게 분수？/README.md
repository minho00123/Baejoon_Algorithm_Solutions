# [Bronze III] 이게 분수? - 2863 

[문제 링크](https://www.acmicpc.net/problem/2863) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>Perica was always very good at math. His only weak points were addition and division. To help him with that, his teacher presented him with the following problem. </p>

<p>She gave him a 2 by 2 table, containing positive integers A, B, C and D. </p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/frac1(1).png" style="height:105px; width:128px"></p>

<p>We say that the value of a table is equal to: </p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 111.4%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mfrac space="3"><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mfrac><mi>A</mi><mi>C</mi></mfrac><mo>+</mo><mfrac><mi>B</mi><mi>D</mi></mfrac></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[\frac{A}{C}+\frac{B}{D}\]</span> </mjx-container></p>

<p>Perica’s task is to find the minimum number of 90 degrees clockwise rotations required to maximize the value of a given table. </p>

<p>Result of a single clockwise rotation is shown below.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/frac2(1).png" style="height:130px; width:323px"></p>

### 입력 

 <p>The first line of input contains two space separated integers, A and B. </p>

<p>The second line of input contains two space separated integers, C and D. </p>

<p>All integers are positive and not greater than 100. </p>

### 출력 

 <p>The first and only line of output must contain a single integer, minimum number of clockwise rotations required to maximize the table’s value.</p>

