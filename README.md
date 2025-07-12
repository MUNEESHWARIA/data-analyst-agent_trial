\# Data Analyst Agent



A comprehensive data analysis API that uses machine learning and data processing techniques to analyze various datasets, create visualizations, and answer complex analytical questions.



\## Features



\- \*\*Web Scraping\*\*: Automatically scrapes and analyzes data from Wikipedia and other sources

\- \*\*Data Processing\*\*: Handles large datasets with pandas and DuckDB

\- \*\*Statistical Analysis\*\*: Performs correlation analysis, regression, and other statistical computations

\- \*\*Data Visualization\*\*: Creates scatter plots, regression lines, and other visualizations

\- \*\*API Integration\*\*: RESTful API that accepts POST requests with analysis tasks

\- \*\*Multi-format Support\*\*: Handles JSON, CSV, and various data formats



\## API Endpoints



\### POST /api/

Main data analysis endpoint that accepts analysis task descriptions.



\*\*Usage:\*\*

```bash

curl -X POST "https://your-app-url.com/api/" -F "file=@question.txt"

```



\### GET /health

Health check endpoint to verify the service is running.



\### GET /

Home endpoint with API documentation.



\## Supported Analysis Types



\### 1. Wikipedia Movie Analysis

\- Scrapes highest-grossing films data

\- Analyzes box office performance

\- Creates correlation plots

\- Answers specific questions about movie data



\### 2. Indian Court Data Analysis

\- Queries large court judgment datasets

\- Calculates case processing delays

\- Performs regression analysis on court data

\- Creates visualizations of court performance



\### 3. Generic Data Analysis

\- Processes various data formats

\- Performs statistical analysis

\- Creates custom visualizations



\## Sample Questions



The API can handle complex analytical questions like:



1\. "How many $2 bn movies were released before 2020?"

2\. "Which is the earliest film that grossed over $1.5 bn?"

3\. "What's the correlation between Rank and Peak?"

4\. "Draw a scatterplot of Rank and Peak with regression line"



\## Technical Stack



\- \*\*Backend\*\*: Flask (Python)

\- \*\*Data Processing\*\*: Pandas, NumPy, DuckDB

\- \*\*Visualization\*\*: Matplotlib, Seaborn

\- \*\*Web Scraping\*\*: BeautifulSoup, Requests

\- \*\*Database\*\*: DuckDB for large dataset queries



\## Response Format



The API returns responses in JSON format, typically as arrays or objects depending on the query:



```json

\[1, "Titanic", 0.485782, "data:image/png;base64,..."]

```



Or for complex queries:

```json

{

&nbsp; "question1": "answer1",

&nbsp; "question2": "answer2",

&nbsp; "visualization": "data:image/png;base64,..."

}

```



\## Installation



1\. Clone the repository

2\. Install dependencies: `pip install -r requirements.txt`

3\. Run the application: `python app.py`



\## Deployment



The application is designed to be deployed on various platforms:

\- Heroku

\- Render

\- Railway

\- Google Cloud Platform

\- AWS



\## License



MIT License - see LICENSE file for details.



\## Contributing



1\. Fork the repository

2\. Create a feature branch

3\. Commit your changes

4\. Push to the branch

5\. Create a Pull Request



\## Support



For issues and questions, please open an issue in the GitHub repository.

