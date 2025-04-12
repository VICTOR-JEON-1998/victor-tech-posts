# [작업일지] Next.js 백엔드에서 JWT 인증 유지 흐름 구현하기 &ndash; 로그인 이후 인증 API 만들기
**Posted on**: 2025-04-12

<p>오늘은 Next.js 기반 API 백엔드 프로젝트에서<br /><b>로그인 이후 인증 흐름을 유지하는 구조</b>를 구현했다.</p>
<p>즉, 로그인한 사용자가 <b>다른 API를 호출할 때도 본인이 맞는지 자동 인증</b>되는 로직을 만든 것.</p>
<p>&nbsp;</p>
<h3>구현 목표</h3>
<ul>
<li>로그인 시 발급된 JWT 토큰을 API 요청에 활용</li>
<li>서버에서 JWT 유효성 검증</li>
<li>유저 정보를 응답하는 /api/me API 구현</li>
<li>추후 모든 인증이 필요한 API에 재사용 가능한 인증 로직 설계</li>
</ul>
<p>&nbsp;</p>
<h4>1. JWT 토큰 검증 유틸 함수 생성</h4>
<pre class="bash" id="code_1744437541303"><code>// lib/verifyToken.ts

import jwt from 'jsonwebtoken'

const JWT_SECRET = process.env.JWT_SECRET || 'default_secret'

export function verifyToken(token: string) {
  try {
    const decoded = jwt.verify(token, JWT_SECRET)
    return decoded
  } catch (error) {
    return null
  }
}</code></pre>
<h4>2. 인증된 유저만 접근 가능한 /api/me API</h4>
<pre class="bash" id="code_1744437574135"><code>// pages/api/me.ts

import { verifyToken } from '@/lib/verifyToken'
import { PrismaClient } from '@prisma/client'
import type { NextApiRequest, NextApiResponse } from 'next'

const prisma = new PrismaClient()

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'GET') return res.status(405).json({ message: '허용되지 않은 메서드입니다.' })

  const authHeader = req.headers.authorization
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ message: '인증 정보가 없습니다.' })
  }

  const token = authHeader.split(' ')[1]
  const decoded = verifyToken(token)

  if (!decoded || typeof decoded !== 'object' || !('userId' in decoded)) {
    return res.status(401).json({ message: '유효하지 않은 토큰입니다.' })
  }

  const user = await prisma.user.findUnique({
    where: { id: decoded.userId as string },
    select: { id: true, email: true, createdAt: true },
  })

  if (!user) return res.status(404).json({ message: '유저를 찾을 수 없습니다.' })

  return res.status(200).json({ user })
}</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3>  Postman 테스트 흐름</h3>
<ol>
<li>로그인 API (/api/auth/login) 호출 &rarr; JWT 토큰 발급</li>
<li>Authorization 헤더에 Bearer &lt;토큰&gt; 형식으로 /api/me 호출</li>
<li>토큰이 유효할 경우 &rarr; 로그인한 사용자 정보 반환</li>
</ol>
<p>&nbsp;</p>
<h3>  배운 점</h3>
<ul>
<li>JWT 기반 인증을 위한 유틸 함수 구조</li>
<li>인증 미들웨어 없이도 간단히 처리 가능한 방식</li>
<li>인증 흐름을 모듈화해 다른 API에도 재사용 가능함</li>
<li>추후 게시글 작성, 댓글 등 API에도 동일한 방식 적용 가능</li>
</ul>
<hr />
<h3>✅ 다음 목표</h3>
<ul>
<li>인증이 필요한 게시글 작성 API로 확장</li>
<li>Flutter와 연동하여 토큰 저장 + 자동 로그인 구현</li>
</ul>