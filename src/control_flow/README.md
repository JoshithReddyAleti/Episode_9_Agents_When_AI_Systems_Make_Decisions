# 🚦 Control Flow — How Agents Decide What Happens Next

> *The decisions between decisions. This is where agents succeed or fail.*

---

## Conditional Branching (`conditional_branching.py`)

Agent chooses different paths based on results:

```
If tool_result indicates success:
    → proceed to next step
If tool_result indicates need for more data:
    → call another tool
If tool_result indicates failure:
    → try recovery strategy
```

**Common failure:** LLM misreads tool result → wrong branch. Solution: structured tool outputs + explicit branching logic in prompt.

---

## Loops and Iteration (`loops_and_iteration.py`)

Agents loop until task is done. But:
- Loop can be infinite (agent never satisfies its own termination)
- Loop can be too short (agent gives up too early)
- Loop can be inefficient (repeats similar actions)

**Enterprise safeguards:**
```python
class AgentLoop:
    max_iterations = 20        # hard limit
    max_cost_dollars = 5.0     # cost budget
    max_time_seconds = 300      # time budget
    same_action_limit = 3       # detect stuck-in-loop
```

---

## Termination Conditions (`termination_conditions.py`)

When should the agent stop?

- **Task complete** — LLM declares done
- **Max iterations reached** — hit hard limit
- **Cost budget exhausted** — hit dollar limit
- **Time budget exhausted** — hit time limit
- **Stuck detection** — same action repeated N times
- **Human interruption** — user cancels
- **Fatal error** — unrecoverable failure

Every termination reason should be logged and monitored.

---

## Recovery Strategies (`recovery_strategies.py`)

When something fails:
- **Retry same action** — for transient errors
- **Retry with different args** — for arg errors
- **Try different tool** — for tool-specific failures
- **Ask for help** — escalate to human
- **Give up gracefully** — report failure to user

Multi-strategy recovery beats single-strategy every time.

---

## Human-in-the-Loop (`human_in_the_loop.py`)

Insert human checkpoints:

**Approval gate:** Agent must get human OK before executing certain actions.
```
Agent plans: "Send email to customer"
Gate: [requires human approval]
Human: approve/reject
Agent: proceeds or aborts
```

**Ambiguity resolution:** Agent asks human when unsure.
```
Agent: "The user said 'the client'. There are 3 clients in our system. Which one?"
Human: "The one from yesterday's meeting"
Agent: proceeds
```

**Safety intervention:** Human can pause/redirect anytime.

---

## Approval Gates (`approval_gates.py`)

Specific human-in-the-loop for high-stakes actions.

**Enterprise pattern:**
```python
HIGH_STAKES_ACTIONS = {
    "send_email_to_customer",
    "make_payment",
    "delete_user_data",
    "publish_content",
    "call_external_api_with_cost",
}

def should_require_approval(action):
    return action.name in HIGH_STAKES_ACTIONS or action.estimated_cost > 10
```

---

## Interruption Handling (`interruption_handling.py`)

Users can:
- Cancel a running agent
- Redirect mid-task
- Correct wrong actions
- Provide additional context

Agent must handle these gracefully — not just terminate but preserve context.

---

*Previous: [← Agent State & Memory](../agent_state_and_memory/README.md) · Next: [Autonomous Agents →](../autonomous_agents/README.md)*

*Back to [main README](../../README.md)*
