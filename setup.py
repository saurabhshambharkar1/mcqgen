from setuptools import find_packages,setup


setup (
    name="mcqgenerator",
    version="0.0.1",
    author="saurabh shhambharkar",
    author_email="saurabhshambharkar1@gmail.com",
    find_packages=find_packages(),
    intall_requires = ["pandas","openai","langchain","python-dotenv","streamlit","PyPDF2","langchain_community"]
)