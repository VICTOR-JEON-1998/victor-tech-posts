# CKA Basic : About POD [ENG]
**Posted on**: 2025-04-09

<p>Pod is the <b>smallest deployable unit in Kubernetes</b>, used to run one or more containers.<br />While most Pods typically contain just one container, there are situations where it makes sense to run <b>multiple tightly-coupled containers together inside the same Pod</b>.</p>
<p>This is useful when those containers need to <b>work closely together</b>, for example:</p>
<ul>
<li>An application container (e.g., a Node.js server), and</li>
<li>A log collector container (e.g., Busybox tailing logs)</li>
</ul>
<p>These containers <b>share the same network and filesystem</b>, making their interaction seamless.</p>
<p>&nbsp;</p>
<h3>In Kubernetes, containers within a Pod share three key things:</h3>
<ol>
<li><b>Network (Network Namespace)</b>
<ul>
<li>All containers in the Pod share the <b>same IP address and port space</b>.</li>
<li>They can communicate via localhost, just like processes in the same machine.</li>
<li>From outside the Pod, access must go through a Kubernetes Service.</li>
</ul>
</li>
<li><b>Storage (Volumes)</b>
<ul>
<li>Pods can use shared volumes, such as emptyDir, so that <b>multiple containers can access and exchange data or logs</b>.</li>
<li>This enables containers to share files easily within the Pod lifecycle.</li>
</ul>
</li>
<li><b>Lifecycle</b>
<ul>
<li>Containers inside a Pod are <b>created and destroyed together</b>.</li>
<li>If one container fails or exits, it may impact the entire Pod, depending on the configuration.</li>
</ul>
</li>
</ol>
<h3>Real-world Example</h3>
<p>Suppose you have:</p>
<ul>
<li>A Node.js container writing logs to /app/logs/app.log</li>
<li>A Busybox container tailing /logs/app.log to send logs elsewhere</li>
</ul>
<p>If both containers run in the same Pod and share an emptyDir volume, they can interact directly &mdash; one writes, one reads &mdash; all within the same isolated unit.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3>Summary</h3>
<p>A <b>Pod is a logical host</b> for one or more tightly coupled containers that need to share:</p>
<ul>
<li><b>Network space (IP and ports)</b></li>
<li><b>Storage (via Volumes)</b></li>
<li><b>Lifecycle and management (created/terminated together)</b></li>
</ul>
<p>In practice, you rarely define Pods manually.<br />Instead, you manage Pods through higher-level controllers like Deployment, Job, or CronJob, which handle rolling updates, scaling, and restart policies more effectively.</p>