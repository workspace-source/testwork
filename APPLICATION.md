# Claude for Startups — Application Draft (ReviewPilot)

> Replace everything in [brackets] with your real info. Only claim what is true.

## Checklist before applying
- [ ] Founded in the last 5 years (or funded in the last 2) — company registered
- [ ] Claude Console account created **with your company email**
- [ ] Company email domain matches the website domain
- [ ] Website live (deploy `index.html` to Vercel/Netlify/GitHub Pages and connect your domain)
- [ ] Code pushed to a public/private GitHub repo you can link
- [ ] Apply logged in from the same company-email account

## Company description (short)
ReviewPilot is an AI code review and documentation agent for small development teams. It uses Claude to analyze git diffs for bugs and security risks and to generate documentation that stays in sync with the code. We are in private beta, with a working CLI prototype and a GitHub Action in development.

## What are you building?
Small teams (2–20 developers) rarely have time for thorough code review, and their docs go stale. ReviewPilot plugs into their git workflow and returns structured, file-specific review feedback and up-to-date documentation, so senior engineers spend less time on routine review.

## How will you use Claude?
- Claude API (Messages) as the core engine for diff review and docs generation
- Long-context analysis of diffs and multi-file context
- Structured markdown outputs consumed by a GitHub Action to post inline PR comments
- Planned: tool use for fetching repo files on demand, and prompt caching for repeated repo context to control cost

## Current stage / traction
- Stage: pre-seed / bootstrapped, MVP in development and internal testing
- Built: CLI prototype (`reviewpilot.py`), landing page
- Next 90 days: GitHub Action, test on [N] open-source repos, onboard [5–10] beta teams
- Traction: [waitlist signups / beta users — only real numbers]

## Why credits matter
Credits let us run evaluation across many real repositories to tune review quality and measure cost per review before we start charging, which is the main risk for a usage-based product.

## Business model
Per-seat SaaS for teams: [Free tier for OSS, ~\$15–25/dev/month for teams].

## Go-to-market
Open-source maintainers first (free tier, GitHub Marketplace listing), then small startups via developer communities and content on code review quality.

## 12-month goals
- 50 active teams, GitHub Marketplace listing, reviewed-PR volume of [X]/month
