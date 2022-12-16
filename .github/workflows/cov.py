import os
import sys
import pytest
import coverage

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
pytest.main(['--cov-report', 'term', '--cov=src'])
cov = coverage.Coverage()
cov.load()

print(f'FAIL: Coverage below 100%, write more unit tests!'
      if cov.report(show_missing=False) < 100
      else f'PASS: Coverage 100%')