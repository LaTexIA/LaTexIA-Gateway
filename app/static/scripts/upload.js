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
    formData.append("file", fileInput.files[0]);

    originalImage.src = URL.createObjectURL(fileInput.files[0]);

    try {
        // Enviar imagen para preprocesamiento
        let response = await fetch("/process-image/", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error("Error en preprocesamiento");

        const blob = await response.blob();
        const processedImageUrl = URL.createObjectURL(blob);
        processedImage.src = processedImageUrl;

        // Preparar la imagen preprocesada (blob) para enviarla a predicción
        const predictFormData = new FormData();
        predictFormData.append("file", blob, "processed_image.jpg");

        // Enviar la imagen preprocesada para predicción
        response = await fetch("/predict/", {
            method: "POST",
            body: predictFormData
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
