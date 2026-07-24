# 📋 Planning — When Agents Think Before They Act

> *Reactive agents fail on complex tasks. Planning agents figure out the whole path before starting.*

---

## Why Planning Matters

Simple ReAct agents make decisions one step at a time. This works for simple tasks but fails when:
- The task has 5+ steps
- Early decisions affect what's possible later
- Backtracking is expensive
- Coordination is needed between steps

Planning agents solve this by producing an explicit plan before execution.

---

## Task Decomposition (`task_decomposition.py`)

Break a complex task into atomic sub-tasks.

```
Goal: "Write a competitive analysis of AI code editors"

Decomposed:
  1. Identify major AI code editors (Cursor, Copilot, Zed, Windsurf, ...)
  2. Research each editor: features, pricing, market share
  3. Compare across dimensions: capability, price, ecosystem
  4. Identify strengths and weaknesses of each
  5. Draft analysis
  6. Add data visualizations
```

**Rule:** Each sub-task should be executable in 1-3 tool calls. If it's larger, decompose further.

---

## Goal-Oriented Planning (`goal_oriented_planning.py`)

Instead of decomposing a task, express a goal and let the agent figure out how to reach it.

```
Goal state: "I have a fully working RAG system deployed to production"

Agent works backwards:
  To reach goal, I need: deployed system
  To deploy, I need: tested code + deployment config
  To have tested code, I need: implementation + test suite
  To implement, I need: architecture design
  ...
  Start: research the domain
```

**When to use:** When the path isn't obvious. When creativity in approach matters.

---

## Hierarchical Planning (`hierarchical_planning.py`)

Plans have levels:
- **Strategy:** High-level goals (weeks/months)
- **Tactics:** Multi-step tasks (days)
- **Actions:** Tool calls (seconds/minutes)

```
Strategy: Launch product
├── Tactic: Build MVP
│   ├── Action: Write feature spec
│   ├── Action: Implement core features
│   └── Action: Deploy alpha
├── Tactic: Get first users
│   ├── Action: Reach out to network
│   └── Action: Collect feedback
└── Tactic: Iterate to v1
```

The agent operates at whatever level is appropriate for the current situation.

---

## Plan Validation (`plan_validation.py`)

Before executing, verify the plan makes sense:

- **Completeness:** Does the plan actually achieve the goal?
- **Feasibility:** Can each step be executed with available tools?
- **Ordering:** Do steps respect dependencies?
- **Efficiency:** Any obvious redundancies?
- **Safety:** Any steps that require human approval?

```python
def validate_plan(plan, goal, tools):
    if not covers_goal(plan, goal):
        return "Plan doesn't achieve goal"
    for step in plan:
        if not can_execute(step, tools):
            return f"Step '{step}' has no matching tool"
    if has_circular_deps(plan):
        return "Plan has circular dependencies"
    return "OK"
```

---

## Plan Revision (`plan_revision.py`)

Plans made upfront rarely survive contact with reality. Revise when:
- A step fails
- A step reveals unexpected information
- The goal changes mid-execution
- New information suggests a better path

**Two revision strategies:**
1. **Local revision:** Change only affected steps
2. **Full re-planning:** Discard plan, start over with new info

Trade-off: local is faster but may miss globally better solutions.

---

## Dependency Tracking (`dependency_tracking.py`)

Some steps depend on others. Track this explicitly:

```python
plan = [
    Step("research_editors", depends_on=[]),
    Step("compare_features", depends_on=["research_editors"]),
    Step("draft_analysis", depends_on=["compare_features"]),
    Step("add_visualizations", depends_on=["compare_features"]),  # parallel with draft
    Step("finalize_report", depends_on=["draft_analysis", "add_visualizations"]),
]
```

Enables parallel execution of independent steps.

---

## Plan Execution Monitor (`plan_execution_monitor.py`)

Watch the plan as it executes:

- Which steps succeeded?
- Which failed?
- Is progress on schedule?
- Any signs the plan is going wrong?

Enables early intervention instead of running a broken plan to completion.

---

## Files in This Directory

| File | What It Covers |
|---|---|
| `task_decomposition.py` | Breaking tasks into sub-tasks |
| `goal_oriented_planning.py` | Backward planning from goals |
| `hierarchical_planning.py` | Multi-level plans |
| `plan_validation.py` | Verifying plans before execution |
| `plan_revision.py` | Adapting plans during execution |
| `dependency_tracking.py` | Managing step dependencies |
| `plan_execution_monitor.py` | Watching plans execute |

---

*Previous: [← Tool Use](../tool_use/README.md) · Next: [Single-Agent Architectures →](../single_agent_architectures/README.md)*

*Back to [main README](../../README.md)*
