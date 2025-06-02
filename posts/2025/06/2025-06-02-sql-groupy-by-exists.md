# [SQL] 문제 풀이 성능 개선 (GROUPY BY / EXISTS)
**Posted on**: 2025-06-02

<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/131536" rel="noopener&nbsp;noreferrer" target="_blank">https://school.programmers.co.kr/learn/courses/30/lessons/131536</a></p>
<figure contenteditable="false" id="og_1748837483618"><a href="https://school.programmers.co.kr/learn/courses/30/lessons/131536" rel="noopener" target="_blank">
<div class="og-image">&nbsp;</div>
<div class="og-text">
<p class="og-title">프로그래머스</p>
<p class="og-desc">SW개발자를 위한 평가, 교육의 Total Solution을 제공하는 개발자 성장을 위한 베이스캠프</p>
<p class="og-host">programmers.co.kr</p>
</div>
</a></figure>
<p>&nbsp;</p>
<p>성능 개선 전 나의 풀이</p>
<pre class="sql" id="code_1748837497263"><code>SELECT
    USER_ID,
    PRODUCT_ID
FROM (
    SELECT
    USER_ID,
    PRODUCT_ID,
    COUNT(*) AS cnt
    FROM
        ONLINE_SALE
    GROUP BY
        USER_ID,
        PRODUCT_ID
    HAVING
        cnt &gt; 1
) AS sub 
ORDER BY USER_ID ASC, PRODUCT_ID DESC</code></pre>
<p>&nbsp;</p>
<p>위처럼 하나의 테이블을 별개로 만든 뒤에 그 안에서 필요한 컬럼들을 뽑는 형태로 쿼리를 구성하였지만</p>
<p>그럴 필요가 없었다.</p>
<p>&nbsp;</p>
<p>아래처럼 바로 쓸 수 있다.</p>
<pre class="sql" id="code_1748837699215"><code>SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) &gt; 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC</code></pre>
<p>&nbsp;</p>
<p>하지만 이것의 성능을 더 높일 방법이 있다.</p>
<p>EXISTS 를 사용하면 된다.</p>
<p>&nbsp;</p>
<p>테이블이 수십만 건 이상이고, 중복 여부만 판단하고 중복 개수 자체는 필요 없다면 EXISTS를 사용하는 것이 낫다.</p>
<p>(중복의 정확한 개수가 필요할 때는 COUNT/GROUP BY가 더 낫다)</p>
<pre class="sql" id="code_1748839459542"><code>SELECT DISTINCT A.USER_ID, A.PRODUCT_ID
FROM ONLINE_SALE A
WHERE EXISTS (
  SELECT 1 #보통 관례적으로 쓰임
  FROM ONLINE_SALE B # 동일한 데이터의 다른 테이블
  WHERE A.USER_ID = B.USER_ID #user_id가 같고
    AND A.PRODUCT_ID = B.PRODUCT_ID # product_id가 같지만
    AND A.ONLINE_SALE_ID &lt;&gt; B.ONLINE_SALE_ID # idx가 다른 것들을 골라낸다는 의미. &lt;&gt;는 같지 않다는 뜻! 
)</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p style="text-align: center;"><b>EXISTS가 더 빠른 이유는 뭘까?</b></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">1. 조건 만족시 즉시 종료</p>
<p style="text-align: left;">2. 불필요한 정렬/집계 연산이 없음</p>
<p style="text-align: left;">3. 존재만 판단함 빠르게</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>