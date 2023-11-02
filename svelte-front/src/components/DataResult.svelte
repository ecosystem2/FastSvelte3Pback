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

<div class="data-output">
    <br />
    {#if logContents}
        {#each logContents.split("#") as line}
            <p>{line}</p>
        {/each}
    {:else}
        <p>No log contents available</p>
    {/if}
</div>

<style>
    div {
        width: 100%;
        height: 100%;
    }
</style>
