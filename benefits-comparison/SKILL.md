---
name: benefits-comparison
description: Compare employee benefits packages across two or more employers to find the optimal enrollment strategy for a family or individual. Use this skill proactively whenever someone mentions open enrollment, a spouse or family member starting a new job with benefits, "which plan should I pick", putting kids on one parent's insurance versus another, HSA vs FSA decisions, dual coverage or coordination of benefits, or comparing medical/dental/vision plans between employers. Invoke this skill even if the user doesn't say "benefits comparison" — any time someone is trying to decide how to allocate a family across multiple employer health insurance options, this skill applies.
argument-hint: "[path to benefits documents folder]"
---

# Benefits Comparison

## What This Skill Does

Guides a complete analysis of multiple employer benefit packages to find the lowest true-cost enrollment strategy for a family, accounting for:

- Medical, dental, and vision premiums by enrollment tier
- Deductibles, out-of-pocket maximums, and copay structures
- HSA and FSA eligibility and tax savings
- Coordination of benefits (COB) when both spouses have employer coverage
- Orthodontic, specialty care, and network availability
- Qualifying life event (QLE) windows and action deadlines

Outputs a formatted Word document (`generate_report.py`) with full scenario rundowns.

---

## Phase 1 — Ask Clarifying Questions First

**Before reading any documents**, gather the following. Some answers will be obvious from the conversation — only ask about what you don't already know. Ask in a conversational way, not as a rigid questionnaire.

### Family profile (always ask if not provided)
- Who is in the family? Names, relationships, approximate ages — especially children's ages, since pediatric copays and orthodontic timing matter.
- Any known or anticipated health needs? Orthodontics, chronic conditions, planned procedures, pregnancy, frequent sick visits, mental health, specialty care?
- What city and state does the family live in? (Some networks — like Kaiser — are unavailable in rural areas. Confirming location rules out options early.)

### Employer details (always ask if not provided)
- Which employers are offering coverage, and who is the employee at each?
- What are the plan year dates for each employer? (e.g., Jan–Dec, Apr–Mar, Jul–Jun) — these affect proration and QLE windows.
- What is each employee's pay frequency? (Biweekly = 26 pay periods; semi-monthly = 24; monthly = 12)

### Current enrollment (ask if triggered by a life event)
- Who is currently enrolled on what plan?
- Is there an active HSA? Current balance? Annual contribution?
- Is anyone contributing to an FSA (Health Care or Dependent Care)?
- Is there a qualifying life event triggering this review? If so, when exactly does the QLE window close?

### Follow-up clarifications (ask if ambiguous after reading documents)
- If a plan is labeled with a dollar amount (e.g., "HDHP 1700"), confirm what that number refers to — it's usually the individual deductible, but verify.
- If the user says "everyone is on my plan," confirm the exact enrollment tier (Family vs. Employee + Children vs. Employee + Spouse).
- If a rate table has rows for different hours-worked tiers (e.g., "30+ hours" vs. "36+ hours"), ask which tier the employee qualifies for.
- If the plan document is dated more than two years ago, note it and ask the user to confirm with HR that the benefits haven't changed.

---

## Phase 2 — Extract Plan Data

For each employer, extract plan details from provided documents. Medical first, then dental and vision.

### Handling image-based PDFs

Many benefit booklets are scanned — the `Read` tool will return 0 characters or only metadata. If this happens, use the bundled render script:

```bash
python3 scripts/render_pdf_pages.py "path/to/booklet.pdf" "output/pages_dir" --scale 2
```

Read the rendered PNG files visually. For hard-to-read rate tables, re-render those specific pages at `--scale 4` and crop if needed.

### Medical plan extraction checklist

For each plan:

| Field | Notes |
|-------|-------|
| Plan name / type | HDHP, PPO, HMO, EPO |
| HSA eligible? | HDHP with 2026 IRS minimums: $1,700 ind / $3,400 fam deductible |
| Deductible — ind / fam | |
| Out-of-pocket max — ind / fam | |
| PCP copay | Does deductible apply first, or is copay flat? |
| Specialist copay | |
| Urgent care copay | |
| Emergency room | Copay + coinsurance? |
| Rx — generic / brand / specialty | |
| Outpatient surgery / hospital stay | |
| Labs / imaging | |
| Premiums by tier | EO, EE+Spouse, EE+Children, Family — note pay period unit |
| Employer HSA contribution | Annual amount, if any |
| Network carrier | Regence, Blue Shield, Cigna, etc. |

