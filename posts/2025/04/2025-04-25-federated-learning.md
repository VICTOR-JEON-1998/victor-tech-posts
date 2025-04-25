# Federated Learning이란?
**Posted on**: 2025-04-25

<h2>Federated Learning이란?</h2>
<p>Federated Learning(FL, 연합 학습)은 <b>데이터를 중앙 서버에 모으지 않고</b> 각 기기나 조직이 <b>자신의 데이터를 로컬에서 학습</b>하고, <b>모델의 파라미터만 중앙 서버와 공유</b>하는 <b>분산형 머신러닝 프레임워크</b>입니다.</p>
<p>이는 특히 다음과 같은 환경에서 각광받고 있습니다:</p>
<ul>
<li><b>개인정보 보호가 중요한 의료, 금융 분야</b></li>
<li><b>IoT 장치 및 엣지 컴퓨팅 환경</b></li>
<li><b>규제가 엄격한 조직 간 협업 시나리오</b></li>
</ul>
<h3>  FL의 핵심 장점:</h3>
<ul>
<li>데이터 유출 위험 &darr;</li>
<li>개인정보보호법(GDPR 등) 준수 &uarr;</li>
<li>중앙 장애점(SPOF) 제거</li>
</ul>
<p>예를 들어, 병원 A, B, C가 각자의 환자 데이터를 활용해 <b>AI 기반 암 진단 모델을 공동 학습</b>하면서도, <b>환자 데이터는 병원 밖으로 절대 나가지 않는</b> 구조가 가능합니다.</p>
<p>&nbsp;</p>
<h2>  원리: Federated Learning은 어떻게 작동하는가?</h2>
<h3> ️ 기본 흐름</h3>
<ol>
<li><b>초기 모델 배포</b>: 중앙 서버가 공통의 초기 모델을 여러 클라이언트(병원, 모바일, IoT 장치 등)에 배포</li>
<li><b>로컬 학습</b>: 각 클라이언트는 자기 데이터만을 이용해 모델을 학습</li>
<li><span style="color: #ee2323;"><b>모델 파라미터 전송: 학습 결과인 파라미터(가중치)를 중앙 서버에 전송 &lt;- 제일 중요한 원리라고 생각함!</b></span></li>
<li><b>파라미터 집계</b>: 중앙 서버는 Federated Averaging 알고리즘 등을 통해 모든 파라미터를 평균내거나 최적화</li>
<li><b>업데이트된 모델 재배포</b>: 개선된 공통 모델을 다시 각 클라이언트에 배포 &rarr; 반복</li>
</ol>
<p>  데이터는 <b>절대 이동하지 않고</b>, <b>모델만 이동</b>함으로써 프라이버시를 보장합니다.</p>
<p>&nbsp;</p>
<h2>  보안 및 프라이버시 보호 메커니즘</h2>
<h3>  1. Differential Privacy (DP)</h3>
<ul>
<li>클라이언트가 서버에 파라미터를 전송할 때 <b>임의의 노이즈를 추가</b>하여 데이터 유추를 방지</li>
<li>예: Apple의 iOS 키보드 자동완성은 FL + DP 적용 사례</li>
</ul>
<h3>  2. Secure Aggregation</h3>
<ul>
<li>서버조차도 개별 클라이언트의 모델 업데이트를 <b>복호화 없이 집계</b>할 수 있도록 설계</li>
<li>각 클라이언트는 암호화된 모델을 공유하고, 서버는 이를 <b>동형암호</b>나 <b>멀티 파티 계산(MPC)</b> 기법으로 집계</li>
</ul>
<h2>  실전 적용 사례</h2>
<div><span></span>
<div>산업적용 사례
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td><b>모바일</b></td>
<td>Google Gboard 키보드 입력 추천 &rarr; 수억 개 디바이스에서 로컬 학습</td>
</tr>
<tr>
<td><b>헬스케어</b></td>
<td>여러 병원이 공통 진단 모델 개발에 참여 &rarr; 데이터는 병원 외부 유출 없음</td>
</tr>
<tr>
<td><b>금융</b></td>
<td>카드사 간 사기 탐지 모델 공유 &rarr; 각사 고객 정보 노출 없이 고도화된 AI 구축</td>
</tr>
</tbody>
</table>
</div>
</div>
<pre id="code_1745569619072" style="background-color: #f8f8f8; color: #383a42; text-align: start;"><code>sequenceDiagram
    participant Server
    participant ClientA
    participant ClientB
    Server-&gt;&gt;ClientA: 모델 초기값 배포
    Server-&gt;&gt;ClientB: 모델 초기값 배포
    ClientA-&gt;&gt;ClientA: 로컬 데이터로 학습
    ClientB-&gt;&gt;ClientB: 로컬 데이터로 학습
    ClientA--&gt;&gt;Server: 파라미터 전송 (DP 적용)
    ClientB--&gt;&gt;Server: 파라미터 전송 (DP 적용)
    Server-&gt;&gt;Server: Federated Averaging
    Server-&gt;&gt;ClientA: 업데이트된 모델 재배포
    Server-&gt;&gt;ClientB: 업데이트된 모델 재배포</code></pre>
