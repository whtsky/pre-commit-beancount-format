# pre-commit-beancount-format

Format `.beancount` files using [bean-format](https://beancount.github.io/docs/running_beancount_and_generating_reports.html#bean-format)

## Usage
Add this to your `.pre-commit-config.yaml`:
```yaml
-   repo: https://github.com/whtsky/pre-commit-beancount-format
    sha: '2.3.4'  # Use the sha / tag you want to point at
    hooks:
    -   id: beancount-format
```
