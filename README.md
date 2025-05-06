# Student Performance Predictor

A machine learning-powered web application that predicts student performance based on various factors. Built with Flask and deployed on AWS Elastic Beanstalk.

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


## Acknowledgments

- AWS Elastic Beanstalk for hosting
- Flask framework
- CatBoost for machine learning capabilities