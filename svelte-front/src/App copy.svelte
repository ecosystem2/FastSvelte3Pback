<script>
  // @ts-nocheck

  import "carbon-components-svelte/css/white.css";
  import { onMount } from "svelte";
  import DataInput from "./components/DataInput.svelte";
  import DataResult from "./components/DataResult.svelte";

  //onMount is a lifecycle method - it allows us to run commands when this component is mounted.
  //set todos from our todo service and subscribe to await this value
  //below makes variables accessible - allows us to print what is inside the variable e.g. to console
</script>

<main>
  <h2>Open 3P Validator</h2>

  <DataInput />
  <DataResult />
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
