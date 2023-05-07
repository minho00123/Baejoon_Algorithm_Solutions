# [Bronze III] 생장점 - 1703 

[문제 링크](https://www.acmicpc.net/problem/1703) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>The branchorama tree grows in an extraordinarily regular way. A juvenile specimen is a slender sapling topped by a growth tip with a single leaf. During each growing season, each of the tree’s growth tips splits into a number of branches and by the end of the season each of those branches is topped by a fully-formed growth tip and its leaf. Remarkably, every growth tip on a tree splits into the same number of branches, though this number can vary from year to year.</p>

<p>For example, here are the juvenile form and the results of the first three years of growth for one of the trees in Farmer Brown’s orchard:</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/1703/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-12%20%EC%98%A4%EC%A0%84%208.31.45.png" style="height:204px; width:550px"></p>

<p>As you might imagine, branchorama trees have a tendency to overcrowd themselves. So each winter Farmer Brown takes a saw out to the orchard and lops a few branches off the most overgrown trees. Here’s what our specimen tree and its neighbour looked like at the end of one year’s pruning session:</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/1703/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-12%20%EC%98%A4%EC%A0%84%208.31.53.png" style="height:215px; width:500px"></p>

<p>Though the leaves are large and very efficient at photosynthesis, they are found only at the intact growth tips at the ends of a tree’s smallest branches. So it is important not to prune a tree so heavily that it is left without enough leaves to sustain itself.</p>

<p>Farmer Brown would like to know how many leaves each tree has, but considers it tedious to count the leaves themselves. It is more interesting to count the branch ‘splitting factor’ at each level of a tree and the total number of branches that have been pruned at each level, and calculate from this data the number of remaining growth tips and, hence, leaves.</p>

<p>The fieldwork has already been done by Farmer Brown, and you are to write a program to do this calculation on the data gathered.</p>

### 입력 

 <p>Input consists of one line for each tree, terminated by a line containing only ‘0’. Each tree line contains an integer, a, which is the tree’s age (1 ≤ a ≤ 20), followed by 2a other integers, all separated by spaces. From left to right, these integers are the splitting factor and pruning count for the tree’s lowest level (i.e., the tree’s first year of growth), followed by the splitting factor and pruning count for the second level, and so on.</p>

### 출력 

 <p>For each tree, output a line giving the number of leaves on the tree.</p>

<p>You may assume that the tree’s leaf count and the leaf count of a similarly shaped tree that has never been pruned both fit in a standard signed 32-bit integer.</p>

