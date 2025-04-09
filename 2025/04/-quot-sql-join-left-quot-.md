# &quot;SQL 마스터하기: JOIN으로 데이터 합치기와 LEFT로 문자열 자르기&quot;
**Posted on**: 2024-09-20

SQL JOIN 및 LEFT 함수 설명
    



<h1>SQL JOIN 및 LEFT 함수 설명</h1>
<p>SQL에서 두 테이블 중에서 조건에 맞는 행들만을 뽑아서 합치는 함수가 있다. 그것이 바로 JOIN이다.</p>

<p>JOIN은 SQL에서 두 개 이상의 테이블을 결합하여 데이터를 조회하는 데 사용됩니다. 다음은 다양한 JOIN 유형과 그 사용법을 예시와 함께 상세히 설명하겠습니다.</p>

<h2>1. INNER JOIN</h2>
<strong>정의:</strong> INNER JOIN은 두 테이블에서 조건을 만족하는 행만 반환합니다. 즉, 두 테이블 모두에 존재하는 데이터만 포함됩니다.

<h3>예시:</h3>
<p>두 개의 테이블이 있습니다.</p>

<strong>employees</strong>
<table>
    <tr>
        <th>id</th>
        <th>name</th>
        <th>department_id</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Alice</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Bob</td>
        <td>2</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Charlie</td>
        <td>NULL</td>
    </tr>
</table>

<strong>departments</strong>
<table>
    <tr>
        <th>id</th>
        <th>department_name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>2</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Sales</td>
    </tr>
</table>

<strong>쿼리:</strong>
<pre><code>SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>name</th>
        <th>department_name</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>IT</td>
    </tr>
</table>

<strong>설명:</strong> Alice와 Bob은 각각 HR과 IT 부서에 속해 있으므로 두 행이 반환됩니다. Charlie는 부서가 NULL이기 때문에 결과에 포함되지 않습니다.

<hr />

<h2>2. LEFT JOIN</h2>
<strong>정의:</strong> LEFT JOIN은 왼쪽 테이블의 모든 행을 반환하고, 오른쪽 테이블의 조건에 맞는 행이 없으면 NULL을 반환합니다.

<strong>쿼리:</strong>
<pre><code>SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>name</th>
        <th>department_name</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>NULL</td>
    </tr>
</table>

<strong>설명:</strong> LEFT JOIN은 employees 테이블의 모든 행을 포함합니다. Charlie는 부서가 없으므로 department_name이 NULL입니다.

<hr />

<h2>3. RIGHT JOIN</h2>
<strong>정의:</strong> RIGHT JOIN은 오른쪽 테이블의 모든 행을 반환하고, 왼쪽 테이블의 조건에 맞는 행이 없으면 NULL을 반환합니다.

<strong>쿼리:</strong>
<pre><code>SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>name</th>
        <th>department_name</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Sales</td>
    </tr>
</table>

<strong>설명:</strong> RIGHT JOIN은 departments 테이블의 모든 행을 포함합니다. Sales 부서에는 직원이 없으므로 name은 NULL입니다.

<hr />

<h2>4. FULL OUTER JOIN</h2>
<strong>정의:</strong> FULL OUTER JOIN은 두 테이블의 모든 행을 반환하며, 조건에 맞지 않는 경우 NULL로 표시합니다.

<strong>쿼리:</strong>
<pre><code>SELECT employees.name, departments.department_name
FROM employees
FULL OUTER JOIN departments ON employees.department_id = departments.id;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>name</th>
        <th>department_name</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Sales</td>
    </tr>
</table>

<strong>설명:</strong> FULL OUTER JOIN은 employees와 departments 두 테이블의 모든 행을 반환합니다. Charlie는 부서가 없어서 NULL이고, Sales 부서는 직원이 없어서 name이 NULL입니다.

<hr />

<h2>5. CROSS JOIN</h2>
<strong>정의:</strong> CROSS JOIN은 두 테이블의 데카르트 곱을 반환합니다. 즉, 각 행이 다른 테이블의 모든 행과 결합됩니다.

<strong>쿼리:</strong>
<pre><code>SELECT employees.name, departments.department_name
FROM employees
CROSS JOIN departments;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>name</th>
        <th>department_name</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Alice</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>Alice</td>
        <td>Sales</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>Sales</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>Sales</td>
    </tr>
</table>

<strong>설명:</strong> 각 직원은 모든 부서와 조합되므로, 총 9개의 행이 반환됩니다.

<hr />

