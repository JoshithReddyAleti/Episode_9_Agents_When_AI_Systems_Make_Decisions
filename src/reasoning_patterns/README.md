# 🧠 Reasoning Patterns — How Agents Actually Think

> *The LLM's reasoning strategy determines whether the agent works or fails. These are the patterns that make agents reliable.*

---

## Why Reasoning Patterns Matter

Give an LLM a task and access to tools. What happens?
- Sometimes it calls the right tool with the right arguments
- Sometimes it makes up tools that don't exist (hallucination)
- Sometimes it loops forever
- Sometimes it gives up too early
- Sometimes it uses the tool but ignores the result

The difference between "sometimes works" and "reliably works" is the reasoning pattern. Each pattern has strengths, weaknesses, and specific use cases.

---

## The 7 Reasoning Patterns

### 1. ReAct — Reason + Act (`react_pattern.py`)

The foundational pattern. Introduced by Yao et al. (2022).

```
Thought: [LLM reasons about what to do]
Action: [LLM chooses a tool + arguments]
Observation: [System returns tool result]
Thought: [LLM reasons about the result]
Action: [LLM chooses next action]
...
Thought: I have enough information.
Final Answer: [LLM's response]
```

**Strengths:** Interleaves reasoning with actions. Reasoning steps are visible → debuggable. Works with any tool.

**Weaknesses:** Sequential (slow). No planning (can wander). No self-correction.

**Best for:** Straightforward tool-use tasks. Q&A over tools. Simple agent workflows.

---

### 2. Plan-and-Execute (`plan_and_execute.py`)

Introduced by Wang et al. Separate planning from execution.

```
Phase 1 — PLAN:
  LLM creates a step-by-step plan for the entire task upfront.
  Plan: [
    "Step 1: Search for information about X",
    "Step 2: Extract key facts",
    "Step 3: Compare with known data",
    "Step 4: Draft response"
  ]

Phase 2 — EXECUTE:
  Execute each step. After each step, check if the plan needs revision.
```

**Strengths:** Explicit planning → predictable behavior. Fewer LLM calls than pure ReAct. Plans can be reviewed/approved by humans.

**Weaknesses:** Plans can be wrong from the start. Doesn't adapt as well to unexpected results.

**Best for:** Complex multi-step tasks. Tasks with clear structure. When humans need to approve plans.

---

### 3. Chain-of-Thought Agents (`chain_of_thought_agents.py`)

Not a full agent pattern — a reasoning augmentation. Add "think step by step" to any agent.

```
Thought: The user wants X. To find X, I need to Y. Y requires calling tool Z.
Action: tool_Z(args)
```

**Strengths:** Improves any reasoning-heavy agent. Nearly free (just prompt engineering).

**Weaknesses:** Doesn't fundamentally change the pattern. Same failure modes as base pattern.

**Best for:** Enhancement to any other pattern. Especially valuable for math, logic, multi-fact reasoning.

---

### 4. Tree-of-Thought Agents (`tree_of_thought_agents.py`)

Explore multiple reasoning paths, pick the best. Introduced by Yao et al.

```
Step 1: LLM generates 3 possible next actions
Step 2: LLM evaluates each option
Step 3: Continue with the best 1-2 options
Step 4: Repeat until goal reached
Step 5: If a path fails, backtrack and try another
```

**Strengths:** Doesn't get stuck on the first bad idea. Better for complex problems.

**Weaknesses:** Expensive (3-5x LLM calls). Complex to implement. Slow.

**Best for:** Genuinely hard problems where the first approach might be wrong. Research tasks. Creative tasks.

---

### 5. Self-Ask (`self_ask.py`)

The LLM asks itself follow-up questions before answering.

```
Question: What is the capital of the country where the Eiffel Tower is?

Are follow-up questions needed? Yes.
Follow-up: Where is the Eiffel Tower?
Intermediate answer: Paris, France.
Follow-up: What is the capital of France?
Intermediate answer: Paris.
So the final answer is: Paris.
```

**Strengths:** Great for multi-hop questions. Explicit decomposition.

**Weaknesses:** Only useful for question-answering, not general agent tasks.

**Best for:** RAG systems, question-answering agents, research tasks.

---

### 6. Reflexion (`reflexion.py`)

Introduced by Shinn et al. (2023). Agent that learns from its mistakes within a session.

```
Attempt 1: Agent tries to solve task → fails
Reflection: LLM analyzes why it failed
  "The tool call failed because I passed the wrong argument format.
   Next time, I should verify the schema before calling."
Attempt 2: Agent tries again, informed by reflection → succeeds
```

**Strengths:** Self-improving within a session. Handles complex tasks that require iteration.

**Weaknesses:** Multiple attempts = higher cost. Requires clear success/failure signals.

**Best for:** Coding agents. Complex problem-solving. Tasks where failures are informative.

---

### 7. LLM Compiler (`llm_compiler.py`)

Introduced by Kim et al. (2024). Parallel task execution.

```
Traditional ReAct: Sequential
  Tool_A → wait → Tool_B → wait → Tool_C → wait → Answer

LLM Compiler: Parallel where possible
  ┌─ Tool_A ─┐
  ├─ Tool_B ─┤ ─→ Merge results ─→ Answer
  └─ Tool_C ─┘
```

**Strengths:** Much faster for parallelizable tasks. Better throughput.

**Weaknesses:** Requires the LLM to identify independent operations. Complex implementation.

**Best for:** Data gathering across multiple sources. Research agents. Any task with independent sub-tasks.

---

## The Comparison Matrix

| Pattern | Complexity | LLM Calls | Latency | Best For |
|---|---|---|---|---|
| ReAct | ⭐⭐ | Medium | Medium | Standard tool use |
| Plan-and-Execute | ⭐⭐⭐ | Low-Medium | Medium | Multi-step tasks |
| Chain-of-Thought | ⭐ | Same as base | Same as base | Enhancement |
| Tree-of-Thought | ⭐⭐⭐⭐ | High | High | Complex problems |
| Self-Ask | ⭐⭐ | Medium | Medium | Multi-hop Q&A |
| Reflexion | ⭐⭐⭐⭐ | High | Very high | Coding, iteration |
| LLM Compiler | ⭐⭐⭐⭐ | Medium (parallel) | Low | Parallel workloads |

---

## How to Choose

```
Simple tool-use task?
  → ReAct (industry default)

Multi-step task with clear structure?
  → Plan-and-Execute

Complex problem where first approach might be wrong?
  → Tree-of-Thought

Multi-hop question-answering?
  → Self-Ask

Task where agent should learn from failures?
  → Reflexion

Task with many independent operations?
  → LLM Compiler
```

---

## Files in This Directory

| File | Pattern | When To Use |
|---|---|---|
| `react_pattern.py` | ReAct | Default choice |
| `plan_and_execute.py` | Plan-and-Execute | Complex multi-step |
| `chain_of_thought_agents.py` | CoT enhancement | Add to any pattern |
| `tree_of_thought_agents.py` | ToT | Hard problems |
| `self_ask.py` | Self-Ask | Multi-hop Q&A |
| `reflexion.py` | Reflexion | Iterative improvement |
| `llm_compiler.py` | LLM Compiler | Parallel tasks |

---

*Previous: [← Foundations](../foundations/README.md) · Next: [Tool Use →](../tool_use/README.md)*

*Back to [main README](../../README.md)*
