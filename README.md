# loop-lab

A deliberately tiny text-stats CLI whose real job is to be the proving ground for the
**Finn-loop** pipeline (`/finn-spec` → `/loop /finn-build` → `/loop /finn-review` → human merge).

## Usage

```
pip install -e .
loop-lab somefile.txt
echo "hello world" | loop-lab
```

## Development

```
pip install -e . ruff pytest
ruff check .
pytest
```

## The loop

- Issues live in Linear; a human applies the `agent-ready` label to release work to the builder.
- `/loop /finn-build` claims one issue per pass and opens a PR (never merges).
- `/loop /finn-review` posts a `Finn-loop review of <sha>` verdict and sets
  `loop-approved` / `loop-changes-requested` / `needs-human-review` labels.
- A human merges `loop-approved` PRs with green required checks.
