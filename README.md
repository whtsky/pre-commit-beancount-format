# pre-commit-beancount-format

Format `.beancount` files using [bean-format](https://beancount.github.io/docs/running_beancount_and_generating_reports.html#bean-format)

## Usage

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/whtsky/pre-commit-beancount-format
  rev: "2.3.4" # Use the sha / tag you want to point at
  hooks:
    - id: beancount-format
```

Or, if you use `.bean` as your beancount files' extensions rather than `.beancount`:

```yaml
- repo: https://github.com/whtsky/pre-commit-beancount-format
  rev: "2.3.4" # Use the sha / tag you want to point at
  hooks:
    - id: beancount-format
      files: \.bean$
```

To use custom arguments:

```yaml
- repo: https://github.com/whtsky/pre-commit-beancount-format
  rev: "2.3.4" # Use the sha / tag you want to point at
  hooks:
    - id: beancount-format
      args: ["--currency-column=60"]
```