<p>&nbsp;</p>
<h2>⚙️ 문제점 ①: 통신 효율성의 한계와 최적화 전략</h2>
<p>Federated Learning(FL)의 가장 큰 기술적 병목 중 하나는 <b>통신 비용</b>입니다. 특히 수천~수만 개의 디바이스가 동시에 참여하는 환경에서는 각 클라이언트가 매 라운드마다 파라미터를 주고받는 것이 심각한 네트워크 부하를 유발합니다.</p>
<h3>  문제점</h3>
<ul>
<li>대역폭 소모 증가</li>
<li>에너지 소비 &uarr; (특히 모바일 기기)</li>
<li>실시간 협업 어려움</li>
</ul>
<h3>⚙️ 해결 방법</h3>
<ul>
<li><b>스팟 업로드</b>: 모든 클라이언트가 매 라운드 참여 X &rarr; 일부만 참여 (Federated Dropout)</li>
<li><b>파라미터 압축</b>: 양자화(Quantization), 희소화(Sparsification)</li>
<li><b>지연 업데이트</b>: 로컬 업데이트 여러 번 후 한 번만 전송</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>  문제점 ②: 데이터 이질성(Non-IID) 문제</h2>
<h3>  FL 특유의 환경</h3>
<ul>
<li>각 클라이언트가 가진 데이터는 <b>상호 독립적이지 않고, 분포도 다름</b></li>
<li>&rarr; 모델 훈련 편향 발생 가능성</li>
<li>예: 병원 A는 고령자 중심, 병원 B는 청소년 중심</li>
</ul>
<h3>  해결 전략</h3>
<ul>
<li><b>클라이언트 샘플링 전략 조정</b></li>
<li><b>퍼스널라이즈드 FL(PFL)</b>: 공통 모델 + 로컬 최적화 분기 적용</li>
<li><b>Meta-Learning 기반 FL</b>: 각 클라이언트의 상황에 최적화된 로컬 파인튜닝을 유도</li>
</ul>
<p>&nbsp;</p>
<h2>⚙️ 심화 개념 ③: 모델 드리프트 &amp; 지속적 학습</h2>
<p>FL에서는 로컬 데이터가 시간이 지남에 따라 바뀔 수 있습니다 (데이터 드리프트).<br />&rarr; 이에 대한 대응 없이는 모델 성능이 저하됨.</p>
<h3>  적용 전략</h3>
<ul>
<li>Drift 감지 알고리즘 도입 (KL Divergence, Wasserstein Distance 등)</li>
<li>지속적 학습 연계: 온라인 학습 기반 미니 배치 적용</li>
</ul>
<p>&nbsp;</p>
<h2>⚔️ 위협 1: 모델 반추 공격 (Model Inversion Attack)</h2>
<h3>  개념</h3>
<p>공격자가 서버 또는 악의적인 클라이언트로 위장해, <b>전달받은 파라미터를 역추론하여 원래의 학습 데이터를 복원</b>하려는 공격입니다.</p>
<p>예를 들어, 병원에서 로컬 학습 후 전송한 파라미터를 분석하여, 암 진단 데이터의 이미지나 개인 프로필을 유추해낼 수 있습니다.</p>
<h3> ️ 방어 전략</h3>
<ul>
<li><b>Differential Privacy</b>: 파라미터에 노이즈를 주입해 데이터 재구성 확률을 수학적으로 낮춤</li>
<li><b>Homomorphic Encryption</b>: 암호화된 상태로 연산 가능, 서버는 데이터 내용을 모르고도 평균 산출 가능</li>
</ul>
<hr />
<h2>⚔️ 위협 2: Free-Rider Problem</h2>
<h3>  개념</h3>
<p>어떤 클라이언트가 실제로는 <b>로컬 학습에 참여하지 않고</b>, <b>다른 클라이언트의 학습 결과만 받아서 혜택</b>을 보는 비협력적 행위.</p>
<h3> ️ 방어 전략</h3>
<ul>
<li><b>신뢰 기반 기여도 평가 (Trust-based weighting)</b><br />모델 업데이트의 기여도를 측정하여 반영 비중을 조정</li>
<li><b>학습 감사 로그(Audit Trail)</b><br />참여 이력을 저장하고, 조작 행위를 탐지할 수 있도록 설계</li>
</ul>
<hr />
<h2>⚔️ 위협 3: 중간자 공격 (Man-in-the-Middle)</h2>
<h3>  개념</h3>
<p>FL 통신 중간에 개입해 파라미터를 탈취 또는 변조하는 공격</p>
<h3> ️ 방어 전략</h3>
<ul>
<li><b>TLS + Mutual Authentication</b><br />클라이언트-서버 간 신뢰 구축 및 메시지 암호화</li>
<li><b>Secure Aggregation Protocols (SAP)</b><br />각 클라이언트가 전달한 파라미터를 복호화 없이 집계 가능</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>  미래 전망: Federated AI 생태계의 방향성</h2>
<h3>  1. Cross-Silo FL &rarr; Cross-Device FL</h3>
<ul>
<li>기존 기관 간 협업(Cross-Silo)에서 수백만 단말 참여(Cross-Device)로 전환</li>
<li><b>에너지 최적화</b>, <b>지속적 연결성 유지</b>, <b>참여 신뢰 검증</b>이 주요 과제로 부상</li>
</ul>
<h3>  2. FL + LLM (대규모 언어 모델)의 융합</h3>
<ul>
<li>개인화된 LLM을 각 사용자 단말에서 학습 &rarr; 사용자 맞춤형 응답 제공 (개인 프롬프트 튜닝)</li>
<li>예: LocalGPT + FL 방식으로 보안성 강화</li>
</ul>
<h3>  3. FL + ZKP (Zero-Knowledge Proof)</h3>
<ul>
<li>파라미터의 진위성 검증을 위해 &lsquo;지식 노출 없이 진짜임을 증명&rsquo;하는 <b>ZKP와의 결합</b> 논의 중</li>
<li>고신뢰 환경에서의 협업 가능성 확대</li>
</ul>