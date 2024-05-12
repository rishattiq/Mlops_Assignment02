import requests
from bs4 import BeautifulSoup
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from subprocess import call

# Sources for data extraction
sources = ['https://www.dawn.com/', 'https://www.bbc.com/']

# Function to extract links from websites
def extract_links(source_url):
    try:
        reqs = requests.get(source_url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error extracting links from {source_url}: {e}")
        return []

# Function to extract titles and descriptions from articles
def extract_articles(source_url):
    try:
        reqs = requests.get(source_url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        articles = []
        for article in soup.find_all('article'):
            title = article.find('h1').text.strip() if article.find('h1') else "No title found"
            description = article.find('p').text.strip() if article.find('p') else "No description found"
            articles.append({'title': title, 'description': description})
        return articles
    except Exception as e:
        print(f"Error extracting articles from {source_url}: {e}")
        return []

# Function for data transformation
def transform():
    print("Transformation")

# Function for data loading
def load():
    print("Loading")

# DAG definition
default_args = {
    'owner': 'airflow-demo',
    'start_date': datetime(2024, 5, 10),
    'schedule_interval': '@daily',
}

dag = DAG(
    'mlops_dag',
    default_args=default_args,
    description='A simple DAG for MLOps',
    catchup=False
)

# Task to extract links from websites
task_extract_links = PythonOperator(
    task_id='extract_links',
    python_callable=extract_links,
    op_kwargs={'source_url': sources},
    dag=dag
)

# Task to extract titles and descriptions from articles
task_extract_articles = PythonOperator(
    task_id='extract_articles',
    python_callable=extract_articles,
    op_kwargs={'source_url': sources},
    dag=dag
)

# Task for data transformation
task_transform = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag
)

# Task for data loading
task_load = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)

# Define task dependencies
task_extract_links >> task_extract_articles >> task_transform >> task_load

# Task for DVC push
def dvc_push():
    try:
        os.system("dvc push")
    except Exception as e:
        print(f"Error pushing to DVC: {e}")

# Task to push data to DVC
task_dvc_push = PythonOperator(
    task_id='dvc_push',
    python_callable=dvc_push,
    dag=dag
)

# Task to version metadata against each DVC push
def version_metadata():
    try:
        call(["dvc", "commit", "-m", "Versioning metadata"])
    except Exception as e:
        print(f"Error versioning metadata: {e}")

# Task to version metadata against each DVC push
task_version_metadata = PythonOperator(
    task_id='version_metadata',
    python_callable=version_metadata,
    dag=dag
)

# Define task dependencies
task_load >> task_dvc_push >> task_version_metadata
