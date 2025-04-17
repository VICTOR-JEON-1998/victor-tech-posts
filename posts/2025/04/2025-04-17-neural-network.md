# 신경망(Neural Network)의 수학적 이해와 아키텍처 심화 분석
**Posted on**: 2025-04-17

<h1>신경망(Neural Network)의 수학적 이해와 아키텍처 심화 분석</h1>
<hr />
<h2>1. 신경망의 수학적 정의</h2>
<p>신경망은 함수 근사기(Function Approximator)로 볼 수 있습니다.<br />다층 퍼셉트론(Multilayer Perceptron, MLP)은 다음과 같은 형태의 함수 <span><span>f&thinsp;⁣:Rn&rarr;Rmf \colon \mathbb{R}^n \rightarrow \mathbb{R}^m</span><span><span><span>f</span><span><span>:</span></span><span><span>R</span><span><span><span><span><span><span><span>n</span></span></span></span></span></span></span></span><span>&rarr;</span></span><span><span><span>R</span><span><span><span><span><span><span><span>m</span></span></span></span></span></span></span></span></span></span></span> 를 구성합니다:</p>
<h3>▶️ 기본 연산 구조:</h3>
<p><span><span><span>a(l)=f(W(l)a(l&minus;1)+b(l))a^{(l)} = f(W^{(l)} a^{(l-1)} + b^{(l)})</span><span><span><span><span>a</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span><span>=</span></span><span><span>f</span><span>(</span><span><span>W</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span><span><span>a</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>&minus;</span><span>1</span><span>)</span></span></span></span></span></span></span></span></span><span>+</span></span><span><span><span>b</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span><span>)</span></span></span></span></span></p>
<ul>
<li><span><span>ll</span><span><span><span>l</span></span></span></span>: 레이어 인덱스</li>
<li><span><span>W(l)W^{(l)}</span><span><span><span><span>W</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span></span>: 가중치 행렬</li>
<li><span><span>b(l)b^{(l)}</span><span><span><span><span>b</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span></span>: 편향 벡터</li>
<li><span><span>ff</span><span><span><span>f</span></span></span></span>: 비선형 활성화 함수 (ReLU, tanh, sigmoid 등)</li>
<li><span><span>a(l)a^{(l)}</span><span><span><span><span>a</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span></span>: 레이어 <span><span>ll</span><span><span><span>l</span></span></span></span>의 출력 (activation)</li>
</ul>
<hr />
<h2>2. Universal Approximation Theorem (보편 근사 정리)</h2>
<blockquote>
<p><b>&ldquo;적절한 비선형 활성화 함수와 충분한 뉴런 수만 있다면, 단일 은닉층 신경망도 모든 연속 함수를 근사할 수 있다.&rdquo;</b></p>
</blockquote>
<p>하지만:</p>
<ul>
<li>&ldquo;근사 가능&rdquo;과 &ldquo;실제로 학습 가능&rdquo;은 다름</li>
<li>**Depth(깊이)**와 **Representation(표현력)**이 실질적인 성능에 중요함</li>
</ul>
<h3>▶️ 깊은 네트워크가 얕은 네트워크보다 좋은 이유:</h3>
<ul>
<li>표현력: 깊은 네트워크는 지수적으로 더 많은 비선형 경계를 만들 수 있음</li>
<li>파라미터 수 절감: 같은 기능을 얕은 구조로 만들면 더 많은 노드가 필요함</li>
</ul>
<hr />
<h2>3. 역전파(Backpropagation)의 수학적 구조</h2>
<p>역전파는 손실 함수 <span><span>LL</span><span><span><span>L</span></span></span></span>에 대해 가중치 <span><span>WW</span><span><span><span>W</span></span></span></span>의 그라디언트를 계산하는 알고리즘입니다.</p>
<h3>▶️ 체인 룰 기반 파생:</h3>
<p><span><span><span>&part;L&part;W(l)=&part;L&part;a(l)&sdot;&part;a(l)&part;z(l)&sdot;&part;z(l)&part;W(l)\frac{\partial L}{\partial W^{(l)}} = \frac{\partial L}{\partial a^{(l)}} \cdot \frac{\partial a^{(l)}}{\partial z^{(l)}} \cdot \frac{\partial z^{(l)}}{\partial W^{(l)}}</span><span><span><span><span><span><span><span><span><span><span>&part;</span><span><span>W</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span><span></span><span><span><span>&part;</span><span>L</span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span>=</span></span><span><span><span><span><span><span><span><span><span>&part;</span><span><span>a</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span><span></span><span><span><span>&part;</span><span>L</span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span>&sdot;</span></span><span><span><span><span><span><span><span><span><span>&part;</span><span><span>z</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span><span></span><span><span><span>&part;</span><span><span>a</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span>&sdot;</span></span><span><span><span><span><span><span><span><span><span>&part;</span><span><span>W</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span><span></span><span><span><span>&part;</span><span><span>z</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span></span><span>​</span></span><span><span></span></span></span></span></span></span></span></span></span></p>
<ul>
<li><span><span>z(l)=W(l)a(l&minus;1)+b(l)z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}</span><span><span><span><span>z</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span><span>=</span></span><span><span><span>W</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span><span><span>a</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>&minus;</span><span>1</span><span>)</span></span></span></span></span></span></span></span></span><span>+</span></span><span><span><span>b</span><span><span><span><span><span><span><span><span>(</span><span>l</span><span>)</span></span></span></span></span></span></span></span></span></span></span></span></li>
<li>각 레이어에서의 미분을 <b>체인 룰</b>로 누적하여 역방향으로 전달</li>
</ul>
<h3>▶️ 주의할 점:</h3>
<ul>
<li>가중치 초기화가 잘못되면 그래디언트 소실/폭주 발생 (&rarr; He, Xavier 초기화 등장)</li>
<li>ReLU가 그라디언트 소실 문제를 해결했으나, dying ReLU 문제는 여전히 존재함</li>
</ul>
<hr />
<h2>4. 과적합과 정규화 기법</h2>
<h3>▶️ 과적합 방지 전략</h3>
<div><span></span>
<div>기법원리
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>Dropout</td>
<td>학습 중 무작위로 일부 뉴런을 제거하여 공동 적응 방지</td>
</tr>
<tr>
<td>L2 정규화 (Weight Decay)</td>
<td>파라미터 크기를 줄여 모델 복잡도 감소</td>
</tr>
<tr>
<td>Early Stopping</td>
<td>검증 손실이 증가하면 조기 종료</td>
</tr>
<tr>
<td>Batch Normalization</td>
<td>각 층의 입력 분포를 정규화하여 학습 안정성 향상</td>
</tr>
</tbody>
</table>
</div>
</div>
<hr />
<h2>5. 신경망의 한계와 구조적 대응</h2>
<h3>❌ 기존 MLP의 한계</h3>
<div><span></span>
<div>문제원인
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>시계열/순서 인식 불가</td>
<td>순차 정보 고려 X</td>
</tr>
<tr>
<td>고차원 이미지 처리 비효율</td>
<td>모든 픽셀에 Fully Connected</td>
</tr>
</tbody>
</table>
</div>
</div>
<hr />
<h2>6. 딥러닝 구조 확장 원리</h2>
<h3>▶️ Convolutional Neural Network (CNN)</h3>
<ul>
<li>**위치 기반 local filter (kernel)**을 활용</li>
<li>파라미터 수 감소 + 공간 정보 유지</li>
<li>이미지, 음성 처리에 적합</li>
</ul>
<p><span><span><span>y=f(W&lowast;x+b)y = f(W * x + b)</span><span><span><span>y</span><span>=</span></span><span><span>f</span><span>(</span><span>W</span><span>&lowast;</span></span><span><span>x</span><span>+</span></span><span><span>b</span><span>)</span></span></span></span></span></p>
<ul>
<li>*: 컨볼루션 연산</li>
</ul>
<hr />
<h3>▶️ Recurrent Neural Network (RNN)</h3>
<ul>
<li>이전 시점의 출력을 현재 입력에 반영</li>
</ul>
<p><span><span><span>ht=f(Wxt+Uht&minus;1+b)h_t = f(Wx_t + Uh_{t-1} + b)</span><span><span><span><span>h</span><span><span><span><span><span><span><span>t</span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span>=</span></span><span><span>f</span><span>(</span><span>W</span><span><span>x</span><span><span><span><span><span><span><span>t</span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span>+</span></span><span><span>U</span><span><span>h</span><span><span><span><span><span><span><span><span>t</span><span>&minus;</span><span>1</span></span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span>+</span></span><span><span>b</span><span>)</span></span></span></span></span></p>
<ul>
<li>시계열 데이터, 자연어 처리에 유리</li>
<li>그러나 장기 의존성 학습 어려움 (&rarr; LSTM, GRU 등장)</li>
</ul>
<hr />
<h3>▶️ Transformer (Self-Attention 기반)</h3>
<blockquote>
<p>"모든 입력 간 상호작용을 병렬적으로 계산"</p>
</blockquote>
<p><span><span><span>Attention(Q,K,V)=softmax(QKTdk)V\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^T}{\sqrt{d_k}} \right) V</span><span><span><span><span>Attention</span></span><span>(</span><span>Q</span><span>,</span><span>K</span><span>,</span><span>V</span><span>)</span><span>=</span></span><span><span><span>softmax</span></span><span><span><span>(</span></span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>d</span><span><span><span><span><span><span><span>k</span></span></span></span><span>​</span></span><span><span></span></span></span></span></span></span></span><span><span></span></span></span><span>​</span></span><span><span></span></span></span></span></span></span><span></span><span><span><span>Q</span><span><span>K</span><span><span><span><span><span><span><span>T</span></span></span></span></span></span></span></span></span></span></span><span>​</span></span><span><span></span></span></span></span></span><span><span>)</span></span></span><span>V</span></span></span></span></span></p>
<ul>
<li>텍스트, 코드, 이미지 등 모든 시퀀스에 강력함</li>
<li>GPT, BERT, LLaMA, Claude, Gemini 등의 기반 구조</li>
</ul>
<hr />
<h2>7. 학습 최적화: 손실 함수와 옵티마이저</h2>
<div><span></span>
<div>목적선택 예시
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>회귀</td>
<td>MSE (Mean Squared Error)</td>
</tr>
<tr>
<td>이진 분류</td>
<td>Binary Cross Entropy</td>
</tr>
<tr>
<td>다중 분류</td>
<td>Categorical Cross Entropy</td>
</tr>
<tr>
<td>불균형 데이터</td>
<td>Focal Loss, AUC Loss</td>
</tr>
</tbody>
</table>
</div>
</div>
<h3>▶️ Optimizer 종류</h3>
<div><span></span>
<div>Optimizer특징
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>SGD</td>
<td>고전적 방식, 학습률 튜닝 중요</td>
</tr>
<tr>
<td>Momentum</td>
<td>방향성 반영 (관성 효과)</td>
</tr>
<tr>
<td>RMSprop</td>
<td>학습률 자동 조절 (2차 모멘트)</td>
</tr>
<tr>
<td>Adam</td>
<td>모멘텀 + RMSprop 결합, 현재 가장 널리 사용</td>
</tr>
</tbody>
</table>
</div>
</div>
<hr />
<h2>8. 실전 설계 시 고려해야 할 하이퍼파라미터</h2>
<ul>
<li><b>은닉층 수 / 뉴런 수</b></li>
<li><b>학습률 / 스케줄러</b></li>
<li><b>Batch Size</b></li>
<li><b>활성화 함수</b></li>
<li><b>초기화 방법</b></li>
<li><b>Regularization 기법</b></li>
</ul>
<blockquote>
<p>이들의 조합이 모델 성능의 90%를 좌우합니다.</p>
</blockquote>
<hr />
<h2>  마무리 요약</h2>
<blockquote>
<p>신경망은 단순한 블랙박스가 아니라,<br /><b>미분 가능한 함수들을 층층이 쌓아올린 거대한 수학적 구조</b>이며,<br />이 구조를 최적화하는 알고리즘이 바로 딥러닝의 본질입니다.</p>
</blockquote>