# 🤖 Agents — When AI Systems Make Decisions

> **Episode 9 of the [AI Engineering Roadmap 2026](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) Newsletter Series**
>
> *"A chain executes a plan. An agent decides the plan. That's the entire difference — and it changes everything."*

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-agents-534AB7?style=flat-square)
![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-red?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=flat-square)
![Episode](https://img.shields.io/badge/Episode-9%20of%2010-534AB7?style=flat-square)

**[📖 Newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) · [⬅️ Episode 8](https://github.com/JoshithReddyAleti/Episode_8_AI_Evaluation_Validation_and_Governance) · [🗺️ Roadmap](docs/ROADMAP.md)**

</div>

---

## 🎯 What Is This?

Episodes 1-8 taught you to build AI systems that follow instructions. Episode 9 teaches you to build AI systems that **make decisions**.

An agent is an LLM system that decides what to do next. Not just how to respond — but which tool to call, in what order, whether to retry, when to ask for help, and when to stop. This shift from "following a script" to "deciding a script" is the single biggest capability jump in AI engineering.

This episode is the complete guide: reasoning patterns, tool use, planning, single-agent and multi-agent architectures, autonomous agents, production patterns, safety, and every major framework.

---

## 🧠 The Core Concept

```
CHAIN:  Input → Step A → Step B → Step C → Output
        (Fixed pipeline. Same steps for every input.)

AGENT:  Input → [LLM decides: what to do?] → Action → Observation → 
        [LLM decides: what next?] → Action → Observation → ... → Output
        (Dynamic pipeline. Different steps per input.)
```

The chain follows the plan. The agent MAKES the plan.

---

## 📚 The Complete Deep-Dive Guides

Every section has an in-depth README. Read them in order for maximum understanding.

### Part 1: Foundations
| Guide | What You'll Learn |
|---|---|
| [`src/foundations/README.md`](src/foundations/README.md) | What is an agent (really), agent vs chain vs workflow, the agent loop, autonomy spectrum |
| [`src/reasoning_patterns/README.md`](src/reasoning_patterns/README.md) | ReAct, Plan-and-Execute, Tree-of-Thought, Self-Ask, Reflexion, LLM Compiler — how agents think |

### Part 2: Core Mechanics
| Guide | What You'll Learn |
|---|---|
| [`src/tool_use/README.md`](src/tool_use/README.md) | Tool design principles, selection logic, parallel execution, error recovery |
| [`src/planning/README.md`](src/planning/README.md) | Task decomposition, hierarchical planning, plan validation and revision |
| [`src/agent_state_and_memory/README.md`](src/agent_state_and_memory/README.md) | Working memory, episodic memory, context strategies, memory hierarchies |
| [`src/control_flow/README.md`](src/control_flow/README.md) | Branching, loops, termination conditions, human-in-the-loop, interruption |

### Part 3: Architectures
| Guide | What You'll Learn |
|---|---|
| [`src/single_agent_architectures/README.md`](src/single_agent_architectures/README.md) | 6 canonical patterns — simple ReAct, tool-calling, planning, conversational, autonomous, stateful |
| [`src/multi_agent_systems/README.md`](src/multi_agent_systems/README.md) | Communication protocols, coordinator patterns, hierarchies, consensus, delegation |
| [`src/autonomous_agents/README.md`](src/autonomous_agents/README.md) | Goal-setting, self-monitoring, self-correction, autonomy boundaries |

### Part 4: Production
| Guide | What You'll Learn |
|---|---|
| [`src/production_agents/README.md`](src/production_agents/README.md) | Observability, cost management, rate limiting, circuit breakers, deployment |
| [`src/safety_and_alignment/README.md`](src/safety_and_alignment/README.md) | Action boundaries, permissions, output verification, kill switches |
| [`src/frameworks/README.md`](src/frameworks/README.md) | LangGraph, CrewAI, AutoGen, OpenAI Swarm, LlamaIndex, SmolAgents — honest comparison |
| [`src/real_world_agents/README.md`](src/real_world_agents/README.md) | 7 real-world agent types with full implementations |

---

## 🏗️ The Anatomy of an Agent

```
┌─────────────────────────────────────────────────────────────────┐
│                          AN AGENT                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐       │
│  │  BRAIN — the LLM that makes decisions                │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌──────────┐ │
│  │ TOOLS      │  │ MEMORY     │  │ STATE      │  │ GOALS    │ │
│  │ (what it   │  │ (what it   │  │ (where it  │  │ (what    │ │
│  │  can DO)   │  │  remembers)│  │  is now)   │  │  it wants│ │
│  │            │  │            │  │            │  │  to do)  │ │
│  └────────────┘  └────────────┘  └────────────┘  └──────────┘ │
│                                                                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌──────────┐ │
│  │ CONTROL    │  │ SAFETY     │  │ OBSERV-    │  │ COST     │ │
│  │ FLOW       │  │ BOUNDARIES │  │ ABILITY    │  │ LIMITS   │ │
│  │ (how it    │  │ (what it   │  │ (how you   │  │ (how it  │ │
│  │  decides)  │  │  cannot    │  │  watch it) │  │  budgets)│ │
│  │            │  │  do)       │  │            │  │          │ │
│  └────────────┘  └────────────┘  └────────────┘  └──────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

Every production agent has all 8 components. Skip any of them and you have a demo, not a product.

---

## 🎯 When To Use An Agent (And When NOT To)

### ✅ Use an agent when:
- The task requires **multiple steps** you can't predetermine
- Different queries need **different tools** or **different sequences**
- The system needs to **adapt** based on intermediate results
- You need **reasoning** about which action to take next
- The workflow requires **retry / reflection** based on failures

### ❌ Do NOT use an agent when:
- The task is a fixed pipeline — use a chain
- You know all the steps upfront — use a workflow
- Cost matters and a simpler approach works
- Latency matters (agents have variable, unpredictable latency)
- Debugging clarity matters (agent decisions are hard to trace)
- The task is simple — one LLM call is enough

**The 90/10 rule:** In production, 90% of use cases are better served by chains or workflows. Only 10% actually need agent decision-making. Choose deliberately.

Read [`docs/WHEN_TO_USE_AGENTS.md`](docs/WHEN_TO_USE_AGENTS.md) for the full decision framework.

---

## 📖 Documentation Deep-Dives

| Guide | What You'll Learn |
|---|---|
| [`docs/AGENT_TAXONOMY.md`](docs/AGENT_TAXONOMY.md) | The complete classification of agent types |
| [`docs/WHEN_TO_USE_AGENTS.md`](docs/WHEN_TO_USE_AGENTS.md) | Decision framework — agent, chain, or workflow? |
| [`docs/AGENT_DESIGN_PRINCIPLES.md`](docs/AGENT_DESIGN_PRINCIPLES.md) | The 10 principles for building reliable agents |
| [`docs/SINGLE_VS_MULTI_AGENT.md`](docs/SINGLE_VS_MULTI_AGENT.md) | When multi-agent beats single-agent (and when it doesn't) |
| [`docs/COMMON_ANTI_PATTERNS.md`](docs/COMMON_ANTI_PATTERNS.md) | Mistakes every agent engineer makes once |
| [`docs/AGENT_FAILURE_MODES.md`](docs/AGENT_FAILURE_MODES.md) | Loops, hallucinated tools, action failures, wrong plans |
| [`docs/COST_AND_LATENCY.md`](docs/COST_AND_LATENCY.md) | The economics of agent systems |
| [`docs/PRODUCTION_CHECKLIST.md`](docs/PRODUCTION_CHECKLIST.md) | 30-item checklist before deploying an agent |
| [`docs/DECISION_FRAMEWORK.md`](docs/DECISION_FRAMEWORK.md) | Which pattern, framework, and architecture for your use case |
| [`docs/INTERVIEW_PREP.md`](docs/INTERVIEW_PREP.md) | How to talk about agents in interviews |

---

## ⚡ Quick Start

```bash
git clone https://github.com/JoshithReddyAleti/Episode_9_Agents_When_AI_Systems_Make_Decisions.git
cd Episode_9_Agents_When_AI_Systems_Make_Decisions

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# Run examples in order
python examples/01_your_first_agent.py
python examples/02_react_agent_from_scratch.py
python examples/05_multi_agent_research_team.py
```

---

## 💼 Resume Bullets

> **Option 1:** Engineered agentic AI systems with ReAct reasoning, dynamic tool selection, multi-agent coordination, and production-grade observability — demonstrating the shift from static chains to autonomous decision-making systems.

> **Option 2:** Built and compared agent architectures across LangGraph, CrewAI, AutoGen, and custom frameworks — with cost management, safety boundaries, human-in-the-loop patterns, and 7 real-world agent implementations (research, coding, browser automation, workflow).

> **Option 3:** Designed enterprise-grade agentic systems covering single-agent, multi-agent, and autonomous architectures — with permission systems, action verification, audit logging, circuit breakers, and rollback mechanisms.

---

## 🎤 Interview Story

> *"The distinction between a chain and an agent is where the decision-making lives. In a chain, I write the logic — step A, then step B, then step C. In an agent, the LLM decides the logic at runtime. That's more powerful but far more complex to build well: you need reasoning patterns like ReAct, tool selection accuracy, planning capabilities, state management, safety boundaries, cost limits, and observability. Most production 'agents' are actually workflows with agent-like framing — real autonomous agents are rare because they're hard to debug and expensive to run. The engineering skill is knowing when the decision-making complexity is worth it."*

---

## 📚 Part of the AI Engineering Roadmap 2026

| Episode | Topic | Link |
|---|---|---|
| 1-8 | Foundations through Evaluation & Governance | [See main roadmap](docs/ROADMAP.md) |
| **9** | **Agents: When AI Systems Make Decisions** | **← You are here** |
| 10 | The finale — coming soon | [Subscribe](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) |

---

<div align="center">

**If this helped you, give it a ⭐ — agents are where AI engineering gets really interesting.**

[Episode 8](https://github.com/JoshithReddyAleti/Episode_8_AI_Evaluation_Validation_and_Governance) · [Newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/)

</div>
