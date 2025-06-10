
document.getElementById("uploadForm").onsubmit = async function(event) {
    event.preventDefault();
    let fileInput = document.getElementById("fileInput").files[0];
    let formData = new FormData();
    formData.append("file", fileInput);
    let response = await fetch("/upload", { method: "POST", body: formData });
    let result = await response.json();
    document.getElementById("uploadResult").innerText = result.message;
};