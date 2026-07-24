# 🔧 Tool Use — The Skill That Makes Agents Actually Useful

> *An agent without tools is just an LLM in a loop. Tools are what turn thinking into doing.*

---

## What Is A Tool?

A tool is a function the agent can call to affect the world or gather information. Tools give agents capabilities beyond text generation:

- **Information tools:** search, database queries, API calls, file reads
- **Action tools:** send email, create file, execute code, make API calls
- **Reasoning tools:** calculator, code interpreter, symbolic solver
- **Communication tools:** talk to other agents, message users, ask for approval

---

## Tool Design Principles (`tool_design_principles.py`)

The single most important skill in agent engineering. Bad tool design = bad agents.

### 1. Single Responsibility
Each tool does ONE thing. Not "search_and_summarize" — that's two tools.

### 2. Clear Descriptions
The LLM reads the description to decide when to use the tool. Vague description → wrong tool selection.

**Bad:** "Does search."
**Good:** "Search the company's internal documentation for technical articles. Use this when the user asks about internal processes, product specs, or architecture decisions. Returns up to 5 matching article excerpts with source URLs."

### 3. Typed Inputs (Pydantic)
Force the LLM to structure inputs correctly.

```python
class SearchInput(BaseModel):
    query: str = Field(description="The search query")
    max_results: int = Field(default=5, ge=1, le=20)
    filter_by_date: Optional[str] = Field(None, description="ISO date")
```

### 4. Structured Outputs
Return dicts, not free-form strings. The LLM must be able to interpret the result reliably.

### 5. Errors Are Data
Never raise exceptions from tools. Return error messages the LLM can read and reason about.

```python
def search(query: str) -> dict:
    try:
        results = do_search(query)
        return {"success": True, "results": results}
    except TimeoutError:
        return {"success": False, "error": "Search timed out. Try a shorter query."}
```

---

## Tool Selection Logic (`tool_selection_logic.py`)

The LLM has N tools. It must pick the right one. This fails when:

- Tools have overlapping descriptions
- Too many tools (>15 tools = confusion)
- Descriptions don't match user intent language
- The LLM defaults to a familiar tool when a specialized one would be better

**Improvements:**
- Fewer tools (aim for <10)
- Distinct, non-overlapping capabilities
- Test tool selection accuracy as a metric (see Episode 8)
- Consider hierarchical tools (categorize before selecting)

---

## Parallel Tool Execution (`parallel_tool_execution.py`)

Modern LLMs (GPT-4o, Claude Sonnet) can call multiple tools in parallel:

```
User: "What's the weather in Tokyo AND London AND Paris?"

Sequential (slow):     Parallel (fast):
  weather(Tokyo)         weather(Tokyo)  ┐
  wait                   weather(London) ├─ all at once
  weather(London)        weather(Paris)  ┘
  wait                   wait for all
  weather(Paris)         combine results
  wait
  combine results
```

**When it works:** Independent tool calls with no data dependency.
**Speedup:** 2-5x for parallelizable workloads.

---

## Tool Result Handling (`tool_result_handling.py`)

**Common failure mode:** Agent ignores tool results.

Example: Weather tool returns "18°C". Agent responds "It's warm outside" (didn't use the actual number).

**Fixes:**
- Include results explicitly in next prompt
- Add "USE THIS DATA in your response" instructions
- Validate that key facts from tool results appear in agent response

---

## Tool Error Recovery (`tool_error_recovery.py`)

Tools fail. Agents must handle:
- Network timeouts → retry with exponential backoff
- Invalid arguments → let LLM correct and retry
- Rate limits → wait and retry
- Permanent failures → give up gracefully, tell user

**Retry with LLM correction pattern:**
```
Tool call fails → include error in next LLM prompt → LLM adjusts arguments → retry
```

---

## Nested Tool Calls (`nested_tool_calls.py`)

Advanced pattern: tools that use other tools internally. Careful — this can hide agent decision-making.

**Better pattern:** Flatten to top-level tools when possible. Keep the LLM aware of what's happening.

---

## Dynamic Tool Registration (`dynamic_tool_registration.py`)

Enterprise pattern: expose different tools to different users based on permissions.

```python
def get_tools_for_user(user):
    tools = [search, calculator]  # everyone gets these
    if user.can_send_email:
        tools.append(send_email)
    if user.is_admin:
        tools.append(admin_tool)
    return tools
```

Security-critical: never expose tools based on the LLM's request. The LLM cannot request new permissions.

---

## Files in This Directory

| File | What It Covers |
|---|---|
| `tool_design_principles.py` | The 5 principles |
| `tool_selection_logic.py` | How LLMs choose tools |
| `parallel_tool_execution.py` | Concurrent tool calls |
| `tool_result_handling.py` | Making the LLM use results |
| `tool_error_recovery.py` | Retries, fallbacks |
| `nested_tool_calls.py` | Tools calling tools |
| `dynamic_tool_registration.py` | Permission-based tool access |

---

*Previous: [← Reasoning Patterns](../reasoning_patterns/README.md) · Next: [Planning →](../planning/README.md)*

*Back to [main README](../../README.md)*
