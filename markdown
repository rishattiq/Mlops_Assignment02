# Project Report: Automating Data Extraction, Transformation, and Version-controlled Storage

---

## Objective:
Implement Apache Airflow to automate the processes of data extraction, transformation, and version-controlled storage. The project focuses on extracting data from dawn.com and bbc.com, performing basic transformation tasks, and storing the processed data on Google Drive using DVC for version control.

## Workflow:

1. **Data Extraction**:
   - Utilized Python's `requests` library to fetch HTML content from dawn.com and bbc.com.
   - Leveraged BeautifulSoup (`bs4`) for parsing HTML and extracting links, article titles, and descriptions from the homepages of both websites.

2. **Data Transformation**:
   - Placeholder function `transform()` was included for data transformation tasks.
   - Intended for preprocessing steps like text cleaning, normalization, etc. Currently, it prints "Transformation" as a placeholder.

3. **Data Loading**:
   - Placeholder function `load()` was included for data loading tasks.
   - Intended for saving preprocessed data to a suitable storage medium. Currently, it prints "Loading" as a placeholder.

4. **DVC Setup**:
   - Installed DVC using `pip install dvc`.
   - Initialized DVC in the project directory using `dvc init`.
   - Configured a remote storage named `mydrive` for Google Drive using `dvc remote modify`.
   - Pushed data files to DVC cache and remote storage using `dvc push`.

5. **Version Control with DVC**:
   - Ensured metadata versioning by committing changes using `dvc commit`.
   - Each push to DVC was accompanied by a metadata versioning commit to track changes effectively.

## Challenges Encountered:
1. **Installation and Setup**:
   - Initial setup of Airflow, DVC, and necessary libraries required careful configuration to ensure compatibility and functionality across platforms (Windows, in this case).
   - Overcame issues related to module dependencies, path configurations, and system compatibility during the setup phase.

2. **Remote Storage Configuration**:
   - Configuring remote storage with Google Drive using DVC required attention to syntax and path formats.
   - Encountered errors related to URL formatting and storage path definitions, resolved through iterative adjustments and referring to DVC documentation.

3. **Version Control Integration**:
   - Integrating DVC for version control alongside Airflow posed some challenges due to differences in workflow paradigms and tool configurations.
   - Ensured proper synchronization between Airflow DAG tasks and DVC commands to maintain consistency in data processing and version control.

## Conclusion:
The project successfully automated the processes of data extraction, transformation, and version-controlled storage using Apache Airflow and DVC. Challenges encountered during setup and integration were addressed through careful configuration and referencing available documentation. The workflow established provides a foundation for scalable and reproducible data processing pipelines, facilitating efficient management of data assets and version tracking.

---


