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

<div class="container">
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
    <h4>Upload a .csv or .json file to test your data.</h4>
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
        <label>
            <input
                type="radio"
                bind:group={selectedEndpoint}
                value="http://localhost:8000/materials/"
            />
            Materials
            <!-- Add more radio buttons for additional endpoints -->
        </label>
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
    <br />
    <br />
    <h3>Disclaimers...</h3>
    <h3>Files are not stored..</h3>
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%; /* Adjust this according to your layout */
    }
    .logo {
        height: 12em;
        padding: 0.2em;
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
        font-family: Calibri;
        align-content: center;
    }
    h3 {
        color: #222222;
        font-size: 0.8rem;
        font-family: Arial;
    }

    h4 {
        color: #222222;
        font-size: 0.8rem;
        font-family: Arial;
    }

    br {
        line-height: 4;
    }

    label {
        display: block;
        color: #222222;
        align-content: left;
        font-family: Arial;
    }
    input {
        display: inline-block;
        color: #222222;
        padding: 0.2em;
        height: 2em;
        font-size: 1rem;
        place-items: center;
        font-family: Arial;
    }
    button {
        display: inline-block;
        color: #222222;
        height: 2em;
        font-size: 1rem;
        place-items: center;
        justify-content: center;
        border: #222222;
        font-family: Arial;
    }
</style>
