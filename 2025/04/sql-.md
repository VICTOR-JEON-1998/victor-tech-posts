# SQL 문제 풀이 : 프로그래머스 (잡은 물고기의 평균 길이 구하기)
**Posted on**: 2024-09-19

SQL 문제 정리
    



<h1>SQL 문제 정리</h1>

<h2>문제 링크</h2>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/293259">문제 링크</a></p>

<h2>문제 포인트</h2>
<ol>
    <li><strong>반올림:</strong> <code>ROUND</code>를 사용할 수 있으며, <code>ROUND(대상, 2)</code>는 대상에 대해 소수점 둘째 자리로 반올림합니다 (셋째 자리에서 반올림을 수행).</li>
    <li><strong>CASE문 활용:</strong> CASE문의 위치에 대해서 어려움을 느끼는 중입니다.</li>
</ol>

<h2>문제 설명</h2>
<p>문제를 보면 길이 평균을 구해야 하는데, 길이가 NULL인 대상들에 대해서는 10으로 길이를 치환한 후 그에 따른 평균을 구해야 합니다. 여기서 <code>CASE</code>문은 <code>AVG</code> 문 안에서 사용되었습니다.</p>

<h2>내가 쓴 코드</h2>
<pre>
SELECT 
    ROUND(AVG(CASE 
            WHEN LENGTH IS NULL THEN 10
            ELSE LENGTH
        END), 2) AS AVERAGE_LENGTH
FROM FISH_INFO;
</pre>

<h2>주요 포인트</h2>
<p>CASE문의 끝은 <code>END</code>가 따르며, 조건문이기 때문에 해당되지 않는 조건들에 대해서는 <code>ELSE</code> 처리를 해줘야 함을 잊지 말아야 합니다.</p>