# 🌍 Real-World Agents — Complete Implementations

> *Not toy examples. Actual patterns you can adapt to build production agents.*

---

## The 7 Agent Types

### 1. Research Agent (`research_agent.py`)
Searches multiple sources, synthesizes findings, produces reports.
**Tools:** web search, PDF reader, RAG on internal docs.
**Reasoning:** Plan-and-Execute for complex topics.
**Output:** Structured research reports with citations.

### 2. Coding Agent (`coding_agent.py`)
Writes, tests, and debugs code.
**Tools:** file operations, code execution, testing, git.
**Reasoning:** Reflexion for iterative improvement.
**Safety:** Sandboxed execution, no direct production access.

### 3. Customer Support Agent (`customer_support_agent.py`)
Handles support tickets end-to-end.
**Tools:** knowledge base search, order lookup, refund initiation.
**Reasoning:** ReAct + conversation history.
**Safety:** Refund limits, escalation to humans for edge cases.

### 4. Data Analysis Agent (`data_analysis_agent.py`)
Answers questions from data.
**Tools:** SQL execution, Python code execution, visualization.
**Reasoning:** Plan-and-Execute + Reflexion.
**Output:** Charts, tables, insights.

### 5. Content Creation Agent (`content_creation_agent.py`)
Drafts, edits, and publishes content.
**Tools:** research, drafting, editing, CMS API.
**Reasoning:** Multi-agent (research → draft → edit → review).
**Safety:** Human approval before publishing.

### 6. Workflow Automation Agent (`workflow_automation_agent.py`)
Handles business processes end-to-end.
**Tools:** email, calendar, CRM, task management APIs.
**Reasoning:** Planning agent.
**Safety:** Approval for external communications.

### 7. Browser Agent (`browser_agent.py`)
Automates web browser tasks.
**Tools:** Playwright/Selenium (click, type, navigate, extract).
**Reasoning:** ReAct with vision (screenshot analysis).
**Safety:** Sandboxed browser, rate limits, no financial transactions.

---

## Common Patterns Across All Agents

Every production agent has:

1. **Clear scope** — narrowly defined purpose
2. **Curated tools** — 5-10 tools, not 50
3. **Persistent state** — remembers past interactions
4. **Observability** — every step logged
5. **Cost controls** — budget per execution
6. **Safety layers** — approvals for risky actions
7. **Evaluation** — quality metrics tracked
8. **Human handoff** — knows when to escalate

Skip any of these and you have a demo, not a product.

---

## Files in This Directory

Each file is a complete, production-ready agent implementation pattern (not a full application, but the core architecture and reasoning).

---

*Previous: [← Frameworks](../frameworks/README.md)*

*Back to [main README](../../README.md)*
