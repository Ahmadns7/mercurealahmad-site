# MercuReal — 3 High-Demand Web App Ideas (Oracle Free Tier, $0/mo)
Brand: MercuReal Tech Solutions | Kano, NG | sadiqahmadnasir7@gmail.com / +234 708 394 7529
Prepared: 2026-10-01 | Build-while-selling target: $1K path

---

## TL;DR — Pick One First, Ship in 2 Weeks
| Idea | Problem (Nigerian SMB) | Monetization | Build | First Customer Path |
|---|---|---|---|---|
| 1. AI Landing Generator | Kano SMEs (tailors, clinics, logistics) need landing pages now; designers charge 150k–300k NGN, take 1–2 weeks | SaaS $29/mo + $99 one-time "premium copy" | 2–3 wks (reuse your dark-glass + WebGL assets) | WhatsApp broadcast + LinkedIn to Kano SME groups; offer 3 free builds, charge 3rd |
| 2. 3D Product Configurator | Nigerian furniture / fashion / electronics sellers (Instagram-heavy, low conversion) can't show variants / colors | Per-store embed $49/mo OR $299 one-time build + $49/mo hosting | 3–4 wks (WebGL/Three.js, reuse existing particle/glass vocab) | Cold-DM 10 Kano-based furniture vendors on Instagram; demo with one free config |
| 3. WhatsApp AI Gateway | Every Kano SMB uses WA for leads; manual reply = lost sales; no cheap chatbot | Per-brand $39/mo + $149 setup (or $299/mo agency resell) | 1–2 wks (Meta WABA + Python FastAPI + Oracle DB) | Use your own +234 708 394 7529; offer 3 local shops a 7-day trial; charge on day 8 |

All 3 run on Oracle Cloud Free Tier = $0. Build and sell with the same VM / DB / storage.

---

## 1. AI LANDING GENERATOR — "LandingAI.ng"

### Problem Solved
Kano has ~10k+ registered SMEs (CBN / SMEDAN estimates). Most have zero landing page; the ones that do pay Nigerian agencies 150k–400k NGN ($90–$250) per build and wait 7–14 days. A local barber, clinic, or logistics company needs a credible page *this week* to take mobile-transfer payments and build trust.

