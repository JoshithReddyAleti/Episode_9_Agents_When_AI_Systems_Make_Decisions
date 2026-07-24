# Single-Agent vs Multi-Agent — When Each Wins

## Single-Agent Wins When...
- Task fits in one agent's context/capabilities
- Coordination overhead > specialization benefit
- Latency matters
- Cost matters
- Debuggability matters

## Multi-Agent Wins When...
- Task naturally splits by expertise (researcher + writer + editor)
- Parallel work saves significant time
- Peer review improves quality
- Different agents need different models/tools
- The task requires multiple perspectives

## The Cost Reality
Multi-agent typically costs 3-10x more than single-agent for the same task. Justify it with quality/speed gains.

## The Debugging Reality
Debugging multi-agent = debugging N agents + their interactions. Complexity grows exponentially.

## The Recommendation
Start single-agent. Add agents only when a specific bottleneck is identified.
