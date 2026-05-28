# Coordination of Benefits (COB) Rules Reference

## What Is COB?

When a person is covered by two health plans simultaneously, Coordination of Benefits rules determine:
1. Which plan pays first (primary)
2. Which plan pays second (secondary)

The secondary plan can pick up some or all of what the primary didn't pay, potentially reducing out-of-pocket costs significantly. However, dual coverage is not always worth the extra premium.

---

## Birthday Rule — For Dependent Children

When children are covered by both parents' employer plans, the **birthday rule** determines which plan is primary:

> **The parent whose birthday falls earlier in the calendar year has primary coverage for the children.**

- Compare **month and day only** — the year of birth is irrelevant.
- If both parents share the same birthday, the parent who has been covered longer under their current plan is primary.

**Example:**
- Parent A born March 15 → birthday = March 15
- Parent B born December 30 → birthday = December 30
- **Parent A's plan is primary** for the children because March comes before December.

**Practical implication:** Always identify which parent has the earlier birthday before modeling dual-coverage scenarios for children. The plan that is primary absorbs the bulk of costs first.

**Exception:** If the parents are separated, divorced, or have a court order specifying coverage, that order governs regardless of birthdays.

---

## Employee Coverage (For the Employee Themselves)

For an employee who is enrolled in both their own employer's plan and a spouse's plan:
- **Primary:** The employee's own employer plan
- **Secondary:** The spouse's plan

This means if Employee A joins Employee B's plan:
- For A's own medical expenses: A's plan pays first, B's plan pays second
- For B's own medical expenses: B's plan pays first, A's plan pays second
- For children covered by both: birthday rule applies

---

## How Secondary Coverage Works

After the primary plan processes a claim, the process is:

1. Primary plan pays its share and issues an Explanation of Benefits (EOB)
2. EOB is submitted to the secondary plan (sometimes automatically, sometimes the member must submit it)
3. Secondary plan calculates what it would have paid if it were the only plan
4. Secondary plan pays the lesser of: (a) what it would have paid as sole insurer, or (b) the remaining balance after primary paid
5. **The combined payment from both plans cannot exceed the actual billed amount** — no profit from dual coverage

**Timing:** Claims with secondary coverage take longer to process because the EOB from the primary must be received first. Budget 4–8 weeks for full resolution on complex claims.

---

## Is Dual Coverage Worth It?

### When it makes sense
- One plan has a high deductible; the secondary plan's copays effectively neutralize the primary deductible for routine visits
- The secondary plan premium is low or zero (e.g., employer pays 100% for employee-only tier)
- Family has predictably high healthcare utilization (chronic conditions, specialty visits, ongoing procedures)
- A specific benefit exists on one plan (e.g., ortho coverage) that the primary doesn't have

### When it usually doesn't
- The added annual premium exceeds the realistic secondary coverage benefit
- Administrative burden is high: two insurance cards, two EOBs, possible pre-authorization conflicts
- Both plans are HDHPs — secondary HDHP coverage doesn't reduce the primary's deductible; the deductible still must be met first

### Quick break-even test
```
Break-even point = (Extra annual premium for dual coverage)
                 ÷ (Estimated % of out-of-pocket secondary actually covers)

If break-even > realistic annual healthcare spending → dual coverage probably not worth it
```

---

## COB Example

**Setup:** Child covered by both parents' plans. Parent A's plan is primary (earlier birthday). Child has a specialist visit billed at $300.

| Step | Amount |
|------|--------|
| Primary plan: 80% coinsurance after $200 deductible | Primary pays $80; member owes $220 |
| Secondary plan receives primary EOB | Sees $220 remaining |
| Secondary plan applies $40 specialist copay | Secondary pays up to $40; member owes $0–$40 |
| **Actual out-of-pocket** | **$0–$40 instead of $220** |

Without secondary coverage, the member would have paid $220 out of pocket. With secondary, they pay $0–$40 depending on how the secondary plan coordinates.

---

## RETA Trust and COB

Many Catholic school district plans (including Sacred Heart systems) are administered through RETA Trust, which is a self-insured cooperative administered by Blue Shield of California using the BlueCard PPO network.

**COB considerations for RETA Trust plans:**
- RETA Trust follows standard COB rules and birthday rule
- Claims coordination process may differ slightly from fully insured plans — the plan administrator (Blue Shield CA) handles it
- For members in Oregon/other states, confirm that the BlueCard PPO network in their area includes their regular providers
- Self-insured plans sometimes have narrower out-of-state coverage; confirm if specialists or procedures might occur out-of-state

---

## Common COB Mistakes to Avoid

1. **Assuming dual coverage means no out-of-pocket** — The secondary still applies its own rules. You may still owe a secondary copay or coinsurance.

2. **Forgetting to submit to secondary** — Secondary coverage only activates when a claim is submitted. The member (or provider) must file the secondary claim with the EOB from primary attached.

3. **Comparing deductibles across plans** — The secondary plan's deductible doesn't stack with the primary's. The secondary calculates its payment on the remaining balance, not on the full billed amount.

4. **Adding a spouse to a plan just for COB** when the premium cost exceeds the realistic coverage benefit — always run the break-even test.

5. **Birthday rule applies to calendar birthday, not birth year** — A parent born on January 2 is primary over a parent born on December 31, regardless of age difference.

---

## Network Interaction Under COB

| Situation | Primary | Secondary | Result |
|-----------|---------|-----------|--------|
| Both plans in-network | In-network rates | In-network rates | Best outcome |
| Primary in-network, secondary out-of-network | In-network rates | Minimal or no coverage | Secondary adds little value |
| Primary out-of-network, secondary in-network | Out-of-network (high costs) | Secondary pays as if primary had been in-network | Can help, but primary out-of-network costs are still high |

**Recommendation:** Always use in-network providers for both plans when possible. Out-of-network scenarios can create unexpected gaps even with dual coverage.
