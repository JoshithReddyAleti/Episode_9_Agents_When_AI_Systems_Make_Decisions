# 🤝 Multi-Agent Systems — Teams of AI Agents

> *One agent has one perspective. A team can debate, delegate, and specialize.*

---

## When Multi-Agent Beats Single-Agent

Multi-agent is NOT better by default. It's more expensive, slower, and harder to debug. Use multi-agent when:

- The task naturally decomposes into roles (researcher, writer, editor)
- Different specialists produce better output than a generalist
- Parallel work saves significant time
- Peer review improves quality

**Otherwise, one strong agent beats a team of weaker agents.**

---

## Agent Communication (`agent_communication.py`)

Agents exchange information through:
- **Message passing** — structured messages between agents
- **Shared memory** — common state all agents read/write
- **Broadcasts** — one-to-many announcements
- **Blackboard** — shared workspace where agents post/read intermediate results

**Protocol design matters:** Ad-hoc communication → chaos. Enterprise systems use structured message schemas (Pydantic).

---

## Coordinator Pattern (`coordinator_pattern.py`)

One agent (coordinator) delegates to specialists. Specialists don't talk to each other directly.

```
       ┌── Coordinator ──┐
       │       │          │
   Researcher Analyst Writer
   (specialist tasks)
```

**Strengths:** Clear control flow. Debuggable. Coordinator has global view.
**Weaknesses:** Coordinator is a bottleneck. Single point of failure.

---

## Hierarchical Teams (`hierarchical_teams.py`)

Multiple layers of coordinators.

```
       CEO Agent (goals, strategy)
       /              \
   Manager A       Manager B
   /     \          /     \
  Worker Worker  Worker Worker
```

**When to use:** Very complex tasks. Enterprise workflows. When teams get big enough that one coordinator can't manage everything.

---

## Peer-to-Peer Agents (`peer_to_peer_agents.py`)

Agents communicate directly, no central coordinator.

**Strengths:** Resilient. Parallel. No bottleneck.
**Weaknesses:** Hard to reason about. Prone to loops.

**Best for:** Truly independent parallel work. Research/exploration tasks.

---

## Specialist Agents (`specialist_agents.py`)

Each agent has a narrow, focused role:
- Researcher agent (finds information)
- Analyst agent (interprets data)
- Writer agent (drafts prose)
- Editor agent (refines prose)
- Fact-checker agent (verifies claims)

Each has its own tools, prompts, and success criteria.

---

## Consensus Mechanisms (`consensus_mechanisms.py`)

When multiple agents disagree:
- **Voting:** Majority wins
- **Weighted voting:** Weights based on agent expertise
- **Debate:** Agents argue until one convinces the others
- **Judge agent:** A separate agent decides
- **Human-in-the-loop:** Escalate to human

---

## Task Delegation (`task_delegation.py`)

Coordinator decides which specialist gets which sub-task:
- By expertise (analyst gets analysis tasks)
- By availability (least busy agent)
- By cost (cheaper agent for simple tasks)
- By past performance (agent that succeeded on similar tasks)

---

## Shared Memory Agents (`shared_memory_agents.py`)

Common state accessible by all agents:
- Facts everyone knows
- Intermediate results
- Task progress
- Learned lessons

**Critical:** Prevent write conflicts. Version state. Log changes.

---

## Design Principles

1. **Fewer agents when possible** — 2-4 agents beats 10 in most cases
2. **Clear roles** — every agent should have one specific purpose
3. **Structured communication** — messages have schemas, not free text
4. **Explicit coordination** — clear who decides what
5. **Cost budgets** — multi-agent easily 10x cost of single-agent

---

*Previous: [← Single-Agent Architectures](../single_agent_architectures/README.md) · Next: [Agent State & Memory →](../agent_state_and_memory/README.md)*

*Back to [main README](../../README.md)*
