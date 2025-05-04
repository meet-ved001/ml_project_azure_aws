document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const predictButton = document.getElementById('predictButton');
    const resultSection = document.getElementById('result-section');
    const loadingSpinner = document.getElementById('loading-spinner');
    const predictionResult = document.getElementById('prediction-result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading state
        predictButton.disabled = true;
        predictButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        
        // Submit the form
        form.submit();
    });
    
    // Validate input scores
    const readingScore = document.getElementById('reading_score');
    const writingScore = document.getElementById('writing_score');
    
    function validateScore(input) {
        const value = parseInt(input.value);
        if (value < 0) input.value = 0;
        if (value > 100) input.value = 100;
    }
    
    readingScore.addEventListener('change', () => validateScore(readingScore));
    writingScore.addEventListener('change', () => validateScore(writingScore));

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading spinner
        loadingSpinner.style.display = 'block';
        resultSection.style.display = 'none';

        // Collect form data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            // Send prediction request
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            // Hide loading spinner
            loadingSpinner.style.display = 'none';

            if (response.ok) {
                // Display result
                resultSection.style.display = 'block';
                predictionResult.innerHTML = `
                    <div class="result-card ${getResultClass(result.prediction)}">
                        <div class="result-icon">
                            ${getResultIcon(result.prediction)}
                        </div>
                        <div class="result-content">
                            <h3>Prediction Result</h3>
                            <p>${getResultMessage(result.prediction)}</p>
                            <p>Confidence: ${(result.confidence * 100).toFixed(2)}%</p>
                        </div>
                    </div>
                `;
            } else {
                // Display error
                resultSection.style.display = 'block';
                predictionResult.innerHTML = `
                    <div class="result-card error">
                        <div class="result-icon">⚠️</div>
                        <div class="result-content">
                            <h3>Error</h3>
                            <p>${result.error || 'An error occurred while processing your request. Please try again.'}</p>
                        </div>
                    </div>
                `;
            }

            // Scroll to result
            resultSection.scrollIntoView({ behavior: 'smooth' });

        } catch (error) {
            console.error('Error:', error);
            loadingSpinner.style.display = 'none';
            resultSection.style.display = 'block';
            predictionResult.innerHTML = `
                <div class="result-card error">
                    <div class="result-icon">⚠️</div>
                    <div class="result-content">
                        <h3>Error</h3>
                        <p>Network error: Please check your connection and try again.</p>
                    </div>
                </div>
            `;
        }
    });

    function getResultClass(prediction) {
        if (prediction === 'Good') return 'success';
        if (prediction === 'Average') return 'warning';
        return 'error';
    }

    function getResultIcon(prediction) {
        if (prediction === 'Good') return '🎉';
        if (prediction === 'Average') return '📊';
        return '⚠️';
    }

    function getResultMessage(prediction) {
        if (prediction === 'Good') return 'The student is predicted to perform well!';
        if (prediction === 'Average') return 'The student is predicted to have average performance.';
        return 'The student might need additional support.';
    }
}); 