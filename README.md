# Agents-RAG

Notes and code snippets on RAG, AI Agents.

## Routing evaluation

The labeled routing prompts are in `evals/routing_dataset.jsonl`. Run the evaluator from the application environment so the target module's dependencies and Django settings are available:

```text
python evals/evaluate_routing.py --module library.ai.graph
```

The command prints accuracy and each mismatch, and exits with status 1 when any example is misclassified. Use `--dataset`, `--module`, and `--function` to evaluate another dataset or classifier.
