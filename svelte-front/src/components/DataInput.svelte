<script>
    import { logContentsStore } from "./store";

    let file = null;
    let selectedEndpoint = "";
    let data = null;

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

        try {
            const response = await fetch(selectedEndpoint, {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                console.log("CSV file sent successfully");
                data = await response.json(); // Initialize the data variable
                console.log(data.message);
                if (data.log_contents) {
                    console.log(data.log_contents);
                    logContentsStore.set(data.log_contents);
                }
            } else {
                console.error("Error sending CSV file");
            }
        } catch (error) {
            console.error("An error occurred:", error);
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
    <p>This service is used to test if your data complies with the standard.</p>
    <p>
        Upload a .csv, .json or .xlsx file and select a schema level below to
        test your data.
    </p>
    <br />
    <input type="file" on:change={handleFileInput} />
    <br />
    <br />
    <div class="settings">
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
    <button on:click={sendCSV}>Send</button>
    <br />
    <br />
    <details>
        <summary>Guidance:</summary>
        <p1>
            This tool is provided freely as part of the distribution of the Open
            3P standard for packaging data.
        </p1>
        <p1>
            <br />
            <br />You can view the documentation of the standard
            <a href="https://standard.open3p.org/2.0/">here</a>.
        </p1>
        <br />
        <br />
        <p1>
            The Open 3P <a href="https://www.open3p.org/">website</a> also provides
            additional learning resources and access to the Open 3P help desk service.
        </p1>
    </details>
    <details>
        <summary>Validation:</summary>
        <p1>
            This tool tests your data against the schema for Open 3P. It does
            not store your data.
        </p1>
        <p1>
            <br />
            <br /> The validator looks for column headings that are required and
            recommended within the standard. Please refer to the
            <a
                href="https://standard.open3p.org/2.0/3_Data_Specification/3_1_Base_Materials/"
                >documentation</a
            > for each schema to correctly label your columns.
        </p1>
        <br />
        <br />
        <p1>
            You are able to include columns not in the schema e.g. for use
            within your organisation. These will be ignored during validation.
        </p1>
        <br />
        <br />
        <p1>
            Results are delivered as JSON. "DataFrameSchema" errors indicate
            columns required by Open3P.
        </p1>
        <br />
        <br />
        <p1>
            "Column" errors indicate failures at a cell/value level. Column,
            failure case and index keys will help you to debug the error.
        </p1>
        <br />
        <br />
        <p1>
            A summary copy of each row with one or more failures is identified
            at the bottom of each error.
        </p1>
        <br />
        <br />
        <p1
            >You are able to download a log of error reports. The validation API
            can also be accessed via command line (see Documentation).
        </p1>
    </details>
    <details>
        <summary>Documentation:</summary>
        <p1>
            Validation results are delivered by the <a
                href="https://pandera.readthedocs.io/en/stable/index.html"
            >
                Pandera
            </a>library.
        </p1>
        <br />
        <br />
        <p1>
            This service is accessible as an API via the following portal: <a
                href="https://open3p.ecosystem2.co.uk/api/docs"
            >
                API.
            </a>
        </p1>
        <br />
        <br />
        <p1>
            Access to this tool is found under the Apache License 2.0. The
            source code can be found here LINK to GiT.
        </p1>
        <br />
        <br />
    </details>
</div>

<style>
    div.settings {
        display: grid;
        grid-template-columns: max-content max-content;
        grid-gap: 5px;
    }
    div.settings label {
        text-align: left;
    }
    div.settings label:after {
        content: ":";
    }
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%; /* Adjust this according to your layout */
    }
    .logo {
        height: 12.7em;
        padding: 0.1em;
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
        font-size: 2.4rem;
        font-family: Calibri;
        align-content: center;
    }
    h3 {
        color: #222222;
        font-size: 1rem;
        font-family: Arial;
    }

    h4 {
        color: #222222;
        font-size: 1rem;
        font-family: Arial;
    }

    p {
        color: #222222;
        font-family: Arial;
        font-size: 1rem;
        width: 80%;
        text-justify: center;
    }

    a {
        color: #336767;
        font-family: Arial;
        font-size: 1rem;
        width: 80%;
        text-justify: center;
        text-decoration: underline;
    }

    p1 {
        color: #222222;
        font-family: Arial;
        font-size: 1rem;
        width: 80%;
        text-justify: center;
    }

    br {
        line-height: 3;
    }
    input[type="file"] {
        display: inline-block;
        color: #222222;
        border: 1px solid #ccc;
        padding: 6px 12px;
        font-size: 1rem;
        cursor: pointer;
        margin: 0 auto;
        text-align: right;
        font-family: Arial;
    }

    input[type="radio"] {
        display: inline-block;
        color: #222222;
        padding: 0.2em;
        height: 1.4em;
        font-size: 1rem;
        place-items: left;
        font-family: Arial;
    }

    label {
        display: block;
        color: #222222;
        align-content: left;
        font-family: Arial;
    }
    button {
        display: inline-block;
        color: #222222;
        height: 2.4em;
        font-size: 1rem;
        place-items: center;
        justify-content: center;
        border: #222222;
        font-family: Arial;
    }
    details {
        font-family: Arial;
        color: #222222;
        text-align: center;
        padding-bottom: 4%;
        width: 80%;
    }
    summary {
        cursor: pointer;
        height: 2em;
        color: #222222;
        padding-bottom: 4%;
    }
    details[open] > summary {
        color: #222222;
        padding-bottom: 4%;
    }
</style>
