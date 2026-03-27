# 🔎 PRM Open-Source Reference Shortlist (Next.js + Prisma)

> Filter used: Next.js App Router projects, Prisma ORM, 100+ stars, permissive license (MIT), and recently updated.  
> Stars/recency snapshot: 2026-03-27.

### 🚀 Top Best & Related Links (Quick Access)

**Top Best (start here)**
1. [next-saas-stripe-starter](https://github.com/mickasmt/next-saas-stripe-starter) — strongest overall for Auth.js + Prisma + Stripe billing/webhooks + admin patterns.
2. [chadnext](https://github.com/moinulmoin/chadnext) — great Lucia + Prisma + Stripe + OTP/email template reference.
3. [nextcrm-app](https://github.com/pdovhomilja/nextcrm-app) — best production-style admin/CRM architecture and transactional email patterns.

**Related Links**
- [next-auth-roles-template](https://github.com/mickasmt/next-auth-roles-template)
- [saasy-land](https://github.com/pjborowiecki/saasy-land)
- [codebaseup-core](https://github.com/jhavej/codebaseup-core)

| Repository | Stars | Reuse Best For | Files/Folders to Study |
|---|---:|---|---|
| [mickasmt/next-saas-stripe-starter](https://github.com/mickasmt/next-saas-stripe-starter) | 2968 | Auth.js + Prisma JWT session flow, RBAC/admin patterns, SaaS billing (Stripe checkout, webhooks, customer portal), React Email/Resend setup | `auth.ts`, `prisma/schema.prisma`, `app/api/webhooks/stripe/route.ts`, `actions/generate-user-stripe.ts`, `actions/open-customer-portal.ts`, `app/(protected)/admin`, `app/(protected)/dashboard`, `lib/subscription.ts`, `lib/stripe.ts`, `lib/email.ts`, `emails/magic-link-email.tsx` |
| [moinulmoin/chadnext](https://github.com/moinulmoin/chadnext) | 1322 | Lucia auth starter patterns, Stripe + webhook routes, OTP UI primitives, React Email templates | `prisma/schema.prisma`, `src/lib/server/auth/`, `src/app/api/auth/`, `src/app/api/stripe/`, `src/app/api/webhooks/`, `src/lib/server/payment.ts`, `src/components/ui/input-otp.tsx`, `emails/verification.tsx`, `emails/thanks.tsx` |
| [mickasmt/next-auth-roles-template](https://github.com/mickasmt/next-auth-roles-template) | 336 | Clean role-based auth (Auth.js + Prisma), user role management, admin dashboard skeleton | `auth.ts`, `actions/update-user-role.ts`, `components/forms/user-role-form.tsx`, `app/(protected)/admin`, `app/(protected)/layout.tsx`, `config/dashboard.ts`, `prisma/schema.prisma`, `emails/magic-link-email.tsx` |
| [pdovhomilja/nextcrm-app](https://github.com/pdovhomilja/nextcrm-app) | 561 | Production-grade admin/CRM dashboard architecture, approval/workflow style APIs, rich transactional emails, auth guard patterns | `app/[locale]/`, `app/api/`, `lib/auth.ts`, `lib/auth-guards.ts`, `prisma/schema.prisma`, `emails/PasswordReset.tsx`, `emails/InviteUser.tsx`, `emails/NewTaskComment.tsx` |
| [pjborowiecki/saasy-land](https://github.com/pjborowiecki/saasy-land) | 425 | Multi-tenant SaaS starter structure with NextAuth v5 + Prisma branch options, App Router organization, billing scaffolding patterns | `src/auth.ts`, `src/app/`, `src/actions/`, `src/lib/`, `src/app/api/auth/`, `prisma/schema.prisma` |
| [jhavej/codebaseup-core](https://github.com/jhavej/codebaseup-core) | 121 | Minimal but clean App Router + NextAuth + Prisma monorepo boilerplate for extracting auth/session/base RBAC plumbing | `apps/`, `packages/`, `.env.local.example`, `README.md` |

### Feature-to-Repository Mapping (for your PRM requirements)

1. **Authentication System (multi-role, JWT/session, RBAC)**  
   Start with: `next-saas-stripe-starter`, `next-auth-roles-template`, `chadnext`

2. **Payment Integration (commissions/split payouts/invoices)**  
   Best Stripe foundations: `next-saas-stripe-starter`, `chadnext`  
   Note: true **Stripe Connect split payout** logic (platform fee + partner/supplier transfers) is typically custom and not fully implemented in these starters.

3. **Admin Dashboard (user mgmt, workflows, analytics, audit trail patterns)**  
   Start with: `nextcrm-app`, `next-saas-stripe-starter`, `next-auth-roles-template`

4. **Multi-tenant SaaS Billing (plans, usage, portal, webhooks)**  
   Start with: `next-saas-stripe-starter`, `saasy-land`

5. **Real-time Notifications (in-app + email triggers)**  
   Closest reusable building blocks here are from `nextcrm-app` (`app/api/*`, email/event workflow patterns) and `chadnext` webhook pipeline.  
   For strict Supabase Realtime/Pusher channels, you’ll likely compose this layer on top of these starters.

6. **Email Templates (React Email/Resend)**  
   Start with: `nextcrm-app`, `chadnext`, `next-saas-stripe-starter`, `next-auth-roles-template`
