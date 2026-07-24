# Common Agent Anti-Patterns

## 1. Too Many Tools
Giving the agent 30 tools "just in case." Confuses tool selection. Fix: curate to <10 focused tools.

## 2. Vague Tool Descriptions
"Does search stuff." LLM can't decide when to use it. Fix: specific, exhaustive descriptions.

## 3. No Termination Limits
Agent loops forever burning cost. Fix: max_iterations, max_cost, max_time — always.

## 4. Trusting Agent Self-Assessment
Agent says "task complete" but it isn't. Fix: external verification, not agent's self-report.

## 5. No Rollback for Actions
Agent takes wrong action, can't undo. Fix: only allow reversible actions, or require approval.

## 6. Ignoring Failure Modes
"It works when I test it." Doesn't work when it doesn't. Fix: adversarial testing.

## 7. Multi-Agent For Everything
Fashion-driven design. Fix: use single-agent unless multi-agent genuinely helps.

## 8. No Observability
Can't debug what went wrong. Fix: LangSmith/Langfuse from day one.

## 9. Autonomous Without Boundaries
Agent can do anything. Fix: explicit allow-list and deny-list of actions.

## 10. Skipping Evaluation
No way to know if it's actually working. Fix: eval datasets, quality metrics, monitoring.
