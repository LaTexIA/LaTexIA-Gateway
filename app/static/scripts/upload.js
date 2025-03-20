document.getElementById("uploadButton").addEventListener("click", async () => {
    const fileInput = document.getElementById("imageInput");
    const originalImage = document.getElementById("originalImage");
    const processedImage = document.getElementById("processedImage");
    const latexCode = document.getElementById("latexCode");
    const latexPreview = document.getElementById("latexPreview");

    if (fileInput.files.length === 0) {
        alert("Por favor, selecciona una imagen.");
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    originalImage.src = URL.createObjectURL(fileInput.files[0]);

    try {
        // Enviar imagen para preprocesamiento
        let response = await fetch("http://api_gateway:8000/preprocess/", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error("Error en preprocesamiento");

        const preprocessedData = await response.json();
        processedImage.src = preprocessedData.processed_image_url;

        // Enviar imagen preprocesada al modelo de predicción
        response = await fetch("http://api_gateway:8000/predict/", {
            method: "POST",
            body: JSON.stringify({ image_url: preprocessedData.processed_image_url }),
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) throw new Error("Error en la predicción");

        const predictionData = await response.json();
        latexCode.textContent = predictionData.latex_code;

        // Actualizar vista previa con MathJax
        latexPreview.innerHTML = `\\[${predictionData.latex_code}\\]`;
        MathJax.typesetPromise();
    } catch (error) {
        alert("Error en el procesamiento: " + error.message);
    }
});
