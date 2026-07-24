# Agent Cost and Latency — The Economics

## Cost Reality
- Simple LLM call: $0.001 - $0.01
- Chain (3 LLM calls): $0.003 - $0.03
- Simple agent (ReAct with 5 iterations): $0.05 - $0.20
- Complex agent (planning + reflection): $0.50 - $2.00
- Multi-agent (research team): $2.00 - $10.00

10x-100x cost multiplier vs. single LLM calls.

## Latency Reality
- Single LLM call: 0.5-2 seconds
- Chain: 2-6 seconds
- Simple agent: 10-60 seconds
- Complex agent: 1-5 minutes
- Multi-agent: 5-30 minutes

Users don't wait 5 minutes. Design accordingly.

## Optimization Strategies
1. Use smaller models for routing decisions
2. Cache tool results (embeddings, search results)
3. Aggressive termination limits
4. Parallel tool calls
5. Streaming to show progress
6. Cheaper models for simple sub-tasks
7. Skip agent for simple queries (route to direct LLM)
