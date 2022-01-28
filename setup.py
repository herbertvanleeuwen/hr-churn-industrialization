from setuptools import setup, find_packages

setup(name='hr_churn_api',
      version='2.0.0',
      description='Api for the employee churn prediction',
      author='Herbert van Leeuwen',
      author_email='herbertvanleeuwen@godatadriven.nl',
      install_requires=open('requirements.txt').read().splitlines(),
      package_dir={"": 'src'},
      packages=find_packages('src'),
      zip_safe=False,
      entry_points={
          "console_scripts": [
                "start-api = hr_churn.cli:main",
          ],
      }
      )
