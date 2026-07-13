# Phase 9 OTNS-MAPS directed runner

## Result

Phase 9 is complete in the OTNS-MAPS branch
`feature/directed-parent-switch-phase9`.

The OTNS-MAPS runner now supports `scenario_type: directed_parent_switch` for
the preferred-parent multicast, unicast, and fast-response unicast variants.
Nine scenarios cover two, three, and four routers while the existing static
stock scenarios remain their baselines.

## Runner behavior

The runner:

1. creates the routers with stock or fast-response FTD executables;
2. waits 300 simulated seconds;
3. creates the preferred-parent MED and waits 5 simulated seconds;
4. identifies the observed current parent;
5. deterministically selects a non-current router using the scenario seed;
6. sends `prefparent switch <extaddr> <mode>`;
7. requires a structured `event=requested` acknowledgement;
8. immediately deletes the initial parent;
9. observes the child for 360 simulated seconds;
10. records the final parent, controller events, classification, and router
    topology changes.

Asynchronous `PREFPARENT` output can arrive before the synchronous response to
an OTNS command. Scalar response parsing now excludes those event lines while
the directed runner captures controller events separately.

## Executable isolation and provenance

Global MTD and FTD executables remain supported for homogeneous runs. Scenario
nodes may override those defaults with `nodes.<name>.executable`; node creation
then uses OTNS `add ... exe "<path>"`.

Every node records:

- resolved executable path;
- executable SHA-256;
- declared firmware profile;
- OTNS node ID.

Directed scenarios reject contradictory combinations, including multicast with
fast-response routers, fast-response routers with non-unicast mode, stock MTDs,
missing executables, and router profiles that disagree with the scenario.

## Classification

The result includes hardware-aligned labels for missing or unmapped parents,
missing targets, leader-parent cases, rejected commands, successful target
attachment, non-target attachment, no reattachment, and router topology
changes. Leader-parent and topology-change labels are informational and do not
invalidate a successful target attachment.

## Validation

Five automated tests cover scenario validation, contradictory profiles,
asynchronous event/scalar parsing, deterministic mock target selection, and
structured event parsing. All nine scenarios also complete in mock mode.

The deterministic real two-router exit matrix used the Phase 8 binaries:

- multicast with stock FTD routers: selected target reached;
- unicast with stock FTD routers: selected target reached;
- unicast with fast-response FTD routers: selected target reached.

All real runs acknowledged the command, emitted the selected-parent controller
events, ended on the requested target, and recorded binary hashes for all three
nodes.

Phase 10 can now add protocol-event timestamp extraction and hardware-comparable
attach intervals.
