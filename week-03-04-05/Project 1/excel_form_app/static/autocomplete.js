// Wait until the document is fully loaded
$(document).ready(function () {

    // Listen for keyup events on the input field with id "id_titlos"
    $("#id_titlos").on("keyup", function () {

        // Get the current value of the input field
        let query = $(this).val();

        // If the input has less than 2 characters, stop execution
        if (query.length < 2) return;

        // Send an AJAX request to the server for autocomplete suggestions
        $.ajax({
            // URL that handles the autocomplete request
            url: "/ajax/autocomplete/title/", // or use a data attribute in template

            // Data sent to the server (query string)
            data: { q: query },

            // Function executed when the request is successful
            success: function (data) {

                // Select the suggestion box element
                let box = $("#title-suggestions");

                // Clear previous suggestions
                box.empty();

                // Loop through the results returned from the server
                data.results.forEach(item => {

                    // Add each suggestion as a clickable div
                    box.append(`<div class="suggestion-item">${item}</div>`);
                });

                // When a suggestion is clicked
                $(".suggestion-item").click(function () {

                    // Set the input value to the selected suggestion
                    $("#id_titlos").val($(this).text());

                    // Clear the suggestion box
                    box.empty();
                });
            }
        });
    });
});