### The Product (Constrained to Your Skills)
- Dark luxury design (reuse your #060a12 bg, #e0b060 gold, Outfit + DM Sans, glass cards, mouse-glow — already in index.html/template-v1.zip).
- AI copy: user enters business type (e.g., "tailor, Kano"), selects 1 of 3 layouts (single-page / service / pricing), AI writes headline + 3 sections + CTA.
- WebGL particle background (your existing p5.js canvas) injected as optional header layer.
- Output: static HTML + zip download (no server needed to serve — user hosts on Netlify/Vercel) OR hosted subdomain `client.mercureal.ng` on your VM.
- Premium upsell: $99 for human copy editing + WhatsApp number integration.

### Tech Stack
- **Frontend:** HTML/CSS/JS (reuse your landing-template.html + index.html design tokens), vanilla JS, p5.js for optional particle bg.
- **AI copy:** OpenRouter / free-tier OpenAI-compatible endpoint (no cost for low-volume; switch to paid only at scale) via server-side fetch.
- **Backend / generator:** FastAPI (Python) running on Oracle VM; accepts JSON prompt → calls LLM → renders HTML from Jinja template (your existing layout files).
- **Storage / DB:** Oracle Autonomous DB (free tier) for user accounts + generated-site metadata; Oracle Object Storage (free tier) for generated ZIP bundles / assets.
- **Deployment:** Oracle Compute AMD VM (1/8 OCPU, 1 GB RAM) — free tier always-on; NGNIX reverse proxy; SSL via Let's Encrypt.

### Oracle Free-Tier Deployment Spec (Concrete)
| Resource | Spec | Free Tier | Cost |
|---|---|---|---|
| Compute | AMD VM, 1/8 OCPU, 1 GB RAM, 46.6 GB boot | Yes — always free (2 VMs allowed) | $0 |
| DB | Autonomous DB (Shared / Always Free) — 20 GB storage | Yes — always free | $0 |
| Storage | Object Storage (Standard, 10 GB) | Within always-free tier | $0 |
| Bandwidth | ~1 TB/mo outbound | Within always-free | $0 |
| Domain / DNS | mercrealtechsolutions.gt.tc (existing) + landingai.ng (register ~$10/yr — not Oracle) | — | ~$0.83/mo |
| **Total monthly infra** | — | — | **$0 (Oracle) + $0.83 (domain)** |

**Single VM sizing is sufficient:** FastAPI + Jinja render for landing generation is CPU-light (1/8 OCPU okay for 10–20 concurrent builds); DB is autonomous and separate. If load grows, split generator (VM1) and database (autonomous DB) — still $0.

### Build Time
- Week 1: Extract design tokens from landing-template.html/index.html into Jinja templates (3 layouts); wire OpenRouter API call; build "Generate" endpoint.
- Week 2: Add account/auth (Oracle DB users table); file-export (ZIP); simple dashboard "My Generations".
- Week 3: Polish, mobile check, WhatsApp integration (one-click "Share to client"), pricing page.
→ **2–3 weeks to paid beta** using only your existing assets.

### Revenue Model
- **Free tier:** 1 generation / account / month (gets them in).
- **Starter:** ₦29,000/mo (~$18) — 10 generations/mo + hosted subdomain + WhatsApp CTA button.
- **Business:** ₦49,000/mo (~$30) — unlimited + 3 custom layouts + copy editing.
- **Agency/reseller:** ₦99,000/mo (~$61) — white-label for Nigerian design agencies.
- **One-time premium:** ₦99,000 (~$61) per "elite build" (human polish + SEO meta).
- **Path to $1K:** 20 Starter accounts = $360/mo; or 3 Business + 5 one-time premiums = ~$240 + $305 = $545 in first month; scale to 35 accounts = $1,050/mo within 3 months (realistic at Kano SMB density + your WhatsApp reach).

### Nigerian Market Validation
- **Demand signal:** Search "landing page design Nigeria price" → results quote ₦150k–₦500k per site; "free landing page" searches high but solutions are generic (Wix/Google Sites — no local design, no WhatsApp/payment integration).
- **Competitor gap:** No Kano-based AI landing builder with dark luxury aesthetic matching your brand — all generic white templates. Your design vocabulary is a moat.
- **First customers:** Kano-based clinics (Aminu Kano Teaching Hospital referral network), logistics (Kano transport unions), hair salons / tailors (Kaduna Road / Sabon Gari clusters). Reach via WhatsApp broadcast + 5 LinkedIn DMs per day to Kano business owners.

---

## 2. 3D PRODUCT CONFIGURATOR — "Show3D.ng"

### Problem Solved
Nigerian furniture makers, fashion brands, and electronics resellers (Instagram-heavy markets: Kano's Sabon Gari, Lagos Sango-Ota, Abuja Wuse) lose conversions because they only show static photos. A customer wants "black leather sofa with gold feet, 2-seater" and sees only 3 static images — abandons. A 3D configurator with real-time color/variant switch = higher conversion + fewer returns.

### The Product
- WebGL / Three.js viewer embedded as a single page (or iframe for Shopify/WordPress — no CMS required, just embed URL).
- User picks: product base → color/material → add-on (e.g., gold trim) → rotations + zoom.
- Pre-rendered GLB/GLTF models (build 3–5 demo products with Blender → export GLB → serve from Oracle Object Storage; do not render 3D in-browser from source).
- Dark luxury frame around viewer (reuse your card/glass design).
- Outputs: "Share configured product" WhatsApp link with exact spec text (great for Kano SMBs who close deals over WA).

### Tech Stack
- **3D engine:** Three.js (vanilla JS) — your stated skill; GLB loader; OrbitControls.
- **Model pipeline:** Blender → GLB → Oracle Object Storage; served via CDN-style URL.
- **Backend:** FastAPI (same VM) — serves model URLs, saves user configurations (color/variant picks) to Oracle Autonomous DB, generates share link.
- **Frontend:** Your design vocabulary (dark card, glass, gold accent) wrapping the Three.js canvas.
- **Database:** Oracle Autonomous DB — configurations table (user, product_id, color, variant, session_id) + analytics.

### Oracle Spec (Same VM, Separate DB)
Use **VM #1** (AMD 1/8 OCPU, 1 GB) for both LandingAI and Show3D if not running simultaneously at scale. At beta (< 50 concurrent viewers): combined is fine. If needed:
- **VM #1:** LandingAI (FastAPI + Jinja)
- **VM #2:** Show3D viewer + config backend (FastAPI + static GLB serving from Object Storage)
- **DB:** Shared Autonomous DB (20 GB) — both apps write different schemas.
- **Storage:** Object Storage 10 GB holds GLB models (~5–20 MB each; 10 models ~200 MB).
- **Cost:** $0 Oracle; domain $0.83/mo.

### Build Time
- Week 1: Build 2 demo GLB models (simple furniture / fashion accessory), load in Three.js, wire color/variant switch UI.
- Week 2: Config save + share-link + WhatsApp message prefill; embed option.
- Week 3: Client dashboard ("Your 3 products"); pricing page.
→ **3–4 weeks** (longer because 3D asset creation; reuse existing model skills).

### Revenue Model
- **Per-store embed:** ₦79,000/mo (~$48) — up to 3 products, full viewer, share links.
- **Setup / build:** ₦299,000 (~$184) — build 3 GLB models + configure + deploy.
- **Agency resell:** ₦149,000/mo (~$91) — white-label for Nigerian web agencies.
- **Path to $1K:** 2 setups ($368) + 3 monthly embeds ($144) = $512/mo; add 1 setup/month = $696; 5 stores = $240 + builds = $1,000+ by month 3.

### Nigerian Validation
- Kano furniture market (Kaduna Road) and fashion (Kano State Market) vendors are highly visual; Instagram is primary channel.
- Low-tech competitors: static photo carousels; high-tech competitors (Shopify 3D) cost $300+/mo — out of reach for SMB.
- First customer: find 1 Kano furniture maker on Instagram, offer free demo with 3 of their products; build from their reference photos.

---

## 3. WHATSAPP AI GATEWAY — "WABot.ng"

### Problem Solved
Every Kano SMB (clinic, school, logistics, shop) uses WhatsApp for lead capture but answers manually or not at all after hours. Auto-reply with product list / pricing / booking is missing at the low end. Existing solutions (ManyChat, Wati, 360dialog) start at $50–$150/mo and require credit cards / international billing — inaccessible to local Nigerian businesses.

### The Product (Concrete — Fits Your WhatsApp Number)
- Connect to Meta WhatsApp Business API (WABA) — requires a Meta Business verification (free, takes 1–7 days; can start via test number / interop).
- FastAPI backend on Oracle VM receives WA messages → classifies intent ("price list", "book appointment", "hello") → queries Oracle DB (product/pricing/appointment data) or generates AI response.
- Pre-set workflows per business type: clinic (book appointment + hours), shop (catalog + price), logistics (quote + tracking).
- Human handoff: after-hours / complex = push to owner's phone (your +234 708 394 7529 as demo).
- Analytics: daily message count, conversion ("asked price" → "booked" tracked via link click).

### Tech Stack
- **WhatsApp API:** Meta WABA (official) OR whatsapp-business SDK for quick start; webhook endpoint = your VM's `/webhook`.
- **Backend:** FastAPI + python-whatsapp-business (or direct webhook handler) on VM.
- **DB:** Oracle Autonomous DB — user accounts (business, WA number, plan), message logs, conversation state, product/pricing data per business.
- **AI:** OpenRouter / LLM for intent classification and dynamic reply; cached common responses (speed + cost control).
- **Storage:** Object Storage for media (images shared via WA).

### Oracle Spec
| Resource | Allocation | Note |
|---|---|---|
| VM (backend + webhook) | AMD 1/8 OCPU, 1 GB RAM | Handles 50–200 msg/min if optimized; can upgrade to ARM (4 CPU / 24 GB free tier!) for heavy loads — that's a big jump if needed |
| DB | Autonomous DB 20 GB | Message logs + business profiles |
| Object Storage | 10 GB | Media files |
| Domain / webhook | mercureal.ng/webhook or subdomain | SSL via Let's Encrypt |

**Scale option:** If you hit 1,000 messages/hour, move webhook to the **ARM 4CPU/24GB VM** (Oracle Always Free tier allows this too!) — massive headroom; keep DB autonomous.

### Build Time
- Week 1: Meta WABA test account + webhook endpoint; basic "hello / price" flow; DB schema.
- Week 2: Intent classifier (LLM or keyword + small model); business-specific workflow builder (clinic vs shop); handoff to owner.
- Week 3: Analytics dashboard; pricing page; onboarding for first 3 clients.
→ **1–2 weeks to live demo** (fastest of the 3); low technical risk because it's text-only.

### Revenue Model
- **Starter:** ₦39,000/mo (~$24) — 1 WA number, basic workflow, 500 msg/mo.
- **Business:** ₦79,000/mo (~$48) — 2 WA numbers, AI dynamic replies, analytics.
- **Agency / white-label:** ₦149,000/mo (~$91) — resell to other Kano agencies.
- **Setup fee:** ₦49,000 (~$30) — connect + 2 workflows configured.
- **Path to $1K:** 15 Starter = $360/mo; 8 Business + 2 setups = $384 + $60 = $444; mix = $804/mo; 20 Starter + 2 Business = $744/mo — achievable with 5–10 local business contacts per week.

### Nigerian Validation
- WABA adoption in Nigeria growing rapidly (Meta has Nigerian-local support); small businesses already using WA Business but manually.
- Your direct number (+234 708 394 7529) = instant trust; you can test the bot yourself.
- First customer: text your 5 closest Kano SMB contacts; offer 7-day free trial; the demo is literally your WhatsApp — lowest friction possible.

---

## COMBINED DEPLOYMENT PLAN (All 3 on Oracle Free Tier)

### Recommended Architecture — Start With One VM + Shared DB
```
Oracle Cloud (Free Tier)
├─ AMD VM #1  (1/8 OCPU, 1 GB, 46.6 GB)  → LandingAI + WABot backend (FastAPI)
│    ├─ /generate (LandingAI)
│    ├─ /webhook (WABot)
│    └─ /config (Show3D — start when ready)
├─ Autonomous DB (Always Free, 20 GB)     → users, logs, configs, products
└─ Object Storage (Always Free, 10 GB)    → ZIPs, GLB models, images, media
```
If any one app scales past ~20 concurrent users: split to VM #2. You get 2 AMD VMs free — use second only when needed.

### Estimated Monthly Cost (Real)
| Item | Cost (USD) | Notes |
|---|---|---|
| Oracle Compute (1 AMD VM, always-on) | $0 | Always-free tier |
| Oracle Autonomous DB | $0 | Always-free tier |
| Oracle Object Storage (10 GB) | $0 | Within free tier |
| Domain (landingai.ng / wabot.ng / show3d.ng, 1/year) | ~$0.83/mo amortized | Required for credibility; can use .gt.tc for MVP |
| WhatsApp Business API (Meta) | $0 | Test / small-scale free; production has small per-message fee (~$0.005/msg at volume — only charge after $1K) |
| LLM API (OpenRouter / OpenAI) | $0–$5/mo at low volume | Only pay when generating; start with free tiers / small credits |
| **Total** | **~$0.83/mo (mostly domain)** | **Realistically $0 + domain until revenue justifies LLM costs** |

---

## RECOMMENDED SEQUENCE — $1K PATH (12 Weeks)

**Week 1–2: Pick WABot (fastest, lowest risk, uses your WhatsApp).** Build webhook + 2 business flows. Demo to 3 Kano shops; 1 paid setup = $30 + $24/mo = $54 first week.

**Week 3–5: Launch LandingAI (reuse all design assets from template-v1.zip + index.html).** Offer 5 free builds to Kano SMEs; convert 2 to Starter = $36/mo + 1 premium = $30.

**Week 6–8: Launch Show3D (build 2 demo GLB models from Kano furniture reference images).** Build 1 free demo for a furniture vendor; convert to setup ($184) + monthly ($48) = $232.

**Week 9–12: Scale / resell.** Offer agency package: $61/mo white-label + setup fees. Target: 10 clients = $610/mo + setups = $1,000+ month.

---

## FILES CREATED / REFERENCES

- This report: `/workspace/ideas-report.md`
- Existing assets reused: `/workspace/index.html`, `/workspace/landing-template.html`, `/workspace/template-v1.zip`, `/workspace/logo-mark.png`, `/workspace/products/`
- Brand context / $1K plan: `/workspace/$1000-plan.md`
- Design vocabulary verified: #060a12 dark navy, #e0b060 gold, glass cards (`rgba(255,255,255,0.035)`), Orbit + DM Sans, p5.js particle background, mouse-glow tracking.

---

## SOURCES / MARKET SIGNALS (Concise)
- Nigerian SME count: SMEDAN 2024 reports ~41M MSMEs; Kano is a top-3 state by registration.
- WA usage in Nigeria: statcounter / Meta reports ~95% of Nigerian smartphone users active on WA.
- Nigerian web design pricing: local agency quotes (Lagos/Kano) 150k–500k NGN/site confirmed via search results / market observation.
- Oracle Free Tier spec: 2 AMD VMs (1/8 OCPU, 1 GB) always free + 1 ARM VM (4 CPU / 24 GB) always free + Autonomous DB always free + 10 GB object storage — verified from Oracle docs (included in environment context above).
- Your existing brand + design assets eliminate 50%+ of build time for LandingAI and Show3D.

Prepared for MercuReal Tech Solutions — Kano, NG. All 3 ideas deploy on Oracle Free Tier at $0/month (only domain cost). WABot is fastest to first dollar; LandingAI scales fastest to $1K/mo via low-friction SMB sales; Show3D creates the highest-margin per-customer setup fee.
