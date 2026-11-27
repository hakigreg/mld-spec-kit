# Next iterations

These are suggestions, not implemented or verified Lab behavior. Do them one at a time, beginning with the spec and then reconciling downstream artifacts.

1. **Change `Hello` to `Hi`.** Learn how an intended output change flows through the spec, contract, tasks, code, and checks. Observe `Hi, Ada!` after implementation. This is the README exercise.
2. **Add an optional greeting word.** Define its default and valid values in the spec. Learn how a new input affects a command contract and edge cases. Observe two different greeting lines from the same program.
3. **Add a second independent user story for batch names.** Specify how multiple names are separated and what happens with an invalid entry. Learn how tasks can be grouped by story. Observe several output lines while the original single-name story still works.
4. **Use `$speckit-clarify` on an intentionally ambiguous requirement.** For example, say “handle unusual names” without defining the rule. Learn how clarification changes a spec before planning. Observe a precise acceptance scenario replacing the vague phrase.
5. **Try `$speckit-analyze` and `$speckit-converge` after an intentional mismatch.** Learn the difference between cross-artifact consistency and implementation completeness. Observe the reported gap, repair the source artifact or code, and rerun the check.
