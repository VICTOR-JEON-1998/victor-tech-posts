# NestJS에서 JWT 인증 흐름 구현하기
**Posted on**: 2025-04-16

<p>&nbsp;</p>
<p>&nbsp;</p>
<h1>NestJS에서 JWT 인증 흐름 구현하기</h1>
<h2>1. JWT란 무엇인가?</h2>
<p>JWT(Json Web Token)는 인증 정보를 저장하고 전송하는 데 사용되는 표준화된 토큰 형식입니다.</p>
<ul>
<li><b>구성 요소</b>: 헤더(Header), 페이로드(Payload), 서명(Signature)</li>
<li><b>장점</b>: 토큰 기반이므로 서버에 상태를 저장하지 않아도 됨 (Stateless), 분산 시스템에 적합.</li>
<li><b>단점</b>: 토큰이 길어질 수 있고, 갱신되지 않으면 보안 취약점이 생길 가능성 있음.</li>
<li><b>사용 사례</b>: 사용자 인증, 권한 검증, 세션 관리 대체 등.</li>
</ul>
<h2>2. NestJS 프로젝트 구성</h2>
<p>NestJS는 TypeScript 기반의 Node.js 프레임워크로, 모듈(Module), 컨트롤러(Controller), 서비스(Service)로 구조화되어 있습니다.</p>
<ul>
<li><b>필요 패키지 설치</b>:
<pre class="coffeescript"><code>
npm install @nestjs/jwt @nestjs/passport passport passport-jwt
                </code></pre>
</li>
<li><b>파일 구조</b>:
<pre class="stylus"><code>
src/
├── auth/
│   ├── auth.module.ts
│   ├── auth.controller.ts
│   ├── auth.service.ts
│   ├── jwt.strategy.ts
└── main.ts
                </code></pre>
</li>
<li><b>기본 설정</b>: Nest CLI를 이용해 새로운 모듈을 생성하고, 필요한 의존성을 추가.</li>
</ul>
<h2>3. @nestjs/jwt 모듈 설치 및 설정</h2>
<p>JwtModule은 JWT 토큰 생성 및 검증을 처리합니다.</p>
<ul>
<li><b>JwtModule 설정</b>:
<pre class="typescript"><code>
import { JwtModule } from '@nestjs/jwt';
import { Module } from '@nestjs/common';

@Module({
  imports: [
    JwtModule.register({
      secret: 'yourSecretKey', // 실제 환경에서는 환경 변수로 관리
      signOptions: { expiresIn: '1h' },
    }),
  ],
})
                </code></pre>
</li>
<li><b>환경 변수 적용</b>:.env 파일을 만들어 JWT_SECRET과 JWT_EXPIRATION_TIME 관리.</li>
</ul>
<h2>4. 로그인 API에서 토큰 발급</h2>
<ul>
<li><b>컨트롤러에서 인증 처리</b>:
<pre class="less"><code>
@Post('login')
async login(@Body() loginDto: LoginDto): Promise&lt;{ accessToken: string }&gt; {
  return this.authService.login(loginDto);
}
                </code></pre>
</li>
<li><b>서비스에서 토큰 생성</b>:
<pre class="typescript"><code>
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
  constructor(private readonly jwtService: JwtService) {}

  async login(user: any) {
    const payload = { username: user.username, sub: user.userId };
    return {
      accessToken: this.jwtService.sign(payload),
    };
  }
}
                </code></pre>
</li>
</ul>
<h2>5. 인증 가드(AuthGuard) 적용</h2>
<ul>
<li><b>JWT 전략 구현</b>:
<pre class="scala"><code>
import { PassportStrategy } from '@nestjs/passport';
import { ExtractJwt, Strategy } from 'passport-jwt';

export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor() {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      ignoreExpiration: false,
      secretOrKey: 'yourSecretKey',
    });
  }

  async validate(payload: any) {
    return { userId: payload.sub, username: payload.username };
  }
}
                </code></pre>
</li>
<li><b>가드 사용</b>:
<pre class="kotlin"><code>
@UseGuards(AuthGuard('jwt'))
@Get('protected')
getProtectedRoute() {
  return 'This is a protected route';
}
                </code></pre>
</li>
</ul>
<h2>6. 인증된 사용자 정보 가져오기 (@Req, @UseGuards)</h2>
<ul>
<li><b>사용자 정보 확인</b>:
<pre class="less"><code>
@Get('me')
@UseGuards(AuthGuard('jwt'))
getProfile(@Req() req) {
  return req.user;
}
                </code></pre>
</li>
<li><b>이점</b>: 인증된 사용자의 정보를 바로 활용 가능.</li>
</ul>
<h2>7. 토큰 검증 흐름 설명</h2>
<ol>
<li>클라이언트가 로그인 시도 &rarr; 서버에서 JWT 생성.</li>
<li>생성된 JWT는 클라이언트가 저장하고 이후 요청의 헤더에 포함.</li>
<li>서버는 요청을 받을 때 JWT의 서명을 검증 &rarr; 인증 성공 시 요청 처리.</li>
<li>토큰이 만료되거나 변조된 경우 &rarr; 요청 거부.</li>
</ol>
<h2>8. 보안 고려사항</h2>
<ul>
<li><b>토큰 만료 관리</b>: 짧은 만료 시간 설정 후 필요 시 갱신.</li>
<li><b>비밀 키 보호</b>: 환경 변수로 관리하고 버전 관리에서 제외.</li>
<li><b>HTTPS 사용</b>: 중간자 공격 방지.</li>
<li><b>추가 인증 방법</b>: 토큰 이외에도 IP 제한, 2FA 등 추가 보안 강화.</li>
</ul>
<p>이 주제를 따라 차근차근 코드를 작성하면 JWT 인증이 적용된 NestJS 애플리케이션을 만들 수 있습니다. ✨</p>