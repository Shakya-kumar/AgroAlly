$(document).ready(function() {
    $('#crop-form').on('submit', function(event) {
        event.preventDefault();
        var formData = {
            'N': parseFloat($('#N').val()),
            'P': parseFloat($('#P').val()),
            'K': parseFloat($('#K').val()),
            'temperature': parseFloat($('#temperature').val()),
            'humidity': parseFloat($('#humidity').val()),
            'ph': parseFloat($('#ph').val()),
            'rainfall': parseFloat($('#rainfall').val())
        };

        $.ajax({
            type: 'POST',
            url: 'http://localhost:5000/predict',
            data: JSON.stringify(formData),
            contentType: 'application/json',
            success: function(response) {
                $('#result').html(`
                    <h2>Based on your input, your soil is suitable to grow ${response.crop} (${response.hindi_name}).</h2>
                    <pre>${JSON.stringify(response.details, null, 2)}</pre>
                `);
            },
            error: function(error) {
                $('#result').html('<p>An error occurred</p>');
            }
        });
    });
});