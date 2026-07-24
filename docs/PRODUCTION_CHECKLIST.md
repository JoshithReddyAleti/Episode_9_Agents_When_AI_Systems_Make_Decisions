# Production Agent Deployment Checklist

## Design (10 items)
- [ ] Agent has a clearly defined, narrow purpose
- [ ] Tool set is curated (<10 tools) with clear descriptions
- [ ] Reasoning pattern is chosen deliberately (not just ReAct by default)
- [ ] Termination conditions are explicit
- [ ] Cost budget per execution is defined
- [ ] Latency SLA is defined
- [ ] Failure modes have been enumerated
- [ ] Human handoff points are identified
- [ ] Rollback strategy exists for reversible actions
- [ ] Approval requirements for high-stakes actions

## Safety (10 items)
- [ ] Action allow-list is enforced
- [ ] Action deny-list is enforced
- [ ] Permission system respects user roles
- [ ] Kill switches exist at multiple levels
- [ ] Audit logging captures every action
- [ ] Prompt injection defenses are in place
- [ ] Sensitive data is never in prompts
- [ ] Adversarial testing has been done
- [ ] Incident response plan is documented
- [ ] Legal/compliance review completed for high-risk use cases

## Operations (10 items)
- [ ] Observability (LangSmith/Langfuse) is configured
- [ ] Cost tracking per user/execution exists
- [ ] Rate limits are configured at multiple levels
- [ ] Circuit breakers protect downstream services
- [ ] Graceful degradation on failures
- [ ] Alerts on quality/cost/latency issues
- [ ] Rollback procedure is tested
- [ ] Runbook for common issues exists
- [ ] Team is trained on incident response
- [ ] Monitoring dashboards are set up

30 items. Skip any at your peril.
