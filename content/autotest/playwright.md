python3 -m venv .venv
. .venv/bin/activate
python -m pip  install --upgrade pip
python -m pip install --upgrade setuptools wheel
python -m pip install playwright
playwright install
playwright install-deps chromium

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()
```