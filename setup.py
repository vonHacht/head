from setuptools import setup, find_packages, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        raise SystemExit(subprocess.call([sys.executable, 'test/__init__.py']))

def run_setup():

      setup(name='head',
            version='0.0.1',
            description='localize heads',
            url='https://github.com/vonHacht/head',
            author='KJ',
            author_email='kjvonhacht@gmail.com',
            license='MIT',
            packages=find_packages(),
            zip_safe=False
            )

try:
      run_setup()
except Exception as e:
      raise e






