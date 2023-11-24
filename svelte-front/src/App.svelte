<script>
  // @ts-nocheck
  import { onMount } from "svelte";
  import DataInput from "./components/DataInput.svelte";
  import DataResult from "./components/DataResult.svelte";

  //onMount is a lifecycle method - it allows us to run commands when this component is mounted.
</script>

<main class="root">
  <div class="side-bar">
    <DataInput />
  </div>
  <div class="contents">
    <DataResult />
  </div>
</main>

<style>
  :global(html),
  :global(body) .root {
    height: 100vh;
    width: 100vw;
    margin: 0;
    display: grid;
    grid-template-areas: "side contents";
    grid-template-rows: auto 2fr;
    grid-template-columns: 1fr 3fr;
  }

  .side-bar {
    grid-area: side;
    background: rgb(155, 155, 155);
    width: 100%;
    height: 100%;
  }
  .contents {
    grid-area: contents;
    background: whitesmoke;
    border-left: 1.4px solid #000;
    width: 100%;
    height: 100%;
    padding-left: 4%;
    overflow: scroll;
    position: relative;
  }
</style>