### Dental plan extraction checklist

| Field | Notes |
|-------|-------|
| Annual max per person | |
| Deductible — ind / fam | Is it waived for preventive? |
| Preventive (Class I) | Typically 100% |
| Basic / Restorative (Class II) | |
| Major — crowns, etc. (Class III) | |
| Orthodontics | Lifetime max payout? Age limit (adults included)? |
| Waiting periods | By service class? |
| Premiums by tier | |

### Vision plan extraction checklist

| Field | Notes |
|-------|-------|
| Exam copay / frequency | Every 12 months? |
| Frame allowance — standard / featured | |
| Contact lens allowance | |
| Standard progressive copay | |
| Premium / custom progressive copay | |
| Premiums by tier | Confirm $0 tiers are truly $0 |
| Network | VSP, EyeMed, etc. |

---

## Phase 3 — Build Enrollment Scenarios

Always model these standard scenarios, adapted to the actual plans available. Eliminate options unavailable in the family's region before building scenarios.

| Scenario | Description |
|----------|-------------|
| Status Quo | Everyone on Employee A's current plan |
| Split — Kids to Spouse's Plan | Employee A self-only + spouse self-only on their plan + kids on spouse's plan |
| Split — Kids to Employee A's Plan | Employee A + children on their plan + spouse self-only on theirs |
| Double Coverage — Employee A joins Spouse's Plan | Employee A on both plans, family arrangement TBD |
| Upgrade Employee A's Plan | Employee A moves to a lower-deductible plan at their employer |
| Optimized Custom | Whatever the data suggests is the true cost winner |

**Ask the user:** "Are there specific scenarios you'd like me to include or compare?" — they may have a hunch worth modeling.

---

## Phase 4 — Apply Rules

Read `references/hsa_fsa_rules.md` before calculating any scenario involving an HDHP.
Read `references/cob_rules.md` before calculating any dual-coverage or birthday-rule scenario.

### Quick-reference rules

**HSA eligibility**
- Employee must be on an HSA-qualified HDHP with no other disqualifying health coverage.
- Spouse on a non-HDHP does NOT disqualify the employee — unless the spouse's plan also covers the employee.
- Spouse must waive any general-purpose Health Care FSA at their employer to protect the employee's HSA. A Limited-Purpose FSA (dental/vision only) is fine.
- Dental and vision stand-alone plans do NOT disqualify an HSA.
- 2026 HSA limits: $4,400 self-only / $8,750 family; catch-up (55+): +$1,000.

**Dependent Care FSA**
- Fully compatible with HSA — no conflict.
- 2026 limit: $5,000/yr (married filing jointly).
- Covers daycare, preschool, after-school programs for children under 13.
- Does NOT cover informal grandparent care unless the caregiver is unrelated and can provide a TIN for tax purposes.
- Can enroll mid-year on a QLE (starting new daycare counts).

**QLE windows**
- Typically 30 days from the qualifying event to change elections at each employer.
- Confirm the exact window with each HR team — some employers allow 31 days or have different rules.

---

## Phase 5 — Calculate Costs

For each scenario:

```
Annual Premium  = biweekly premium × 26  (or monthly × 12)
                  — sum all plans the family is enrolled in

HSA Tax Savings = (employee HSA contribution + employer HSA contribution)
                  × marginal tax rate
                  — use 22% federal if unknown; ask user if they know their bracket

DCFSA Savings   = DCFSA contribution × marginal tax rate

Estimated OOP   — use judgment based on family profile:
  • Young healthy adults:             10–20% of individual OOP max
  • Children, frequent illness:       $500–$1,500/yr per child (HDHP = no copays until deductible met)
  • PPO with copays:                  estimate visit count × copay amount
  • Known procedures (ortho, etc.):   use actual plan benefit amounts

Net Annual Cost = Annual Premium + Estimated OOP
                − HSA Tax Savings − DCFSA Savings
```

**If the user knows their actual healthcare usage, ask them to describe it** and use that instead of estimates.

---

## Phase 6 — Generate the Word Document

Once all scenarios are calculated, write a `data.json` file using the schema below, then run:

```bash
python3 scripts/generate_report.py data.json --output "LastName_Benefits_Comparison_YYYY-YY.docx"
```

