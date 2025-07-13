document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const postingDateInput = document.getElementById('posting_date');

    // Tự động điền ngày hôm nay cho posting_date
    const today = new Date().toISOString().split('T')[0];
    postingDateInput.value = today;

    // Add or modify the submit handler to show loading
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const button = this.querySelector('button[type="submit"]');
        const spinner = button.querySelector('.loading-spinner');
        button.classList.add('loading');
        button.disabled = true;
        spinner.classList.remove('hidden');  // Show spinner
        
        // 1. Thu thập dữ liệu từ form
        const formData = {
            job_title: document.getElementById('job_title').value,
            experience_level: document.getElementById('experience_level').value,
            employment_type: document.getElementById('employment_type').value,
            company_location: document.getElementById('company_location').value || null,
            company_size: document.getElementById('company_size').value,
            employee_residence: document.getElementById('employee_residence').value || null,
            remote_ratio: parseInt(document.getElementById('remote_ratio').value, 10),
            required_skills: document.getElementById('required_skills').value || null,
            education_required: document.getElementById('education_required').value,
            years_experience: parseInt(document.getElementById('years_experience').value, 10),
            industry: document.getElementById('industry').value || null,
            posting_date: postingDateInput.value,
            benefits_score: parseFloat(document.getElementById('benefits_score').value)
        };

        // 2. Gửi yêu cầu đến API
        try {
            const response = await fetch('http://127.0.0.1:8000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'An error occurred');
            }

            const result = await response.json();
            
            // 3. Hiển thị kết quả
            resultText.textContent = `$${result.predicted_salary_usd.toLocaleString('en-US', { maximumFractionDigits: 0 })}`;
            resultContainer.classList.remove('hidden');

        } catch (error) {
            resultText.textContent = `Error: ${error.message}`;
            resultContainer.classList.remove('hidden');
            console.error('There was an error!', error);
        } finally {
            button.classList.remove('loading');
            button.disabled = false;
            spinner.classList.add('hidden');  // Hide spinner
        }
    });
}); 