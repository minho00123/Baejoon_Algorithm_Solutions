# [Bronze III] 자전거 속도 - 2765 

[문제 링크](https://www.acmicpc.net/problem/2765) 

### 성능 요약

메모리: 31256 KB, 시간: 48 ms

### 분류

사칙연산, 수학

### 문제 설명

<p>Most bicycle speedometers work by using a Hall Effect sensor fastened to the front fork of the bicycle. A magnet is attached to one of the spokes on the front wheel so that it will line up with the Hall Effect switch once per revolution of the wheel. The speedometer monitors the sensor to count wheel revolutions. If the diameter of the wheel is known, the distance traveled can be easily be calculated if you know how many revolutions the wheel has made. In addition, if the time it takes to complete the revolutions is known, the average speed can also be calculated.</p>

<p>For this problem, you will write a program to determine the total distance traveled (in miles) and the average speed (in Miles Per Hour) given the wheel diameter, the number of revolutions and the total time of the trip. You can assume that the front wheel never leaves the ground, and there is no slipping or skidding.</p>

### 입력 

 <p>Input consists of multiple datasets, one per line, of the form:</p>

<p>diameter revolutions time</p>

<p>The diameter is expressed in inches as a floating point value. The revolutions is an integer value. The time is expressed in seconds as a floating point value. Input ends when the value of revolutions is 0 (zero).</p>

### 출력 

 <p>For each data set, print:</p>

<p>Trip #N: distance MPH</p>

<p>Of course N should be replaced by the data set number, distance by the total distance in miles (accurate to 2 decimal places) and MPH by the speed in miles per hour (accurate to 2 decimal places). Your program should not generate any output for the ending case when revolutions is 0.</p>

