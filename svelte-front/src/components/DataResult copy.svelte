<script>
    import { onMount } from "svelte";

    let logContents = "";

    const setupWebSocket = () => {
        const socket = new WebSocket("ws://localhost:8000/ws");

        socket.onmessage = (event) => {
            logContents = event.data;
        };
    };

    onMount(() => {
        setupWebSocket();
    });
</script>

<div>
    <br />
    {#if logContents}
        {#each logContents.split("#") as line}
            <p>{line}</p>
        {/each}
    {:else}
        <p>No log contents available</p>
    {/if}
</div>
