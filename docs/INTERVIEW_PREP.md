# Interview Prep — Episode 9

## "What's the difference between a chain and an agent?"
> "A chain executes a predetermined sequence — the engineer specifies the steps at design time. An agent decides the sequence at runtime — the LLM looks at the current state and picks the next action. Chains are predictable and cheap. Agents are flexible but expensive, harder to debug, and can fail in more ways. Most systems people call 'agents' are actually workflows with dynamic routing."

## "Walk me through the ReAct pattern."
> "ReAct interleaves reasoning and action. Each iteration: the LLM produces a Thought about what to do next, then an Action (calling a tool with arguments), then observes the Observation (the tool's result). It repeats until it decides the task is done and produces a Final Answer. It's the foundational pattern behind most agents. Strengths: reasoning is visible so debuggable. Weaknesses: sequential, can wander, doesn't plan ahead."

## "How do you decide between single-agent and multi-agent?"
> "Start single-agent. Move to multi-agent only when the task naturally decomposes into roles that would benefit from specialization — like researcher, writer, editor. Multi-agent is typically 3-10x more expensive and much harder to debug. Justify it with concrete quality or speed gains, not because it sounds impressive."

## "How do you keep an agent from running away?"
> "Multiple layers. Hard limits: max iterations, max cost, max time. Detection: stuck-in-loop detection, same-action-repeated. Safety: action allow-lists, permission systems, approval gates for high-stakes actions. Kill switches at multiple levels. Circuit breakers on downstream services. Every layer catches a different failure mode."

## "What's the biggest mistake people make building agents?"
> "Giving them too much autonomy too fast. People love the idea of an agent that can 'do anything,' but that's exactly what makes them dangerous and unreliable. Production agents are highly constrained — narrow scope, curated tools, explicit safety layers, human-in-the-loop for anything risky. The engineering is in the constraints, not the freedom."

## Resume Bullet
> Designed and implemented production-grade agent systems using LangGraph and CrewAI — with ReAct reasoning, planning capabilities, multi-agent coordination, comprehensive observability, cost controls, safety boundaries, and 7 real-world agent implementations covering research, coding, customer support, and browser automation.
