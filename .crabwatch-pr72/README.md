# Crabwatch PR 72 integration test

Tests rust-lang/crabwatch#72 at c47da856ea94c8ec51fb1eb975e07eb6110b76df.
The source workflow is saved as original-workflow.txt. The tested action step
retains its exact condition, action SHA, and inputs; only an id and
continue-on-error are added so expected failures can be asserted.
Checkout and config download are unchanged. The integration harness uses a
branch push trigger and a fixture matrix in place of organization rulesets.

Fixtures are created after checkout in each runner. The workflow containing
ACTIONS_ALLOW_UNSECURE_COMMANDS is only scanned; it is never executed.
The original settings must fail on the same nested finding that the PR ignores.
Expected failures must contain the insecure-commands audit to rule out failures
caused by setup or infrastructure.

Scenarios: clean root with nested finding, root finding, missing root, empty
root, empty workflows directory, root docs only, and root hidden file only.
