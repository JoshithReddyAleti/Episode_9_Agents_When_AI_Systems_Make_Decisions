# 🌳 Agent Taxonomy — The Complete Classification

## By Autonomy Level
- **Reactive:** Responds to inputs, no planning (basic ReAct)
- **Deliberative:** Plans before acting (Plan-and-Execute)
- **Reflective:** Self-monitors and self-corrects (Reflexion)
- **Autonomous:** Sets its own sub-goals from a mission

## By Structure
- **Single-agent:** One agent, one loop
- **Multi-agent centralized:** Coordinator + specialists
- **Multi-agent decentralized:** Peer-to-peer
- **Hierarchical:** Multiple layers of coordinators

## By Reasoning Pattern
- ReAct, Plan-and-Execute, Tree-of-Thought, Reflexion, LLM Compiler (see src/reasoning_patterns/README.md)

## By Purpose
- **Retrieval agent** — mostly reads/queries
- **Action agent** — mostly writes/modifies
- **Analytical agent** — mostly reasons/computes
- **Creative agent** — mostly generates content
- **Conversational agent** — mostly interacts with users

## By Deployment
- **Interactive:** Responds to user requests (chat)
- **Background:** Runs on schedule (batch)
- **Event-driven:** Runs on triggers (webhook)
- **Continuous:** Always running (streaming)

Understanding where your agent fits helps you pick the right patterns and tools.
