<script>
    let file = null;

    const handleFileInput = (event) => {
        file = event.target.files[0];
    };

    const sendCSV = async () => {
        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch("http://localhost:8000/upload", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            console.log("CSV file sent successfully");
        } else {
            console.error("Error sending CSV file");
        }
    };
</script>

<div>
    <input type="file" on:change={handleFileInput} />
    <button on:click={sendCSV}>Send CSV</button>
</div>

<style>
    h2 {
        color: #888;
    }

    p {
        color: #888;
        height: 5em;
        font-size: 1.25rem;
    }
    input {
        color: #888;
        height: 2em;
        font-size: 1rem;
    }
</style>