<h2>요약</h2>
<ul>
    <li><strong>INNER JOIN:</strong> 두 테이블의 공통된 데이터만 반환.</li>
    <li><strong>LEFT JOIN:</strong> 왼쪽 테이블의 모든 데이터와 오른쪽 테이블의 일치하는 데이터.</li>
    <li><strong>RIGHT
    <li><strong>RIGHT JOIN:</strong> 오른쪽 테이블의 모든 데이터와 왼쪽 테이블의 일치하는 데이터.</li>
    <li><strong>FULL OUTER JOIN:</strong> 두 테이블의 모든 데이터.</li>
    <li><strong>CROSS JOIN:</strong> 모든 조합을 반환하는 데카르트 곱.</li>
</ul>

<p>이 중에서도 INNER JOIN이 실무에서 가장 자주 쓰인다. 나머지는 파악만 해두고 필요할 때 찾아서 사용하면 좋을 것 같다.</p>

<hr />

<h2>문자열을 자르는 방법</h2>
<p>문자열을 자르는 방법이 있다. SUBSTRING 등 여러 방법이 있지만 LEFT만 알아도 편리하게 쓸 수 있다. 응용으로 RIGHT까지 사용할 수 있을 것이다.</p>

<h3>LEFT() 함수 설명</h3>
<p><code>LEFT()</code> 함수는 SQL에서 문자열의 왼쪽에서부터 지정한 길이만큼의 문자를 반환합니다.</p>

<strong>구문:</strong> <code>LEFT(string, length)</code><br />
- <strong>string:</strong> 자르고자 하는 문자열<br />
- <strong>length:</strong> 반환할 문자의 수

<h3>예시 1: 직원 이름 자르기</h3>

<strong>테이블 구조</strong>
1. <strong>employees</strong>
<table>
    <tr>
        <th>id</th>
        <th>name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Alice Johnson</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Bob Smith</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Charlie Brown</td>
    </tr>
</table>

<strong>LEFT() 쿼리:</strong>
<pre><code>SELECT id, LEFT(name, 5) AS short_name
FROM employees;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>id</th>
        <th>short_name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Alice</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Bob S</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Char</td>
    </tr>
</table>

<strong>설명:</strong> <code>LEFT(name, 5)</code>는 각 이름의 왼쪽에서 5글자를 반환합니다. Alice의 경우 "Alice", Bob의 경우 "Bob S", Charlie는 "Char"로 잘립니다.

<hr />

<h3>예시 2: 상품 코드 자르기</h3>

<strong>테이블 구조</strong>
1. <strong>products</strong>
<table>
    <tr>
        <th>id</th>
        <th>product_code</th>
    </tr>
    <tr>
        <td>1</td>
        <td>P12345</td>
    </tr>
    <tr>
        <td>2</td>
        <td>A98765</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Z54321</td>
    </tr>
</table>

<strong>LEFT() 쿼리:</strong>
<pre><code>SELECT id, LEFT(product_code, 1) AS code_prefix
FROM products;</code></pre>

<strong>결과:</strong>
<table>
    <tr>
        <th>id</th>
        <th>code_prefix</th>
    </tr>
    <tr>
        <td>1</td>
        <td>P</td>
    </tr>
    <tr>
        <td>2</td>
        <td>A</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Z</td>
    </tr>
</table>

<strong>설명:</strong> <code>LEFT(product_code, 1)</code>는 각 상품 코드의 첫 번째 문자를 반환합니다. P12345에서 "P", A98765에서 "A", Z54321에서 "Z"가 반환됩니다.

<hr />

<h2>요약</h2>
<ul>
    <li><code>LEFT()</code> 함수는 문자열의 왼쪽에서부터 지정한 수만큼 문자를 잘라서 반환합니다.</li>
    <li>이를 통해 문자열의 특정 부분을 쉽게 추출할 수 있습니다.</li>
</ul>

<h3>응용할 수 있는 문제</h3>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/164673">여기</a>에서 문제를 확인할 수 있습니다.</p>

<h3>나의 풀이 공개</h3>
<pre><code>SELECT 
USED_GOODS_BOARD.TITLE, USED_GOODS_BOARD.BOARD_ID, 
USED_GOODS_REPLY.REPLY_ID, USED_GOODS_REPLY.WRITER_ID, USED_GOODS_REPLY.CONTENTS, LEFT(USED_GOODS_REPLY.CREATED_DATE,10) AS CREATED_DATE
FROM USED_GOODS_BOARD
INNER JOIN USED_GOODS_REPLY ON (USED_GOODS_BOARD.BOARD_ID = USED_GOODS_REPLY.BOARD_ID 
and USED_GOODS_BOARD.CREATED_DATE LIKE "2022-10%")
ORDER BY USED_GOODS_REPLY.CREATED_DATE, USED_GOODS_BOARD.TITLE</code></pre>