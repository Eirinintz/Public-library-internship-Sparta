$(document).ready(function () {
    // Autocomplete for the "title" input field
    $("#id_titlos").on("keyup", function () {
        let query = $(this).val();  // Get the current value
        if (query.length < 2) return;  // Skip if less than 2 characters

        // AJAX request to fetch title suggestions
        $.ajax({
            url: "/ajax/autocomplete/title/", // URL to fetch title suggestions
            data: { q: query },  // Send the current input value
            success: function (data) {
                let box = $("#title-suggestions");  // Container for suggestions
                box.empty();  // Clear previous suggestions

                // Add each suggestion as a clickable div
                data.results.forEach(item => {
                    box.append(`<div class="suggestion-item">${item}</div>`);
                });

                // Fill the input when a suggestion is clicked
                $(".suggestion-item").click(function () {
                    $("#id_titlos").val($(this).text());
                    box.empty();
                });
            }
        });
    });

    // Autocomplete for the "ekdoths" (publisher) input field
    $("#id_ekdoths").on("keyup", function () {
        let query = $(this).val();  // Get the current value
        if (query.length < 2) return;  // Skip if less than 2 characters

        // AJAX request to fetch publisher suggestions
        $.ajax({
            url: "/ajax/autocomplete/ekdoths/", // URL to fetch publisher suggestions
            data: { q: query },  // Send the current input value
            success: function (data) {
                let box = $("#ekdoths-suggestions");  // Container for suggestions
                box.empty();  // Clear previous suggestions

                // Add each suggestion as a clickable div
                data.results.forEach(item => {
                    box.append(`<div class="suggestion-item">${item}</div>`);
                });

                // Fill the input when a suggestion is clicked
                $(".suggestion-item").click(function () {
                    $("#id_ekdoths").val($(this).text());
                    box.empty();
                });
            }
        });
    });
});
