<script>
    import { onMount } from "svelte";
    import { logContentsStore } from "./store";

    let logContents = "";

    // Subscribe to changes in the store
    logContentsStore.subscribe((value) => {
        logContents = value;
        console.log("logContents:", logContents); // Log to the console
    });

    /*const tableHeading = [
        "schema_context",
        "column",
        "check",
        "failure_case",
        "index",
    ];
            {#each tableHeading as heading}
            <th>{heading}</th>
        {/each}
*/
    const downloadLog = () => {
        const blob = new Blob([logContents], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "validation_errors.log";
        link.click();
    };
</script>

<div class="container">
    <br />
    {#if logContents}
        <button on:click={downloadLog}>Download Log File</button>
        <br />
        <br />
        <br />
        <br />
        <pre>
            {logContents}
        </pre>
        <br />
    {:else}
        <p>No log contents available</p>
    {/if}
</div>

<style>
    .container {
        display: inline-block;
        justify-content: center;
    }

    .container pre {
        text-align: left;
    }

    button {
        vertical-align: middle;
        margin-left: 20%;
    }
</style>
