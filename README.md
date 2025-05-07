# Student Performance Predictor

A machine learning-powered web application that predicts student performance based on various factors. Built with Flask and deployed on AWS Elastic Beanstalk.

## Project Overview

This project aims to predict student performance using machine learning techniques. The application provides an intuitive interface for educators to input student data and receive performance predictions, helping them identify students who might need additional support.

## Project Goals

- Develop a machine learning model to predict student performance
- Create an intuitive web interface for easy interaction
- Provide real-time predictions based on student data
- Deploy the application on AWS for scalability and reliability
- Enable educators to make data-driven decisions about student support

## Dataset Description

The project uses a comprehensive student dataset with the following features:

- **Demographic Information**:
  - Gender (Male, Female)
  - Age
  - Race_Ethnicity (Group A, B, C, D AND E)
  - Parent's education level
  - Lunch (standard, free)
  - test_preparation (none, completed)
  - math_score, reading_score and writing_score

- **Academic Factors**:
  - Previous test scores
  - Study time
  - Attendance rate
  - Course load

- **Environmental Factors**:
  - Family support
  - Internet access
  - Living conditions
  - Travel time to school

- **Target Variable**:
  - Final grade/performance score

## Features

- Machine learning model for student performance prediction
- Interactive web interface
- Real-time predictions
- Responsive design
- AWS cloud deployment

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: CatBoost
- **Deployment**: AWS Elastic Beanstalk
- **Version Control**: Git

## Project Structure

```
├── application.py          # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
├── .ebextensions/         # AWS Elastic Beanstalk configurations
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
├── src/                   # Source code
├── artifacts/             # ML model artifacts
└── notebook/              # Jupyter notebooks for model development
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- AWS Account (for deployment)

## Local Setup

1. **Clone the repository**
   ```bash
   git clone [your-repository-url]
   cd student-performance-predictor
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally**
   ```bash
   python application.py
   ```
   The application will be available at `http://localhost:5000`

## Dashboard Interface

1. **Input Form**
   - User-friendly form to input student data
   - Real-time validation of inputs
   - Clear field descriptions and help text
   - 
![image](https://github.com/user-attachments/assets/3754eed1-5716-438f-9c19-12e145e2918a)

2. **Prediction Output**
   - Clear display of predicted performance
   - Confidence score for predictions
   - Visual representation of results
![image](https://github.com/user-attachments/assets/b2b38f88-f4b7-4e99-9ab7-ad77c02b47c8)

## Deployment to AWS Elastic Beanstalk

### Windows Deployment

1. **Package the application**
   ```bash
   package_app.bat
   ```

2. **Deploy to AWS**
   ```bash
   deploy.bat
   ```

### Linux/Mac Deployment

1. **Package the application**
   ```bash
   ./deploy.sh
   ```

2. **Deploy to AWS**
   ```bash
   ./deploy.sh
   ```

## Environment Variables

The following environment variables are required:

- `FLASK_APP`: application.py
- `FLASK_ENV`: production
- `PYTHONPATH`: /var/app/current

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- AWS Elastic Beanstalk for hosting
- Flask framework
- CatBoost for machine learning capabilities
