from django.test import TestCase

import sys
# Create your test
sys.path.insert(0, '..')

from utils import qncloud

print(qncloud.gen_token())