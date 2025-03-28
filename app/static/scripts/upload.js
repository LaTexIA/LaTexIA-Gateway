document.getElementById("uploadButton").addEventListener("click", async () => {
    const fileInput = document.getElementById("imageInput");
    const originalImage = document.getElementById("originalImage");
    const processedImagesContainer = document.getElementById("processedImagesContainer");
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

        const processedData = await response.json();
        console.log("Processed Data:", processedData);
        const images = processedData.images;

        // Limpiar el contenedor y mostrar todas las imágenes decodificadas
        processedImagesContainer.innerHTML = "";
        images.forEach(encoded => {
            const img = document.createElement("img");
            img.src = `data:image/png;base64,${encoded}`;
            processedImagesContainer.appendChild(img);
        });

        // Función para convertir base64 a Blob
        function base64ToBlob(b64Data, contentType = "image/png", sliceSize = 512) {
            const byteCharacters = atob(b64Data);
            const byteArrays = [];
            for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
                const slice = byteCharacters.slice(offset, offset + sliceSize);
                const byteNumbers = new Array(slice.length);
                for (let i = 0; i < slice.length; i++) {
                    byteNumbers[i] = slice.charCodeAt(i);
                }
                const byteArray = new Uint8Array(byteNumbers);
                byteArrays.push(byteArray);
            }
            return new Blob(byteArrays, { type: contentType });
        }

        // Filtrado de los caracteres con agujeros
        function filtrarComandos(latexComandos) {
            const latexHoles = {
                "0": 1, "6": 1, "8" : 2, "9" : 1, 
                "a": 1, "A": 1, "b": 1, "B": 1, "d" : 1, "D" :1,
                "e" : 1, "g" : 1, "o" : 1, "O" : 1, "p": 1, "P" : 1, 
                "q": 1, "Q": 1, "\\emptyset": 1,
                "\\alpha": 1, "\\beta": 2, "\\theta": 2, "\\phi": 2, "\\varphi": 1,
                "\\delta": 1, "\\varrho": 1, "\\varpi": 1,
                "\\infty": 2
            };

            let resultado = [];
            let skip = 0;

            for (let i = 0; i < latexComandos.length; i++) {
                if (skip > 0) {
                    skip--; // Saltar este comando
                    continue;
                }

                let comando = latexComandos[i];

                if (latexHoles.hasOwnProperty(comando)) {
                    skip = latexHoles[comando]; // Omitir los siguientes 'n' comandos
                    continue; // No agregar el comando con agujeros
                }

                resultado.push(comando);
            }

            return resultado;
        }


        // Iterar sobre cada imagen, enviar a la predicción y almacenar el resultado
        const predictions = [];
        for (const encoded of images) {
            const blob = base64ToBlob(encoded);
            const predictFormData = new FormData();
            predictFormData.append("file", blob, "processed_image.jpg");

            const predictResponse = await fetch("/predict/", {
                method: "POST",
                body: predictFormData
            });
            if (!predictResponse.ok) {
                predictions.push("Error en la predicción");
                continue;
            }
            const predictionData = await predictResponse.json();
            predictions.push(predictionData.latex_code);
        }
        let f_predictions = filtrarComandos(predictions)

        // Mostrar resultados de la predicción
        latexCode.textContent = f_predictions.join(" ");
        //latexPreview.innerHTML = predictions.map(code => `\\[${code}\\]`).join("<br>");
        //MathJax.typesetPromise();
    } catch (error) {
        alert("Error en el procesamiento: " + error.message);
    }
});