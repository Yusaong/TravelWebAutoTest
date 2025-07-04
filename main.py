import os
import pytest

pytest.main()
os.system(f'allure generate allure-results -o allure-report --clean')