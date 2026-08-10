# 🏭 Production Agents — What Makes Them Work In The Wild

> *A demo agent works once. A production agent works reliably, cheaply, and observably at scale.*

---

## The Production Reality Check

Your agent works in your notebook. In production it needs to:
- Handle 1000s of concurrent users
- Never exceed cost budgets
- Recover from all failures gracefully
- Produce audit logs for every decision
- Deploy and roll back safely
- Meet SLAs on latency and quality

This is where 90% of "agent projects" die.

---

## Observability (`observability.py`)

You cannot fix what you cannot see. Every agent execution needs:

- **Trace ID** — track a single execution end-to-end
- **Per-step logs** — every LLM call, tool call, decision
- **Latency breakdown** — where does time go?
- **Cost per execution** — track spending
- **Success/failure classification** — what went wrong?

**Tools:** LangSmith, Langfuse, Phoenix, custom OpenTelemetry integration.

---

## Cost Management (`cost_management.py`)

Agents are expensive. A single agent execution can cost $0.05-$5.00.

**Cost controls:**
```python
class CostManager:
    def check_before_action(self, action):
        if self.spent_this_execution + action.est_cost > self.max_per_execution:
            raise BudgetExceeded()
        if self.spent_this_user_today + action.est_cost > self.max_per_user_day:
            raise UserBudgetExceeded()
```

**Optimization:**
- Use smaller/cheaper models for routine tasks
- Cache repeated tool calls
- Skip agent logic for simple queries
- Set aggressive termination limits

---

## Rate Limiting (`rate_limiting.py`)

Protect:
- Against runaway agents (accidentally recursive)
- Against abuse (malicious users driving up costs)
- Downstream APIs (respect their rate limits)
- Your budget (spending caps)

**Layers:**
- Per-user rate limit (queries/minute)
- Per-tenant rate limit (queries/hour)
- Global rate limit (queries/second)
- API-specific rate limits (respect external API limits)

---

## Timeout Handling (`timeout_handling.py`)

Agents can hang:
- LLM API slow
- Tool call slow
- Agent stuck in reasoning loop
- Deadlock in multi-agent coordination

**Every operation needs a timeout:**
- LLM call: 30s
- Tool call: 60s (or per-tool)
- Full agent execution: 5 minutes
- Multi-agent workflow: 15 minutes

Graceful timeout: return partial results with clear "timeout" indication.

---

## Graceful Degradation (`graceful_degradation.py`)

When things fail, degrade gracefully:
- Primary LLM fails → try backup model
- Tool fails → try alternative tool
- Complex reasoning fails → fall back to simple response
- Agent fails → return best-effort answer + apology

**Never** just crash. Always return something useful.

---

## Agent Versioning (`agent_versioning.py`)

Track:
- Prompt versions
- Tool versions
- Model versions
- Configuration versions

Enable:
- A/B testing between agent versions
- Fast rollback when new version is worse
- Comparison of quality/cost between versions
- Reproducibility (rerun old queries with old agent)

---

## Circuit Breakers (`circuit_breakers.py`)

Stop cascading failures:

```python
class CircuitBreaker:
    def __init__(self):
        self.failure_count = 0
        self.state = "closed"  # closed | open | half-open
    
    def call(self, action):
        if self.state == "open":
            raise CircuitOpen("Service failing, not calling")
        try:
            result = action()
            self.reset()
            return result
        except Exception:
            self.failure_count += 1
            if self.failure_count >= 5:
                self.state = "open"
                schedule_reopen(60)  # try again in 60s
            raise
```

Applied to: LLM calls, tool calls, downstream services.

---

## Deployment Patterns (`deployment_patterns.py`)

- **Shadow deployment:** New version runs alongside old, doesn't affect users
- **Canary deployment:** 5% of traffic goes to new version, monitor
- **Blue-green:** Two identical environments, swap on deploy
- **Feature flags:** Toggle agent behavior without redeploying
- **Kill switch:** Instant disable if something goes wrong

---

## The Production Checklist (Preview)

Before deploying an agent to production, verify:
- Cost per query is within budget
- Latency p99 is within SLA
- All failure modes have handlers
- Observability is comprehensive
- Rate limits are configured
- Circuit breakers are in place
- Rollback plan is tested
- Alerts are configured
- Team is trained on incident response

Full checklist: [`docs/PRODUCTION_CHECKLIST.md`](../../docs/PRODUCTION_CHECKLIST.md)

---

*Previous: [← Autonomous Agents](../autonomous_agents/README.md) · Next: [Safety & Alignment →](../safety_and_alignment/README.md)*

*Back to [main README](../../README.md)*
