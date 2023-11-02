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
    <a href="https://www.open3p.org/" target="_blank" rel="noreferrer">
        <img
            src="/src/assets/open3P_assets/Open3PColour.svg"
            class="logo svelte"
            alt="Open 3PLogo"
        />
    </a>
    <h2>Open 3P Validator</h2>
    <br />
    <h3>The Open 3P validation tool is used to test if</h3>
    <h3>your data complies with the standard.</h3>
    <br />
    <h3>Upload a .csv or .json file to test your data.</h3>
    <br />
    <input type="file" on:change={handleFileInput} />
    <br />
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
        <br />
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/materials/"
            />
            Materials
            <!-- Add more radio buttons for additional endpoints -->
        </label>
    </div>
    <br />
    <br />
    <button on:click={sendCSV}>Send CSV</button>
    <br />
    <br />
    <br />
    <h3>Disclaimers...</h3>
    <h3>Files are not stored..</h3>
</div>

<style>
    .logo {
        height: 12em;
        padding: 0.3em;
        will-change: filter;
        transition: filter 300ms;
    }
    .logo:hover {
        filter: drop-shadow(0 0 2em #353ffd);
    }
    .logo.svelte:hover {
        filter: drop-shadow(0 0 2em #ffffffaa);
    }
    h2 {
        color: #222222;
        font-size: 2rem;
    }
    h3 {
        color: #222222;
        font-size: 0.8rem;
    }
    br {
        line-height: 7;
    }

    label {
        display: block;
        position: relative;
        text-align: center;
    }
    input {
        display: inline-block;
        color: #222222;
        padding: 0.3em;
        height: 2em;
        font-size: 1rem;
        place-items: center;
        justify-content: center;
        margin: 0 auto;
    }
    button {
        display: inline-block;
        color: #222222;
        height: 2em;
        font-size: 1rem;
        place-items: center;
        justify-content: center;
        border: #222222;
    }
</style>
