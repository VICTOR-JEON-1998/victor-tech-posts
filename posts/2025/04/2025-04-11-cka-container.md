# CKA - Container
**Posted on**: 2025-04-11

<h2>컨테이너(Container)란?</h2>
<p>컨테이너는 <b>운영체제 수준의 격리를 기반으로 애플리케이션을 실행</b>하는 기술입니다.<br />물리 서버, 가상머신(VM)과는 다른 차원의 <b>가볍고 빠른 실행 환경</b>을 제공합니다.</p>
<hr />
<h2>  핵심 개념</h2>
<h3>1. <b>이미지(Image)와 컨테이너(Container)의 차이</b></h3>
<ul>
<li><b>이미지</b>: 애플리케이션 실행에 필요한 코드, 라이브러리, 종속성을 묶은 <b>불변의 실행 패키지</b></li>
<li><b>컨테이너</b>: 이미지를 실행시킨 <b>실행 인스턴스</b>, 상태를 가지며 메모리와 CPU를 점유함</li>
</ul>
<hr />
<h3>2. <b>컨테이너의 특징</b></h3>
<div><br />
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td><b>경량성</b></td>
<td>전체 운영체제가 아닌 커널 공유 방식 (VM 대비 매우 작음)</td>
</tr>
<tr>
<td><b>이식성</b></td>
<td>어떤 환경에서도 동일하게 실행 (Dev &rarr; Test &rarr; Prod)</td>
</tr>
<tr>
<td><b>격리성</b></td>
<td>네트워크, 파일 시스템, 프로세스를 별도로 분리 (namespace)</td>
</tr>
<tr>
<td><b>빠른 시작/종료</b></td>
<td>수 초 이내에 실행 가능 (VM보다 훨씬 빠름)</td>
</tr>
<tr>
<td><b>불변성</b></td>
<td>한 번 생성된 이미지는 바뀌지 않음 (Immutable Infrastructure)</td>
</tr>
</tbody>
</table>
</div>
<h2>&nbsp;</h2>
<h2>  내부 구성 요소 (리눅스 기반)</h2>
<h3>✅ 1. Namespace</h3>
<p>컨테이너의 <b>격리 환경</b>을 만들기 위한 핵심 기능</p>
<ul>
<li>pid, net, mnt, uts, ipc, user 등의 공간을 분리함</li>
<li>&rarr; 컨테이너는 마치 독립된 리눅스처럼 보이게 됨</li>
</ul>
<h3>✅ 2. Cgroups</h3>
<ul>
<li>컨테이너의 리소스(CPU, Memory, IO 등)를 <b>제한하고 제어</b></li>
<li>예: 컨테이너 A는 메모리 512Mi만 사용 가능 같은 제약 설정</li>
</ul>
<h3>✅ 3. OverlayFS (파일 시스템)</h3>
<ul>
<li>이미지 레이어를 읽기 전용으로 유지하고, 변경사항만 쓰기 가능하게 오버레이</li>
<li>레이어드 아키텍처로 빌드 속도, 캐싱 효과 극대화</li>
</ul>
<p>&nbsp;</p>
<h2>  컨테이너 실행 과정 (containerd 기준)</h2>
<ol>
<li>사용자가 이미지 지정 &rarr; containerd가 이미지 pull</li>
<li>이미지 Layer &rarr; Union Mount (OverlayFS)</li>
<li>containerd &rarr; runc 호출 &rarr; clone() + namespace + cgroups 설정</li>
<li>프로세스가 container 내부에서 실행됨</li>
</ol>
<p>아래는 보다 더 자세한 세부 설명!</p>
<h3>  전체 흐름 요약</h3>
<ol>
<li><b>이미지 선택</b></li>
<li><b>이미지 레이어 다운로드 및 병합 (OverlayFS)</b></li>
<li><b>런타임 호출 (runc)</b> &rarr; clone() 호출로 격리 공간 생성</li>
<li><b>namespace, cgroups, rootfs, net 등 초기화</b></li>
<li><b>컨테이너 내부에서 프로세스 실행</b></li>
</ol>
<p>&nbsp;</p>
<h3>1️⃣ 사용자가 컨테이너 실행 요청 (docker run, ctr run 등)</h3>
<ul>
<li>사용자는 nginx:latest와 같은 이미지 지정</li>
<li>Docker는 내부적으로 containerd를 호출</li>
<li>containerd는 OCI(Open Container Initiative) 표준을 따라 동작함</li>
</ul>
<h3>2️⃣ containerd &rarr; 이미지 pull &amp; Unpack</h3>
<ul>
<li>이미지를 <b>layer 단위</b>로 레지스트리에서 받아옴 (tarball 형태)</li>
<li>레이어들은 Read-only이고, 마지막에 OverlayFS로 합쳐짐</li>
<li>Top 레이어는 쓰기 가능(writeable), 나머지는 읽기 전용</li>
</ul>
<h3>3️⃣ runc 호출 &rarr; 격리된 환경 생성</h3>
<ul>
<ul>
<li>containerd는 runc(하위 런타임)를 실행해 실제 컨테이너를 생성</li>
<li>runc는 리눅스의 clone() 시스템 콜을 이용해 <b>새로운 네임스페이스로 프로세스를 생성</b></li>
<li><b> 이 순간부터는 **독립된 "미니 리눅스 공간"**이 탄생함</b><b></b></li>
</ul>
</ul>
<h3>4️⃣ 격리 및 제한 적용</h3>
<h4>  Namespace</h4>
<p>&rarr; 격리된 세계 만들기 (PID, Network, Mount, Hostname 등 분리)</p>
<div>
<div>타입설명
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>pid</td>
<td>프로세스 목록 분리 (컨테이너 밖의 프로세스 안 보임)</td>
</tr>
<tr>
<td>net</td>
<td>자체 네트워크 스택 사용 (IP, 포트 분리)</td>
</tr>
<tr>
<td>mnt</td>
<td>파일 시스템 마운트 격리</td>
</tr>
<tr>
<td>uts</td>
<td>호스트 이름 분리 (컨테이너마다 다른 hostname)</td>
</tr>
<tr>
<td>ipc</td>
<td>프로세스 간 통신 분리 (shared memory 등)</td>
</tr>
</tbody>
</table>
</div>
</div>
<h4>  Cgroups</h4>
<p>&rarr; 자원 사용 제한</p>
<ul>
<li>CPU, Memory, IO, PID 개수 등을 제한</li>
<li>예: max 512Mi memory, 1 core CPU</li>
</ul>
<pre class="sql" id="code_1744272109929"><code>/sys/fs/cgroup/...</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3>5️⃣ rootfs, 환경변수, 네트워크 구성</h3>
<ul>
<li>컨테이너 루트 파일 시스템 설정 (chroot 느낌)</li>
<li>/proc, /dev, /sys 등 필수 시스템 디렉토리 마운트</li>
<li>지정된 환경 변수, 사용자, 작업 디렉토리 등을 초기화</li>
<li>Network namespace 내에서 가상 이더넷(veth pair) 연결</li>
</ul>
<p>&nbsp;</p>
<h3>6️⃣ 프로세스 시작 (CMD / ENTRYPOINT)</h3>
<ul>
<li>마침내 컨테이너의 메인 프로세스가 실행됨<br />예: nginx, node app.js, python main.py</li>
<li>PID 1로 실행되며, 종료되면 컨테이너 전체도 종료됨</li>
<li>표준 출력은 containerd &rarr; Docker Engine &rarr; 터미널로 전달됨</li>
</ul>