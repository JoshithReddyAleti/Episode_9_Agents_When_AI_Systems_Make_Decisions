# 🧰 Agent Frameworks — Honest Comparison

> *Every framework is opinionated. Match the opinion to your problem.*

---

## The Frameworks

### LangGraph (`langgraph_agents.py`)
**Focus:** Stateful, graph-based agent workflows.
**Strengths:** Full control over agent loops, cycles, human-in-the-loop, checkpointing. Great for complex agents. Production-ready.
**Weaknesses:** Steeper learning curve. Manual state management.
**Best for:** Production systems needing custom control flow.

### CrewAI (`crewai_agents.py`)
**Focus:** Role-based multi-agent teams.
**Strengths:** Fast to build. Natural abstractions (agents, tasks, crews). Great for content/research workflows.
**Weaknesses:** Less control than LangGraph. Opinionated abstractions.
**Best for:** Multi-agent systems that fit the "team of specialists" mental model.

### AutoGen (Microsoft) (`autogen_agents.py`)
**Focus:** Multi-agent conversation-based systems.
**Strengths:** Rich conversation patterns. Strong Microsoft ecosystem integration.
**Weaknesses:** Complex for simple use cases.
**Best for:** Enterprise Microsoft-stack deployments.

### OpenAI Swarm (`openai_swarm.py`)
**Focus:** Lightweight agent orchestration.
**Strengths:** Very simple. Direct integration with OpenAI. Fast prototyping.
**Weaknesses:** Experimental. Limited features. OpenAI-only.
**Best for:** Learning agent patterns. Quick prototypes.

### LlamaIndex Agents (`llamaindex_agents.py`)
**Focus:** Data-focused agents (Episode 6).
**Strengths:** Great for RAG-heavy agents. Rich data connectors.
**Weaknesses:** Less feature-rich than LangGraph for pure agent workflows.
**Best for:** Agents that primarily query data.

### SmolAgents (Hugging Face) (`smolagents.py`)
**Focus:** Minimal, code-first agents.
**Strengths:** Extremely lightweight. Agents write and execute code.
**Weaknesses:** Newer, smaller community.
**Best for:** Code-execution agents. Data analysis.

### Custom Framework (`custom_agent_framework.py`)
Sometimes the right choice: your own thin agent layer. When existing frameworks don't fit, don't force it.

---

## Framework Comparison Matrix (`framework_comparison.md`)

| Feature | LangGraph | CrewAI | AutoGen | Swarm | LlamaIndex | SmolAgents |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Single agent | ✅✅ | ✅ | ✅ | ✅✅ | ✅ | ✅✅ |
| Multi-agent | ✅✅ | ✅✅ | ✅✅ | ✅ | ✅ | ❌ |
| Human-in-loop | ✅✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Cycles/loops | ✅✅ | ✅ | ✅ | Limited | Limited | ✅ |
| Checkpointing | ✅✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Learning curve | Steep | Easy | Medium | Very Easy | Medium | Easy |
| Production ready | ✅✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| RAG focus | Custom | Custom | Custom | Custom | ✅✅ | ❌ |

---

## Decision Guide

- **Building for production, need control** → LangGraph
- **Team of role-based agents** → CrewAI
- **Microsoft ecosystem** → AutoGen
- **Quick prototype** → Swarm
- **RAG-heavy agent** → LlamaIndex
- **Code-executing agent** → SmolAgents
- **None fit perfectly** → Custom (thin layer over OpenAI/Anthropic APIs)

---

*Previous: [← Safety & Alignment](../safety_and_alignment/README.md) · Next: [Real-World Agents →](../real_world_agents/README.md)*

*Back to [main README](../../README.md)*
