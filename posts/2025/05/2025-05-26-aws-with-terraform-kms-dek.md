# AWS with Terraform (KMS , DEK, 암복호화)
**Posted on**: 2025-05-26

<p>&nbsp;</p>
<p>EC2에 IAM을 내장시켜서 Secret Manager와 연동하게 하는게 안전함</p>
<ol>
<li>IAM으로 EC2에 데이터 요청 권한 및 복호화 권한을 할당</li>
<li>EC2가 Secret Manger에 권한 요청</li>
</ol>
<blockquote>
<p>모듈안에 작성 후 값들은 다 variable화 되어있어야 한다</p>
</blockquote>
<p>테라폼 코드 상 Key에다가 실제 값들을 입력함.</p>
<ul>
<li>Terraform Plan</li>
</ul>
<p>코드와 현재상태를 비교해서 바뀐 것이 뭔지 출력해줌</p>
<ul>
<li>Terraform apply</li>
</ul>
<p>plan에서 예측한 변경사항을 실제로 실행함</p>
<p>Q. 코드에서 Var는 뭘 의미하는지?</p>
<p>&rarr; Terraform 코드 안의 var.변수이름은 varibales.tf나 .tfvars에서 정의한 변수 값을 불러오는 방식</p>
<pre class="routeros"><code># variables.tf
variable "aws_region" {
  type = string
}

# terraform.tfvars
aws_region = "ap-northeast-2"

# main.tf
provider "aws" {
  region = var.aws_region  # &larr; 여기서 사용
}
</code></pre>
<p>Q. KMS는 Terraform에서 어떻게 사용하나?</p>
<h3>① KMS 키 생성</h3>
<pre class="nginx"><code>resource "aws_kms_key" "example" {
  description             = "Key for S3 encryption"
  deletion_window_in_days = 7
}

</code></pre>
<h3>② S3에 적용 예시</h3>
<pre class="nginx"><code>resource "aws_s3_bucket" "secure_bucket" {
  bucket = "my-secure-bucket"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "aws:kms"
        kms_master_key_id = aws_kms_key.example.arn
      }
    }
  }
}

</code></pre>
<p>이렇게 하면 S3에 저장된 객체가 <b>KMS로 암호화</b></p>
<p><a href="http://key.tf">key.tf</a> ?</p>
<p><a href="http://key.tf">key.tf</a> 파일은 보통 KMS키 관련 리소스가 들어감</p>
<p>KMS 키를 생성하고 &rarr; <a href="http://kms.tf">kms.tf</a></p>
<p>SecureString Parameter을 생성하고 &rarr; <a href="http://ssm.tf">ssm.tf</a></p>
<p>그때 사용하는 암호화 키를 KMS에서 가져옴 &rarr; key_id 연결</p>
<h2>SOPS에서 암호화가 어떻게 이뤄지는가?</h2>
<h3>terraform.tfvars</h3>
<pre class="ini"><code>db_password = "my-super-secret"

</code></pre>
<hr />
<h3>SOPS가 이 파일을 암호화할 때 하는 일</h3>
<pre class="stylus"><code>sops -e -i terraform.tfvars

</code></pre>
<p>이렇게 실행하면 <b>SOPS 내부에서 자동으로 다음이 수행됨</b>:</p>
<h3>내부 동작</h3>
<ol>
<li>랜덤한 **DEK (Data Encryption Key)**를 생성한다 (AES 256 대칭키)</li>
<li>이 DEK를 사용해 db_password 값을 암호화한다</li>
<li>DEK 자체를 AWS KMS 키 or PGP 키로 암호화한다 (=&gt; CMK로 DEK를 잠금)</li>
<li>암호화된 DEK + 암호화된 값 + 암호 방식 메타데이터를 모두 .enc 파일에 포함시킨다</li>
</ol>
<h2>결과 파일 (terraform.tfvars.enc) 예시</h2>
<pre class="dts"><code>db_password = "ENC[AES256_GCM,data:abc123...,type:str]" 
# DEK로 암호화된 값이 들어감, 복호화하려면 DEK가 필요

sops:
  kms:
    - arn: arn:aws:kms:ap-northeast-2:123456789012:key/abc...
      enc: AQICAHg...
  enc_seed: ...
  version: "3.7.1"
  mac: "..."

</code></pre>
<p>&nbsp;</p>
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>ENC[...]</td>
<td>db_password를 암호화한 결과 (DEK로 암호화됨)</td>
</tr>
<tr>
<td>sops.kms.enc</td>
<td>DEK를 암호화한 값 (KMS CMK로 암호화됨)</td>
</tr>
<tr>
<td>sops.kms.arn</td>
<td>어떤 KMS 키로 DEK를 암호화했는지</td>
</tr>
<tr>
<td>sops.enc_seed, mac, version</td>
<td>무결성, 재현성 보장용 메타정보</td>
</tr>
</tbody>
</table>