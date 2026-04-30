# Cross-Project Audit — NAVYA Ecosystem

**Audit Date:** 2026-04-30
**Auditor:** Qwen Code (Centaur Workflow)

---

## 1. Portfolio Website (portfolio-website)

**Repo:** https://github.com/navyapdh11/portfolio-website
**Deploy:** https://portfolio-website-perth-tea.vercel.app
**Stack:** Next.js 16.2.2 · React 19.2.4 · TypeScript 5 · Tailwind CSS v4
**Commits:** 115 | **Contributors:** 2

### Key Metrics
| Metric | Value |
|--------|-------|
| Overall Score | 47/100 |
| SSG Pages Generated | 1,087 |
| API Routes | 13 |
| Client Components | 35 ("use client") |
| Security | 25/100 |
| SEO | 55/100 |

### Critical Issues
1. Hardcoded admin secret (`aasta-clean-admin-2026`)
2. Prisma schema defined but NEVER used
3. In-memory data store — lost on every cold start
4. `/api/projects` and `/api/config` have zero authentication
5. Rate limiter exists but is never imported

### Top Recommendation
Wire Prisma to all API routes, add JWT auth, convert 20+ client components to Server Components.

---

## 2. Nepal Store (nepal-store)

**Repo:** https://github.com/navyapdh11/nepal-store
**Deploy:** Render Blueprint (Free Tier)
**Stack:** React 18 · Vite 5 · Express 4 · Prisma 5 · PostgreSQL
**Commits:** 28 | **Contributors:** 1

### Key Metrics
| Metric | Value |
|--------|-------|
| Overall Score | 24/100 |
| Products | 450 (9 categories × 50) |
| Components | 11 |
| Test Coverage | 3 passing Vitest tests |
| Security | 15/100 |
| SEO | 5/100 |
| UX/UI Design | 75/100 |

### Critical Issues
1. Mismatched JWT secrets across Express and Vercel services
2. Plaintext password storage and comparison
3. `.env` committed to git
4. Prisma/SQLite contradiction (schema says PostgreSQL, .env says SQLite)
5. SPA with no routing — all content at single URL (zero SEO value)

### Top Recommendation
Add react-router-dom routing, wire Prisma to database, fix authentication, add JSON-LD structured data.

### UX/UI Strengths
- Exceptional glassmorphism and 3D card hover effects
- Distinctive Nepali aesthetic (earthy tones, Dhaka-inspired accents)
- Clean bento grid homepage layout
- Premium HD photography presentation
- Well-implemented Framer Motion animations

---

## 3. NAVYA Local Dev Server (NAVYA-LOCAL-DEV-SERVER)

**Repo:** https://github.com/navyapdh11/NAVYA-LOCAL-DEV-SERVER
**Stack:** Python · FastAPI · Docker · MCP Servers
**Status:** Active development

### Key Features
- Governance dashboard with local SEO tools
- MCP server orchestration
- AI reasoning infrastructure
- Knowledge base with 3-layer architecture

---

## 4. Cross-Project Patterns

### Common Issues Across All Projects
1. **Security:** Hardcoded secrets, no auth middleware, plaintext passwords
2. **Database:** Prisma defined but unused across all projects
3. **Testing:** Minimal to no test coverage
4. **CI/CD:** No automated pipelines
5. **SEO:** Minimal structured data, no sitemaps, no meta descriptions

### Common Strengths
1. **Design:** Premium visual language (glassmorphism, bento grids, 3D effects)
2. **TypeScript:** Strict mode enabled, zero `any` types in portfolio-website
3. **Architecture:** Clean component separation, well-organized file structure
4. **AI Integration:** Nanochat, AI Companion Kernel, reasoning infrastructure

---

## 5. Priority Cross-Project Actions

| Priority | Action | Projects Affected |
|----------|--------|-------------------|
| P0 | Remove all hardcoded secrets | All 3 |
| P0 | Wire Prisma to databases | portfolio-website, nepal-store |
| P0 | Add bcrypt password hashing | nepal-store |
| P1 | Set up GitHub Actions CI/CD | All 3 |
| P1 | Add JSON-LD structured data | portfolio-website, nepal-store |
| P1 | Add meta descriptions + OG tags | nepal-store |
| P2 | Add unit + E2E tests | All 3 |
| P2 | Add rate limiting | All 3 |
| P2 | Implement product search | nepal-store |
| P3 | Version tagging | All 3 |
| P3 | Feature branch workflow | All 3 |

---

*Last updated: 2026-04-30*
