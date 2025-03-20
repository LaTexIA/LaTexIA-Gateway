document.getElementById("uploadButton").addEventListener("click", async function () {
  const input = document.getElementById("imageInput");
  if (!input.files.length) {
      alert("Por favor, selecciona una imagen.");
      return;
  }

  const formData = new FormData();
  formData.append("file", input.files[0]);

  try {
      const response = await fetch("/process-image/", {
          method: "POST",
          body: formData
      });

      if (!response.ok) throw new Error("Error en el procesamiento.");

      const blob = await response.blob();
      document.getElementById("processedImage").src = URL.createObjectURL(blob);
  } catch (error) {
      alert("Hubo un error al enviar la imagen.");
      console.error(error);
  }
});
