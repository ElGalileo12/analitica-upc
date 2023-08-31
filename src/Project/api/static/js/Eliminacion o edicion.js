const documentoInput = document.getElementById("ID_C_DOCUMENTO");
    const editarLink = document.getElementById("editarLink");
    const eliminarLink = document.getElementById("eliminarLink");

    documentoInput.addEventListener("input", () => {
        const valorDocumento = documentoInput.value;
        editarLink.href = `/api/edicionstd/${valorDocumento}`;
        eliminarLink.href = `/api/eliminacionstd/${valorDocumento}`;
    });