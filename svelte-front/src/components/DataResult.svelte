<script>
    import { onMount } from "svelte";
    import { logContentsStore } from "./store";

    let logContents = "";

    // Subscribe to changes in the store
    logContentsStore.subscribe((value) => {
        logContents = value;
        console.log("logContents:", logContents); // Log to the console
    });

    /*
    const setupWebSocket = () => {
        const socket = new WebSocket("ws://localhost:8000/ws");

        socket.onmessage = (event) => {
            logContents = event.data;
        };
    };
*/
    const downloadLog = () => {
        const blob = new Blob([logContents], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "validation_errors.log";
        link.click();
    };

    //    onMount(() => {
    //        setupWebSocket();
    //    });
</script>

<div>
    <br />
    {#if logContents}
        <pre>
            {logContents}
        </pre>
        <br />
        <button on:click={downloadLog}>Download Log File</button>
    {:else}
        <p>No log contents available</p>
    {/if}
</div>
