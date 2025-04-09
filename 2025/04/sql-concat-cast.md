# SQL 공부 : 프로그래머스 문제풀이 (잡은 물고기 중 가장 큰 물고기의 길이 구하기) CONCAT , CAST
**Posted on**: 2024-09-13

<p>문제 링크</p>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/298515" rel="noopener&nbsp;noreferrer" target="_blank">https://school.programmers.co.kr/learn/courses/30/lessons/298515</a></p>
<figure contenteditable="false" id="og_1726193113633"><a href="https://school.programmers.co.kr/learn/courses/30/lessons/298515" rel="noopener" target="_blank">
<div class="og-image">&nbsp;</div>
<div class="og-text">
<p class="og-title">프로그래머스</p>
<p class="og-desc">코드 중심의 개발자 채용. 스택 기반의 포지션 매칭. 프로그래머스의 개발자 맞춤형 프로필을 등록하고, 나와 기술 궁합이 잘 맞는 기업들을 매칭 받으세요.</p>
<p class="og-host">programmers.co.kr</p>
</div>
</a></figure>
<p>&nbsp;</p>
<p><b>KEY POINT</b></p>
<ul>
<li>MAX
<ul>
<li>가장 큰 길이 확인</li>
</ul>
</li>
<li>CONCAT
<ul>
<li>문자열 합치기!</li>
</ul>
</li>
</ul>
<pre class="sql" id="code_1726193182759"><code>SELECT CONCAT('Hello, ', 'World!') AS Greeting;</code></pre>
<p>&nbsp;</p>
<ul>
<li>CAST
<ul>
<li>타입 변환</li>
</ul>
</li>
</ul>
<pre class="sql" id="code_1726193250897"><code>CAST(expression AS target_data_type)</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<div>
<div>
<h3>CONCAT과 CAST 설명</h3>
<ul>
<li><b>CONCAT 함수</b>는 여러 문자열을 결합하여 하나의 문자열을 생성합니다.</li>
<li><b>CAST 함수</b>는 데이터 타입을 다른 타입으로 변환합니다.</li>
</ul>
<h4>간단한 예시</h4>



    
    
    SQL Functions: CONCAT and CAST
    


    <h1>SQL Functions: CONCAT and CAST</h1>
    
    <div class="example">
        <h2>1. CONCAT Function</h2>
        <p>The <code>CONCAT</code> function combines multiple strings into a single string.</p>
        <pre><code>SELECT CONCAT('Hello, ', 'World!') AS Greeting;
-- Result: Hello, World!
        </code></pre>
    </div>

    <div class="example">
        <h2>2. CAST Function</h2>
        <p>The <code>CAST</code> function converts a value from one data type to another.</p>
        <pre><code>SELECT CAST(123 AS VARCHAR(10)) AS NumberAsString;
-- Result: 123
        </code></pre>
    </div>

    <div class="example">
        <h2>3. Using CONCAT and CAST Together</h2>
        <p>Combine a number (converted to a string) with another string using <code>CONCAT</code> and <code>CAST</code>.</p>
        <pre><code>SELECT CONCAT('The total is ', CAST(SUM(Price) AS VARCHAR(10))) AS Total
FROM Sales;
-- Example Result: The total is 1500
        </code></pre>
    </div>



</div>
</div>
<p>&nbsp;</p>
<div>
<div>&nbsp;</div>
</div>
<p>&nbsp;</p>