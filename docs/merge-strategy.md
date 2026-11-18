# Git Merge Strategy Comparison

## 1. Merge Commit

- Preserves the complete branch history.
- Creates a separate merge commit.
- Clearly shows when feature branches were integrated.
- Can make the main branch history more detailed.

## 2. Squash Merge

- Combines all feature branch commits into one commit.
- Keeps the main branch history clean and readable.
- Preserves individual commits in the pull request history.
- Useful for small or focused feature branches.

## 3. Rebase Merge

- Replays feature commits onto the target branch.
- Creates a linear commit history.
- Avoids an additional merge commit.
- Rewrites commit history and requires care when sharing branches.

## Recommended Strategy

For this project, Squash Merge is recommended for the dashboard pull request because it combines the feature implementation and review improvements into one clean commit on main.

Merge Commit is useful when preserving branch integration history is important.

Rebase Merge is useful when a linear history is preferred.

The best strategy depends on the team's workflow and project requirements.
