<script>
  // @ts-nocheck
  import { onMount } from "svelte";
  import DataInput from "./components/DataInput.svelte";
  import DataResult from "./components/DataResult.svelte";

  //onMount is a lifecycle method - it allows us to run commands when this component is mounted.
  //set todos from our todo service and subscribe to await this value
  //below makes variables accessible - allows us to print what is inside the variable e.g. to console
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
    background: grey;
    width: 100%;
    height: 100%;
    display: flex;
    padding-left: 2%;
    place-items: center;
  }
  .contents {
    grid-area: contents;
    background: whitesmoke;
    width: 100%;
    height: 100%;
    display: flex;
    padding-left: 4%;
  }
</style>
