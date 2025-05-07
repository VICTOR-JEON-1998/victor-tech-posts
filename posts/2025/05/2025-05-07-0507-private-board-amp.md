# [작업일지] 0507  Private Board 이모지 리액션 기능 디버깅 &amp; 개선 작업 기록
**Posted on**: 2025-05-07

<h3>1️⃣ <b>PostgreSQL Docker 컨테이너 실행</b></h3>
<ul>
<li>문제: docker ps 명령어가 작동하지 않음 (permission denied)</li>
<li>해결:
<ul>
<li>sudo usermod -aG docker $USER &rarr; 이후 newgrp docker로 권한 부여</li>
<li>docker run 명령어로 PostgreSQL 컨테이너 수동 실행<br />✅ DB 정상 실행 확인</li>
</ul>
</li>
</ul>
<hr />
<h3>2️⃣ <b>Prisma 마이그레이션 적용</b></h3>
<ul>
<li>문제: User 테이블이 존재하지 않아 Prisma가 작동하지 않음</li>
<li>해결:
<ul>
<li>npx prisma migrate dev --name init 수행</li>
<li>schema.prisma 기반 테이블 생성 완료<br />✅ Prisma 연결 정상화</li>
</ul>
</li>
</ul>
<hr />
<h3>3️⃣ <b>이모지 리액션 기능 오류 디버깅</b></h3>
<ul>
<li>초기 문제: Flutter에서 이모지를 눌러도 count 변동 없음</li>
<li>백엔드 로그 확인 결과:
<ul>
<li>500 에러 &rarr; emojiKey가 없는 경우</li>
<li>400 에러 &rarr; 필드 누락</li>
<li>userId가 undefined로 찍힘</li>
</ul>
</li>
</ul>
<hr />
<h3>4️⃣ <b>Flutter 요청 파라미터 오류 수정</b></h3>
<ul>
<li>문제: 프론트에서 emojiKey 대신 emoji를 보냄</li>
<li>해결: data: {'emojiKey': emojiKey}로 수정<br />✅ 백엔드에서 기대한 필드명과 일치시킴</li>
</ul>
<hr />
<h3>5️⃣ <b>백엔드 핸들러 오류 수정</b></h3>
<ul>
<li>문제: return 문이 함수 바깥에 있어 SyntaxError 발생</li>
<li>해결: handler() 함수 안으로 옮김</li>
</ul>
<hr />
<h3>6️⃣ <b>emojiKey &rarr; 이모지 매핑 객체 누락</b></h3>
<ul>
<li>문제: emojiKeyToEmoji is not defined 에러 발생</li>
<li>해결: 아래 객체 정의 추가</li>
</ul>
<div>
<div><span><span><span>const</span></span><span> emojiKeyToEmoji = { </span><span><span>like</span></span><span>: </span><span><span>' '</span></span><span>, </span><span><span>laugh</span></span><span>: </span><span><span>' '</span></span><span>, </span><span><span>wow</span></span><span>: </span><span><span>' '</span></span><span>, }; </span></span></div>
</div>
<p>&nbsp;</p>
<hr />
<h3>7️⃣ <b>Prisma .create() 구문 오류</b></h3>
<ul>
<li>문제: userId: user.id, { 오타로 인해 Prisma가 user 필드를 요구함</li>
<li>해결: 중괄호 오타 제거 &rarr; 정상 작동 형태로 수정</li>
</ul>
<hr />
<h3>8️⃣ <b>남은 문제</b></h3>
<ul>
<li>user.id가 undefined로 남아 있음</li>
<li>원인 의심:
<ul>
<li>verifyToken(token)이 id 없이 { email: ... }만 반환</li>
<li>JWT 생성 시 payload에 id가 누락된 구조일 가능성</li>
</ul>
</li>
<li>해결 예정:
<ul>
<li>verifyToken() 디코딩 결과 확인 필요</li>
<li>로그인 시 jwt.sign({ id, email }, ...) 확인 필요</li>
</ul>
</li>
</ul>