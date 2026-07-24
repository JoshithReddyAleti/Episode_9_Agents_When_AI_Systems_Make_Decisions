# 🌱 Foundations — What Is An Agent, Really?

> *Before you build one, you need to understand exactly what one is — and what one isn't.*

---

## The Precise Definition

An agent is an LLM system where the **LLM decides the next action** based on the current state, rather than following a predetermined sequence of steps.

Three properties define an agent:
1. **It has tools** it can choose to use
2. **It observes** the results of its actions
3. **It decides** what to do next based on those observations

Remove any of the three and you don't have an agent — you have something simpler (and often better).

---

## Agent vs Chain vs Workflow

The three are not the same. Confusing them causes bad architecture decisions.

### Chain
```
Input → LLM_1 → LLM_2 → LLM_3 → Output
```
Fixed sequence. Every input goes through the same steps. Deterministic control flow (though outputs are stochastic).

**Example:** "Extract entities → classify sentiment → generate summary"

### Workflow
```
Input → [Branching logic] → Different paths based on input type
```
Multiple predefined paths. The engineer specifies WHICH path to take under what conditions. Still deterministic control flow.

**Example:** "If query is a question, do RAG. If query is a command, call tools. Otherwise, direct answer."

### Agent
```
Input → LLM decides → Action → Observation → LLM decides → Action → ... → Output
```
Dynamic path. The LLM decides at each step. Non-deterministic control flow.

**Example:** "Solve this task using whatever tools you need, in whatever order makes sense."

### The Critical Distinction

| | Chain | Workflow | Agent |
|---|---|---|---|
| **Who decides the steps?** | Engineer at design time | Engineer at design time | LLM at runtime |
| **Predictable?** | ✅ | ✅ (per path) | ❌ |
| **Debuggable?** | Easy | Easy | Hard |
| **Cost predictable?** | ✅ | ✅ | ❌ |
| **Latency predictable?** | ✅ | ✅ | ❌ |
| **Best for** | Simple pipelines | Multi-path logic | Genuinely novel problems |

---

## The Agent Loop

Every agent follows this loop:

```
┌──────────────────────────────────────────────────────┐
│                                                       │
│  1. OBSERVE                                           │
│     Look at current state + user input                │
│                                                       │
│  2. THINK                                             │
│     LLM reasons: what should I do next?               │
│                                                       │
│  3. ACT                                               │
│     Execute the chosen action (call tool, respond)    │
│                                                       │
│  4. OBSERVE RESULT                                    │
│     See what happened                                 │
│                                                       │
│  5. DECIDE                                            │
│     ├── Task complete → return final answer          │
│     └── Not complete → loop back to step 1           │
│                                                       │
└──────────────────────────────────────────────────────┘
```

**Every agent implementation is this loop.** LangGraph agents, CrewAI agents, custom agents — they all follow this pattern. What varies:
- HOW the LLM reasons (ReAct, Plan-and-Execute, etc.)
- WHAT tools it has
- WHAT state it maintains
- WHAT termination conditions exist

---

## The Autonomy Spectrum

Not all "agents" have the same amount of autonomy. Understand where your system sits:

```
LESS AUTONOMOUS ──────────────────────────────► MORE AUTONOMOUS

Chain      Workflow    Tool Agent    Planning Agent    Autonomous Agent
   │           │             │              │                  │
Fixed        Path         Chooses         Plans + executes    Sets its
sequence    depends on    tools per       multi-step tasks    own goals,
of steps    input type    query          from goals          adapts,
                                                              learns

Cost:      Low ─────────────────────────────────► High
Latency:   Low ─────────────────────────────────► Variable
Reliability: High ────────────────────────────────► Lower
Debuggability: Easy ─────────────────────────────► Hard
```

**The engineering rule:** Use the LEAST autonomous approach that solves your problem. More autonomy = more failure modes, higher cost, harder debugging.

---

## Files in This Directory

| File | What It Explains |
|---|---|
| `what_is_an_agent.py` | The precise definition with runnable comparison to non-agents |
| `agent_vs_chain.py` | Side-by-side implementation of same task as chain vs agent |
| `agent_vs_workflow.py` | Side-by-side comparison of workflow vs agent |
| `the_agent_loop.py` | The observe-think-act-observe-decide loop from scratch |
| `autonomy_spectrum.py` | Same task at 5 different autonomy levels |
| `decision_making_basics.py` | How LLMs make decisions in practice |

---

## The Central Lesson of This Section

Most systems called "agents" in blog posts and tutorials are actually workflows. That's often FINE — workflows are usually the right choice. The mistake is calling them agents to sound impressive, then trying to debug them like agents.

**Know what you're building. Choose deliberately.**

---

*Next: [Reasoning Patterns →](../reasoning_patterns/README.md) — how agents actually think*

*Back to [main README](../../README.md)*
