# 🏛️ Single-Agent Architectures — 6 Canonical Patterns

> *One agent, many designs. Pick the right pattern for the job.*

---

## The 6 Patterns

### 1. Simple ReAct Agent (`simple_react_agent.py`)
The foundational pattern. LLM loops through Thought → Action → Observation until done.
**Best for:** Straightforward tool-use tasks. Q&A. Simple workflows.

### 2. Tool-Calling Agent (`tool_calling_agent.py`)
Uses native function-calling APIs (OpenAI tool calling, Anthropic tool use). No custom parsing.
**Best for:** Production systems where reliability > flexibility.

### 3. Planning Agent (`planning_agent.py`)
Explicit planning phase before execution. Plans are inspectable and revisable.
**Best for:** Complex multi-step tasks. Tasks requiring human approval of plans.

### 4. Conversational Agent (`conversational_agent.py`)
Maintains conversation history + tool use. The pattern behind ChatGPT with tools.
**Best for:** Chat interfaces, ongoing user interaction.

### 5. Autonomous Agent (`autonomous_agent.py`)
Self-directed. Sets its own sub-goals. Runs until goal is achieved.
**Best for:** Well-scoped tasks with clear success criteria. Requires strong safety boundaries.

### 6. Stateful Agent (`stateful_agent.py`)
Maintains persistent state across sessions. Remembers past interactions and their outcomes.
**Best for:** Long-running assistants. Multi-session workflows.

---

## Comparison

| Pattern | Complexity | Best For | Failure Modes |
|---|---|---|---|
| Simple ReAct | ⭐⭐ | Basic tool use | Loops, wandering |
| Tool-Calling | ⭐⭐ | Production reliability | Provider lock-in |
| Planning | ⭐⭐⭐ | Multi-step tasks | Wrong plans |
| Conversational | ⭐⭐⭐ | Chat interfaces | Context bloat |
| Autonomous | ⭐⭐⭐⭐ | Well-scoped goals | Runaway execution |
| Stateful | ⭐⭐⭐⭐ | Cross-session | State corruption |

---

*Previous: [← Planning](../planning/README.md) · Next: [Multi-Agent Systems →](../multi_agent_systems/README.md)*

*Back to [main README](../../README.md)*
