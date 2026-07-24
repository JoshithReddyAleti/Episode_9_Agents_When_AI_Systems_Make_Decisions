# When To Use Agents — The Decision Framework

## The 90/10 Rule
90% of use cases labeled "agents" would work better as workflows. Only 10% actually need agent decision-making. Choose deliberately.

## Use An Agent When...
- Steps cannot be predetermined at design time
- Different queries need genuinely different approaches
- The task requires reasoning about which tool to use
- The system must adapt based on intermediate results
- You need retry/reflection loops
- Cost and latency are acceptable trade-offs for flexibility

## Use A Chain When...
- Steps are always the same (extract → transform → load)
- Debuggability matters more than flexibility
- Cost/latency must be predictable
- You know all steps upfront

## Use A Workflow When...
- Multiple predefined paths exist
- You can predict which path based on input
- You need some flexibility but not full autonomy

## Use One LLM Call When...
- Task is simple
- Cost/latency matters
- Reliability is critical
- Complexity isn't warranted

## The Framework
```
Does the task always have the same steps?
  YES → Chain

Are there a small number of paths based on input?
  YES → Workflow (with routing)

Does the LLM genuinely need to decide the sequence?
  YES → Agent (start with simple ReAct)

Do you need cycles / reflection / multi-source coordination?
  YES → Advanced agent pattern (LangGraph)
```
