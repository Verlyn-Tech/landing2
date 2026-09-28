# Project Instructions & Agent Memory

## External Services & Third-Party Platforms (One CLI)

The **One CLI (`one`)** is installed on this machine (`C:\Users\krish\AppData\Roaming\npm\one.cmd`). It connects AI agents to 750+ third-party platforms (including Gmail, Slack, Shopify, HubSpot, Stripe, GitHub, Google Calendar, Airtable, etc.) through their APIs.

### Core Directive:
**Whenever you need to interact with any third-party platform or external service, use the `one` skill and the `one` CLI.**

### Workflow:
1. `one --agent connection list` — List connected platforms, keys, and access levels
2. `one --agent actions search <platform> "<query>" -t execute` — Search for platform actions
3. `one --agent actions knowledge <platform> <actionId>` — Read documentation/schema before executing (REQUIRED)
4. `one --agent actions execute <platform> <actionId> <connectionKey> -d '<json>'` — Execute the action

### Available Resources:
- Workspace Skill: `.agents/skills/one/SKILL.md`
- Global Skill: `~/.agents/skills/one/SKILL.md`
- CLI documentation: `one guide all` or `one guide overview`
