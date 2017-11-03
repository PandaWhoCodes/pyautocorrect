from distutils.core import setup

setup(name='pyautocorrect',
      version='0.1.0',
      packages=['pyautocorrect'],
      package_data={'pyautocorrect': ['shakespeare.txt']},
      description='Python 2/3 Spell Corrector',
      author='Thomas Ashish Cherian',
      author_email='ufoundashish@gmail.com',
      url='https://github.com/PandaWhoCodes/pyautocorrect',
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3', ],
      keywords='auto-correct spell corrector')
