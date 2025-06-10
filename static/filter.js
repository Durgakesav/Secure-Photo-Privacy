document.addEventListener("DOMContentLoaded", function () {
    const filterForm = document.getElementById("filterForm");
    const downloadButton = document.getElementById("downloadButton");
    
    filterForm.addEventListener("submit", function (event) {
        event.preventDefault();
        
        const filterType = document.getElementById("filter_type").value;
        const imageId = window.location.pathname.split("/").pop();

        fetch(`/edit_image/${imageId}`, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `filter_type=${filterType}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.filtered_image) {
                const filteredImageTag = document.querySelector("h3 + img");
                filteredImageTag.src = `/static/filtered/${data.filtered_image}`;
                filteredImageTag.alt = "Filtered Image";
                
                downloadButton.style.display = "inline-block";
                downloadButton.onclick = function () {
                    window.location.href = `/download/${data.filtered_image}`;
                };
            } else {
                alert("Failed to apply filter. Please try again.");
            }
        })
        .catch(error => console.error("Error applying filter:", error));
    });
});
