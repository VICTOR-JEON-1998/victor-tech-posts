# ⚽ MLOps 포트폴리오 프로젝트 시작합니다 &ndash; 축구로 배우는 AI
**Posted on**: 2025-04-15

<h2>&nbsp;</h2>
<p>안녕하세요, 이번 블로그 시리즈에서는<br /><b>축구선수 이적료 예측 프로젝트를 통해 MLOps를 실전으로 학습해보는 과정</b>을 공유합니다.</p>
<hr />
<h3>  왜 축구인가요?</h3>
<p>평소 축구를 좋아하는 사람으로서, 단순한 공부가 아닌<br /><b>"내가 좋아하는 걸로 재밌게 실무 역량을 키울 수 없을까?"</b> 하는 생각이 들었습니다.</p>
<p>그 결과,</p>
<blockquote>
<p>선수의 나이, 포지션, 경기 기록 등을 바탕으로 이적료를 예측하고, 이를 실험 관리 + 서빙 + 자동화 + 배포하는 MLOps 파이프라인으로 구현한다면 어떨까?<br />라는 아이디어로 이번 프로젝트가 시작되었습니다.</p>
</blockquote>
<hr />
<h3>  프로젝트 목표</h3>
<p>이 프로젝트는 단순히 모델 하나를 만드는 것이 아닙니다.<br />**"실제 서비스를 운영하는 수준의 머신러닝 시스템을 구축해보는 것"**이 목표입니다.</p>
<ul>
<li>scikit-learn으로 회귀 모델 개발</li>
<li>MLflow로 실험 추적 및 관리</li>
<li>FastAPI로 REST API 서빙</li>
<li>Docker로 컨테이너화</li>
<li>GitHub Actions로 retrain 자동화</li>
<li>Kubernetes or Docker Compose로 배포</li>
<li>Prometheus + Grafana로 모니터링 (선택)</li>
</ul>
<hr />
<h3>  앞으로의 계획</h3>
<p>이 시리즈는 총 8~9편으로 구성될 예정입니다.<br />단순한 코드 나열이 아니라 <b>각 단계마다 &ldquo;왜 이렇게 하는가&rdquo;에 집중하여 설명</b>합니다.</p>
<p>  각 포스트는 다음 내용을 다룹니다:</p>
<ol>
<li>데이터 수집 및 EDA</li>
<li>모델링 및 기본 실험</li>
<li>MLflow 실험 관리</li>
<li>FastAPI 서빙</li>
<li>Docker 컨테이너화</li>
<li>GitHub Actions 자동화</li>
<li>Kubernetes 배포 (선택)</li>
<li>모니터링 &amp; 운영 (선택)</li>
<li>회고 및 포트폴리오 정리</li>
</ol>
<hr />
<h3> ️ GitHub &amp; 실행 환경</h3>
<ul>
<li>전체 프로젝트 코드:&nbsp; <a href="https://github.com/VICTOR-JEON-1998/mlops-fc" rel="noopener" target="_blank" title="GitHub">https://github.com/VICTOR-JEON-1998/mlops-fc</a></li>
<li>실행 환경: Python, scikit-learn, FastAPI, MLflow, Docker, GitHub Actions</li>
</ul>
<hr />
<h3>  기대 효과</h3>
<p>이 프로젝트를 통해</p>
<ul>
<li>MLOps 전체 흐름을 이해하고</li>
<li>구조적 프로젝트를 확보하며</li>
<li>직접 구현 경험을 어필할 수 있습니다.</li>
</ul>
<hr />
<p>시작은 소박하지만, 끝은 강력한 무기가 될 것입니다.</p>
<p>다음 글에서는 실제 사용한 데이터를 소개하고,<br />EDA(탐색적 데이터 분석)를 진행해보겠습니다.</p>
<p>  이어지는 글: [Part 1 &ndash; 데이터 수집 및 분석]</p>