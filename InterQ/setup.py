from distutils.core import setup

setup(name='InterQ',
      version='1.0',
      description='Questions generator from text input',
      author='Yash Marane',
      author_email='yashmarane1358@gmail.com',
      packages=['InterQ', 'InterQ.encoding', 'InterQ.mcq'],
      url="https://github.com/maraneyash/NLP-based-automated-questions-generator",
      install_requires=[

           'torch==1.10.0',
           'transformers==4.12.0',
           'sense2vec==2.0.0',
           'strsim==0.0.3',
           'six==1.15.0',
           'networkx==2.6.3',
           'numpy==1.21.5',
           'scipy==1.4.1',
           'scikit-learn==1.0.2',
           'unidecode==1.3.4',
           'future==0.16.0',
           'joblib==1.1.0',
           'pytz==2018.9',
           'python-dateutil==2.8.2',
           'flashtext==2.7',
           'pandas==1.3.5'
      ],
      package_data={'InterQ': ['interq.py',
                                 'mcq.py', 'train_gpu.py', 'encoding.py']}
      )
