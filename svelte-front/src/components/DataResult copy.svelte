<script>
    import { onMount } from "svelte";

    let logContents = "";

    const setupWebSocket = () => {
        const socket = new WebSocket("ws://localhost:8000/ws");

        socket.onmessage = (event) => {
            logContents = event.data;
        };
    };

    const downloadLog = () => {
        const blob = new Blob([logContents], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "validation_errors.log";
        link.click();
    };

    onMount(() => {
        setupWebSocket();
    });
</script>

<div>
    <br />
    {#if logContents}
        <table style="width:100%">
            {#each logContents.split("\n") as line}
                {#if line.trim().length > 0}
                    <tr>
                        {#each line.trim().split(/\s{2,}/) as item}
                            <td style="padding: 5px; border: 1px solid #ddd;"
                                >{item}</td
                            >
                        {/each}
                    </tr>
                {/if}
            {/each}
        </table>
        <br />
        <button on:click={downloadLog}>Download Log File</button>
    {:else}
        <p>No log contents available</p>
    {/if}
</div>
