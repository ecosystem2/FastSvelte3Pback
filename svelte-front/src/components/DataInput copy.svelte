<script>
    let file = null;
    let selectedEndpoint = "";

    const handleFileInput = (event) => {
        file = event.target.files[0];
    };

    const sendCSV = async () => {
        if (!selectedEndpoint) {
            console.error("No endpoint selected");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch(selectedEndpoint, {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            console.log("CSV file sent successfully");
            const data = await response.json();
            if (data.log_contents) {
                console.log(data.log_contents); // Log the received log contents
            }
        } else {
            console.error("Error sending CSV file");
        }
    };
</script>

<div>
    <br />
    <br />
    <input type="file" on:change={handleFileInput} />
    <br />
    <div>
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/basematerials/"
            />
            Base Materials
        </label>
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/materials/"
            />
            Materials
        </label>
        <!-- Add more radio buttons for additional endpoints -->
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/components/"
            />
            Components
        </label>
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/completepackaging/"
            />
            Complete Packaging
        </label>
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/multipack/"
            />
            Multipack
        </label>
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/loadcatalogue/"
            />
            Load Catalogue
        </label>
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/load/"
            />
            Load
        </label>
    </div>
    <br />
    <br />
    <button on:click={sendCSV}>Send CSV</button>
    <br />
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
    br {
        line-height: 3;
    }

    input {
        color: #888;
        height: 2em;
        font-size: 1rem;
        max-width: 280px;
        text-align: center;
    }
</style>