Requires: `python3 -m pip install python-docx`

### data.json schema

```json
{
  "report_title": "LastName Family Benefits Comparison YYYY-YY",
  "generated_date": "YYYY-MM-DD",
  "family": {
    "last_name": "...",
    "members": [
      {"name": "...", "relationship": "Employee (Employer 1)", "notes": ""}
    ],
    "location": "City, State"
  },
  "employers": [
    {
      "name": "...",
      "primary_employee": "...",
      "plan_year": "Month – Month",
      "pay_periods_per_year": 26,
      "medical_plans": [
        {
          "name": "...",
          "type": "HDHP",
          "hsa_eligible": true,
          "deductible_individual": 0,
          "deductible_family": 0,
          "oop_max_individual": 0,
          "oop_max_family": 0,
          "pcp_copay": "...",
          "specialist_copay": "...",
          "urgent_care_copay": "...",
          "er_cost": "...",
          "rx_generic": "...",
          "rx_brand": "...",
          "premiums_by_tier": {
            "employee_only": 0.00,
            "employee_spouse": 0.00,
            "employee_children": 0.00,
            "family": 0.00,
            "tier_unit": "biweekly"
          }
        }
      ],
      "employer_hsa_contribution_annual": 0,
      "dental": {
        "carrier": "...",
        "annual_max_per_person": 0,
        "deductible_individual": 0,
        "preventive_pct": 100,
        "basic_pct": 0,
        "major_pct": 0,
        "ortho_benefit": "...",
        "premiums_by_tier": {}
      },
      "vision": {
        "carrier": "...",
        "exam_copay": 0,
        "frame_allowance_standard": 0,
        "frame_allowance_featured": 0,
        "contacts_allowance": 0,
        "premium_progressive_copay": "...",
        "premiums_by_tier": {}
      }
    }
  ],
  "scenarios": [
    {
      "id": "1",
      "name": "Scenario 1 — ...",
      "description": "...",
      "assignments": {"MemberName": "PlanName"},
      "annual_premiums": 0.00,
      "hsa_eligible": false,
      "hsa_employer_contribution": 0,
      "hsa_tax_savings": 0,
      "dcfsa_tax_savings": 0,
      "estimated_oop": 0,
      "net_annual_cost": 0,
      "pros": ["..."],
      "cons": ["..."],
      "recommended": false,
      "recommendation_note": ""
    }
  ],
  "recommendation": {
    "best_scenario_id": "...",
    "headline": "...",
    "reasoning": "...",
    "action_items": [
      {"task": "...", "deadline": "...", "owner": "..."}
    ]
  },
  "dental_vision_comparison": "...",
  "additional_notes": "..."
}
```

---

## Phase 7 — Deliver the In-Chat Summary

After saving the Word document, give the user a short in-chat summary:

1. Recommended scenario — 1–2 sentences on why
2. Estimated annual savings vs. status quo
3. Top 2–3 action items with deadlines
4. Path where the Word document was saved

---

## Tips and Edge Cases

- **Image-based PDFs are common** — Always try `Read` first; if it returns fewer than 100 characters of actual content, treat it as image-based and use `render_pdf_pages.py`.
- **Plan year mismatches** — If two employers have different plan years, note it in the report. Mid-year changes, prorated costs, and staggered QLE windows get complicated.
- **Self-insured plans (e.g., RETA Trust)** — Catholic school systems often use RETA Trust, administered by Blue Shield of California. Claims are self-insured, not underwritten insurance. Fine for in-network use; note it if there are concerns about out-of-state coverage.
- **Regional network gaps** — Always confirm the plan's network covers the family's location before modeling it as an option. Kaiser, for example, is unavailable in most rural areas.
- **Ortho timing** — If a child is near typical ortho age (11–14), the lifetime orthodontic maximum becomes a significant plan differentiator. Ask whether the user expects to use this benefit.
- **Stale documents** — Check the effective date on every plan summary. A dental summary from 2019 may not reflect current benefits. Flag it and recommend confirming with HR.
- **Employer HSA contributions** — Often buried in the benefit booklet, not on the rate sheet. Search for "HSA," "Health Savings," or "employer contribution" in the booklet.
- **When the user pushes back on a recommendation** — They often know something you don't (usage patterns, proximity to a specific provider, upcoming procedure). Ask before defending the math.
