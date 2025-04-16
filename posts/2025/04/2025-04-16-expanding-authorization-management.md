# Expanding Authorization Management
**Posted on**: 2025-04-16

Expanding Authorization Management in NestJS


  <h1>Expanding Authorization Management in NestJS</h1>

  <p>
    In the previous article, we implemented a basic JWT authentication flow. In this follow-up, 
    we’ll enhance our setup by introducing <strong>role-based authorization</strong>. This involves defining 
    roles such as <strong>admin, user, and guest</strong>, and controlling access to specific APIs based on these roles.
  </p>

  <h2>1. What is Role-Based Authorization?</h2>
  <ul>
    <li>Authorization is granted based on the user's assigned roles.</li>
    <li>Example: Admins can access all APIs, regular users can access certain features, and guests may have read-only permissions.</li>
  </ul>

  <h2>2. Adding Roles to the User Object</h2>
  <p>Include the role information in the JWT payload when generating tokens:</p>
  <pre><code>
const payload = {
  username: user.username,
  sub: user.userId,
  role: user.role // e.g., 'admin', 'user', 'guest'
};
  </code></pre>

  <h2>3. Creating a Custom Decorator - Roles()</h2>
  <p>We create a custom decorator to define roles for handlers:</p>
  <pre><code>
// roles.decorator.ts
import { SetMetadata } from '@nestjs/common';

export const Roles = (...roles: string[]) => SetMetadata('roles', roles);
  </code></pre>

  <h2>4. Implementing the RolesGuard</h2>
  <pre><code>
// roles.guard.ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.getAllAndOverride('roles', [
      context.getHandler(),
      context.getClass(),
    ]);
    if (!requiredRoles) return true;

    const { user } = context.switchToHttp().getRequest();
    return requiredRoles.includes(user.role);
  }
}
  </code></pre>

  <h2>5. Applying Roles in Controllers</h2>
  <pre><code>
@UseGuards(AuthGuard('jwt'), RolesGuard)
@Roles('admin')
@Get('admin-data')
getAdminData() {
  return 'This API is accessible by admins only.';
}
  </code></pre>

  <h2>6. Security Design Tips</h2>
  <ul>
    <li>Standardize roles using enums to prevent typos</li>
    <li>Manage roles in the database for easier updates</li>
    <li>Provide clear error messages for unauthorized access</li>
  </ul>

  <p>
    By following these steps, you can expand NestJS applications from simple authentication 
    to detailed authorization management, resulting in a more secure and flexible system.
  </p>