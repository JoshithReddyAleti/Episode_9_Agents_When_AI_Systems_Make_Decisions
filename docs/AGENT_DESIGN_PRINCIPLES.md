# The 10 Agent Design Principles

1. **Choose the simplest pattern that works.** Start with ReAct. Move to advanced only when needed.

2. **Fewer tools is better than more.** 5 well-designed tools > 30 vague tools.

3. **Structured inputs and outputs.** Pydantic on every tool. No free-form text at boundaries.

4. **Errors are data.** Tools return errors as messages, not exceptions.

5. **Hard limits, always.** Max iterations, max cost, max time. Never trust the agent to stop.

6. **Observability from day one.** If you can't see it, you can't fix it.

7. **Safety layers, not single controls.** Defense in depth.

8. **Fail gracefully.** Return best-effort answer + explanation of failure, never crash.

9. **Test with real production queries.** Curated evals miss real-world distribution shift.

10. **Version everything.** Prompts, tools, models, configs. Enable rollback.
