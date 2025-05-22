# 2025-05-22 Airline DevOps Project Progress Log
**Posted on**: 2025-05-22

<h1>  2025-05-22 Airline DevOps Project Progress Log</h1>
<h2>✅ Today's Goal</h2>
<ul>
<li>Organize initial Terraform project structure</li>
<li>Prepare AWS resources (ECR, EC2, Security Group)</li>
<li>Ensure all configurations stay within the free tier</li>
</ul>
<hr />
<h2>  Project Directory Structure</h2>
<pre><code>airline-devops-demo/
└── terraform/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf</code></pre><hr />
<h2> ️ Work Details</h2>
<h3>1. Code Separation &amp; Security Group Enhancement</h3>
<ul>
<li>Split Terraform configuration into <code>main.tf</code>, <code>variables.tf</code>, and <code>outputs.tf</code></li>
<li>EC2 instance configured with <code>t2.micro</code> (free tier)</li>
<li>SSH access restricted to <code>180.64.226.122/32</code> (your public IP)</li>
<li>HTTP/HTTPS ports open to the public</li>
</ul>
<h3>2. Terraform Initialization</h3>
<ul>
<li>Ran <code>terraform init</code> to download AWS provider</li>
<li><code>.terraform.lock.hcl</code> generated for provider version lock-in</li>
</ul>
<hr />
<h2>⚠️ Notes</h2>
<ul>
<li><code>terraform apply</code> has not been executed yet</li>
<li>EC2 key pair is passed via the <code>key_pair_name</code> variable</li>
<li>Next step involves automating Docker setup using <code>user_data</code></li>
</ul>
<hr />
<h2>⏭️ Next Steps</h2>
<ul>
<li>Execute <code>terraform apply</code> to create infrastructure</li>
<li>Add <code>user_data</code> script to install Docker on EC2 automatically</li>
<li>Dockerize Node.js app and push to ECR</li>
<li>Pull image and run the app on EC2 instance</li>
</ul>