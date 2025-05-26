# AWS with Terraform
**Posted on**: 2025-05-26

<h3>SOPS</h3>
<p>Secret Operations</p>
<p>AWS에서 만든 CLI 기반의 Secret 관리 도구</p>
<p>Gitops 환경에서 비밀 값을 안전하게 파일에 저장하고 버전 관리할 수 있도록 도와줌.</p>
<p>다양한 키 백엔드(KMS)와 연동 가능</p>
<p>암호화된 상태로 커밋하고 팀원들은 복호화된 키로만 복호화 가능</p>
<p>terraform-provider-sops 또는 외부 data source 활용 가능</p>
<h3>AWS KMS?</h3>
<p>암호화 키(CMK)를 안전하게 저장하고 암복호화 연산을 AWS에서 대신수행해주는 서비스</p>
<p>쉽게 키를 만드는 서비스</p>
<p>암호화 과정에 대한 공부를 해보자.</p>
<p>봉투 암호화 알고리즘</p>
<p>암호화하는 키를 KMS를 만듬</p>
<h3>작동 원리</h3>
<ol>
<li>SOPS가 암호화 요청</li>
</ol>
<pre class="routeros"><code># secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
stringData:
  password: my-plaintext-password

</code></pre>
<pre class="stylus"><code>sops -e -i secret.yaml

</code></pre>
<pre class="less"><code>stringData:
  password: ENC[AES256_GCM,data:o8rE...,type:str]
sops:
  kms:
    - arn: arn:aws:kms:ap-northeast-2:123456789012:key/abcde-...-xyz
      enc: AQICAHgz8h...
  ...
  
  
</code></pre>
<ul>
<li>password만 암호화됨</li>
<li>어떤 kms키(arn)을 사용했는지 기록됨</li>
<li>sops블록에 호화 정보 포함</li>
</ul>
<h3>DEK CMK 쉬운 설명</h3>
<p>친구에게 편지를 쓰고 자물쇠 상자에 넣어서 잠근다.</p>
<p>이때 자물쇠는 DEK!</p>
<p>자물쇠를 열 수 있는 열쇠는 그냥 보내면 위험하니까 은행 금고에 보관한다.</p>
<p>은행 금고는 KMS! 열쇠는 CMK!</p>
<p>친구에게 은행(KMS)에 가서 권한 확인 후 열쇠를 받으라고 한다.</p>