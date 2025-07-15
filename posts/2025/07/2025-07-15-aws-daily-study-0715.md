# [aws daily study] 0715
**Posted on**: 2025-07-15

<blockquote>
<p>Route 53 관련</p>
</blockquote>
<p>모든 VPN에서 DNS 해석 &rArr; Private Host Zone 연결</p>
<p>Route 53 Resolver Inbound Endpoint ?</p>
<p>온프레미스 &rArr; AWS로 DNS 질의 보낼 수 있게 해주는 서비스</p>
<ul>
<li>온프레미스 DNS가 VPC 내부의 Route 53 Private DNS 를 질의할 수 있게 해주는 진입점</li>
<li>VPC에 Rout53 Resolver Inbound Endpoint 생성
<ul>
<li>내부 IP가 부여됨</li>
</ul>
</li>
<li>온프레미스 DNS 서버에 조건부 포워딩 설정
<ul>
<li>도메인 질의 시, 위 인바운드 IP로 포워딩</li>
</ul>
</li>
</ul>
<blockquote>
<p>리전 장애 대응</p>
</blockquote>
<p>API Gateway와 Lambda 는 리전 단위 서비스이다.</p>
<blockquote>
<p>계정관리</p>
</blockquote>
<p>AWS Organizations</p>
<ul>
<li>계정들을 OU로 그룹화 가능</li>
</ul>
<p>SCP</p>
<ul>
<li>SCP가 제일 최상위 규칙</li>
<li>조직 내 계정 / OU가 어떤 서비스 / 액션을 사용할 수 있는지를 제한하는 정책</li>
<li>Root, OU, Account 레벨에 적용 가능</li>
</ul>
<blockquote>
<p>Load Balancing</p>
</blockquote>
<ul>
<li>NLB는 TCP 기반으로, HTTP 세션 관리 기능이 부족하다.</li>
<li>ALB는 HTTP 기반 세션 스티키 가능 &rArr; 트래픽 분산 및 사용자 경험 유지에 적합함</li>
</ul>
<blockquote>
<p>CloudFront</p>
</blockquote>
<p>전세계에 제공할 서비스,. 엣지 기준으로 빠른서비스 동작.</p>
<p>CloudFront Function VS Lambda Edge</p>
<p>CloudFront Function이 더 가볍고 빠르다</p>
<blockquote>
<p>EKS는 강력하지만 ECS보다 운영 복잡도가 크다.</p>
</blockquote>