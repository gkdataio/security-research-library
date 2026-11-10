# Program and scope change feed

The [retained JSON feed](../exports/program-change-history.json) stores semantic differences between saved public program records. It includes asset additions and removals, moves between in-scope and out-of-scope, bounty eligibility, qualifications, policy summaries and program status. When a whole program is added or removed, its normalized snapshot is retained so its scope is not lost.

The feed begins empty. No historical changes have been backfilled, and no live source review was performed to initialize it. Existing Git history still preserves earlier repository snapshots.

## Record a change

After updating canonical records and regenerating their affected exports, run this offline command **before committing**, while HEAD is still the previous saved snapshot:

```sh
python3 scripts/check_program_changes.py --base HEAD --record-history
```

Review and commit `exports/program-change-history.json` with the canonical changes. If the data update is already committed, select its preceding commit with `--base <commit>`. Choose a baseline immediately before the intended update: overlapping or broad comparisons can describe the same transition in multiple batches. The tool does not automatically capture changes between runs or reconstruct intermediate states.

Each batch has a stable ID, recording time, baseline Git commit, semantic before/after inventory digests and detailed per-program changes. Asset-row changes include added and removed rows. Repeating an identical comparison does not append another batch or change its recording time. A no-change run leaves retained entries intact. Review-time changes, row ordering and duplicate-row cleanup alone do not create events.

The writer uses a lock and atomic replacement, preserves existing entries, and rejects malformed history instead of resetting it. If a lock remains after an interrupted process, confirm there is no active writer before removing the lock. History is versioned in Git; commit it to make local additions durable on the remote.

## Evidence limits

`recorded_at` is when the comparison was recorded, not when an external program changed its terms. A baseline commit identifies repository evidence, not an independently verified effective date. A saved scope difference can be a correction or capture improvement rather than a newly changed official policy. Source links and current official terms still need review.

Live HTTP hashes remain separate, local review signals. They are never promoted to verified scope changes in this feed. The checker refuses `--record-history` with `--live`. Run saved-data retention after reviewing and updating canonical public evidence. No program discovery, target testing, private data or new network requests are needed for retention.

The local HTTP-state file is validated before any request or rewrite, including in plan mode. Malformed entries or timestamps without a timezone stop the check with a clear error and leave the file unchanged. They are not silently discarded, because that could lose a failed attempt's cooldown or a last-good fingerprint. Repair the affected local record from known evidence before resuming; deleting the state would discard those protections.
