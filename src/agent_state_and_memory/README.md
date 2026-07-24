# 🧠 Agent State & Memory — What Agents Remember

> *An agent without memory is just a stateless function. What it remembers determines what it can do.*

Episode 7 covered general memory in AI systems. This section focuses on memory patterns SPECIFIC to agents.

---

## Working Memory (`working_memory.py`)

The agent's scratchpad — the intermediate reasoning and observations DURING task execution.

```
Working memory contents:
  Goal: "Find best restaurant near me under $50"
  Thought: "I need to know user's location first"
  Action: get_location()
  Observation: "San Francisco, CA"
  Thought: "Now search for restaurants"
  Action: search_restaurants(location="SF", max_price=50)
  Observation: [list of 20 restaurants]
  Thought: "Now I need to narrow down by reviews..."
```

Working memory is discarded when the task ends. Persistent memory is different.

---

## Episodic Memory for Agents (`episodic_memory_agent.py`)

Agents remember past task executions:
- What was the task?
- What plan did I use?
- What tools worked?
- What failed?
- Final outcome?

**Use case:** Agent gets similar task in the future → recall past approach → save time.

---

## Persistent State (`persistent_state.py`)

State that survives across sessions:
- User preferences learned over time
- Facts accumulated
- Task templates that worked
- Failure patterns to avoid

Combines with Episode 7's persistence layer (SQLite, Redis).

---

## Context Window Strategies (`context_window_strategies.py`)

Agent context window fills up with:
- System prompt (fixed)
- Available tools (fixed)
- Task goal
- Working memory (grows with steps)
- Retrieved memories (variable)

**Compression strategies:**
- Summarize old working memory when it exceeds budget
- Drop tool call details, keep tool decisions
- Compress observations to key facts
- Aggressive truncation of tool output

---

## Memory Hierarchy (`memory_hierarchy.py`)

Different memory tiers for different needs:

```
Working memory (current task)         → in RAM, discarded after task
Session memory (current session)      → in RAM, discarded after session
Short-term persistent (days)          → SQLite
Long-term persistent (months+)        → Vector store + database
Archive (compliance)                  → Cold storage
```

Move memories through tiers as they age.

---

## State Serialization (`state_serialization.py`)

Save agent state to disk. Resume later.

Enables:
- Long-running agents that pause for human review
- Recovery from crashes
- Audit trails (know exactly what state agent was in)
- Debugging (replay from any checkpoint)

**Enterprise pattern:** Every agent action creates a checkpoint. Any action can be undone.

---

*Previous: [← Multi-Agent Systems](../multi_agent_systems/README.md) · Next: [Control Flow →](../control_flow/README.md)*

*Back to [main README](../../README.md)*
