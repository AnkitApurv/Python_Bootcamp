# Python Automation

## Automation schedulers

1. Apache airflow - heavyweight solution, suitable when
    - many automation need to be managed
    - forming pipelines of python and non-python steps
2. linux systemd service and timer - easily available lightweight solution, suitable when
    - few automation need to be managed
3. Windows scheduler - easily available, suitable when
    - no other solution is available

## Web automation

1. Microsoft playwright
    - easier api
    - Apache 2.0 license (open source)
    - environmental setup is mostly auto-managed
2. Selenium
    - most popular and open source
    - requires some manual environmental setup

