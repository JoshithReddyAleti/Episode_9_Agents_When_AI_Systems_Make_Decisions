# Agent Failure Modes — Every Way Agents Break

## Reasoning Failures
- **Wrong tool selection:** LLM picks the wrong tool for the task
- **Hallucinated tools:** LLM tries to call tools that don't exist
- **Ignored observations:** LLM doesn't use tool results in reasoning
- **Wandering:** LLM doesn't stay focused on the goal
- **Circular reasoning:** LLM keeps trying the same failed approach

## Execution Failures
- **Tool errors:** External services fail
- **Timeout:** Operations take too long
- **Rate limits:** APIs reject calls
- **Malformed arguments:** LLM passes invalid tool args

## Control Flow Failures
- **Infinite loops:** Agent never terminates
- **Premature termination:** Agent gives up too early
- **Stuck states:** Agent repeats same action

## Systemic Failures
- **Cost explosion:** Runaway costs
- **Latency explosion:** Runs for hours instead of minutes
- **Cascade failures:** One tool failure breaks everything downstream

## Safety Failures
- **Unauthorized actions:** Agent does something it shouldn't
- **Data leakage:** Agent reveals sensitive info
- **Manipulation:** Adversarial user makes agent misbehave

## Mitigation Layers
Every failure mode above has a mitigation in this repo. See src/production_agents/ and src/safety_and_alignment/.
