# 🛡️ Safety & Alignment — Keeping Agents On The Rails

> *An agent that can do anything can do the wrong thing. Safety isn't optional — it's the foundation.*

---

## The Threat Model

An agent with tool access can:
- Send unauthorized emails
- Make unauthorized payments
- Delete data
- Leak sensitive information
- Take actions with legal/reputational consequences
- Get manipulated by adversarial users

Safety systems prevent this while preserving useful capability.

---

## Action Boundaries (`action_boundaries.py`)

Explicit lists of what the agent CAN and CANNOT do:

```python
class ActionBoundaries:
    ALLOWED_ACTIONS = {
        "search_docs", "read_calendar", "draft_email",
    }
    REQUIRES_APPROVAL = {
        "send_email", "create_meeting", "modify_document",
    }
    FORBIDDEN = {
        "delete_user_data", "modify_billing", "access_other_users_data",
    }
    
    def check(self, action):
        if action.name in self.FORBIDDEN:
            raise ForbiddenAction()
        if action.name in self.REQUIRES_APPROVAL:
            return "APPROVAL_REQUIRED"
        if action.name not in self.ALLOWED_ACTIONS:
            raise UnknownAction()
        return "ALLOWED"
```

---

## Permission Systems (`permission_systems.py`)

Different users have different permissions. Agent inherits user's permissions.

```python
def get_agent_capabilities(user):
    perms = user.permissions
    tools = [tool for tool in ALL_TOOLS if tool.required_permission in perms]
    return AgentCapabilities(tools=tools, user_id=user.id)
```

**Critical:** Agent CANNOT expand its own permissions. Only the user can.

---

## Output Verification (`output_verification.py`)

Before an agent's action is executed, verify:
- Are the parameters valid?
- Does the action match user intent?
- Does the action respect boundaries?
- Would the action be reversible if wrong?

For non-reversible actions (send email, make payment), verification is strict.

---

## Rollback Mechanisms (`rollback_mechanisms.py`)

When an action is wrong, undo it:
- Emails: can't unsend, but can send apology + notify support
- Data changes: version control, restore previous state
- Payments: refund flow
- External API calls: compensating transactions

Design agents so that most actions are reversible OR require explicit approval.

---

## Audit Logging (`audit_logging.py`)

Every agent action is logged:
- What action was taken?
- Why (LLM reasoning)?
- What was the input?
- What was the outcome?
- Who authorized it?
- Timestamp

Immutable. Searchable. Retained for compliance (typically 7 years).

Combines with Episode 8's governance and audit trails.

---

## Alignment Checks (`alignment_checks.py`)

Does the agent's action match:
- The user's stated intent?
- The system's stated goals?
- Ethical principles?
- Legal requirements?

**Alignment classifier:** Runs before high-stakes actions.

```python
def is_aligned(action, user_intent, system_goals):
    alignment_score = llm_judge.evaluate(
        action=action, intent=user_intent, goals=system_goals,
        criteria=["matches intent", "respects goals", "no harm"]
    )
    return alignment_score > ALIGNMENT_THRESHOLD
```

---

## Kill Switches (`kill_switches.py`)

Emergency stops:
- Individual agent kill (stop this execution)
- User agent kill (stop all this user's agents)
- Global kill (stop all agents in the system)

**Response time SLA:** Kill switch must take effect in < 1 second.

Every kill switch usage generates an alert. Post-incident review is mandatory.

---

## The Layered Defense

```
Layer 1: User authentication (right person)
Layer 2: Permission check (allowed to do X?)
Layer 3: Action boundary (allowed operation?)
Layer 4: Approval gate (needs human OK?)
Layer 5: Alignment check (matches intent?)
Layer 6: Output verification (valid parameters?)
Layer 7: Rate limits (not runaway?)
Layer 8: Audit log (record forever)
Layer 9: Kill switch (emergency stop)
```

Every layer catches a different failure mode. Redundancy is a feature.

---

*Previous: [← Production Agents](../production_agents/README.md) · Next: [Frameworks →](../frameworks/README.md)*

*Back to [main README](../../README.md)*
