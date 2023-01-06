import pytest
import coverage
from pathlib import Path

root = Path(__file__).parents[2]
pytest.main([f'{root}', f'--cov={root}', '--cov-report', 'xml'])

cov = coverage.Coverage()
cov.load()

print(f'FAIL: Coverage below 100%, write more unit tests!'
      if cov.report(show_missing=False, omit='*/tests/test_*') < 100
      else f'PASS: Coverage 100%')