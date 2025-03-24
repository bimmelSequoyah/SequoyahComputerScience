document.addEventListener("DOMContentLoaded", function() {
    async function extractFirstFrame(gifSrc) {
        return new Promise((resolve) => {
            const canvas = document.createElement("canvas");
            const ctx = canvas.getContext("2d");
            const tempImg = new Image();
            tempImg.crossOrigin = "anonymous";  // To avoid CORS issues.

            tempImg.onload = () => {
                canvas.width = tempImg.width;
                canvas.height = tempImg.height;
                ctx.drawImage(tempImg, 0, 0);  // Extract first frame.
                resolve(canvas.toDataURL("image/png"));  // Convert to PNG base64.
            };

            tempImg.src = gifSrc;  // Load the GIF.
        });
    }

    async function setupArtpieces() {
        const artpieces = document.querySelectorAll(".artpiece");
        const tooltip = document.getElementById("tooltip");

        for (const artpiece of artpieces) {
            const img = artpiece.querySelector("img");
            // Hover effects
            artpiece.addEventListener("mouseover", () => {
                tooltip.textContent = img.alt;  // Show tooltip text.
                tooltip.style.display = "block";
                img.src = animatedSrc;  // Set GIF source (play it).
            });

            artpiece.addEventListener("mouseout", () => {
                tooltip.style.display = "none";
                // Don’t reset src here, keep the visibility to "visible"
                img.src = staticSrc;  // Use the first frame on hover out.
            });

            artpiece.addEventListener("mousemove", (event) => {
                tooltip.style.left = event.pageX + 10 + "px";
                tooltip.style.top = event.pageY + 10 + "px";
            });

            // for gifs only
            if (!img || !artpiece.classList.contains("gif")) continue;

            const animatedSrc = img.src;  // Store GIF source.
            img.style.visibility = "hidden";  // Hide it during processing.

            // Extract first frame dynamically.
            const staticSrc = await extractFirstFrame(animatedSrc);
            img.src = staticSrc;  // Set the first frame as the default.
            img.style.visibility = "visible";  // Show it once ready.
        }
    }

    setupArtpieces();  // Initialize the art pieces.

});
